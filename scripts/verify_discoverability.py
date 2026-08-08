#!/usr/bin/env python3
"""Audit the built GlassesResearch site for search-discovery regressions."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

SITE = Path("site")
CANONICAL_ORIGIN = "https://glassesresearch.org"
REQUIRED_SCHEMA_TYPES = {"Organization", "WebSite", "WebPage", "BreadcrumbList"}


class PageSignals(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.canonicals: list[str] = []
        self.meta_name: dict[str, list[str]] = defaultdict(list)
        self.meta_property: dict[str, list[str]] = defaultdict(list)
        self.json_ld: list[str] = []
        self._in_json_ld = False
        self._json_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonicals.append(values.get("href", ""))
        elif tag == "meta":
            content = values.get("content", "").strip()
            if values.get("name"):
                self.meta_name[values["name"]].append(content)
            if values.get("property"):
                self.meta_property[values["property"]].append(content)
        elif tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_parts).strip())
            self._in_json_ld = False
            self._json_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._in_json_ld:
            self._json_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def public_url(html_path: Path) -> str:
    relative = html_path.relative_to(SITE)
    if relative == Path("index.html"):
        return f"{CANONICAL_ORIGIN}/"
    if relative.name == "index.html":
        return f"{CANONICAL_ORIGIN}/{relative.parent.as_posix()}/"
    return f"{CANONICAL_ORIGIN}/{relative.as_posix()}"


def schema_types(payload: object) -> set[str]:
    found: set[str] = set()
    if isinstance(payload, dict):
        schema_type = payload.get("@type")
        if isinstance(schema_type, str):
            found.add(schema_type)
        elif isinstance(schema_type, list):
            found.update(item for item in schema_type if isinstance(item, str))
        for value in payload.values():
            found.update(schema_types(value))
    elif isinstance(payload, list):
        for value in payload:
            found.update(schema_types(value))
    return found


def audit_sitemap(sitemap: Path, html_files: list[Path], errors: list[str]) -> None:
    try:
        root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml is not valid XML: {exc}")
        return

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text.strip() for node in root.findall("sm:url/sm:loc", namespace) if node.text]
    if not locations:
        errors.append("sitemap.xml contains no URL locations")
        return
    if len(locations) != len(set(locations)):
        errors.append("sitemap.xml contains duplicate URLs")
    invalid = [url for url in locations if not url.startswith(f"{CANONICAL_ORIGIN}/")]
    if invalid:
        errors.append(f"sitemap.xml contains non-canonical URLs: {invalid[:5]}")

    expected = {public_url(path) for path in html_files}
    missing = sorted(expected.difference(locations))
    if missing:
        errors.append(f"sitemap.xml is missing rendered pages: {missing[:10]}")


def main() -> None:
    if not SITE.exists():
        fail("site/ does not exist; run mkdocs build first")

    sitemap = SITE / "sitemap.xml"
    robots = SITE / "robots.txt"
    cname = SITE / "CNAME"

    for required in (sitemap, robots, cname):
        if not required.exists():
            fail(f"missing required discoverability artifact: {required}")

    robots_text = robots.read_text(encoding="utf-8")
    if "User-agent: *" not in robots_text or "Allow: /" not in robots_text:
        fail("robots.txt is not explicitly crawlable")
    if f"Sitemap: {CANONICAL_ORIGIN}/sitemap.xml" not in robots_text:
        fail("robots.txt does not advertise the canonical sitemap")

    if cname.read_text(encoding="utf-8").strip() != "glassesresearch.org":
        fail("CNAME does not contain glassesresearch.org")

    html_files = sorted(path for path in SITE.rglob("*.html") if path.name != "404.html")
    if not html_files:
        fail("no rendered HTML pages found")

    errors: list[str] = []
    descriptions: dict[str, list[str]] = defaultdict(list)
    audit_sitemap(sitemap, html_files, errors)

    for html_path in html_files:
        text = html_path.read_text(encoding="utf-8")
        parser = PageSignals()
        parser.feed(text)
        url = public_url(html_path)

        if not parser.title or "GlassesResearch" not in parser.title:
            errors.append(f"{html_path}: missing or incomplete HTML title")

        if parser.canonicals != [url]:
            errors.append(f"{html_path}: canonical must be exactly {url!r}; found {parser.canonicals!r}")

        descriptions_for_page = [value for value in parser.meta_name.get("description", []) if value]
        if not descriptions_for_page:
            errors.append(f"{html_path}: missing meta description")
        else:
            description = descriptions_for_page[0]
            if len(description) < 40:
                errors.append(f"{html_path}: meta description is too short")
            descriptions[description].append(str(html_path))

        if parser.meta_property.get("og:url") != [url]:
            errors.append(f"{html_path}: Open Graph URL must match canonical URL")
        if not parser.meta_property.get("og:title") or not parser.meta_property.get("og:description"):
            errors.append(f"{html_path}: missing Open Graph title/description")
        if not parser.meta_name.get("twitter:card"):
            errors.append(f"{html_path}: missing Twitter card metadata")

        parsed_schema: list[object] = []
        for block in parser.json_ld:
            try:
                parsed_schema.append(json.loads(block))
            except json.JSONDecodeError as exc:
                errors.append(f"{html_path}: invalid JSON-LD: {exc}")
        types: set[str] = set()
        for payload in parsed_schema:
            types.update(schema_types(payload))
        missing_types = REQUIRED_SCHEMA_TYPES.difference(types)
        if missing_types:
            errors.append(f"{html_path}: missing Schema.org types {sorted(missing_types)}")

        relative = html_path.relative_to(SITE).as_posix()
        if relative.startswith("docs/faq/") and relative.split("/")[-2][:2].isdigit():
            if "FAQPage" not in types:
                errors.append(f"{html_path}: question collection is missing FAQPage structured data")

    duplicates = {description: paths for description, paths in descriptions.items() if len(paths) > 1}
    for description, paths in list(duplicates.items())[:10]:
        errors.append(f"duplicate meta description on {paths}: {description!r}")

    if errors:
        fail("discoverability audit failed:\n  " + "\n  ".join(errors[:50]))

    print(
        f"Discoverability audit passed for {len(html_files)} indexable HTML pages: "
        "canonical URLs, unique descriptions, social metadata, structured data, FAQ schema, "
        "robots.txt, sitemap.xml, and CNAME are coherent."
    )


if __name__ == "__main__":
    main()
