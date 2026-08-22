#!/usr/bin/env python3
"""Build RSS and JSON Feed surfaces from canonical GRE verified-change events."""
from __future__ import annotations

import argparse
import email.utils
import json
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

from verified_changes import DEFAULT_CHANGES, validate

SITE = "https://glassesresearch.org"


def timestamp(value: str) -> datetime:
    if "T" in value:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def iso_timestamp(value: str) -> str:
    return timestamp(value).isoformat().replace("+00:00", "Z")


def build_json_feed(events: list[dict], output: Path) -> None:
    payload = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "GlassesResearch — Research & News",
        "home_page_url": f"{SITE}/docs/RESEARCH_NEWS/",
        "feed_url": f"{SITE}/feed.json",
        "description": "Verified smart-glasses research and changes from GlassesResearch. Watching and discovery candidates are excluded.",
        "language": "en-US",
        "items": [],
    }

    for event in events:
        publication = event["publication"]
        payload["items"].append(
            {
                "id": f"{SITE}/changes/{event['id'].lower()}/",
                "url": publication["canonical_url"],
                "title": publication["title"],
                "content_text": publication["summary"],
                "date_published": iso_timestamp(publication["published_at"]),
                "tags": [event["change_type"], *event["alert_match"]["topics"]],
            }
        )

    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build(changes: Path, output: Path) -> int:
    events = validate(changes)["events"]
    events = sorted(events, key=lambda event: (timestamp(event["publication"]["published_at"]), event["id"]), reverse=True)

    rss = ET.Element("rss", {"version": "2.0", "xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "GlassesResearch — Research & News"
    ET.SubElement(channel, "link").text = f"{SITE}/docs/RESEARCH_NEWS/"
    ET.SubElement(channel, "description").text = "Verified smart-glasses research and changes from GlassesResearch. Watching and discovery candidates are excluded."
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "atom:link", {"href": f"{SITE}/feed.xml", "rel": "self", "type": "application/rss+xml"})
    ET.SubElement(channel, "lastBuildDate").text = email.utils.format_datetime(datetime.now(timezone.utc))

    for event in events:
        publication = event["publication"]
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = publication["title"]
        ET.SubElement(item, "link").text = publication["canonical_url"]
        stable = f"{SITE}/changes/{event['id'].lower()}/"
        ET.SubElement(item, "guid", {"isPermaLink": "true"}).text = stable
        ET.SubElement(item, "pubDate").text = email.utils.format_datetime(timestamp(publication["published_at"]))
        ET.SubElement(item, "description").text = publication["summary"]
        ET.SubElement(item, "category").text = event["change_type"]
        for topic in event["alert_match"]["topics"]:
            ET.SubElement(item, "category").text = topic

    output.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(rss, space="  ")
    output.write_bytes(ET.tostring(rss, encoding="utf-8", xml_declaration=True))
    build_json_feed(events, output.with_suffix(".json"))
    return len(events)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    parser.add_argument("--output", type=Path, default=Path(".site-src/feed.xml"))
    args = parser.parse_args()
    count = build(args.changes, args.output)
    if count == 0:
        raise SystemExit("Feed build found no verified GRE events")
    print(f"GRE feeds built with {count} verified items: {args.output} + {args.output.with_suffix('.json')}")


if __name__ == "__main__":
    main()
