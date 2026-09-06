#!/usr/bin/env python3
"""Add guaranteed crawlable public links and research summaries to staged pages."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MODEL_HEADING = re.compile(r"^(#{2,3})\s+(GLS-\d{4})\s+—\s+(.+)$", re.MULTILINE)
CATALOG_ID_ROW = re.compile(
    r"^(\|\s*)(?:\[(GLS-\d{4})\]\([^)]+\)|(GLS-\d{4}))(\s*\|)",
    re.MULTILINE,
)
MODEL_ID = re.compile(r"\bGLS-\d{4}\b")
PUBLIC_INDEX_REL = Path("docs/SITE_INDEX.md")
PUBLIC_INDEX_MARKER = "<!-- generated-public-site-index-link -->"
PUBLIC_PAGE_SUFFIXES = {".md", ".markdown", ".html"}


def canonical(model_id: str) -> str:
    return f"/models/catalog/{model_id.lower()}/"


def link_model_headings(path: Path, valid_ids: set[str]) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        model_id = match.group(2)
        if model_id not in valid_ids:
            return match.group(0)
        following = text[match.end():match.end() + 180]
        if canonical(model_id) in following:
            return match.group(0)
        count += 1
        return f"{match.group(0)}\n\n[Canonical model page]({canonical(model_id)})"

    path.write_text(MODEL_HEADING.sub(replace, text), encoding="utf-8")
    return count


def ensure_catalog_discoverability(output_root: Path, valid_ids: set[str]) -> int:
    """Guarantee one human-facing ledger link to every generated canonical page."""
    catalog_dir = output_root / "models" / "catalog"
    missing_pages = sorted(
        model_id
        for model_id in valid_ids
        if not (catalog_dir / f"{model_id.lower()}.md").is_file()
    )
    if missing_pages:
        raise ValueError(
            "generated canonical model pages missing before discoverability linking: "
            + ", ".join(missing_pages[:20])
        )

    path = output_root / "models" / "THE_LIST.md"
    text = path.read_text(encoding="utf-8")
    linked: set[str] = set()

    def replace(match: re.Match[str]) -> str:
        model_id = match.group(2) or match.group(3)
        if model_id not in valid_ids:
            return match.group(0)
        linked.add(model_id)
        return f"{match.group(1)}[{model_id}]({canonical(model_id)}){match.group(4)}"

    updated = CATALOG_ID_ROW.sub(replace, text)
    missing_links = sorted(valid_ids - linked)
    if missing_links:
        raise ValueError(
            "canonical catalog discoverability links missing for: "
            + ", ".join(missing_links[:20])
        )

    path.write_text(updated, encoding="utf-8")
    return len(linked)


def link_lineage_ids(path: Path, valid_ids: set[str]) -> int:
    text = path.read_text(encoding="utf-8")
    if "<!-- generated-canonical-model-links -->" in text:
        return 0
    ids = sorted(set(MODEL_ID.findall(text)) & valid_ids)
    if not ids:
        return 0
    links = " · ".join(f"[{model_id}]({canonical(model_id)})" for model_id in ids)
    path.write_text(text + f"\n\n## Canonical model pages\n\n<!-- generated-canonical-model-links -->\n{links}\n", encoding="utf-8")
    return len(ids)


def _public_index_link(index_path: Path, page: Path, output_root: Path) -> str:
    rel = page.relative_to(output_root)
    if rel.parts and rel.parts[0] == "docs":
        return Path(*rel.parts[1:]).as_posix()
    return "../" + rel.as_posix()


def ensure_public_site_index(output_root: Path) -> int:
    """Give every staged public page an intentional inbound path without weakening verification."""
    index_path = output_root / PUBLIC_INDEX_REL
    pages = sorted(
        path
        for path in output_root.rglob("*")
        if path.is_file()
        and path != index_path
        and path.suffix.lower() in PUBLIC_PAGE_SUFFIXES
    )

    grouped: dict[str, list[Path]] = {}
    for page in pages:
        rel = page.relative_to(output_root)
        section = rel.parts[0] if len(rel.parts) > 1 else "Site root"
        grouped.setdefault(section, []).append(page)

    lines = [
        "# Complete Public Page Index",
        "",
        "This generated directory lists every public research page included in the current site build. "
        "It is a completeness backstop for readers, crawlers, and publication validation; the curated navigation remains the fastest way to browse GlassesResearch.",
        "",
        "[Back to Tools](TOOLS.md)",
    ]
    for section in sorted(grouped, key=lambda value: (value != "Site root", value.lower())):
        lines.extend(["", f"## {section}", ""])
        for page in grouped[section]:
            rel = page.relative_to(output_root)
            target = _public_index_link(index_path, page, output_root)
            lines.append(f"- [`{rel.as_posix()}`]({target})")

    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    tools_path = output_root / "docs" / "TOOLS.md"
    if not tools_path.is_file():
        raise ValueError("docs/TOOLS.md is missing; cannot anchor the complete public page index")
    tools = tools_path.read_text(encoding="utf-8")
    if PUBLIC_INDEX_MARKER not in tools:
        tools += (
            "\n\n---\n\n## Complete public page index\n\n"
            f"{PUBLIC_INDEX_MARKER}\n"
            "[Browse every published page](SITE_INDEX.md) — the generated completeness index for the current public build.\n"
        )
        tools_path.write_text(tools, encoding="utf-8")
    return len(pages)


def load_map(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {row["id"]: row for row in payload.get("records", [])}


def yn(capabilities: dict, field: str) -> str:
    state = capabilities.get(field, {}).get("value", "unknown")
    return {"yes": "Yes", "no": "No", "unknown": "Not yet verified"}.get(state, str(state))


def research_links(capabilities: dict) -> list[str]:
    links = ["[Compare in the Glasses Finder](/docs/COMPARISON_ENGINE/)", "[Industry timeline](/docs/INDUSTRY_TIMELINE/)"]
    if capabilities.get("bluetooth", {}).get("value") == "yes":
        links.append("[Bluetooth and BLE research](/docs/BLE/)")
    if any(capabilities.get(k, {}).get("value") == "yes" for k in ("sdk_api", "open_source", "self_hostable")):
        links.append("[Firmware research](/docs/Firmware/)")
    return links


def enrich_catalog_pages(output_root: Path) -> int:
    devices = load_map(output_root / "data" / "devices.json")
    capabilities = load_map(output_root / "data" / "finder-capabilities.json")
    comparisons = load_map(output_root / "data" / "comparisons.json")
    scores = load_map(output_root / "data" / "report-card-scores.json")
    changed = 0

    for model_id, record in devices.items():
        path = output_root / "models" / "catalog" / f"{model_id.lower()}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "<!-- generated-research-snapshot -->" in text:
            continue

        caps = capabilities.get(model_id, {}).get("capabilities", {})
        yes_count = sum(v.get("value") == "yes" for v in caps.values())
        no_count = sum(v.get("value") == "no" for v in caps.values())
        unknown_count = sum(v.get("value") == "unknown" for v in caps.values())
        comp = comparisons.get(model_id, {}).get("fields", {})
        verified_specs = sum(
            fact.get("evidence") != "unknown" and str(fact.get("value", "")).lower() != "unknown"
            for fact in comp.values()
        )
        source_count = sum(1 for item in record.get("links", []) if item.get("kind") == "external")
        report_depth = "A GlassesResearch Report Card is available." if model_id in scores else "No Report Card has been published yet."
        links = " · ".join(research_links(caps))

        snapshot = f'''\n## Research snapshot\n\n<!-- generated-research-snapshot -->\n**{record['maker']} {record['model']}** is cataloged as **{record['type']}** with lifecycle state **{record['state']}** and era/release year **{record['era']}**. GlassesResearch currently has **{yes_count} confirmed capabilities**, **{no_count} verified absences**, and **{unknown_count} unresolved capability fields** for this model. The structured comparison record contains **{verified_specs} verified specification fields**, and this page links to **{source_count} external source{'s' if source_count != 1 else ''}**. {report_depth}\n\n### Common questions\n\n- **Does it have a camera?** {yn(caps, 'camera')}\n- **Does it have a display?** {yn(caps, 'display')}\n- **Does it support Bluetooth?** {yn(caps, 'bluetooth')}\n- **Is an SDK or API verified?** {yn(caps, 'sdk_api')}\n- **Is open-source support verified?** {yn(caps, 'open_source')}\n- **Is offline operation verified?** {yn(caps, 'offline_operation')}\n\n### Continue researching\n\n{links}\n'''
        marker = "\n## At a glance\n"
        if marker not in text:
            continue
        text = text.replace(marker, snapshot + marker, 1)
        path.write_text(text, encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    valid_ids = set(load_map(args.output_root / "data" / "devices.json"))
    heading_links = sum(link_model_headings(path, valid_ids) for path in sorted((args.output_root / "models").glob("PROFILES*.md")))
    heading_links += sum(link_model_headings(path, valid_ids) for path in sorted((args.output_root / "docs" / "report-cards").glob("*.md")))
    catalog_links = ensure_catalog_discoverability(args.output_root, valid_ids)
    lineage_links = sum(link_lineage_ids(path, valid_ids) for path in sorted((args.output_root / "lineages").glob("*.md")))
    enriched = enrich_catalog_pages(args.output_root)
    public_index_links = ensure_public_site_index(args.output_root)
    print(
        f"Added {heading_links} heading links, guaranteed {catalog_links} catalog discovery links, "
        f"{lineage_links} lineage links, enriched {enriched} canonical model pages, and indexed "
        f"{public_index_links} public pages"
    )


if __name__ == "__main__":
    main()
