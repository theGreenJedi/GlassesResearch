#!/usr/bin/env python3
from sync_wire_review_state import sync


def main() -> int:
    wire = {
        "schema_version": 1,
        "items": [
            {"discovery_id": "a", "url": "https://example.com/a", "status": "reported"},
            {"discovery_id": "b", "url": "https://example.com/b", "status": "reported"},
            {"discovery_id": "c", "url": "https://example.com/c", "status": "under_review"},
        ],
    }
    queue = {
        "candidates": [
            {
                "url": "https://example.com/a/",
                "triage_state": "needs_editorial_verification",
                "editorial_disposition": "pending",
            },
            {
                "url": "https://example.com/b",
                "triage_state": "adjacent_radar",
                "editorial_disposition": "pending",
            },
            {
                "url": "https://example.com/c",
                "triage_state": "source_review",
                "editorial_disposition": "pending",
            },
        ]
    }
    updated, changed = sync(wire, queue)
    statuses = {item["discovery_id"]: item["status"] for item in updated["items"]}
    assert changed == 1
    assert statuses == {"a": "under_review", "b": "reported", "c": "under_review"}

    resolved_queue = {
        "candidates": [
            {
                "url": "https://example.com/a",
                "triage_state": "needs_editorial_verification",
                "editorial_disposition": "published",
            }
        ]
    }
    updated, changed = sync({"schema_version": 1, "items": [{"url": "https://example.com/a", "status": "reported"}]}, resolved_queue)
    assert changed == 0
    assert updated["items"][0]["status"] == "reported"
    print("wire review-state sync tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
