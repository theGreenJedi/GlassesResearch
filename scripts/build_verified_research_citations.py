#!/usr/bin/env python3
"""Build citation exports for the verified GlassesResearch publication stream."""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from verified_changes import DEFAULT_CHANGES, validate

ORIGIN = "https://glassesresearch.org"
STATUS_MARKER = "**Status:** Verified"


def bib_escape(value: object) -> str:
    return (
        str(value)
        .replace("\\", "\\textbackslash{}")
        .replace("{", "\\{")
        .replace("}", "\\}")
        .replace("&", "\\&")
    )


def date_parts(value: str) -> list[int]:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return [parsed.year, parsed.month, parsed.day]


def citation_record(event: dict) -> dict:
    publication = event["publication"]
    return {
        "id": event["id"].lower(),
        "type": "webpage",
        "title": publication["title"],
        "author": [{"literal": "GlassesResearch"}],
        "publisher": "GlassesResearch",
        "issued": {"date-parts": [date_parts(publication["published_at"])]},
        "URL": publication["canonical_url"],
        "genre": "Verified research publication",
        "note": f"Verified GlassesResearch publication {event['id']}",
    }


def bibtex(event: dict) -> str:
    publication = event["publication"]
    event_id = event["id"]
    key = event_id.lower().replace("-", "")
    title = bib_escape(publication["title"])
    published = date_parts(publication["published_at"])
    return (
        f"@misc{{{key},\n"
        "  author = {{GlassesResearch}},\n"
        f"  title = {{{{{title}}}}},\n"
        f"  year = {{{published[0]}}},\n"
        f"  month = {{{published[1]}}},\n"
        f"  day = {{{published[2]}}},\n"
        f"  howpublished = {{\\url{{{publication['canonical_url']}}}}},\n"
        f"  note = {{Verified GlassesResearch publication {event_id}}}\n"
        "}\n"
    )


def standalone_article_source(site_root: Path, canonical_url: str) -> Path | None:
    parsed = urlparse(canonical_url)
    if parsed.scheme != "https" or parsed.netloc != "glassesresearch.org" or parsed.fragment:
        return None
    prefix = "/docs/news/articles/"
    if not parsed.path.startswith(prefix) or not parsed.path.endswith("/"):
        return None
    relative = parsed.path.strip("/") + ".md"
    path = site_root / relative
    return path if path.is_file() else None


def patch_standalone_article(path: Path, event_id: str) -> None:
    text = path.read_text(encoding="utf-8")
    if STATUS_MARKER not in text:
        raise RuntimeError(f"Verified publication article lacks status marker: {path}")
    if "data/citations/verified-research/" in text:
        raise RuntimeError(f"Citation links were present before the citation build: {path}")
    suffix = event_id.lower()
    links = (
        f"\n\nCite this research: [BibTeX](/data/citations/verified-research/{suffix}.bib) · "
        f"[CSL-JSON](/data/citations/verified-research/{suffix}.json)"
    )
    text = text.replace(STATUS_MARKER, STATUS_MARKER + links, 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    args = parser.parse_args()

    events = validate(args.changes)["events"]
    out_dir = args.site_root / "data" / "citations" / "verified-research"
    out_dir.mkdir(parents=True, exist_ok=True)

    index_records = []
    aggregate = []
    patched_articles = 0

    for event in events:
        event_id = event["id"]
        publication = event["publication"]
        suffix = event_id.lower()

        csl = citation_record(event)
        (out_dir / f"{suffix}.json").write_text(
            json.dumps(csl, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        bib = bibtex(event)
        (out_dir / f"{suffix}.bib").write_text(bib, encoding="utf-8")
        aggregate.append(bib)
        index_records.append(
            {
                "id": event_id,
                "title": publication["title"],
                "published_at": publication["published_at"],
                "canonical_url": publication["canonical_url"],
                "bibtex": f"{ORIGIN}/data/citations/verified-research/{suffix}.bib",
                "csl_json": f"{ORIGIN}/data/citations/verified-research/{suffix}.json",
            }
        )

        article = standalone_article_source(args.site_root, publication["canonical_url"])
        if article is not None:
            patch_standalone_article(article, event_id)
            patched_articles += 1

    index = {
        "schema_version": 1,
        "record_count": len(index_records),
        "semantics": "One citation record per verified GRE publication event; the citation URL remains the human-readable canonical publication surface.",
        "records": index_records,
    }
    (out_dir / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (out_dir / "glassesresearch-verified-research.bib").write_text(
        "\n".join(aggregate), encoding="utf-8"
    )

    print(
        f"Built citation exports for {len(events)} verified publications; "
        f"citation links added to {patched_articles} standalone research articles"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
