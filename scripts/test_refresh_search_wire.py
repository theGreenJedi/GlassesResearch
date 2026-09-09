#!/usr/bin/env python3
"""Regression checks for public-wire discovery velocity helpers."""
from __future__ import annotations

import datetime as dt

from refresh_search_wire import parse_sentinel, velocity_summary


def test_sentinel_only_surfaces_relevant_outbound_publishers() -> None:
    html = b"""
    <html><body>
      <a href="https://www.smartglasses.today/articles">All articles</a>
      <a href="https://kguttag.com/2026/09/09/silicon-carbide-waveguide/">Silicon Carbide Waveguides Pros and Cons</a>
      <a href="https://example.com/football">Tonight's football scores</a>
    </body></html>
    """
    items = parse_sentinel(html, "smartglasses.today", "https://www.smartglasses.today/articles")
    assert len(items) == 1
    assert items[0]["publisher"] == "kguttag.com"
    assert items[0]["source_class"] == "technical_reporting"
    assert items[0]["status"] == "reported"
    assert items[0]["published_at"] == ""


def test_velocity_summary_tracks_discovery_delay() -> None:
    now = dt.datetime(2026, 9, 9, 16, 0, tzinfo=dt.timezone.utc)
    items = [
        {
            "published_at": "2026-09-09T14:00:00Z",
            "discovered_at": "2026-09-09T14:30:00Z",
        },
        {
            "published_at": "2026-09-09T13:00:00Z",
            "discovered_at": "2026-09-09T15:00:00Z",
        },
        {
            "published_at": "",
            "discovered_at": "2026-09-09T15:30:00Z",
        },
    ]
    summary = velocity_summary(items, now)
    assert summary["items_in_window"] == 3
    assert summary["items_published_last_24h"] == 2
    assert summary["items_discovered_last_24h"] == 3
    assert summary["median_discovery_delay_minutes"] == 75.0
    assert summary["p90_discovery_delay_minutes"] == 120.0
    assert summary["within_target_percent"] == 100.0


if __name__ == "__main__":
    test_sentinel_only_surfaces_relevant_outbound_publishers()
    test_velocity_summary_tracks_discovery_delay()
    print("refresh_search_wire regression checks passed")
