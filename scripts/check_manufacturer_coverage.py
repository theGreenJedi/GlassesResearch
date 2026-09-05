#!/usr/bin/env python3
"""Validate whole-manufacturer coverage and surface lineage audit debt.

This check deliberately separates two questions:
1. Is every sufficiently large canonical Maker population assigned to a manufacturer family?
2. Has that family actually received a whole-manufacturer historical audit?

Missing family assignment is a consistency failure. Historical audit debt is emitted as a
warning by default so the existing catalog can be paid down incrementally; --strict-debt
turns those warnings into failures.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data/manufacturer-coverage.json"
THE_LIST = ROOT / "models/THE_LIST.md"
ROW_RE = re.compile(r"^\|\s*(GLS-\d{4})\s*\|\s*([^|]+?)\s*\|", re.M)


def emit_warning(message: str) -> None:
    if __import__("os").environ.get("GITHUB_ACTIONS") == "true":
        print(f"::warning::{message}")
    else:
        print(f"WARNING: {message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-debt", action="store_true", help="fail on unresolved manufacturer audit debt")
    args = parser.parse_args()

    payload = json.loads(LEDGER.read_text(encoding="utf-8"))
    text = THE_LIST.read_text(encoding="utf-8")
    states = set(payload.get("states", {}))
    threshold = int(payload.get("policy", {}).get("coverage_debt_threshold", 3))
    families = payload.get("families", [])

    errors: list[str] = []
    debt: list[str] = []
    maker_to_family: dict[str, str] = {}
    family_by_id: dict[str, dict] = {}

    for family in families:
        family_id = family.get("id")
        if not family_id:
            errors.append("manufacturer coverage family missing id")
            continue
        if family_id in family_by_id:
            errors.append(f"duplicate manufacturer coverage family id: {family_id}")
        family_by_id[family_id] = family

        state = family.get("state")
        if state not in states:
            errors.append(f"{family_id}: unknown state {state!r}")

        for maker in family.get("maker_values", []):
            if maker in maker_to_family:
                errors.append(
                    f"Maker value {maker!r} is assigned to both {maker_to_family[maker]} and {family_id}"
                )
            maker_to_family[maker] = family_id

        for field in ("lineage_path", "audit_path"):
            rel = family.get(field)
            if rel and not (ROOT / rel).exists():
                errors.append(f"{family_id}: {field} does not exist: {rel}")

        if state in {"lineage_reconciled", "monitored"} and not family.get("last_whole_manufacturer_audit"):
            errors.append(f"{family_id}: {state} requires last_whole_manufacturer_audit")

    rows = [(gid, maker.strip()) for gid, maker in ROW_RE.findall(text)]
    maker_counts = Counter(maker for _, maker in rows)
    family_counts: Counter[str] = Counter()
    family_ids: defaultdict[str, list[str]] = defaultdict(list)

    for gid, maker in rows:
        family_id = maker_to_family.get(maker)
        if family_id:
            family_counts[family_id] += 1
            family_ids[family_id].append(gid)

    for maker, count in sorted(maker_counts.items(), key=lambda item: (-item[1], item[0].lower())):
        if count >= threshold and maker not in maker_to_family:
            errors.append(
                f"Maker {maker!r} has {count} canonical models (threshold {threshold}) but no manufacturer-coverage family"
            )

    for family_id, count in sorted(family_counts.items(), key=lambda item: (-item[1], item[0])):
        family = family_by_id[family_id]
        state = family.get("state")
        if count >= threshold and state in {"unreviewed", "partial_map", "audit_in_progress"}:
            ids = ", ".join(sorted(family_ids[family_id]))
            debt.append(
                f"{family.get('label', family_id)} has {count} canonical models but coverage state is {state}; "
                f"whole-manufacturer audit debt remains ({ids})"
            )

    if errors:
        print("Manufacturer coverage check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    for message in debt:
        emit_warning(message)

    if args.strict_debt and debt:
        print(f"Manufacturer coverage debt is strict: {len(debt)} unresolved families.")
        return 1

    print(
        f"Manufacturer coverage check passed: {len(rows)} canonical rows, "
        f"{len(families)} tracked families, {len(debt)} audit-debt warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
