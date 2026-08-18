#!/usr/bin/env python3
"""Regression checks for durable editorial triage state."""
from triage_news_reviews import automated_state, preserve_editorial_fields


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
