#!/usr/bin/env python3
"""Reflect durable editorial triage state on the discovery-only public wire.

This script changes only ``reported`` -> ``under_review`` when the same source URL has
entered an actionable editorial review state. It never marks a wire item verified or
published, and it never copies internal notes or canonical claims onto the wire.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

REVIEW_STATES = {"needs_editorial_verification", "source_review"}


def normalized_url(raw: str) -> str:
    raw = str(raw or "").strip()
    if not raw:
        return ""
    try:
        parts = urlsplit(raw)
        path = parts.path.rstrip("/") or "/"
        return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))
    except ValueError:
        return raw


def sync(wire: dict, queue: dict) -> tuple[dict, int]:
    actionable = {
        normalized_url(item.get("url", ""))
        for item in queue.get("candidates", [])
        if isinstance(item, dict)
        and str(item.get("triage_state", "")) in REVIEW_STATES
        and str(item.get("editorial_disposition", "pending")) == "pending"
        and normalized_url(item.get("url", ""))
    }

    changed = 0
    items = []
    for raw in wire.get("items", []):
        if not isinstance(raw, dict):
            continue
        item = dict(raw)
        desired = "under_review" if normalized_url(item.get("url", "")) in actionable else str(item.get("status", "reported"))
        if desired == "under_review" and item.get("status") != "under_review":
            item["status"] = "under_review"
            changed += 1
        items.append(item)

    result = dict(wire)
    result["items"] = items
    return result, changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wire", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    args = parser.parse_args()

    wire = json.loads(args.wire.read_text(encoding="utf-8"))
    queue = json.loads(args.queue.read_text(encoding="utf-8"))
    updated, changed = sync(wire, queue)
    if changed:
        args.wire.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wire editorial-state sync: promoted_to_under_review={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
