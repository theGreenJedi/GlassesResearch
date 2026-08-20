#!/usr/bin/env python3
"""Verify staged GRE change surfaces and GRE-driven RSS behavior."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from xml.etree import ElementTree as ET

from verified_changes import DEFAULT_CHANGES, validate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    args = parser.parse_args()

    source = validate(args.changes)
    events = source["events"]
    public = json.loads((args.site_root / "data" / "verified-changes.json").read_text(encoding="utf-8"))
    if public.get("event_count") != len(events) or len(public.get("events", [])) != len(events):
        raise SystemExit("Public GRE event count drifted from canonical ledger")
    if "alert_match" in json.dumps(public):
        raise SystemExit("Public GRE payload leaked internal alert-match fields")

    index = args.site_root / "changes" / "index.md"
    if not index.is_file():
        raise SystemExit("Verified changes index is missing")
    for event in events:
        event_id = event["id"]
        page = args.site_root / "changes" / f"{event_id.lower()}.md"
        if not page.is_file() or event_id not in page.read_text(encoding="utf-8"):
            raise SystemExit(f"Verified change resolver missing or malformed: {event_id}")

    news = (args.site_root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
    for event in events:
        marker = f"<!-- verified-change:{event['id']} -->"
        if news.count(marker) != 1:
            raise SystemExit(f"Research & News GRE reference count is not exactly one: {event['id']}")

    affected_models = {model_id for event in events for model_id in event["affected"]["model_ids"]}
    for model_id in affected_models:
        page = args.site_root / "models" / "catalog" / f"{model_id.lower()}.md"
        text = page.read_text(encoding="utf-8")
        if text.count("<!-- verified-change-history -->") != 1:
            raise SystemExit(f"Affected model GRE history missing or duplicated: {model_id}")

    feed = ET.parse(args.site_root / "feed.xml")
    items = feed.findall("./channel/item")
    if len(items) != len(events):
        raise SystemExit(f"GRE RSS item count mismatch: expected {len(events)}, got {len(items)}")
    guids = {item.findtext("guid", "") for item in items}
    for event in events:
        expected = f"https://glassesresearch.org/changes/{event['id'].lower()}/"
        if expected not in guids:
            raise SystemExit(f"GRE RSS stable GUID missing: {event['id']}")
    feed_text = (args.site_root / "feed.xml").read_text(encoding="utf-8")
    if "Halliday G2 remains on Watching" in feed_text:
        raise SystemExit("Watching item leaked into GRE verified RSS feed")

    print(
        f"GRE surfaces verified: {len(events)} events, {len(affected_models)} affected model histories, "
        f"{len(items)} verified RSS items; Watching excluded"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
