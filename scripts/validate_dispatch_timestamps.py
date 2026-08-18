#!/usr/bin/env python3
"""Require dispatch-enabled publications to carry a precise UTC timestamp.

Daily/weekly digest cutoffs are full timestamps. A date-only value such as
2026-08-18 sorts before 2026-08-18T11:17:00Z and can therefore make a same-day
publication disappear behind an earlier digest. Dispatch-enabled publications
must use their actual publication timestamp so replay stays stable and digest
selection remains correct.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "verified-publications.json"
UTC_TS = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


def main() -> int:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked = 0
    for item in payload.get("publications", []):
        if not item.get("dispatch"):
            continue
        checked += 1
        publication_id = str(item.get("id", "<unknown>"))
        published_at = str(item.get("published_at", ""))
        if not UTC_TS.fullmatch(published_at):
            errors.append(
                f"{publication_id}: dispatch-enabled published_at must be a precise UTC timestamp, got {published_at!r}"
            )
            continue
        id_date = publication_id.removeprefix("gr-")[:10]
        if published_at[:10] != id_date:
            errors.append(
                f"{publication_id}: timestamp date {published_at[:10]} does not match publication id date {id_date}"
            )
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Dispatch timestamp contract valid: {checked} dispatch-enabled publications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
