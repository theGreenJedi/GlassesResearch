#!/usr/bin/env python3
"""Focused contract tests for ownership-path and Second Life freshness semantics."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from build_acquisition_surfaces import classify, fresh_listing


def test_classification() -> None:
    device = {"id": "GLS-9999", "maker": "Example", "model": "Glass", "state": "Current"}
    official = {
        "source_type": "manufacturer", "condition": "new", "availability": "available",
        "exact_model_confidence": "high", "url": "https://example.com/glass",
    }
    row = classify(device, [official], {})
    assert row["state"] == "current_new_route_known"
    assert row["official"] == official
    assert row["buy_new"] == official

    family = dict(official, exact_model_confidence="family", availability="unknown")
    row = classify(device, [family], {})
    assert row["official"] is None
    assert row["state"] == "no_verified_acquisition_route"

    dead = dict(official)
    row = classify(device, [dead], {("GLS-9999", dead["url"]): "redirected"})
    assert row["official"] is None
    assert row["buy_new"] is None


def test_second_life_freshness() -> None:
    now = datetime.now(timezone.utc)
    base = {
        "model_id": "GLS-9999", "status": "active", "fresh_for_hours": 24,
        "url": "https://market.example/item/1",
    }
    current = dict(base, last_verified_at=(now - timedelta(hours=1)).isoformat())
    future = dict(base, last_verified_at=(now + timedelta(hours=1)).isoformat())
    stale = dict(base, last_verified_at=(now - timedelta(hours=25)).isoformat())
    unsafe = dict(base, last_verified_at=(now - timedelta(hours=1)).isoformat(), url="javascript:alert(1)")
    unscoped = dict(base, model_id=None, last_verified_at=(now - timedelta(hours=1)).isoformat())

    assert fresh_listing(current, "GLS-9999", now)
    assert not fresh_listing(future, "GLS-9999", now)
    assert not fresh_listing(stale, "GLS-9999", now)
    assert not fresh_listing(unsafe, "GLS-9999", now)
    assert not fresh_listing(unscoped, "GLS-9999", now)


if __name__ == "__main__":
    test_classification()
    test_second_life_freshness()
    print("acquisition surface contract tests passed")
