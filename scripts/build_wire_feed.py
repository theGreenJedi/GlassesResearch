#!/usr/bin/env python3
"""Build RSS and JSON Feed surfaces for the unverified Across the Wire stream."""
from __future__ import annotations

import argparse
import email.utils
import json
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

SITE = "https://glassesresearch.org"


def timestamp(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def iso_timestamp(value: str | None) -> str:
    return timestamp(value).isoformat().replace("+00:00", "Z")


def load_wire(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or not isinstance(payload.get("items"), list):
        raise ValueError("wire state must use schema_version 1 with an items array")
    return [
        item for item in payload["items"]
        if isinstance(item, dict)
        and item.get("status") in {"reported", "under_review"}
        and item.get("title")
        and item.get("url")
    ]


def build_json_feed(items: list[dict], output: Path) -> None:
    payload = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "GlassesResearch — Across the Wire",
        "home_page_url": f"{SITE}/#gr-home-wire-title",
        "feed_url": f"{SITE}/wire/feed.json",
        "description": "Current smart-glasses source reports surfaced by web/news search. Items are discovery signals and are not verified GlassesResearch claims.",
        "language": "en-US",
        "items": [],
    }
    for item in items:
        stable = item.get("discovery_id") or item["url"]
        payload["items"].append({
            "id": f"urn:glassesresearch:wire:{stable}",
            "url": item["url"],
            "title": item["title"],
            "content_text": f"{item.get('status', 'reported').replace('_', ' ').title()} · {item.get('publisher', 'source')} · Unverified discovery signal from Across the Wire.",
            "date_published": iso_timestamp(item.get("published_at") or item.get("discovered_at")),
            "tags": ["across-the-wire", item.get("status", "reported"), item.get("source_class", "source")],
        })
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build(wire: Path, output: Path) -> int:
    items = sorted(
        load_wire(wire),
        key=lambda item: (timestamp(item.get("published_at") or item.get("discovered_at")), item.get("discovery_id", "")),
        reverse=True,
    )

    rss = ET.Element("rss", {"version": "2.0", "xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "GlassesResearch — Across the Wire"
    ET.SubElement(channel, "link").text = f"{SITE}/#gr-home-wire-title"
    ET.SubElement(channel, "description").text = "Current smart-glasses source reports surfaced by web/news search. Discovery signals only; not verified GlassesResearch claims."
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "atom:link", {"href": f"{SITE}/wire/feed.xml", "rel": "self", "type": "application/rss+xml"})
    ET.SubElement(channel, "lastBuildDate").text = email.utils.format_datetime(datetime.now(timezone.utc))

    for item in items:
        entry = ET.SubElement(channel, "item")
        ET.SubElement(entry, "title").text = item["title"]
        ET.SubElement(entry, "link").text = item["url"]
        stable = item.get("discovery_id") or item["url"]
        ET.SubElement(entry, "guid", {"isPermaLink": "false"}).text = f"urn:glassesresearch:wire:{stable}"
        ET.SubElement(entry, "pubDate").text = email.utils.format_datetime(timestamp(item.get("published_at") or item.get("discovered_at")))
        ET.SubElement(entry, "description").text = f"{item.get('status', 'reported').replace('_', ' ').title()} · {item.get('publisher', 'source')} · Unverified discovery signal from Across the Wire."
        ET.SubElement(entry, "category").text = "across-the-wire"
        ET.SubElement(entry, "category").text = item.get("status", "reported")
        ET.SubElement(entry, "category").text = item.get("source_class", "source")

    output.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(rss, space="  ")
    output.write_bytes(ET.tostring(rss, encoding="utf-8", xml_declaration=True))
    build_json_feed(items, output.with_suffix(".json"))
    return len(items)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wire", type=Path, default=Path("data/wire-state.json"))
    parser.add_argument("--output", type=Path, default=Path(".site-src/wire/feed.xml"))
    args = parser.parse_args()
    count = build(args.wire, args.output)
    print(f"Across the Wire feeds built with {count} items: {args.output} + {args.output.with_suffix('.json')}")


if __name__ == "__main__":
    main()
