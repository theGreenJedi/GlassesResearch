#!/usr/bin/env python3
"""Synchronize canonical smart-glasses admissions and derived catalog metadata.

Evidence/admission decisions remain human-controlled in reconciliation packets.
This script performs only mechanical propagation:
- insert missing GLS rows already approved in THE_LIST_RECONCILIATION_*.md packets;
- preserve an explicit Era column when an audit packet provides one;
- derive the canonical count from actual unique GLS rows in THE_LIST.md;
- derive the Edition date from dated canonical admissions and corrections;
- update count statements in THE_LIST.md and models/README.md.

Reconciliation packets may use either the historical seven-column admission schema
(ID, Maker, Model, State, Type, Access, Evidence) or the preferred eight-column
schema that inserts Era between Model and State. Old packets remain valid.

Use --check to fail if running the synchronizer would change tracked source files.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

from catalog_metadata import canonical_model_count, canonical_updated_at, synchronize_edition

ROOT = Path(__file__).resolve().parents[1]
THE_LIST = ROOT / "models" / "THE_LIST.md"
MODELS_README = ROOT / "models" / "README.md"

GLS_ROW_RE = re.compile(r"^\| (GLS-\d{4}) \|", re.M)
COUNT_RE = re.compile(r"(\*\*Count:\*\* )\d+( distinct purchasable models or explicitly marketed product generations)")


def packet_admissions() -> list[tuple[str, str, bool]]:
    """Return (GLS id, canonical markdown row, explicit-era) for approved rows."""
    rows: list[tuple[str, str, bool]] = []
    for path in sorted((ROOT / "models").glob("THE_LIST_RECONCILIATION_*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(
            r"## Admit to canonical purchaser-history ledger\n(.*?)(?=\n## |\Z)",
            text,
            flags=re.S,
        )
        if not match:
            continue
        year_match = re.search(r"(20\d{2})", path.name)
        fallback_era = f"≤{year_match.group(1)}" if year_match else "unknown"
        for line in match.group(1).splitlines():
            if not re.match(r"^\| GLS-\d{4} \|", line):
                continue
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(parts) < 7:
                continue
            explicit_era = len(parts) >= 8
            if explicit_era:
                gls_id, maker, model, era, state, kind, access, evidence = parts[:8]
            else:
                gls_id, maker, model, state, kind, access, evidence = parts[:7]
                era = fallback_era
            source = evidence if evidence.startswith("http") else ""
            evidence_cell = f"primary; [reconciliation]({path.name})"
            if source:
                evidence_cell += f"; [source]({source})"
            canonical = f"| {gls_id} | {maker} | {model} | {era} | {state} | {kind} | {access} | {evidence_cell} |"
            rows.append((gls_id, canonical, explicit_era))
    return rows


def sync_the_list(text: str) -> str:
    admissions = packet_admissions()
    existing = set(GLS_ROW_RE.findall(text))
    missing = [(gid, row) for gid, row, _ in admissions if gid not in existing]
    if missing:
        missing.sort(key=lambda item: int(item[0].split("-")[1]))
        block = (
            "\n## Reconciliation admissions — mechanically synchronized\n\n"
            "These rows were already approved in dated reconciliation packets. This section is inserted mechanically so an approved admission cannot remain outside the canonical ledger.\n\n"
            "| ID | Maker | Model | Era | State | Type | Access | Evidence / links |\n"
            "|---|---|---:|---:|---|---|---|---|\n"
            + "\n".join(row for _, row in missing)
            + "\n\n"
        )
        marker = "## Google Glass is in scope"
        if marker not in text:
            raise RuntimeError(f"Insertion marker not found in {THE_LIST}")
        text = text.replace(marker, block + marker, 1)

    # When a packet carries an explicit evidence-backed era, keep mechanically
    # synchronized rows current with that packet. Seven-column legacy packets do
    # not rewrite existing rows, preserving any manually researched era already set.
    for gid, canonical, explicit_era in admissions:
        if not explicit_era or gid not in existing:
            continue
        pattern = re.compile(rf"^\| {re.escape(gid)} \|.*$", re.M)
        text, replacements = pattern.subn(canonical, text, count=1)
        if replacements != 1:
            raise RuntimeError(f"Could not refresh explicit-era row {gid} in {THE_LIST}")

    count = canonical_model_count(ROOT, text)
    text, replacements = COUNT_RE.subn(rf"\g<1>{count}\g<2>", text, count=1)
    if replacements != 1:
        raise RuntimeError("THE_LIST Count field missing or ambiguous")
    text = re.sub(r"not in the \d+-row count", f"not in the {count}-row count", text)

    updated_at = canonical_updated_at(ROOT, text)
    text = synchronize_edition(text, updated_at)
    return text


def sync_models_readme(text: str, count: int) -> str:
    # Replace prose that is intended to report the current active canonical total,
    # while preserving historical milestone numbers such as the original 145 reconciliation size.
    text = re.sub(
        r"(returns the active canonical count to \*\*)\d+(\*\*)",
        rf"\g<1>{count}\g<2>",
        text,
    )
    text = re.sub(
        r"(active canonical count is now \*\*)\d+(\*\*)",
        rf"\g<1>{count}\g<2>",
        text,
    )
    text = re.sub(
        r"(\*\*every one of the )\d+( active canonical smart-glasses records\*\*)",
        rf"\g<1>{count}\g<2>",
        text,
    )
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if synchronization would change files")
    args = parser.parse_args()

    original_list = THE_LIST.read_text(encoding="utf-8")
    synced_list = sync_the_list(original_list)
    count = canonical_model_count(ROOT, synced_list)
    updated_at = canonical_updated_at(ROOT, synced_list)

    original_models = MODELS_README.read_text(encoding="utf-8")
    synced_models = sync_models_readme(original_models, count)

    changes = []
    if synced_list != original_list:
        changes.append((THE_LIST, synced_list))
    if synced_models != original_models:
        changes.append((MODELS_README, synced_models))

    if args.check:
        if changes:
            print("Canonical model synchronization required:")
            for path, _ in changes:
                print(f"- {path.relative_to(ROOT)}")
            print(f"Derived canonical metadata: {count} models; edition {updated_at}")
            return 1
        print(f"Canonical model synchronization clean: {count} models; edition {updated_at}.")
        return 0

    for path, content in changes:
        path.write_text(content, encoding="utf-8")
    print(
        f"Canonical model synchronization complete: {count} models; edition {updated_at}; "
        f"{len(changes)} file(s) updated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
