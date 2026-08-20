#!/usr/bin/env python3
"""Detect new or changed dispatch-enabled alert payloads across a git revision.

This lets GRE-ledger migrations and non-delivery metadata edits validate without
replaying historical subscriber events. Existing publication IDs remain the
idempotency key; a new or materially changed dispatch payload still activates
staging and canary proof.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import tempfile
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
        # Derivation does not need current-heading validation for the historical side.
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
    args = parser.parse_args()

    current = current_dispatches(args.current)
    previous = previous_dispatches(args.previous_ref)
    changed = sorted(
        publication_id
        for publication_id, payload in current.items()
        if previous.get(publication_id) != payload
    )
    needs_dispatch = bool(changed)
    print(
        "Dispatch delta: "
        + (", ".join(changed) if changed else "none; historical delivery payloads unchanged")
    )
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"needs_dispatch={'true' if needs_dispatch else 'false'}\n")
            handle.write(f"publication_ids={','.join(changed)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
