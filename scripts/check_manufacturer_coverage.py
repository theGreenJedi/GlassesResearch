#!/usr/bin/env python3
"""Validate whole-manufacturer coverage and surface lineage audit debt.

This check deliberately separates two questions:
1. Is every sufficiently large canonical Maker population assigned to a manufacturer family?
2. Has that family actually received a whole-manufacturer historical audit?

Missing family assignment is a consistency failure. Historical audit debt is emitted as a
warning by default so the existing catalog can be paid down incrementally; --strict-debt
turns those warnings into failures.

The base ledger remains ``data/manufacturer-coverage.json``. Optional
``data/manufacturer-coverage-*.json`` supplements allow newly discovered families to be
mapped immediately without falsely rewriting the dated state of the last base audit.
Supplements use the same family schema and are validated for duplicate ids/maker values.
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
SUPPLEMENT_GLOB = "manufacturer-coverage-*.json"
THE_LIST = ROOT / "models/THE_LIST.md"
ROW_RE = re.compile(r"^\|\s*(GLS-\d{4})\s*\|\s*([^|]+?)\s*\|", re.M)


def emit_warning(message: str) -> None:
    if __import__("os").environ.get("GITHUB_ACTIONS") == "true":
        print(f"::warning::{message}")
    else:
        print(f"WARNING: {message}")


def load_coverage() -> tuple[dict, list[dict], list[str]]:
    """Load base policy/state definitions plus optional incremental family mappings."""
    payload = json.loads(LEDGER.read_text(encoding="utf-8"))
    families = list(payload.get("families", []))
    loaded = [str(LEDGER.relative_to(ROOT))]
    for path in sorted((ROOT / "data").glob(SUPPLEMENT_GLOB)):
        if path == LEDGER:
            continue
        supplement = json.loads(path.read_text(encoding="utf-8"))
        if supplement.get("schema_version") != payload.get("schema_version"):
            raise ValueError(
                f"{path.relative_to(ROOT)} schema_version {supplement.get('schema_version')!r} "
                f"does not match base ledger {payload.get('schema_version')!r}"
            )
        families.extend(supplement.get("families", []))
        loaded.append(str(path.relative_to(ROOT)))
    return payload, families, loaded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-debt", action="store_true", help="fail on unresolved manufacturer audit debt")
    args = parser.parse_args()

    try:
        payload, families, loaded_ledgers = load_coverage()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Manufacturer coverage check FAILED:\n- could not load coverage ledger: {exc}")
        return 1

    text = THE_LIST.read_text(encoding="utf-8")
    states = set(payload.get("states", {}))
    threshold = int(payload.get("policy", {}).get("coverage_debt_threshold", 3))

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
        f"{len(families)} tracked families across {len(loaded_ledgers)} ledger file(s), "
        f"{len(debt)} audit-debt warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
