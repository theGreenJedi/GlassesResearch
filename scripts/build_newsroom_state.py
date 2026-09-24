#!/usr/bin/env python3
"""Build the reader-facing newsroom state from verified changes plus an optional editorial lead pin.

The verified desk remains derived only from the canonical verified-change ledger. An explicit
editorial lead pin may feature a reviewed external article without changing its verification
state or promoting it into the verified desk. Lead stories expire after seven days.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

from verified_changes import DEFAULT_CHANGES, validate

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EDITORIAL_LEAD = ROOT / "data" / "editorial-lead.json"
DEFAULT_EDITORIAL_DIR = ROOT / "docs" / "news" / "articles"
SITE_ORIGIN = "https://glassesresearch.org"
LEAD_WINDOW = 6
MAX_LEAD_AGE_DAYS = 7
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


def lead_is_fresh(value: str, now: datetime | None = None) -> bool:
    now = now or datetime.now(timezone.utc)
    published = stamp(value)
    return published <= now and published >= now - timedelta(days=MAX_LEAD_AGE_DAYS)


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


def choose_lead(events: list[dict]) -> dict | None:
    eligible = [event for event in events if lead_is_fresh(event["publication"]["published_at"])]
    recent = sorted(eligible, key=lambda e: stamp(e["publication"]["published_at"]), reverse=True)[:LEAD_WINDOW]
    if not recent:
        return None
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
    if not lead_is_fresh(str(payload["published_at"])):
        return None
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


def load_first_party_editorial(article_dir: Path) -> dict | None:
    """Return the newest fresh GlassesResearch editorial published in the article tree.

    Editorials remain distinct from verified-change events: they may lead the reader-facing
    presentation, but they are never inserted into the verified desk merely by being an editorial.
    """
    candidates: list[dict] = []
    if not article_dir.exists():
        return None

    for path in sorted(article_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not re.search(r"^\*\*Type:\*\*\s*GlassesResearch editorial(?:\s*/.*)?$", text, re.MULTILINE | re.IGNORECASE):
            continue

        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        published_match = re.search(r"^\*\*Published:\*\*\s*([^\n]+?)\s*$", text, re.MULTILINE)
        if not title_match or not published_match:
            raise SystemExit(f"Editorial article lacks title or Published date: {path.relative_to(ROOT)}")

        published_text = published_match.group(1).strip()
        try:
            published = datetime.strptime(published_text, "%B %d, %Y").replace(tzinfo=timezone.utc)
        except ValueError as exc:
            raise SystemExit(f"Editorial Published date must be 'Month D, YYYY': {path.relative_to(ROOT)}") from exc
        published_at = published.isoformat().replace("+00:00", "Z")
        if not lead_is_fresh(published_at):
            continue

        summary_match = re.search(r'^description:\s*"([^"]+)"\s*    hosts = set()
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


def build(
    payload: dict,
    editorial_lead: dict | None = None,
    first_party_editorial: dict | None = None,
) -> dict:
    events = payload["events"]
    ordered = sorted(events, key=lambda e: stamp(e["publication"]["published_at"]), reverse=True)
    latest_at = ordered[0]["publication"]["published_at"] if ordered else None
    automatic_lead = choose_lead(events) if events else None

    # The verified desk and the presentation lead are intentionally different concepts.
    # A first-party editorial can lead the page without becoming a verified-change event.
    lead = automatic_lead
    for candidate in (first_party_editorial, editorial_lead):
        if candidate and (lead is None or stamp(candidate["published_at"]) >= stamp(lead["published_at"])):
            lead = candidate
    return {
        "schema_version": 1,
        "derived_from": "data/verified-changes.json",
        "semantics": "Verified desk state is derived only from verified published changes. A published first-party editorial or explicit reviewed external editorial pin may lead presentation without entering the verified desk. No lead may be more than seven days old.",
        "latest_verified_at": latest_at,
        "lead": lead,
        "latest": [story(event) for event in ordered[:9]],
        "convergence": convergence(events),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    parser.add_argument("--editorial-lead", type=Path, default=DEFAULT_EDITORIAL_LEAD)
    parser.add_argument("--editorial-dir", type=Path, default=DEFAULT_EDITORIAL_DIR)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = validate(args.changes)
    editorial_lead = load_editorial_lead(args.editorial_lead)
    first_party_editorial = load_first_party_editorial(args.editorial_dir)
    state = build(payload, editorial_lead=editorial_lead, first_party_editorial=first_party_editorial)
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
, text, re.MULTILINE)
        if summary_match:
            summary = summary_match.group(1).strip()
        else:
            dek_match = re.search(r"^\*([^*\n].+?)\*\s*$", text, re.MULTILINE)
            summary = dek_match.group(1).strip() if dek_match else ""
        if not summary:
            raise SystemExit(f"Editorial article lacks a reader-facing summary: {path.relative_to(ROOT)}")

        candidates.append({
            "event_id": None,
            "change_type": "editorial",
            "title": title_match.group(1).strip(),
            "summary": summary,
            "url": f"{SITE_ORIGIN}/docs/news/articles/{path.stem}/",
            "published_at": published_at,
            "model_ids": [],
            "lead_mode": "first_party_editorial",
            "review_status": "first_party_published",
            "source_label": "GlassesResearch",
        })

    if not candidates:
        return None
    return max(candidates, key=lambda item: stamp(item["published_at"]))


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
    lead = editorial_lead or automatic_lead
    if editorial_lead and automatic_lead:
        if stamp(automatic_lead["published_at"]) > stamp(editorial_lead["published_at"]):
            lead = automatic_lead
    return {
        "schema_version": 1,
        "derived_from": "data/verified-changes.json",
        "semantics": "Verified desk state is derived only from verified published changes; an explicit editorial lead pin may feature a reviewed external article without changing verification state. No lead may be more than seven days old.",
        "latest_verified_at": latest_at,
        "lead": lead,
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
