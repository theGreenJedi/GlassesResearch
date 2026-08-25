#!/usr/bin/env python3
"""Report Finder filters with zero canonical yes values after staged data generation."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / ".site-src" / "data"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    matrix_path = SITE / "finder-capabilities.json"
    schema_path = SITE / "finder-schema.json"
    if not matrix_path.exists() or not schema_path.exists():
        raise SystemExit("Run `python scripts/prepare_site.py` first; staged Finder data is missing.")

    matrix = load(matrix_path)
    schema = load(schema_path)
    records = matrix.get("records", [])

    print(f"Canonical Finder records: {len(records)}")
    print("filter_id\tlabel\tyes\tno\tunknown\tna\tclassification")
    for group in schema.get("groups", []):
        for filt in group.get("filters", []):
            if filt.get("type") != "capability":
                continue
            field = filt["field"]
            counts = Counter(
                record.get("capabilities", {}).get(field, {}).get("value", "unknown")
                for record in records
            )
            classification = "candidate-zero" if counts["yes"] == 0 else "nonzero"
            print(
                f"{filt['id']}\t{filt['label']}\t{counts['yes']}\t{counts['no']}\t"
                f"{counts['unknown']}\t{counts['na']}\t{classification}"
            )


if __name__ == "__main__":
    main()
