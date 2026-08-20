#!/usr/bin/env python3
"""Build public GRE change surfaces from the canonical verified-change ledger."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from verified_changes import DEFAULT_CHANGES, validate


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def public_event(event: dict[str, Any]) -> dict[str, Any]:
    publication = event["publication"]
    return {
        "id": event["id"],
        "state": event["state"],
        "change_type": event["change_type"],
        "verified_at": event["verified_at"],
        "previous_state": event["previous_state"],
        "new_state": event["new_state"],
        "affected": event["affected"],
        "evidence_urls": event["evidence_urls"],
        "publication": {
            "title": publication["title"],
            "canonical_url": publication["canonical_url"],
            "summary": publication["summary"],
            "published_at": publication["published_at"],
        },
    }


def change_page(event: dict[str, Any]) -> str:
    publication = event["publication"]
    affected = event["affected"]
    lines = [
        f"# {event['id']} — {publication['title']}",
        "",
        f"**Verified:** {event['verified_at']}  ",
        f"**Change type:** `{event['change_type']}`  ",
        f"**Published research:** [{publication['title']}]({publication['canonical_url']})",
        "",
        "## What changed",
        "",
        f"**Before:** {event['previous_state']}",
        "",
        f"**After:** {event['new_state']}",
        "",
    ]
    if affected["model_ids"]:
        lines += ["## Affected models", ""]
        for model_id in affected["model_ids"]:
            lines.append(f"- [{model_id}](/models/catalog/{model_id.lower()}/)")
        lines.append("")
    if affected["relationship_ids"]:
        lines += ["## Affected relationships", ""]
        for relationship_id in affected["relationship_ids"]:
            lines.append(f"- `{relationship_id}`")
        lines.append("")
    lines += ["## Evidence", ""]
    for url in event["evidence_urls"]:
        lines.append(f"- {url}")
    lines += [
        "",
        "This change record does not transfer specifications, scores, firmware behavior, community observations, or verification status to related models through lineage.",
        "",
    ]
    return "\n".join(lines)


def build_index(events: list[dict[str, Any]]) -> str:
    lines = [
        "# Verified Changes",
        "",
        "Stable change records for verified, already-published GlassesResearch work. Discovery candidates and Watching items do not appear here.",
        "",
        "Each `GRE-*` identifier names the change itself. The human-readable research article remains the canonical publication surface.",
        "",
        "| Change | Verified | Type | Published research |",
        "|---|---|---|---|",
    ]
    for event in sorted(events, key=lambda item: item["id"], reverse=True):
        publication = event["publication"]
        lines.append(
            f"| [{event['id']}](/changes/{event['id'].lower()}/) | {event['verified_at']} | "
            f"`{event['change_type']}` | [{publication['title']}]({publication['canonical_url']}) |"
        )
    lines.append("")
    return "\n".join(lines)


def inject_research_news(site_root: Path, events: list[dict[str, Any]]) -> int:
    path = site_root / "docs" / "RESEARCH_NEWS.md"
    text = path.read_text(encoding="utf-8")
    injected = 0
    for event in events:
        heading = event["publication"]["source_heading"]
        marker = f"<!-- verified-change:{event['id']} -->"
        if marker in text:
            continue
        candidates = [f"### {heading}\n", f"### {heading} {{#"]
        index = -1
        insert_at = -1
        simple = candidates[0]
        if simple in text:
            index = text.index(simple)
            insert_at = index + len(simple)
        else:
            prefix = candidates[1]
            index = text.find(prefix)
            if index >= 0:
                newline = text.find("\n", index)
                insert_at = len(text) if newline < 0 else newline + 1
        if index < 0 or insert_at < 0:
            raise RuntimeError(f"Cannot inject GRE reference for missing Research & News heading: {heading}")
        note = f"\n{marker}\n<small>Verified change: [{event['id']}](/changes/{event['id'].lower()}/)</small>\n"
        text = text[:insert_at] + note + text[insert_at:]
        injected += 1
    path.write_text(text, encoding="utf-8")
    return injected


def inject_model_history(site_root: Path, events: list[dict[str, Any]]) -> int:
    by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        for model_id in event["affected"]["model_ids"]:
            by_model[model_id].append(event)
    changed = 0
    for model_id, model_events in by_model.items():
        path = site_root / "models" / "catalog" / f"{model_id.lower()}.md"
        if not path.exists():
            raise RuntimeError(f"GRE affected model page is missing: {model_id}")
        text = path.read_text(encoding="utf-8")
        if "<!-- verified-change-history -->" in text:
            raise RuntimeError(f"GRE history already present before change-surface build: {model_id}")
        lines = ["", "## Verified changes", "", "<!-- verified-change-history -->"]
        for event in sorted(model_events, key=lambda item: item["id"], reverse=True):
            publication = event["publication"]
            lines.append(
                f"- [{event['id']}](/changes/{event['id'].lower()}/) — "
                f"[{publication['title']}]({publication['canonical_url']})"
            )
        lines.append("")
        path.write_text(text.rstrip() + "\n" + "\n".join(lines), encoding="utf-8")
        changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    args = parser.parse_args()

    payload = validate(args.changes)
    events = payload["events"]
    devices = load_json(args.site_root / "data" / "devices.json")
    canonical_ids = {record["id"] for record in devices.get("records", [])}
    lineage = load_json(args.site_root / "data" / "lineage-index.json")
    relationship_ids = {item["id"] for item in lineage.get("relationships", [])}

    for event in events:
        for model_id in event["affected"]["model_ids"]:
            if model_id not in canonical_ids:
                raise RuntimeError(f"GRE {event['id']} references missing staged canonical model {model_id}")
        for relationship_id in event["affected"]["relationship_ids"]:
            if relationship_id not in relationship_ids:
                raise RuntimeError(f"GRE {event['id']} references unknown staged relationship {relationship_id}")

    public_payload = {
        "schema_version": 1,
        "event_count": len(events),
        "semantics": "Verified change identity only. No claim, specification, score, community review, or verification state inherits through lineage.",
        "events": [public_event(event) for event in events],
    }
    out = args.site_root / "data" / "verified-changes.json"
    out.write_text(json.dumps(public_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    changes_dir = args.site_root / "changes"
    changes_dir.mkdir(parents=True, exist_ok=True)
    (changes_dir / "index.md").write_text(build_index(events), encoding="utf-8")
    for event in events:
        (changes_dir / f"{event['id'].lower()}.md").write_text(change_page(event), encoding="utf-8")

    news_refs = inject_research_news(args.site_root, events)
    model_pages = inject_model_history(args.site_root, events)
    print(
        f"Verified change surfaces built: {len(events)} GRE events, {news_refs} Research & News refs, "
        f"{model_pages} affected model pages, {sum(len(e['affected']['relationship_ids']) for e in events)} relationship targets"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
