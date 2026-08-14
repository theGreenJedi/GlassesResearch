#!/usr/bin/env python3
"""Add crawlable canonical-model links to staged editorial research pages."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

MODEL_HEADING = re.compile(r"^(#{2,3})\s+(GLS-\d{4})\s+—\s+(.+)$", re.MULTILINE)
TABLE_ROW = re.compile(r"^(\|\s*(GLS-\d{4})\s*\|\s*[^|]+\|\s*)([^|]+?)(\s*\|)", re.MULTILINE)
MODEL_ID = re.compile(r"\bGLS-\d{4}\b")


def canonical(model_id: str) -> str:
    return f"/models/catalog/{model_id.lower()}/"


def link_model_headings(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        model_id = match.group(2)
        following = text[match.end():match.end() + 180]
        if canonical(model_id) in following:
            return match.group(0)
        count += 1
        return f"{match.group(0)}\n\n[Canonical model page]({canonical(model_id)})"

    path.write_text(MODEL_HEADING.sub(replace, text), encoding="utf-8")
    return count


def link_catalog_rows(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        model_id, model = match.group(2), match.group(3).strip()
        if model.startswith("["):
            return match.group(0)
        count += 1
        return f"{match.group(1)}[{model}]({canonical(model_id)}){match.group(4)}"

    path.write_text(TABLE_ROW.sub(replace, text), encoding="utf-8")
    return count


def link_lineage_ids(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if "<!-- generated-canonical-model-links -->" in text:
        return 0
    ids = sorted(set(MODEL_ID.findall(text)))
    if not ids:
        return 0
    links = " · ".join(f"[{model_id}]({canonical(model_id)})" for model_id in ids)
    path.write_text(text + f"\n\n## Canonical model pages\n\n<!-- generated-canonical-model-links -->\n{links}\n", encoding="utf-8")
    return len(ids)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    heading_links = sum(link_model_headings(path) for path in sorted((args.output_root / "models").glob("PROFILES*.md")))
    heading_links += sum(link_model_headings(path) for path in sorted((args.output_root / "docs" / "report-cards").glob("*.md")))
    catalog_links = link_catalog_rows(args.output_root / "models" / "THE_LIST.md")
    lineage_links = sum(link_lineage_ids(path) for path in sorted((args.output_root / "lineages").glob("*.md")))
    print(f"Added {heading_links} heading links, {catalog_links} catalog links, and {lineage_links} lineage links")


if __name__ == "__main__":
    main()
