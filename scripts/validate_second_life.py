#!/usr/bin/env python3
"""Validate Second Life listing records before they reach the public site."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = {
    "listing_id", "model_id", "model", "source", "condition", "price",
    "first_seen_at", "last_verified_at", "status", "model_match_confidence",
    "fresh_for_hours", "url",
}
STATUSES = {"active", "inactive", "sold", "expired", "removed"}
CONFIDENCE = {"high", "medium", "low", "unknown"}


def parse_time(value: object) -> datetime:
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def validate(payload: dict, now: datetime | None = None) -> list[str]:
    now = now or datetime.now(timezone.utc)
    errors: list[str] = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    listings = payload.get("listings")
    if not isinstance(listings, list):
        return errors + ["listings must be an array"]

    seen_ids: set[str] = set()
    for index, item in enumerate(listings):
        prefix = f"listing[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = sorted(REQUIRED - set(item))
        if missing:
            errors.append(f"{prefix} missing: {', '.join(missing)}")
            continue
        listing_id = str(item["listing_id"])
        if not listing_id or listing_id in seen_ids:
            errors.append(f"{prefix} listing_id must be unique and non-empty")
        seen_ids.add(listing_id)
        model_id = str(item["model_id"])
        if not (len(model_id) == 8 and model_id.startswith("GLS-") and model_id[4:].isdigit()):
            errors.append(f"{prefix} model_id must look like GLS-0000")
        if item.get("status") not in STATUSES:
            errors.append(f"{prefix} has invalid status")
        if item.get("model_match_confidence") not in CONFIDENCE:
            errors.append(f"{prefix} has invalid model_match_confidence")
        try:
            ttl = float(item.get("fresh_for_hours"))
            if ttl <= 0:
                raise ValueError
        except (TypeError, ValueError):
            errors.append(f"{prefix} fresh_for_hours must be > 0")
        parsed = urlparse(str(item.get("url") or ""))
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{prefix} url must be an absolute https URL")
        try:
            first_seen = parse_time(item.get("first_seen_at"))
            verified = parse_time(item.get("last_verified_at"))
            if first_seen > verified:
                errors.append(f"{prefix} first_seen_at is after last_verified_at")
            if verified > now:
                errors.append(f"{prefix} last_verified_at is in the future")
        except (TypeError, ValueError):
            errors.append(f"{prefix} timestamps must be valid ISO-8601 values")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.path.read_text(encoding="utf-8"))
    errors = validate(payload)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(payload.get('listings', []))} Second Life listings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
