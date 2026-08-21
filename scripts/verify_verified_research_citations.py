#!/usr/bin/env python3
"""Verify citation exports for the canonical verified publication stream."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from verified_changes import DEFAULT_CHANGES, validate


def standalone_article_source(site_root: Path, canonical_url: str) -> Path | None:
    parsed = urlparse(canonical_url)
    prefix = "/docs/news/articles/"
    if parsed.scheme != "https" or parsed.netloc != "glassesresearch.org" or parsed.fragment:
        return None
    if not parsed.path.startswith(prefix) or not parsed.path.endswith("/"):
        return None
    path = site_root / (parsed.path.strip("/") + ".md")
    return path if path.is_file() else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    args = parser.parse_args()

    events = validate(args.changes)["events"]
    out_dir = args.site_root / "data" / "citations" / "verified-research"
    index_path = out_dir / "index.json"
    aggregate_path = out_dir / "glassesresearch-verified-research.bib"
    if not index_path.is_file() or not aggregate_path.is_file():
        raise SystemExit("Verified-research citation index or aggregate BibTeX is missing")

    index = json.loads(index_path.read_text(encoding="utf-8"))
    records = index.get("records", [])
    if index.get("record_count") != len(events) or len(records) != len(events):
        raise SystemExit("Verified-research citation count drifted from GRE event count")
    by_id = {record.get("id"): record for record in records}
    if len(by_id) != len(events):
        raise SystemExit("Verified-research citation IDs are missing or duplicated")

    aggregate = aggregate_path.read_text(encoding="utf-8")
    standalone_count = 0
    for event in events:
        event_id = event["id"]
        suffix = event_id.lower()
        publication = event["publication"]
        record = by_id.get(event_id)
        if not record:
            raise SystemExit(f"Citation index is missing {event_id}")
        if record.get("canonical_url") != publication["canonical_url"]:
            raise SystemExit(f"Citation URL drifted from canonical publication: {event_id}")

        bib_path = out_dir / f"{suffix}.bib"
        json_path = out_dir / f"{suffix}.json"
        if not bib_path.is_file() or not json_path.is_file():
            raise SystemExit(f"Citation export missing for {event_id}")
        csl = json.loads(json_path.read_text(encoding="utf-8"))
        if csl.get("id") != suffix or csl.get("URL") != publication["canonical_url"]:
            raise SystemExit(f"CSL citation malformed for {event_id}")
        if csl.get("title") != publication["title"] or csl.get("publisher") != "GlassesResearch":
            raise SystemExit(f"CSL publication identity malformed for {event_id}")
        if f"Verified GlassesResearch publication {event_id}" not in csl.get("note", ""):
            raise SystemExit(f"CSL provenance note missing for {event_id}")

        bib = bib_path.read_text(encoding="utf-8")
        if publication["canonical_url"] not in bib or event_id not in bib:
            raise SystemExit(f"BibTeX citation malformed for {event_id}")
        if f"@misc{{{suffix.replace('-', '')}," not in aggregate:
            raise SystemExit(f"Aggregate BibTeX is missing {event_id}")

        article = standalone_article_source(args.site_root, publication["canonical_url"])
        if article is not None:
            standalone_count += 1
            text = article.read_text(encoding="utf-8")
            for marker in (
                f"/data/citations/verified-research/{suffix}.bib",
                f"/data/citations/verified-research/{suffix}.json",
            ):
                if marker not in text:
                    raise SystemExit(f"Standalone article citation link missing for {event_id}: {marker}")

    print(
        f"Verified-research citations validated: {len(events)} event exports, "
        f"{standalone_count} standalone articles expose citation links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
