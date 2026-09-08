#!/usr/bin/env python3
"""Validate external-catalog reconciliation records.

External catalogs are discovery inputs, not canonical authorities. This guardrail ensures
that each recorded discrepancy has an explicit disposition and that any mapped GLS/ADJ
identifier and evidence path actually exist in the repository.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data/external-catalog-benchmarks.json"
THE_LIST = ROOT / "models/THE_LIST.md"
ADJACENT = ROOT / "models/ADJACENT_WEARABLES.md"
GLS_RE = re.compile(r"\b(GLS-\d{4})\b")
ADJ_RE = re.compile(r"\b(ADJ-\d{4})\b")


def main() -> int:
    try:
        payload = json.loads(LEDGER.read_text(encoding="utf-8"))
        canonical_ids = set(GLS_RE.findall(THE_LIST.read_text(encoding="utf-8")))
        adjacent_ids = set(ADJ_RE.findall(ADJACENT.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"External catalog benchmark check FAILED:\n- could not load inputs: {exc}")
        return 1

    errors: list[str] = []
    states = set(payload.get("states", {}))
    sources = payload.get("sources", [])
    reconciliations = payload.get("reconciliations", [])
    source_ids: set[str] = set()

    for source in sources:
        source_id = source.get("id")
        if not source_id:
            errors.append("benchmark source missing id")
            continue
        if source_id in source_ids:
            errors.append(f"duplicate benchmark source id: {source_id}")
        source_ids.add(source_id)
        if not source.get("url"):
            errors.append(f"{source_id}: missing url")
        count = source.get("reported_model_count")
        if not isinstance(count, int) or count < 1:
            errors.append(f"{source_id}: reported_model_count must be a positive integer")
        if not source.get("observed_on"):
            errors.append(f"{source_id}: missing observed_on date")

    seen: set[tuple[str, str]] = set()
    state_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()

    for row in reconciliations:
        source_id = row.get("source")
        name = (row.get("external_name") or "").strip()
        state = row.get("state")
        key = (source_id, name.casefold())

        if source_id not in source_ids:
            errors.append(f"{name or '<unnamed>'}: unknown source {source_id!r}")
        if not name:
            errors.append(f"{source_id or '<unknown source>'}: reconciliation missing external_name")
        elif key in seen:
            errors.append(f"duplicate reconciliation for {source_id}: {name}")
        seen.add(key)

        if state not in states:
            errors.append(f"{source_id}/{name}: unknown state {state!r}")
            continue

        target = row.get("target_id")
        if state in {"canonical_match", "alias_or_variant"}:
            if target not in canonical_ids:
                errors.append(f"{source_id}/{name}: {state} requires an existing GLS target; got {target!r}")
        elif state == "adjacent":
            if target not in adjacent_ids:
                errors.append(f"{source_id}/{name}: adjacent requires an existing ADJ target; got {target!r}")
        elif target is not None:
            errors.append(f"{source_id}/{name}: state {state} should not carry target_id {target!r}")

        evidence = row.get("evidence_path")
        if not evidence:
            errors.append(f"{source_id}/{name}: missing evidence_path")
        elif not (ROOT / evidence).exists():
            errors.append(f"{source_id}/{name}: evidence_path does not exist: {evidence}")

        if not row.get("note"):
            errors.append(f"{source_id}/{name}: missing explanatory note")

        state_counts[state] += 1
        source_counts[source_id] += 1

    if errors:
        print("External catalog benchmark check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "External catalog benchmark check passed: "
        f"{len(sources)} sources, {len(reconciliations)} explicit reconciliations; "
        + ", ".join(f"{state}={state_counts[state]}" for state in sorted(state_counts))
        + "."
    )
    for source in sources:
        source_id = source["id"]
        print(
            f"- {source['label']}: {source_counts[source_id]} discrepancy records retained "
            f"from a reported {source['reported_model_count']}-model source snapshot."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
