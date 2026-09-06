#!/usr/bin/env python3
"""Verify the published llms.txt research-navigation contract."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ORIGIN = "https://glassesresearch.org"
REPOSITORY = "https://github.com/theGreenJedi/GlassesResearch"
LINK_RE = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")

REQUIRED_INTERNAL = {
    "/models/THE_LIST/": "models/THE_LIST.md",
    "/models/": "models/README.md",
    "/docs/REPORT_CARD/": "docs/REPORT_CARD.md",
    "/evidence/": "evidence/README.md",
    "/lineages/": "lineages/README.md",
    "/dataset/": "dataset/index.md",
    "/data/public/models.json": "data/public/models.json",
    "/gls/": "gls/index.md",
    "/data/gls-index.json": "data/gls-index.json",
    "/docs/news/": "docs/news/README.md",
    "/hacking/": "hacking/README.md",
    "/docs/REFERENCE_DESK/": "docs/REFERENCE_DESK.md",
    "/CITATION.cff": "CITATION.cff",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()

    root = args.site_root
    index = root / "llms.txt"
    if not index.exists():
        fail(f"missing llms.txt at {index}")

    text = index.read_text(encoding="utf-8").strip()
    if not text.startswith("# GlassesResearch"):
        fail("llms.txt must identify GlassesResearch at the top")
    if "navigation index, not an alternate source of product truth" not in text:
        fail("llms.txt is missing its evidence-boundary disclaimer")

    links = LINK_RE.findall(text)
    if len(links) != len(set(links)):
        fail("llms.txt contains duplicate URLs")

    expected_urls = {f"{ORIGIN}{path}" for path in REQUIRED_INTERNAL} | {REPOSITORY}
    missing = sorted(expected_urls.difference(links))
    if missing:
        fail(f"llms.txt is missing required research entrances: {missing}")

    for link in links:
        parsed = urlparse(link)
        if parsed.scheme != "https" or parsed.query or parsed.fragment:
            fail(f"llms.txt link must be stable HTTPS without query/fragment: {link}")
        if link.startswith(ORIGIN):
            path = parsed.path
            target = REQUIRED_INTERNAL.get(path)
            if target is None:
                fail(f"unvalidated internal llms.txt route: {path}")
            if not (root / target).exists():
                fail(f"llms.txt route {path} points to missing staged resource {target}")
        elif link != REPOSITORY:
            fail(f"unexpected external llms.txt destination: {link}")

    print(f"llms.txt contract passed: {len(REQUIRED_INTERNAL)} internal research entrances and repository provenance are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
