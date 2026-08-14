#!/usr/bin/env python3
"""Fail when a public HTML page has no inbound link from another public page."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href)


def page_url(path: Path) -> str:
    rel = path.relative_to(SITE).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return f"/{rel[:-10]}"
    return f"/{rel}"


def target_url(source: Path, href: str) -> str | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or href.startswith(("mailto:", "tel:", "javascript:")):
        return None
    path = unquote(split.path)
    if not path:
        return page_url(source)
    if path.startswith("/"):
        candidate = SITE / path.lstrip("/")
    else:
        candidate = source.parent / path
    if candidate.is_dir():
        candidate /= "index.html"
    elif candidate.suffix == "":
        candidate /= "index.html"
    try:
        candidate = candidate.resolve().relative_to(SITE.resolve())
    except ValueError:
        return None
    full = SITE / candidate
    return page_url(full) if full.is_file() and full.suffix == ".html" else None


def main() -> int:
    if not SITE.is_dir():
        print("site/ is missing; build the site first", file=sys.stderr)
        return 2
    pages = sorted(SITE.rglob("*.html"))
    inbound = {page_url(page): 0 for page in pages}
    for source in pages:
        parser = LinkParser()
        parser.feed(source.read_text(encoding="utf-8"))
        source_url = page_url(source)
        for href in parser.links:
            target = target_url(source, href)
            if target in inbound and target != source_url:
                inbound[target] += 1
    utility_pages = {"/", "/404.html"}
    orphans = sorted(url for url, count in inbound.items() if count == 0 and url not in utility_pages)
    if orphans:
        print("Public pages with no inbound path:", file=sys.stderr)
        for url in orphans:
            print(f"  {url}", file=sys.stderr)
        return 1
    print(f"Public reachability verified: {len(pages)} HTML pages, no orphan pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
