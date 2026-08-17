#!/usr/bin/env python3
"""Generate the public Report Cards hub from canonical catalog data.

The source docs/REPORT_CARD.md preserves the hand-written deep-card material. The
public build gets a generated front door ahead of those legacy/deep sections so
catalog-wide Core Report Card coverage can never drift behind the canonical
model count.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAFE_ALIAS_TYPES = {"rebrand", "retail-brand", "market-name"}
DEEP_HEADING = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
GLS_HEADING = re.compile(r"^#{2,3}\s+(GLS-\d{4})\s+[—-]\s+", re.MULTILINE)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def format_score(value: object) -> str:
    if isinstance(value, (int, float)):
        return f"{float(value):.1f}"
    raw = str(value or "").strip().lower()
    if raw == "na":
        return "N/A"
    return "Unknown"


def legacy_deep_sections() -> str:
    """Keep the hand-written deep cards that historically lived on the hub."""
    source = ROOT / "docs" / "REPORT_CARD.md"
    if not source.exists():
        return ""
    text = source.read_text(encoding="utf-8")
    matches = list(DEEP_HEADING.finditer(text))
    sections: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end]
        if "| Dimension | Score" not in body:
            continue
        sections.append(f"### {match.group(1).strip()}\n{body.strip()}")
    return "\n\n".join(sections)


def library_links() -> tuple[list[str], list[str], list[str], int]:
    report_dir = ROOT / "docs" / "report-cards"
    batches: list[str] = []
    throughput: list[str] = []
    lineages: list[str] = []
    deep_ids: set[str] = set()
    for path in sorted(report_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        deep_ids.update(GLS_HEADING.findall(text))
        link = f"/docs/report-cards/{path.stem}/"
        if path.name.startswith("HIGH_THROUGHPUT_BATCH_"):
            label = path.stem.removeprefix("HIGH_THROUGHPUT_BATCH_")
            throughput.append(f"[High-throughput batch {label}]({link})")
        elif path.name.startswith("BATCH_"):
            label = path.stem.removeprefix("BATCH_")
            batches.append(f"[Core batch {label}]({link})")
        elif path.name.startswith("LINEAGE_") and not path.name.startswith("LINEAGE_PROFILES_"):
            label = path.stem.removeprefix("LINEAGE_").replace("_", " ").title()
            lineages.append(f"[{label}]({link})")
    return batches, throughput, lineages, len(deep_ids)


def alias_map(path: Path | None) -> dict[str, list[str]]:
    found: dict[str, list[str]] = defaultdict(list)
    if not path or not path.exists():
        return found
    payload = load(path)
    for item in payload.get("aliases", []):
        if item.get("alias_type") not in SAFE_ALIAS_TYPES:
            continue
        canonical_id = str(item.get("canonical_id", ""))
        alias = str(item.get("alias", "")).strip()
        if canonical_id and alias and alias not in found[canonical_id]:
            found[canonical_id].append(alias)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", type=Path, required=True)
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--aliases", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    devices = load(args.devices)
    scores = load(args.scores)
    records = devices.get("records", [])
    score_records = {item["id"]: item for item in scores.get("records", [])}
    dimensions = scores.get("dimensions", [])
    labels = {item["id"]: item["label"] for item in dimensions}
    dimension_ids = [item["id"] for item in dimensions]

    device_ids = {item["id"] for item in records}
    score_ids = set(score_records)
    if device_ids != score_ids:
        missing_cards = sorted(device_ids - score_ids)
        extra_cards = sorted(score_ids - device_ids)
        raise RuntimeError(
            "Core Report Card/catalog mismatch: "
            f"missing={missing_cards[:10]} extra={extra_cards[:10]}"
        )
    if len(dimension_ids) != 6:
        raise RuntimeError(f"Expected six Core Report Card dimensions, found {len(dimension_ids)}")

    aliases = alias_map(args.aliases)
    rows: list[str] = []
    for record in sorted(records, key=lambda item: (str(item["maker"]).casefold(), str(item["model"]).casefold(), item["id"])):
        model_id = record["id"]
        model_name = f"{record['maker']} {record['model']}"
        known_as = aliases.get(model_id, [])
        alias_text = ""
        if known_as:
            alias_text = "<br><small>Known as: " + " · ".join(html.escape(name) for name in known_as) + "</small>"
        search_terms = " ".join([model_id, model_name, *known_as]).casefold()
        cells = "".join(f"<td>{html.escape(format_score(score_records[model_id]['scores'].get(dim)))}</td>" for dim in dimension_ids)
        rows.append(
            f'<tr data-search="{html.escape(search_terms, quote=True)}">'
            f'<td><a href="{html.escape(record["public"]["model_page"], quote=True)}"><strong>{html.escape(model_name)}</strong></a>{alias_text}</td>'
            f'<td><code>{html.escape(model_id)}</code></td>{cells}</tr>'
        )

    resolved_any = 0
    resolved_all = 0
    for item in score_records.values():
        values = [item["scores"].get(dim) for dim in dimension_ids]
        resolved = [value for value in values if isinstance(value, (int, float)) or str(value).lower() == "na"]
        if resolved:
            resolved_any += 1
        if len(resolved) == len(dimension_ids):
            resolved_all += 1

    batches, throughput, lineages, deep_id_count = library_links()
    deep_sections = legacy_deep_sections()
    header_cells = "".join(f"<th>{html.escape(labels.get(dim, dim))}</th>" for dim in dimension_ids)
    count = len(records)

    page = f'''---
title: "GlassesResearch Report Cards"
description: "Core Report Cards for all {count} canonical smart-glasses models, plus deeper model and lineage research."
---

# GlassesResearch Report Cards

**{count} Core Report Cards — one for every canonical model in the catalog.**

The catalog-wide Report Card is deliberately compact: **Discreetness, Camera, Visual AI, Hackability, Owner Control, and Android Compatibility**. A card exists for every canonical `GLS-####` identity. `Unknown` means the evidence is not strong enough to score that subject; it is never converted into a zero. `N/A` means the subject genuinely does not apply.

The older ten-dimension cards and batch/lineage packets remain available below as **Extended Research**. They add depth; they do not define catalog coverage.

[Use the Glasses Finder](/docs/COMPARISON_ENGINE/) · [Browse canonical model pages](/models/catalog/) · [Read the scoring method](/docs/REPORT_CARD_METHOD/)

## Six Core subjects

| Subject | What it answers |
|---|---|
| **Discreetness** | How successfully the device passes as ordinary eyewear in normal use. |
| **Camera** | Camera capability and usefulness where evidence supports a score; verified absence is recorded explicitly. |
| **Visual AI** | How useful the glasses are for understanding the wearer's visual environment. |
| **Hackability** | How much practical experimentation, reverse engineering, modification, or supported development is possible. |
| **Owner Control** | How much of the device and software stack remains under the owner's control. |
| **Android Compatibility** | How well the glasses work with Android without unnecessary platform restrictions. |

## Find any Core Report Card

Type a manufacturer, model, canonical ID, or verified retail/rebrand name. The directory is generated from the same canonical catalog and alias ledger used by the Finder.

<label for="report-card-search"><strong>Filter {count} Report Cards</strong></label>
<input id="report-card-search" type="search" placeholder="Try W610, BooaBei, Vuzix, GLS-0039…" autocomplete="off" style="width:100%;max-width:42rem;padding:.65rem;margin:.35rem 0 .5rem;">
<p id="report-card-count" aria-live="polite">Showing all {count} Core Report Cards.</p>

<div style="overflow-x:auto;">
<table id="report-card-directory">
<thead><tr><th>Model</th><th>ID</th>{header_cells}</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>

<script>
(function () {{
  const input = document.getElementById('report-card-search');
  const table = document.getElementById('report-card-directory');
  const count = document.getElementById('report-card-count');
  if (!input || !table || !count) return;
  const rows = Array.from(table.querySelectorAll('tbody tr'));
  function applyFilter() {{
    const query = input.value.trim().toLowerCase();
    let visible = 0;
    rows.forEach((row) => {{
      const match = !query || (row.dataset.search || '').includes(query);
      row.hidden = !match;
      if (match) visible += 1;
    }});
    count.textContent = query
      ? `Showing ${{visible}} of {count} Core Report Cards.`
      : `Showing all {count} Core Report Cards.`;
  }}
  input.addEventListener('input', applyFilter);
}})();
</script>

**Coverage state:** {resolved_any} of {count} cards currently have at least one resolved Core subject; {resolved_all} have all six resolved. Every other cell remains visibly `Unknown` until evidence supports a judgment.

## Extended Research

The deeper research layer currently references **{deep_id_count} canonical GLS identities** across scored batches and lineage packets. These pages may use the older ten-dimension framework because they preserve more detailed research than the compact Core card.

### Batch research

{' · '.join(batches) if batches else 'No batch pages are currently published.'}

### High-throughput research

{' · '.join(throughput) if throughput else 'No high-throughput batch pages are currently published.'}

### Lineage research

{' · '.join(lineages) if lineages else 'No lineage packets are currently published.'}

## Deep-card highlights

{deep_sections if deep_sections else 'No hand-written deep-card highlights are currently published.'}
'''

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(
        f"Generated Report Card hub for {count} canonical models; "
        f"{resolved_any} with at least one resolved Core subject"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
