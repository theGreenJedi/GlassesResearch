#!/usr/bin/env python3
from import_wire_news import build_payload, convert_item


def sample(**overrides):
    item = {
        "discovery_id": "abc123",
        "title": "Example smart glasses launch reaches the US",
        "url": "https://example.com/story",
        "publisher": "Example",
        "source_class": "technical_reporting",
        "published_at": "2026-09-02T12:00:00Z",
        "discovered_at": "2026-09-02T12:05:00Z",
        "status": "reported",
    }
    item.update(overrides)
    return item


def main() -> int:
    converted = convert_item(sample())
    assert converted is not None
    assert converted["relationship"] == "direct"
    assert converted["triage_priority"] == "high"
    assert converted["publication_eligible"] is True
    assert converted["discovery_channel"] == "commodity_wire"
    assert converted["wire_status"] == "reported"
    assert "research_news_review" in converted["routing_targets"]

    policy = convert_item(sample(
        discovery_id="privacy1",
        title="Regulator opens privacy review of AI glasses",
        source_class="reputable_secondary",
    ))
    assert policy is not None
    assert policy["primary_type"] == "policy"
    assert "policy" in policy["content_types"]
    assert "policy_privacy" in policy["routing_targets"]
    assert policy["triage_priority"] == "high"

    primary = convert_item(sample(
        discovery_id="primary1",
        title="Maker previews smart glasses developer program",
        source_class="primary",
    ))
    assert primary is not None
    assert primary["triage_priority"] == "high"

    assert convert_item({"title": "missing identity", "url": "https://example.com"}) is None

    payload = build_payload(
        {"items": [sample(), sample(discovery_id="privacy1", title="Privacy lawsuit targets smart glasses")]},
        "2026-09-02T13:00:00+00:00",
    )
    assert payload["schema"] == 3
    assert payload["candidate_count"] == 2
    assert payload["relationship_counts"] == {"direct": 2}
    assert payload["routing_counts"]["research_news_review"] == 2
    assert payload["source_surface"] == "data/wire-state.json"
    assert "intake only" in payload["publication_policy"]

    print("wire-news import tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
