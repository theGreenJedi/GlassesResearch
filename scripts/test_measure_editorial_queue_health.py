#!/usr/bin/env python3
"""Regression checks for editorial queue health observability."""
from measure_editorial_queue_health import build_health, markdown


def main() -> int:
    queue = {
        "generated_utc": "2026-09-10T12:00:00+00:00",
        "candidates": [
            {
                "id": "a",
                "title": "High review 1",
                "url": "https://example.com/a",
                "triage_state": "needs_editorial_verification",
                "triage_priority": "high",
                "editorial_disposition": "pending",
                "first_seen_utc": "2026-09-10T00:00:00+00:00",
            },
            {
                "id": "b",
                "title": "High review 2",
                "url": "https://example.com/b",
                "triage_state": "source_review",
                "triage_priority": "high",
                "editorial_disposition": "pending",
                "first_seen_utc": "2026-09-06T12:00:00+00:00",
            },
            {
                "id": "c",
                "title": "Normal review",
                "url": "https://example.com/c",
                "triage_state": "needs_editorial_verification",
                "triage_priority": "normal",
                "editorial_disposition": "pending",
                "first_seen_utc": "2026-09-02T12:00:00+00:00",
            },
            {
                "id": "d",
                "title": "Published today",
                "url": "https://example.com/d",
                "triage_state": "editorial_published",
                "triage_priority": "high",
                "editorial_disposition": "published",
                "first_seen_utc": "2026-09-08T12:00:00+00:00",
                "resolved_utc": "2026-09-10T06:00:00+00:00",
            },
            {
                "id": "e",
                "title": "Published last week",
                "url": "https://example.com/e",
                "triage_state": "editorial_published",
                "triage_priority": "normal",
                "editorial_disposition": "published",
                "first_seen_utc": "2026-09-01T12:00:00+00:00",
                "resolved_utc": "2026-09-04T12:00:00+00:00",
            },
        ],
    }

    health = build_health(queue)
    assert health["actionable_pending"]["count"] == 3
    assert health["needs_editorial_verification"]["count"] == 2
    assert health["high_priority_actionable"]["count"] == 2
    assert health["high_priority_needs_editorial_verification"]["count"] == 1
    assert health["high_priority_actionable"]["median_age_hours"] == 48.0
    assert health["high_priority_actionable"]["p90_age_hours"] == 96.0
    assert health["high_priority_actionable"]["over_72h"] == 1
    assert health["needs_editorial_verification"]["over_168h"] == 1
    assert health["verified_publication_throughput"]["retained_published_total"] == 2
    assert health["verified_publication_throughput"]["resolved_last_24h"] == 1
    assert health["verified_publication_throughput"]["resolved_last_7d"] == 2
    assert health["verified_publication_throughput"]["resolved_last_14d"] == 2
    assert health["oldest_high_priority_actionable"][0]["id"] == "b"

    rendered = markdown(health)
    assert "Observability only" in rendered
    assert "High-priority actionable" in rendered
    assert "Published today" not in rendered

    print("editorial queue health regression checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
