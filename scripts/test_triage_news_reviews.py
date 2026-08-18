#!/usr/bin/env python3
"""Regression checks for durable editorial triage state."""
from triage_news_reviews import (
    automated_state,
    preserve_editorial_fields,
    review_key,
    should_check_source,
)


def main() -> int:
    assert automated_state(
        {"relationship": "direct", "content_types": ["model"]},
        {"status": "reachable"},
    ) == "needs_editorial_verification"
    assert automated_state(
        {"relationship": "direct", "content_types": ["policy"]},
        {"status": "unreachable"},
    ) == "source_review"
    assert automated_state(
        {"relationship": "speculative", "content_types": ["model", "rumor"]},
        {"status": "reachable"},
    ) == "watching"
    assert automated_state(
        {"relationship": "adjacent", "content_types": ["research"]},
        {"status": "reachable"},
    ) == "adjacent_radar"
    assert automated_state(
        {"relationship": "irrelevant", "content_types": ["news"]},
        {"status": "reachable"},
    ) == "rejected_noise"

    pharmacy = {
        "relationship": "enabling",
        "content_types": ["optics"],
        "title": "Amazon Pharmacy | Online Prescription",
        "summary": "Prescription delivery, transfers, and refills",
        "url": "https://pharmacy.amazon.com/",
    }
    assert automated_state(pharmacy, {"status": "not_checked"}) == "rejected_noise"

    weak_eyecare = {
        "relationship": "enabling",
        "content_types": ["optics"],
        "title": "Eyecare appointments and prescription services",
        "summary": "General vision care",
        "url": "https://example.invalid/eyecare",
    }
    assert automated_state(weak_eyecare, {"status": "not_checked"}) == "source_review"

    waveguide = {
        "relationship": "enabling",
        "content_types": ["research", "optics"],
        "title": "New waveguide for near-eye displays",
        "summary": "Optical research",
        "url": "https://example.invalid/waveguide",
    }
    assert automated_state(waveguide, {"status": "reachable"}) == "needs_editorial_verification"
    assert should_check_source(waveguide) is True

    standing_watch = {
        "relationship": "direct",
        "content_types": ["model", "video"],
        "title": "Manufacturer/source watch: News – Rokid",
        "source": "manufacturer-watch",
        "url": "https://global.rokid.com/blogs/news",
    }
    assert automated_state(standing_watch, {"status": "reachable"}) == "source_monitor"
    assert should_check_source(standing_watch) is False

    catalog_watch = {
        "relationship": "direct",
        "content_types": ["model"],
        "title": "Manufacturer catalog watch: lucyd.co",
        "source": "configured manufacturer catalog",
        "discovery_channel": "manufacturer_catalog",
        "url": "https://lucyd.co/",
    }
    assert automated_state(catalog_watch, {"status": "reachable"}) == "source_monitor"
    assert should_check_source(catalog_watch) is False

    catalog_lead = {
        "relationship": "direct",
        "content_types": ["sdk"],
        "title": "Manufacturer catalog lead: Request SDK",
        "source": "https://www.everysight.com/",
        "discovery_channel": "manufacturer_catalog",
        "url": "https://www.everysight.com/pages/sdk",
    }
    assert automated_state(catalog_lead, {"status": "reachable"}) == "catalog_review"
    assert should_check_source(catalog_lead) is False

    # Collector IDs are observations, not review identity. The same source URL must
    # consume one editorial slot even when two discovery lanes assign different IDs.
    assert review_key({"id": "aaa", "url": "https://example.com/item/"}) == review_key(
        {"id": "bbb", "url": "https://example.com/item#details"}
    )
    assert review_key({"id": "aaa", "url": "https://example.com/item"}) != review_key(
        {"id": "bbb", "url": "https://example.com/other"}
    )

    record = {"title": "new observation"}
    preserve_editorial_fields(
        record,
        {
            "first_seen_utc": "2026-08-18T00:00:00+00:00",
            "editorial_disposition": "watch",
            "editorial_notes": "preserve this decision",
            "publication_authorized": False,
            "resolved_utc": "2026-08-18T01:00:00+00:00",
        },
    )
    assert record["editorial_disposition"] == "watch"
    assert record["editorial_notes"] == "preserve this decision"
    assert record["first_seen_utc"] == "2026-08-18T00:00:00+00:00"
    assert record["resolved_utc"] == "2026-08-18T01:00:00+00:00"
    assert record["publication_authorized"] is False

    print("triage_news_reviews regression checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
