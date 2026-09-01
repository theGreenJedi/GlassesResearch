#!/usr/bin/env python3
"""Focused Second Life data-contract tests."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from validate_second_life import validate


def listing(now):
    return {
        "listing_id": "example-1",
        "model_id": "GLS-9999",
        "model": "Example Glass",
        "source": "Example Market",
        "condition": "used",
        "price": "$100",
        "first_seen_at": (now - timedelta(hours=2)).isoformat(),
        "last_verified_at": (now - timedelta(hours=1)).isoformat(),
        "status": "active",
        "model_match_confidence": "high",
        "fresh_for_hours": 24,
        "url": "https://example.test/item/1",
    }


def main() -> None:
    now = datetime.now(timezone.utc)
    good = {"schema_version": 1, "listings": [listing(now)]}
    assert not validate(good, now)

    future = listing(now)
    future["last_verified_at"] = (now + timedelta(hours=1)).isoformat()
    assert any("future" in error for error in validate({"schema_version": 1, "listings": [future]}, now))

    unsafe = listing(now)
    unsafe["url"] = "javascript:alert(1)"
    assert any("https" in error for error in validate({"schema_version": 1, "listings": [unsafe]}, now))

    missing = listing(now)
    del missing["model_id"]
    assert any("model_id" in error for error in validate({"schema_version": 1, "listings": [missing]}, now))

    print("Second Life contract tests passed")


if __name__ == "__main__":
    main()
