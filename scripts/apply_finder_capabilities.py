#!/usr/bin/env python3
"""Inject confirmed-positive Finder capability facts into generated comparison records.

The complete yes/no/unknown/N/A truth table remains in finder-capabilities.json. Finder v3
contains several legacy `known()` compatibility checks, so only confirmed `yes` values are
mirrored into comparisons.json until the UI consumes the four-state matrix directly.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comparisons", required=True)
    ap.add_argument("--capabilities", required=True)
    args = ap.parse_args()

    comparison_path = Path(args.comparisons)
    capability_path = Path(args.capabilities)
    comparisons = json.loads(comparison_path.read_text(encoding="utf-8"))
    capabilities = json.loads(capability_path.read_text(encoding="utf-8"))

    by_id = {r["id"]: r for r in capabilities.get("records", [])}
    records = comparisons.setdefault("records", [])
    existing_ids = {r.get("id") for r in records}

    for model_id, cap_record in by_id.items():
        if model_id not in existing_ids:
            records.append({
                "id": model_id,
                "maker": cap_record.get("maker", ""),
                "model": cap_record.get("model", ""),
                "fields": {},
            })

    injected = 0
    for record in records:
        cap_record = by_id.get(record.get("id"))
        if not cap_record:
            continue
        fields = record.setdefault("fields", {})
        for field, fact in cap_record.get("capabilities", {}).items():
            if fact.get("value") != "yes":
                continue
            fields[field] = {
                "value": True,
                "evidence": "finder-matrix",
                "sources": [],
                "note": f"Finder capability matrix: {fact.get('provenance', 'unresolved')}",
            }
            injected += 1

    comparison_path.write_text(json.dumps(comparisons, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Applied {injected} confirmed-positive Finder facts across {len(by_id)} canonical models")


if __name__ == "__main__":
    main()
