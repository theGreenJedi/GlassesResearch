#!/usr/bin/env python3
"""Verify the built GlassesResearch site exposes essential search-discovery signals."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

SITE = Path("site")
CANONICAL_ORIGIN = "https://glassesresearch.org"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not SITE.exists():
        fail("site/ does not exist; run mkdocs build first")

    sitemap = SITE / "sitemap.xml"
    robots = SITE / "robots.txt"
    cname = SITE / "CNAME"

    for required in (sitemap, robots, cname):
        if not required.exists():
            fail(f"missing required discoverability artifact: {required}")

    sitemap_text = sitemap.read_text(encoding="utf-8")
    if f"{CANONICAL_ORIGIN}/" not in sitemap_text:
        fail("sitemap.xml does not contain canonical glassesresearch.org URLs")

    robots_text = robots.read_text(encoding="utf-8")
    if "User-agent: *" not in robots_text or "Allow: /" not in robots_text:
        fail("robots.txt is not explicitly crawlable")
    if f"Sitemap: {CANONICAL_ORIGIN}/sitemap.xml" not in robots_text:
        fail("robots.txt does not advertise the canonical sitemap")

    if cname.read_text(encoding="utf-8").strip() != "glassesresearch.org":
        fail("CNAME does not contain glassesresearch.org")

    html_files = sorted(SITE.rglob("*.html"))
    if not html_files:
        fail("no rendered HTML pages found")

    errors: list[str] = []
    for html_path in html_files:
        text = html_path.read_text(encoding="utf-8")
        if 'rel="canonical"' not in text or CANONICAL_ORIGIN not in text:
            errors.append(f"{html_path}: missing canonical URL")
        if 'property="og:url"' not in text:
            errors.append(f"{html_path}: missing Open Graph URL")
        if 'type="application/ld+json"' not in text:
            errors.append(f"{html_path}: missing JSON-LD")

    if errors:
        fail("discoverability validation failed:\n  " + "\n  ".join(errors[:25]))

    print(
        f"Discoverability checks passed for {len(html_files)} HTML pages; "
        "robots.txt, sitemap.xml, CNAME, canonical URLs, social metadata, and JSON-LD are present."
    )


if __name__ == "__main__":
    main()
