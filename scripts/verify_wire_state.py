#!/usr/bin/env python3
"""Validate the developing-news wire without promoting it to verified research."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ALLOWED_STATUS = {"reported", "under_review"}
ALLOWED_SOURCE_CLASS = {
    "primary",
    "technical_reporting",
    "reputable_secondary",
    "retailer_oem",
    "community",
    "rumor",
}
REQUIRED_ITEM_KEYS = {
    "discovery_id",
    "title",
    "url",
    "publisher",
    "source_class",
    "published_at",
    "discovered_at",
    "status",
}
FORBIDDEN_ITEM_KEYS = {
    "summary",
    "verified",
    "verification",
    "confidence",
    "canonical_gls_id",
    "capabilities",
    "score",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    args = parser.parse_args()
    state = json.loads(args.state.read_text(encoding="utf-8"))

    if state.get("schema_version") != 1:
        raise SystemExit("Wire state schema version must be 1")
    if "not verified GlassesResearch claims" not in str(state.get("semantics", "")):
        raise SystemExit("Wire state must preserve its non-verified semantics")
    items = state.get("items")
    if not isinstance(items, list):
        raise SystemExit("Wire state items must be a list")

    seen = set()
    for item in items:
        if not isinstance(item, dict):
            raise SystemExit("Wire item must be an object")
        missing = REQUIRED_ITEM_KEYS - set(item)
        if missing:
            raise SystemExit(f"Wire item missing fields: {sorted(missing)}")
        forbidden = FORBIDDEN_ITEM_KEYS & set(item)
        if forbidden:
            raise SystemExit(f"Wire item leaks verification/canonical fields: {sorted(forbidden)}")
        if item["status"] not in ALLOWED_STATUS:
            raise SystemExit(f"Invalid wire status: {item['status']!r}")
        if item["source_class"] not in ALLOWED_SOURCE_CLASS:
            raise SystemExit(f"Invalid wire source class: {item['source_class']!r}")
        if not str(item["discovery_id"]).strip() or item["discovery_id"] in seen:
            raise SystemExit("Wire discovery IDs must be non-empty and unique")
        seen.add(item["discovery_id"])
        if not str(item["title"]).strip() or not str(item["publisher"]).strip():
            raise SystemExit("Wire title/publisher must be non-empty")
        parsed = urlparse(str(item["url"]))
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise SystemExit(f"Wire URL must be external HTTP(S): {item['url']!r}")
        if not str(item["discovered_at"]).strip():
            raise SystemExit("Wire discovered_at is required")

    print(f"Wire state verified: items={len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
