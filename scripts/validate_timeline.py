#!/usr/bin/env python3
"""Validate canonical and automatically discovered timeline records."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "timeline" / "schema.json"
EVENTS = ROOT / "timeline" / "events.json"
AUTO = ROOT / "timeline" / "auto-events.json"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def valid_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def main() -> int:
    schema = load(SCHEMA)
    canonical = load(EVENTS)
    auto = load(AUTO)
    errors: list[str] = []

    categories = set(schema["categories"])
    states = set(schema["states"])
    evidence = set(schema["evidence"])
    required = set(schema["required_fields"])
    id_re = re.compile(schema["canonical_id_pattern"])

    ids: set[str] = set()
    for event in canonical.get("events", []):
        missing = required - set(event)
        if missing:
            errors.append(f"{event.get('id', '<missing-id>')}: missing {sorted(missing)}")
            continue
        event_id = event["id"]
        if not id_re.fullmatch(event_id):
            errors.append(f"{event_id}: invalid canonical ID")
        if event_id in ids:
            errors.append(f"{event_id}: duplicate ID")
        ids.add(event_id)
        if not valid_date(event["date"]):
            errors.append(f"{event_id}: invalid ISO date {event['date']!r}")
        if event["category"] not in categories:
            errors.append(f"{event_id}: unknown category {event['category']!r}")
        if event["state"] not in states - {"provisional"}:
            errors.append(f"{event_id}: canonical event may not be provisional")
        if event["evidence"] not in evidence:
            errors.append(f"{event_id}: unknown evidence class {event['evidence']!r}")
        if not isinstance(event["significance"], int) or not 1 <= event["significance"] <= 5:
            errors.append(f"{event_id}: significance must be integer 1..5")
        if not isinstance(event["sources"], list) or not event["sources"]:
            errors.append(f"{event_id}: at least one source is required")
        elif not all(isinstance(url, str) and url.startswith("https://") for url in event["sources"]):
            errors.append(f"{event_id}: every source must be an https URL")

    auto_ids: set[str] = set()
    for event in auto.get("events", []):
        event_id = event.get("id")
        if not isinstance(event_id, str) or not event_id.startswith("AUTO-"):
            errors.append(f"automatic event has invalid ID {event_id!r}")
        if event_id in auto_ids:
            errors.append(f"{event_id}: duplicate automatic ID")
        auto_ids.add(event_id)
        if event.get("state") != "provisional":
            errors.append(f"{event_id}: automatic event must remain provisional")
        if event.get("significance") not in {2, 3, 4}:
            errors.append(f"{event_id}: automatic significance must be 2, 3, or 4")
        if not valid_date(event.get("date")):
            errors.append(f"{event_id}: invalid date")
        if event.get("category") not in categories:
            errors.append(f"{event_id}: invalid category")
        sources = event.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{event_id}: source required")

    ordered = [event["date"] for event in canonical.get("events", [])]
    if ordered != sorted(ordered):
        errors.append("canonical events must be ordered by date")

    if errors:
        print("ERROR: timeline validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(canonical.get('events', []))} canonical timeline events and "
        f"{len(auto.get('events', []))} provisional live signals"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
