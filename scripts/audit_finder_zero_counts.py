#!/usr/bin/env python3
"""Report Finder capability coverage without converting unknowns into claims.

This is an observability tool for issue #382. It classifies zero-verified-match
filters conservatively so research gaps are visible without treating them as
product negatives or verified true-zero categories.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ALLOWED_STATES = {"yes", "no", "unknown", "na"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classify(counts: Counter) -> str:
    if counts["yes"]:
        return "verified-nonzero"
    if counts["unknown"]:
        return "needs-coverage-review"
    return "zero-without-unknowns"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", default="data/finder-schema.json")
    parser.add_argument("--capabilities", default=".site-src/data/finder-capabilities.json")
    parser.add_argument("--output")
    args = parser.parse_args()

    schema = load(Path(args.schema))
    matrix = load(Path(args.capabilities))
    records = matrix.get("records", [])
    if not records:
        raise SystemExit("Finder zero-count audit: capability matrix has no records")

    capability_filters = [
        {"id": f["id"], "label": f["label"], "field": f["field"], "group": group["label"]}
        for group in schema.get("groups", [])
        for f in group.get("filters", [])
        if f.get("type") == "capability"
    ]

    rows = []
    errors = []
    for filt in capability_filters:
        counts = Counter()
        for record in records:
            entry = (record.get("capabilities") or {}).get(filt["field"])
            state = (entry or {}).get("value")
            if state not in ALLOWED_STATES:
                errors.append(f"{record.get('id')} {filt['field']} has invalid or missing state {state!r}")
                continue
            counts[state] += 1
        row = {
            **filt,
            "yes": counts["yes"],
            "no": counts["no"],
            "unknown": counts["unknown"],
            "na": counts["na"],
            "classification": classify(counts),
        }
        rows.append(row)

    if errors:
        print("Finder zero-count audit FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Finder capability coverage audit (verified states only; unknown never equals no)")
    print("group\tfilter\tyes\tno\tunknown\tna\tclassification")
    for row in rows:
        print(
            f"{row['group']}\t{row['label']}\t{row['yes']}\t{row['no']}\t"
            f"{row['unknown']}\t{row['na']}\t{row['classification']}"
        )

    review = [row for row in rows if row["classification"] != "verified-nonzero"]
    print(f"Zero-verified-match capability filters requiring review: {len(review)}")
    for row in review:
        print(f"- {row['label']}: {row['classification']} ({row['unknown']} unknown)")

    if args.output:
        payload = {
            "schema_version": 1,
            "semantics": "Diagnostic only. A zero verified-yes count is not a claim that no matching product exists.",
            "record_count": len(records),
            "filters": rows,
        }
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
