#!/usr/bin/env python3
"""Inject four-state Finder capability facts into generated comparison records."""
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

    # The comparison corpus may not yet contain every canonical model. Add minimal
    # records so Finder can still consume explicit capability facts for every GLS ID.
    for model_id, cap_record in by_id.items():
        if model_id not in existing_ids:
            records.append({
                "id": model_id,
                "maker": cap_record.get("maker", ""),
                "model": cap_record.get("model", ""),
                "fields": {},
            })

    for record in records:
        cap_record = by_id.get(record.get("id"))
        if not cap_record:
            continue
        fields = record.setdefault("fields", {})
        for field, fact in cap_record.get("capabilities", {}).items():
            value = fact.get("value", "unknown")
            # Finder v3 understands booleans best; preserve unknown/N/A explicitly.
            if value == "yes":
                rendered = True
            elif value == "no":
                rendered = False
            elif value == "na":
                rendered = "N/A"
            else:
                rendered = "Unknown"
            fields[field] = {
                "value": rendered,
                "evidence": "finder-matrix" if value not in {"unknown"} else "unknown",
                "sources": [],
                "note": f"Finder capability matrix: {fact.get('provenance', 'unresolved')}",
            }

    comparison_path.write_text(json.dumps(comparisons, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Applied Finder capabilities to {len(by_id)} canonical models")


if __name__ == "__main__":
    main()
