#!/usr/bin/env python3
"""Regression checks for public-wire discovery velocity and provenance helpers."""
from __future__ import annotations

import datetime as dt

from refresh_search_wire import (
    merge_discovery_candidate,
    parse_sentinel,
    provenance_summary,
    velocity_summary,
)


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
    assert items[0]["discovered_via"] == ["Sentinel smartglasses.today"]


def test_dedup_preserves_every_discovery_route() -> None:
    now = dt.datetime(2026, 9, 9, 16, 0, tzinfo=dt.timezone.utc)
    google = {
        "discovery_id": "google-id",
        "title": "Samsung starts developing smart glasses with a color display",
        "url": "https://news.google.com/example",
        "publisher": "SamMobile",
        "source_class": "technical_reporting",
        "published_at": "2026-09-09T13:00:00Z",
        "discovered_at": "",
        "status": "reported",
        "discovered_via": ["Google News"],
        "first_discovered_via": [],
    }
    sentinel = {
        "discovery_id": "sentinel-id",
        "title": "Samsung starts developing smart glasses with a color display",
        "url": "https://sammobile.com/news/example",
        "publisher": "sammobile.com",
        "source_class": "technical_reporting",
        "published_at": "",
        "discovered_at": "",
        "status": "reported",
        "discovered_via": ["Sentinel smartglasses.today"],
        "first_discovered_via": [],
    }
    dedup: dict[str, dict] = {}
    merge_discovery_candidate(dedup, google, {}, now)
    merge_discovery_candidate(dedup, sentinel, {}, now)
    assert len(dedup) == 1
    item = next(iter(dedup.values()))
    assert item["discovered_via"] == ["Google News", "Sentinel smartglasses.today"]


def test_provenance_summary_counts_true_sentinel_rescues() -> None:
    items = [
        {
            "discovered_via": ["Sentinel smartglasses.today", "Google News"],
            "first_discovered_via": ["Sentinel smartglasses.today"],
        },
        {
            "discovered_via": ["Sentinel smartglasses.today", "Google News"],
            "first_discovered_via": ["Google News", "Sentinel smartglasses.today"],
        },
    ]
    summary = provenance_summary(items)
    assert summary["route_counts"]["Sentinel smartglasses.today"] == 2
    assert summary["route_counts"]["Google News"] == 2
    assert summary["sentinel_rescues"] == {"smartglasses.today": 1}


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
    test_dedup_preserves_every_discovery_route()
    test_provenance_summary_counts_true_sentinel_rescues()
    test_velocity_summary_tracks_discovery_delay()
    print("refresh_search_wire regression checks passed")
