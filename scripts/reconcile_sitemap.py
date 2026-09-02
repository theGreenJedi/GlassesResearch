#!/usr/bin/env python3
"""Make the deployed sitemap an exact superset of rendered public HTML pages.

MkDocs normally generates sitemap.xml for us. GlassesResearch additionally audits that
*every* rendered public page is discoverable from that sitemap. This reconciliation step
preserves MkDocs' existing entries/metadata, adds any rendered pages the theme template
omitted, removes stale/non-canonical duplicates, and keeps sitemap.xml.gz in sync.
"""
from __future__ import annotations

import argparse
import gzip
import xml.etree.ElementTree as ET
from pathlib import Path

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", SITEMAP_NS)


def public_url(site_dir: Path, html_path: Path, origin: str) -> str:
    relative = html_path.relative_to(site_dir)
    root = origin.rstrip("/")
    if relative == Path("index.html"):
        return root + "/"
    if relative.name == "index.html":
        return f"{root}/{relative.parent.as_posix()}/"
    return f"{root}/{relative.as_posix()}"


def reconcile(site_dir: Path, origin: str) -> tuple[int, int, int]:
    sitemap = site_dir / "sitemap.xml"
    if not sitemap.exists():
        raise SystemExit(f"missing MkDocs sitemap: {sitemap}")

    try:
        root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        raise SystemExit(f"invalid MkDocs sitemap: {exc}") from exc

    tag = f"{{{SITEMAP_NS}}}url"
    loc_tag = f"{{{SITEMAP_NS}}}loc"
    canonical_prefix = origin.rstrip("/") + "/"

    # Preserve one canonical MkDocs entry per URL, including any existing lastmod or
    # changefreq metadata. Non-canonical or duplicate entries are deliberately dropped.
    entries: dict[str, ET.Element] = {}
    for node in list(root.findall(tag)):
        loc = node.find(loc_tag)
        value = (loc.text or "").strip() if loc is not None else ""
        if value.startswith(canonical_prefix) and value not in entries:
            entries[value] = node

    html_files = sorted(path for path in site_dir.rglob("*.html") if path.name != "404.html")
    expected = {public_url(site_dir, path, origin) for path in html_files}

    added = 0
    for url in sorted(expected):
        if url in entries:
            continue
        node = ET.Element(tag)
        loc = ET.SubElement(node, loc_tag)
        loc.text = url
        entries[url] = node
        added += 1

    stale = set(entries).difference(expected)
    for url in stale:
        del entries[url]

    output_root = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    for url in sorted(entries):
        output_root.append(entries[url])

    xml_bytes = ET.tostring(output_root, encoding="utf-8", xml_declaration=True)
    xml_bytes += b"\n"
    sitemap.write_bytes(xml_bytes)
    with gzip.GzipFile(filename="", mode="wb", fileobj=(site_dir / "sitemap.xml.gz").open("wb"), mtime=0) as handle:
        handle.write(xml_bytes)

    return len(expected), added, len(stale)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--origin", default="https://glassesresearch.org")
    args = parser.parse_args()

    expected, added, removed = reconcile(args.site_dir, args.origin)
    print(
        f"Sitemap reconciled to {expected} rendered public pages "
        f"({added} added, {removed} stale/duplicate canonical entries removed)."
    )


if __name__ == "__main__":
    main()
