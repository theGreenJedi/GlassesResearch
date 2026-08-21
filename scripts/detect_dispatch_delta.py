#!/usr/bin/env python3
"""Detect new or changed dispatch-enabled alert payloads across a git revision.

New publication IDs may legitimately enter the delivery stream. Existing publication
IDs are historical idempotency keys and must not be silently mutated or removed.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

from verified_changes import DEFAULT_CHANGES, publication_manifest, validate

DELIVERY_FIELDS = (
    "id",
    "title",
    "canonical_url",
    "summary",
    "models",
    "brands_lineages",
    "topics",
    "published_at",
)


def delivery_view(item: dict[str, Any]) -> dict[str, Any]:
    return {field: item.get(field) for field in DELIVERY_FIELDS}


def current_dispatches(path: Path) -> dict[str, dict[str, Any]]:
    manifest = publication_manifest(validate(path))
    return {
        item["id"]: delivery_view(item)
        for item in manifest["publications"]
        if item.get("dispatch") is True
    }


def git_show(ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def previous_dispatches(ref: str) -> dict[str, dict[str, Any]]:
    raw = git_show(ref, "data/verified-changes.json")
    if raw is not None:
        payload = json.loads(raw)
        # Historical derivation intentionally skips current Research & News heading validation.
        manifest = publication_manifest(payload)
        return {
            item["id"]: delivery_view(item)
            for item in manifest["publications"]
            if item.get("dispatch") is True
        }

    raw = git_show(ref, "data/verified-publications.json")
    if raw is not None:
        payload = json.loads(raw)
        return {
            item["id"]: delivery_view(item)
            for item in payload.get("publications", [])
            if item.get("dispatch") is True
        }
    return {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--current", type=Path, default=DEFAULT_CHANGES)
    parser.add_argument("--previous-ref", default="HEAD^")
    parser.add_argument(
        "--reject-historical-mutation",
        action="store_true",
        help="Fail if an existing dispatch publication is changed or removed; new IDs remain allowed.",
    )
    args = parser.parse_args()

    current = current_dispatches(args.current)
    previous = previous_dispatches(args.previous_ref)

    new_ids = sorted(set(current) - set(previous))
    mutated_ids = sorted(
        publication_id
        for publication_id in set(current) & set(previous)
        if current[publication_id] != previous[publication_id]
    )
    removed_ids = sorted(set(previous) - set(current))
    changed = sorted(new_ids + mutated_ids)
    needs_dispatch = bool(changed)
    historical_changed = bool(mutated_ids or removed_ids)

    if new_ids:
        print("New dispatch publications: " + ", ".join(new_ids))
    else:
        print("New dispatch publications: none")
    if mutated_ids:
        print("Historical dispatch payloads mutated: " + ", ".join(mutated_ids))
    else:
        print("Historical dispatch payloads mutated: none")
    if removed_ids:
        print("Historical dispatch publications removed: " + ", ".join(removed_ids))
    else:
        print("Historical dispatch publications removed: none")

    print(
        "Dispatch delta: "
        + (", ".join(changed) if changed else "none; historical delivery payloads unchanged")
    )

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"needs_dispatch={'true' if needs_dispatch else 'false'}\n")
            handle.write(f"publication_ids={','.join(changed)}\n")
            handle.write(f"new_publication_ids={','.join(new_ids)}\n")
            handle.write(f"mutated_publication_ids={','.join(mutated_ids)}\n")
            handle.write(f"removed_publication_ids={','.join(removed_ids)}\n")
            handle.write(f"historical_changed={'true' if historical_changed else 'false'}\n")

    if args.reject_historical_mutation and historical_changed:
        print("Historical dispatch payload mutation/removal is not permitted; publish a new event instead.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
