#!/usr/bin/env python3
"""Build a summary-only RSS 2.0 feed from the current Research & News pulse."""
from __future__ import annotations

import argparse
import email.utils
import re
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

SITE = "https://glassesresearch.org"
# The live pulse groups entries under category H2s, so dated stories may be H2 or H3.
HEADING_RE = re.compile(r"^#{2,3}\s+([A-Z][a-z]+ \d{1,2}, \d{4})\s+[—-]\s+(.+?)\s*$", re.M)


def plain_summary(block: str, limit: int = 420) -> str:
    block = re.sub(r"<[^>]+>", " ", block)
    block = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", block)
    block = re.sub(r"[*_`#>]", "", block)
    paragraphs = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", block)]
    text = next(
        (
            p
            for p in paragraphs
            if p
            and not p.startswith("Source:")
            and not p.startswith("Primary source:")
            and not p.startswith("Continue:")
        ),
        "",
    )
    return text if len(text) <= limit else text[: limit - 1].rsplit(" ", 1)[0] + "…"


def slug(title: str) -> str:
    value = title.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


def build(source: Path, output: Path) -> int:
    text = source.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    entries = []
    for index, match in enumerate(matches):
        date_text, title = match.groups()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        date = datetime.strptime(date_text, "%B %d, %Y").replace(tzinfo=timezone.utc)
        entries.append((date, date_text, title, plain_summary(text[match.end():end])))
    entries.sort(key=lambda item: (item[0], item[2].lower()), reverse=True)

    rss = ET.Element("rss", {"version": "2.0", "xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "GlassesResearch — Research & News"
    ET.SubElement(channel, "link").text = f"{SITE}/docs/RESEARCH_NEWS/"
    ET.SubElement(channel, "description").text = "Verified smart-glasses research and news from GlassesResearch. RSS carries summaries; full articles live at GlassesResearch.org."
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "atom:link", {"href": f"{SITE}/feed.xml", "rel": "self", "type": "application/rss+xml"})
    ET.SubElement(channel, "lastBuildDate").text = email.utils.format_datetime(datetime.now(timezone.utc))

    for date, date_text, title, summary in entries:
        anchor = f"{date_text.lower().replace(' ', '-').replace(',', '')}-{slug(title)}"
        url = f"{SITE}/docs/RESEARCH_NEWS/#{anchor}"
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = title
        ET.SubElement(item, "link").text = url
        ET.SubElement(item, "guid", {"isPermaLink": "true"}).text = url
        ET.SubElement(item, "pubDate").text = email.utils.format_datetime(date)
        ET.SubElement(item, "description").text = summary

    output.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(rss, space="  ")
    output.write_bytes(ET.tostring(rss, encoding="utf-8", xml_declaration=True))
    return len(entries)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("docs/RESEARCH_NEWS.md"))
    parser.add_argument("--output", type=Path, default=Path(".site-src/feed.xml"))
    args = parser.parse_args()
    count = build(args.source, args.output)
    if count == 0:
        raise SystemExit("RSS build found no dated Research & News entries")
    print(f"RSS feed built with {count} items: {args.output}")


if __name__ == "__main__":
    main()
