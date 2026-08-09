#!/usr/bin/env python3
"""Verify internal links and static asset references in the built MkDocs site."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

SITE = Path("site").resolve()
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids.add(data["id"] or "")
        for attr in ("href", "src"):
            value = data.get(attr)
            if value:
                self.links.append((attr, value))


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


def resolve_target(page: Path, raw: str) -> tuple[Path | None, str | None]:
    parsed = urlparse(raw)
    if parsed.scheme in SKIP_SCHEMES or raw.startswith("//"):
        return None, None

    fragment = unquote(parsed.fragment) if parsed.fragment else None
    target_path = unquote(parsed.path)

    if not target_path:
        return page, fragment

    if target_path.startswith("/"):
        target = SITE / target_path.lstrip("/")
    else:
        target = page.parent / target_path

    target = target.resolve()
    try:
        target.relative_to(SITE)
    except ValueError:
        return target, fragment

    if target.is_dir():
        target = target / "index.html"
    elif not target.suffix:
        html_candidate = target / "index.html"
        file_candidate = target.with_suffix(".html")
        if html_candidate.exists():
            target = html_candidate
        elif file_candidate.exists():
            target = file_candidate

    return target, fragment


def main() -> int:
    if not SITE.exists():
        print("ERROR: site/ does not exist; build the site first.")
        return 1

    pages = sorted(SITE.rglob("*.html"))
    parsed_pages: dict[Path, PageParser] = {}
    failures: list[str] = []
    checked = 0

    for page in pages:
        parser = parsed_pages.setdefault(page.resolve(), parse_page(page))
        for attr, raw in parser.links:
            target, fragment = resolve_target(page.resolve(), raw)
            if target is None:
                continue
            checked += 1
            try:
                target.relative_to(SITE)
            except ValueError:
                failures.append(f"{page.relative_to(SITE)}: {attr} escapes site root: {raw}")
                continue
            if not target.exists():
                failures.append(f"{page.relative_to(SITE)}: missing target for {attr}={raw!r}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed_pages.setdefault(target.resolve(), parse_page(target))
                if fragment not in target_parser.ids:
                    failures.append(
                        f"{page.relative_to(SITE)}: missing fragment #{fragment} in "
                        f"{target.relative_to(SITE)} from {raw!r}"
                    )

    if failures:
        print(f"Built-site link audit failed with {len(failures)} issue(s):")
        for item in failures:
            print(f"ERROR {item}")
        return 1

    print(f"Built-site link audit passed: {len(pages)} HTML pages, {checked} internal href/src references checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
