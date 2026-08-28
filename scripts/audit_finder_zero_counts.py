#!/usr/bin/env python3
"""Report Finder filter coverage without converting missing evidence into claims.

This is the observability tool for issue #382. It audits capability, buying-source,
condition, and price filters against the staged canonical data. A zero match count is
classified conservatively: missing evidence is a coverage zero, never an implicit no.
Frontend and data-pipeline defects are identified by separate consistency checks and
can be recorded in the audit note once reproduced.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ALLOWED_STATES = {"yes", "no", "unknown", "na"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classify(matches: int, unknown: int) -> str:
    if matches:
        return "verified-nonzero"
    if unknown:
        return "coverage-zero"
    return "true-zero"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", default="data/finder-schema.json")
    parser.add_argument("--capabilities", default=".site-src/data/finder-capabilities.json")
    parser.add_argument("--purchases", default=".site-src/data/purchase-sources.json")
    parser.add_argument("--prices", default=".site-src/data/price-observations.json")
    parser.add_argument("--output")
    args = parser.parse_args()

    schema = load(Path(args.schema))
    matrix = load(Path(args.capabilities))
    purchases = load(Path(args.purchases))
    prices = load(Path(args.prices))
    records = matrix.get("records", [])
    if not records:
        raise SystemExit("Finder zero-count audit: capability matrix has no records")

    record_ids = {record.get("id") for record in records if record.get("id")}
    purchase_by_id = {
        record.get("id"): record.get("sources", [])
        for record in purchases.get("records", [])
        if record.get("id") in record_ids
    }
    price_by_id: dict[str, list[dict]] = {}
    for observation in prices.get("records", []):
        model_id = observation.get("id")
        if model_id in record_ids:
            price_by_id.setdefault(model_id, []).append(observation)

    filters = [
        {**filt, "group": group["label"]}
        for group in schema.get("groups", [])
        for filt in group.get("filters", [])
    ]

    rows = []
    errors = []
    for filt in filters:
        filter_type = filt.get("type")
        row = {
            "group": filt["group"],
            "id": filt["id"],
            "label": filt["label"],
            "type": filter_type,
        }

        if filter_type == "capability":
            counts = Counter()
            for record in records:
                entry = (record.get("capabilities") or {}).get(filt["field"])
                state = (entry or {}).get("value")
                if state not in ALLOWED_STATES:
                    errors.append(
                        f"{record.get('id')} {filt['field']} has invalid or missing state {state!r}"
                    )
                    continue
                counts[state] += 1
            row.update(
                yes=counts["yes"],
                no=counts["no"],
                unknown=counts["unknown"],
                na=counts["na"],
                matches=counts["yes"],
                classification=classify(counts["yes"], counts["unknown"]),
            )

        elif filter_type == "purchase":
            if filt.get("field") != "available_new":
                errors.append(f"unsupported purchase filter {filt['id']!r}")
                continue
            matches = sum(
                1
                for model_id in record_ids
                if any(
                    source.get("availability") == "available"
                    and source.get("condition") in {"new", "refurbished"}
                    for source in purchase_by_id.get(model_id, [])
                )
            )
            # Missing a current purchase route is not evidence that none exists.
            unknown = len(record_ids) - matches
            row.update(matches=matches, unknown=unknown, classification=classify(matches, unknown))

        elif filter_type == "purchase_source":
            matches = sum(
                1
                for model_id in record_ids
                if any(source.get("source_type") == filt.get("value") for source in purchase_by_id.get(model_id, []))
            )
            unknown = len(record_ids) - matches
            row.update(matches=matches, unknown=unknown, classification=classify(matches, unknown))

        elif filter_type == "condition":
            matches = sum(
                1
                for model_id in record_ids
                if any(source.get("condition") == filt.get("value") for source in purchase_by_id.get(model_id, []))
            )
            unknown = len(record_ids) - matches
            row.update(matches=matches, unknown=unknown, classification=classify(matches, unknown))

        elif filter_type == "price_max":
            threshold = float(filt["value"])
            known = 0
            matches = 0
            for model_id in record_ids:
                usable = [
                    float(item["price_usd"])
                    for item in price_by_id.get(model_id, [])
                    if isinstance(item.get("price_usd"), (int, float))
                ]
                if not usable:
                    continue
                known += 1
                if min(usable) <= threshold:
                    matches += 1
            unknown = len(record_ids) - known
            row.update(
                matches=matches,
                known=known,
                unknown=unknown,
                classification=classify(matches, unknown),
            )

        else:
            errors.append(f"unsupported Finder filter type {filter_type!r} for {filt['id']}")
            continue

        rows.append(row)

    if errors:
        print("Finder zero-count audit FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Finder filter coverage audit (missing evidence never equals no)")
    print("group\tfilter\ttype\tmatches\tunknown\tclassification")
    for row in rows:
        print(
            f"{row['group']}\t{row['label']}\t{row['type']}\t{row['matches']}\t"
            f"{row.get('unknown', 0)}\t{row['classification']}"
        )

    review = [row for row in rows if row["classification"] != "verified-nonzero"]
    print(f"Zero-result Finder filters requiring review: {len(review)}")
    for row in review:
        print(
            f"- {row['label']}: {row['classification']} "
            f"({row.get('unknown', 0)} unresolved records)"
        )

    if args.output:
        payload = {
            "schema_version": 2,
            "semantics": (
                "Diagnostic only. Zero matches with unresolved records are coverage-zero, "
                "not claims that no matching product exists. Frontend-zero and data-pipeline-zero "
                "require a reproduced cross-layer defect."
            ),
            "record_count": len(records),
            "filters": rows,
        }
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
