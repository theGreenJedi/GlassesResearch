#!/usr/bin/env python3
"""Verify staged GRE change surfaces, homepage freshness, and GRE-driven RSS behavior."""
from __future__ import annotations

import argparse
import html
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
    infrastructure_footer = (
        "This change record does not transfer specifications, scores, firmware behavior, "
        "community observations, or verification status to related models through lineage."
    )
    for event in events:
        event_id = event["id"]
        page = args.site_root / "changes" / f"{event_id.lower()}.md"
        if not page.is_file():
            raise SystemExit(f"Verified change resolver missing: {event_id}")
        page_text = page.read_text(encoding="utf-8")
        if event_id not in page_text:
            raise SystemExit(f"Verified change resolver malformed: {event_id}")
        if infrastructure_footer in page_text:
            raise SystemExit(f"Verified change resolver leaked editorial infrastructure copy: {event_id}")

    homepage = (args.site_root / "index.md").read_text(encoding="utf-8")
    latest = sorted(events, key=lambda item: item["publication"]["published_at"], reverse=True)[:3]
    if "data-home-verified-stream" not in homepage:
        raise SystemExit("Homepage is not generated from the verified-change stream")
    positions: list[int] = []
    for event in latest:
        marker = f'data-home-gre="{event["id"]}"'
        if homepage.count(marker) != 1:
            raise SystemExit(f"Homepage latest-verified item missing or duplicated: {event['id']}")
        positions.append(homepage.index(marker))
        if html.escape(event["publication"]["title"]) not in homepage:
            raise SystemExit(f"Homepage is missing current verified title: {event['id']}")
        canonical_href = f'href="{event["publication"]["canonical_url"]}"'
        if canonical_href not in homepage:
            raise SystemExit(f"Homepage latest item does not route to published research: {event['id']}")
        change_href = f'/changes/{event["id"].lower()}/'
        if change_href in homepage:
            raise SystemExit(f"Homepage exposes GRE infrastructure instead of published research: {event['id']}")
    if positions != sorted(positions):
        raise SystemExit("Homepage verified changes are not newest-first")
    if "Read the verified change" in homepage:
        raise SystemExit("Homepage uses infrastructure-facing verified-change copy")
    for required in (
        'class="follow-research gr-home-follow"',
        '/docs/RESEARCH_NEWS/#verified-research-alerts',
        'https://glassesresearch.org/feed.xml',
        'feedly.com/i/discover/sources/search/feed/',
        'inoreader.com/feed/',
        'data-copy-feed',
    ):
        if required not in homepage:
            raise SystemExit(f"Homepage follow surface missing: {required}")

    news = (args.site_root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
    if "<small>Verified change:" in news:
        raise SystemExit("Research & News exposes GRE provenance as reader-facing copy")
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
        f"GRE surfaces verified: {len(events)} events, homepage newest {','.join(e['id'] for e in latest)}, "
        f"homepage content-first routing and follow surface present, {len(affected_models)} affected model histories, "
        f"{len(items)} verified RSS items; Watching excluded"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
