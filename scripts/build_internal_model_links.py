#!/usr/bin/env python3
"""Add crawlable model links and evidence-led research summaries to staged pages."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MODEL_HEADING = re.compile(r"^(#{2,3})\s+(GLS-\d{4})\s+—\s+(.+)$", re.MULTILINE)
TABLE_ROW = re.compile(r"^(\|\s*(GLS-\d{4})\s*\|\s*[^|]+\|\s*)([^|]+?)(\s*\|)", re.MULTILINE)
MODEL_ID = re.compile(r"\bGLS-\d{4}\b")


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


def report_card_depth(score_record: dict | None) -> str:
    if not score_record:
        return "No Report Card has been published yet."

    summary = score_record.get("freshness_summary")
    if not isinstance(summary, dict):
        return "A GlassesResearch Report Card is available."

    resolved = int(summary.get("resolved_dimensions", 0) or 0)
    fresh = int(summary.get("fresh", 0) or 0)
    aging = int(summary.get("aging", 0) or 0)
    stale = int(summary.get("stale", 0) or 0)
    unknown = int(summary.get("unknown", 0) or 0)
    unscored = int(summary.get("unscored", 0) or 0)

    if not resolved:
        return (
            "A GlassesResearch Report Card is available, but its Core subjects remain unscored. "
            "[Read the freshness method](/docs/REPORT_CARD_FRESHNESS/)."
        )

    return (
        f"A GlassesResearch Report Card is available. Across its **{resolved} resolved Core score "
        f"dimension{'s' if resolved != 1 else ''}**, evidence freshness is **{fresh} fresh**, "
        f"**{aging} aging**, **{stale} stale**, and **{unknown} freshness-unknown**; "
        f"**{unscored} Core dimension{'s remain' if unscored != 1 else ' remains'} unscored**. "
        "Freshness refers to the evidence supporting each score, not the age of this page. "
        "[Read the freshness method](/docs/REPORT_CARD_FRESHNESS/)."
    )


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
        report_depth = report_card_depth(scores.get(model_id))
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
    catalog_links = link_catalog_rows(args.output_root / "models" / "THE_LIST.md")
    lineage_links = sum(link_lineage_ids(path, valid_ids) for path in sorted((args.output_root / "lineages").glob("*.md")))
    enriched = enrich_catalog_pages(args.output_root)
    print(f"Added {heading_links} heading links, {catalog_links} catalog links, {lineage_links} lineage links, and enriched {enriched} canonical model pages")


if __name__ == "__main__":
    main()