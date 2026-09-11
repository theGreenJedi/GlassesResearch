#!/usr/bin/env python3
"""Require new dispatch-enabled GRE publications to carry a precise UTC timestamp.

Historical delivery payloads are immutable. If an older dispatch predates the precise-
timestamp contract, callers may provide ``--previous-ref`` so that an unchanged legacy
payload is grandfathered rather than forcing an illegal mutation of its idempotency key.
New or changed dispatch payloads must always satisfy the current timestamp contract.
"""
from __future__ import annotations

import argparse
import re

from detect_dispatch_delta import delivery_view, previous_dispatches
from verified_publications import DEFAULT_MANIFEST, validate

UTC_TS = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--previous-ref",
        default=None,
        help=(
            "Optional git ref used to grandfather only unchanged historical dispatch payloads "
            "that predate the precise-timestamp contract."
        ),
    )
    args = parser.parse_args()

    payload = validate(DEFAULT_MANIFEST)
    previous = previous_dispatches(args.previous_ref) if args.previous_ref else {}
    errors: list[str] = []
    checked = 0
    grandfathered = 0

    for item in payload.get("publications", []):
        if not item.get("dispatch"):
            continue
        checked += 1
        publication_id = str(item.get("id", "<unknown>"))
        event_id = str(item.get("event_id", "<unknown GRE>"))
        published_at = str(item.get("published_at", ""))

        if not UTC_TS.fullmatch(published_at):
            historical = previous.get(publication_id)
            if historical is not None and delivery_view(item) == historical:
                grandfathered += 1
                continue
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

    legacy_note = f"; {grandfathered} unchanged legacy payload(s) grandfathered" if grandfathered else ""
    print(f"GRE dispatch timestamp contract valid: {checked} dispatch-enabled publications{legacy_note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
