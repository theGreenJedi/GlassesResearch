#!/usr/bin/env python3
"""Regression checks for explicit editorial decision application."""
from apply_editorial_decisions import apply_payload, decision_map


def main() -> int:
    source = "https://example.com/release/"
    queue = {
        "generated_utc": "2026-08-18T15:00:00+00:00",
        "candidates": [
            {
                "id": "collector-id",
                "url": source,
                "editorial_disposition": "pending",
                "publication_authorized": False,
                "triage_state": "needs_editorial_verification",
                "publication_gate": "blocked_pending_editorial_verification",
            }
        ],
    }
    decisions = {
        "decisions": [
            {
                "source_url": "https://example.com/release#section",
                "disposition": "published",
                "publication_authorized": True,
                "decided_utc": "2026-08-18T15:30:00Z",
                "editorial_notes": "verified",
                "canonical_destinations": ["https://glassesresearch.org/example/"],
                "verified_change_id": "GRE-000123",
                "verified_publication_id": "gr-example",
            }
        ]
    }
    mapped = decision_map(decisions)
    assert len(mapped) == 1
    result = apply_payload(queue, decisions)
    item = result["candidates"][0]
    assert item["editorial_disposition"] == "published"
    assert item["publication_authorized"] is True
    assert item["publication_gate"] == "authorized"
    assert item["triage_state"] == "editorial_published"
    assert item["verified_change_id"] == "GRE-000123"
    assert item["verified_publication_id"] == "gr-example"
    assert result["editorial_decisions_applied"] == 1

    watch = apply_payload(
        queue,
        {"decisions": [{"source_url": source, "disposition": "watch", "publication_authorized": True}]},
    )["candidates"][0]
    assert watch["publication_authorized"] is False
    assert watch["publication_gate"] == "not_publication_eligible"
    assert watch["triage_state"] == "editorial_watch"

    print("editorial decision application regression checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
