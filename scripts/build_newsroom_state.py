#!/usr/bin/env python3
"""Build the reader-facing newsroom state from verified changes plus an optional editorial lead pin.

The verified desk remains derived only from the canonical verified-change ledger. An explicit
editorial lead pin may feature a reviewed external article without changing its verification
state or promoting it into the verified desk.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from verified_changes import DEFAULT_CHANGES, validate

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EDITORIAL_LEAD = ROOT / "data" / "editorial-lead.json"
LEAD_WINDOW = 6
LEAD_WEIGHT = {
    "hardware_change": 6,
    "policy_change": 5,
    "research_release": 5,
    "relationship_change": 4,
    "correction": 4,
    "firmware_change": 4,
    "software_release": 3,
    "availability_change": 3,
    "catalog_admission": 2,
}
TOPIC_LABELS = {
    "hacks_development": "Owner control & development",
    "firmware_software": "Software & firmware",
    "hardware_teardown": "Hardware & teardown",
    "privacy_policy": "Privacy & policy",
    "release_availability": "Release & availability",
    "research_science": "Research & science",
    "standards_regulation": "Standards & regulation",
}


def stamp(value: str) -> datetime:
    raw = value.replace("Z", "+00:00")
    parsed = datetime.fromisoformat(raw)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def story(event: dict) -> dict:
    publication = event["publication"]
    return {
        "event_id": event["id"],
        "change_type": event["change_type"],
        "title": publication["title"],
        "summary": publication["summary"],
        "url": publication["canonical_url"],
        "published_at": publication["published_at"],
        "model_ids": list(event["affected"]["model_ids"]),
        "lead_mode": "auto",
    }


def choose_lead(events: list[dict]) -> dict:
    recent = sorted(events, key=lambda e: stamp(e["publication"]["published_at"]), reverse=True)[:LEAD_WINDOW]
    lead = max(
        recent,
        key=lambda e: (
            LEAD_WEIGHT.get(e["change_type"], 1),
            stamp(e["publication"]["published_at"]),
        ),
    )
    return story(lead)


def load_editorial_lead(path: Path) -> dict | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not payload.get("enabled"):
        return None
    required = ("source_label", "title", "summary", "url", "published_at")
    missing = [key for key in required if not payload.get(key)]
    if payload.get("schema_version") != 1 or payload.get("mode") != "editorial_pin" or missing:
        raise SystemExit(f"Invalid editorial lead configuration; missing={missing}")
    if payload.get("review_status") != "editorially_reviewed_external":
        raise SystemExit("Editorial lead must be explicitly marked editorially_reviewed_external")
    url = str(payload["url"])
    if not url.startswith("https://"):
        raise SystemExit("Editorial lead URL must use HTTPS")
    stamp(str(payload["published_at"]))
    return {
        "event_id": None,
        "change_type": "editorial_pick",
        "title": payload["title"],
        "summary": payload["summary"],
        "url": url,
        "published_at": payload["published_at"],
        "model_ids": [],
        "lead_mode": "editorial_pin",
        "review_status": payload["review_status"],
        "source_label": payload["source_label"],
        "selected_at": payload.get("selected_at"),
    }


def source_hosts(event: dict) -> set[str]:
    hosts = set()
    for url in event.get("evidence_urls", []):
        host = urlparse(url).hostname or ""
        host = host.lower().removeprefix("www.")
        if host:
            hosts.add(host)
    return hosts


def convergence(events: list[dict]) -> list[dict]:
    buckets: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for event in events:
        alert = event.get("alert_match", {})
        for entity in alert.get("brands_lineages", []):
            buckets[("entity", entity)].append(event)
        for topic in alert.get("topics", []):
            buckets[("beat", topic)].append(event)

    themes = []
    for (kind, key), grouped in buckets.items():
        unique = {event["id"]: event for event in grouped}
        grouped = list(unique.values())
        hosts = set().union(*(source_hosts(event) for event in grouped))
        if len(grouped) < 2 or len(hosts) < 2:
            continue
        grouped.sort(key=lambda e: stamp(e["publication"]["published_at"]), reverse=True)
        label = key if kind == "entity" else TOPIC_LABELS.get(key, key.replace("_", " ").title())
        themes.append({
            "kind": kind,
            "label": label,
            "story_count": len(grouped),
            "independent_source_hosts": len(hosts),
            "latest_at": grouped[0]["publication"]["published_at"],
            "story_ids": [event["id"] for event in grouped[:6]],
            "stories": [story(event) for event in grouped[:3]],
        })

    themes.sort(
        key=lambda item: (
            item["independent_source_hosts"],
            item["story_count"],
            stamp(item["latest_at"]),
        ),
        reverse=True,
    )
    return themes[:6]


def build(payload: dict, editorial_lead: dict | None = None) -> dict:
    events = payload["events"]
    ordered = sorted(events, key=lambda e: stamp(e["publication"]["published_at"]), reverse=True)
    latest_at = ordered[0]["publication"]["published_at"] if ordered else None
    automatic_lead = choose_lead(events) if events else None
    return {
        "schema_version": 1,
        "derived_from": "data/verified-changes.json",
        "semantics": "Verified desk state is derived only from verified published changes; an explicit editorial lead pin may feature a reviewed external article without changing verification state.",
        "latest_verified_at": latest_at,
        "lead": editorial_lead or automatic_lead,
        "latest": [story(event) for event in ordered[:9]],
        "convergence": convergence(events),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    parser.add_argument("--editorial-lead", type=Path, default=DEFAULT_EDITORIAL_LEAD)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = validate(args.changes)
    editorial_lead = load_editorial_lead(args.editorial_lead)
    state = build(payload, editorial_lead=editorial_lead)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lead_name = state["lead"].get("event_id") or state["lead"].get("source_label", "none") if state["lead"] else "none"
    print(
        f"Newsroom state built: lead={lead_name}, "
        f"mode={state['lead'].get('lead_mode') if state['lead'] else 'none'}, "
        f"latest={len(state['latest'])}, convergence={len(state['convergence'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
