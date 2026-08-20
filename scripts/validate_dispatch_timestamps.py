#!/usr/bin/env python3
"""Require dispatch-enabled GRE publications to carry a precise UTC timestamp."""
from __future__ import annotations

import re

from verified_publications import DEFAULT_MANIFEST, validate

UTC_TS = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


def main() -> int:
    payload = validate(DEFAULT_MANIFEST)
    errors: list[str] = []
    checked = 0
    for item in payload.get("publications", []):
        if not item.get("dispatch"):
            continue
        checked += 1
        publication_id = str(item.get("id", "<unknown>"))
        event_id = str(item.get("event_id", "<unknown GRE>"))
        published_at = str(item.get("published_at", ""))
        if not UTC_TS.fullmatch(published_at):
            errors.append(
                f"{event_id}/{publication_id}: dispatch-enabled published_at must be a precise UTC timestamp, got {published_at!r}"
            )
            continue
        id_date = publication_id.removeprefix("gr-")[:10]
        if published_at[:10] != id_date:
            errors.append(
                f"{event_id}/{publication_id}: timestamp date {published_at[:10]} does not match publication id date {id_date}"
            )
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"GRE dispatch timestamp contract valid: {checked} dispatch-enabled publications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
