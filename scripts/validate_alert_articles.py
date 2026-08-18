#!/usr/bin/env python3
"""Require every dispatch-enabled verified alert to resolve to a real site article."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "verified-publications.json"
SITE_ORIGIN = "https://glassesresearch.org"
ARTICLE_PREFIX = "/docs/news/articles/"


def article_path(url: str) -> Path:
    parsed = urlparse(url)
    if f"{parsed.scheme}://{parsed.netloc}" != SITE_ORIGIN:
        raise ValueError(f"alert URL must stay on {SITE_ORIGIN}: {url}")
    if not parsed.path.startswith(ARTICLE_PREFIX) or not parsed.path.endswith("/"):
        raise ValueError(f"dispatch-enabled alert must point to a dated GlassesResearch article: {url}")
    slug = parsed.path[len(ARTICLE_PREFIX):].strip("/")
    if not slug:
        raise ValueError(f"article slug missing: {url}")
    return ROOT / "docs" / "news" / "articles" / f"{slug}.md"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []
    dispatch_count = 0
    for item in manifest.get("publications", []):
        if not item.get("dispatch"):
            continue
        dispatch_count += 1
        publication_id = item.get("id", "<unknown>")
        url = str(item.get("canonical_url", ""))
        try:
            path = article_path(url)
        except ValueError as exc:
            errors.append(f"{publication_id}: {exc}")
            continue
        if not path.is_file():
            errors.append(f"{publication_id}: article file does not exist: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        title = str(item.get("title", "")).strip()
        if title and title not in text:
            errors.append(f"{publication_id}: article does not contain ledger title")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Article-backed alert contract valid: {dispatch_count} dispatch-enabled publications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
