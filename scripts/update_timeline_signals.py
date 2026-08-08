#!/usr/bin/env python3
"""Discover provisional smart-glasses timeline signals from curated primary RSS feeds.

This script never edits canonical timeline/events.json. It only maintains the
provisional timeline/auto-events.json layer shown separately on the website.
"""

from __future__ import annotations

import email.utils
import hashlib
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "timeline" / "sources.json"
CANONICAL = ROOT / "timeline" / "events.json"
OUTPUT = ROOT / "timeline" / "auto-events.json"
USER_AGENT = "GlassesResearch-TimelineWatch/1.0 (+https://glassesresearch.org/)"
MAX_EVENTS = 120


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def text(node: ET.Element | None) -> str:
    if node is None or node.text is None:
        return ""
    return re.sub(r"\s+", " ", node.text).strip()


def first_text(item: ET.Element, names: tuple[str, ...]) -> str:
    for child in item.iter():
        local = child.tag.rsplit("}", 1)[-1].lower()
        if local in names:
            value = text(child)
            if value:
                return value
    return ""


def entry_link(item: ET.Element) -> str:
    for child in item.iter():
        local = child.tag.rsplit("}", 1)[-1].lower()
        if local != "link":
            continue
        href = child.attrib.get("href")
        if href:
            return href.strip()
        value = text(child)
        if value.startswith("http"):
            return value
    return ""


def parse_date(value: str) -> str | None:
    if not value:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed is not None:
            return parsed.date().isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    normalized = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized).date().isoformat()
    except ValueError:
        return None


def fetch_feed(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def iter_entries(payload: bytes):
    root = ET.fromstring(payload)
    for node in root.iter():
        local = node.tag.rsplit("}", 1)[-1].lower()
        if local in {"item", "entry"}:
            yield node


def stable_id(source_id: str, link: str, title: str) -> str:
    digest = hashlib.sha256(f"{source_id}\n{link}\n{title}".encode("utf-8")).hexdigest()[:16]
    return f"AUTO-{digest.upper()}"


def relevant(title: str, summary: str, terms: list[str]) -> bool:
    haystack = f"{title} {summary}".lower()
    return any(term.lower() in haystack for term in terms)


def significance(title: str, summary: str, major_terms: list[str]) -> int:
    haystack = f"{title} {summary}".lower()
    return 4 if any(term.lower() in haystack for term in major_terms) else 3


def main() -> int:
    config = load(CONFIG)
    canonical = load(CANONICAL)
    existing = load(OUTPUT) if OUTPUT.exists() else {"events": []}

    canonical_urls = {
        url
        for event in canonical.get("events", [])
        for url in event.get("sources", [])
        if isinstance(url, str)
    }
    events_by_id = {
        event["id"]: event
        for event in existing.get("events", [])
        if isinstance(event, dict) and isinstance(event.get("id"), str)
    }

    failures: list[str] = []
    for source in config.get("sources", []):
        try:
            payload = fetch_feed(source["url"])
            entries = list(iter_entries(payload))
        except Exception as exc:  # watcher should survive one unavailable source
            failures.append(f"{source.get('id')}: {exc}")
            continue

        for item in entries:
            title = first_text(item, ("title",))
            summary = first_text(item, ("description", "summary", "content"))
            link = entry_link(item)
            published = first_text(item, ("pubdate", "published", "updated", "date"))
            event_date = parse_date(published)
            if not title or not link or not event_date:
                continue
            if link in canonical_urls:
                continue
            if not relevant(title, summary, config.get("include_terms", [])):
                continue

            event_id = stable_id(source["id"], link, title)
            events_by_id[event_id] = {
                "id": event_id,
                "date": event_date,
                "title": title,
                "summary": "Automatically discovered primary-source signal. Review the linked source before promotion to canonical history.",
                "category": "industry",
                "state": "provisional",
                "significance": significance(title, summary, config.get("major_terms", [])),
                "evidence": source.get("evidence", "primary"),
                "companies": [source.get("name", source["id"])],
                "models": [],
                "sources": [link],
                "source_feed": source["id"]
            }

    events = sorted(events_by_id.values(), key=lambda event: (event["date"], event["id"]), reverse=True)
    events = events[:MAX_EVENTS]
    document = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "events": events,
    }
    OUTPUT.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Timeline watcher retained {len(events)} provisional signals")
    for failure in failures:
        print(f"WARNING: {failure}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
