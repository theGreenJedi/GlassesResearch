#!/usr/bin/env python3
"""Regression checks for knowledge-flow classification."""
from knowledge_flow import classify_types, enrich_candidate, route_candidate, term_match


def main() -> int:
    assert not term_match("eligible households receive food security benefits", "ble")
    assert term_match("BLE firmware access is documented", "ble")
    assert not term_match("paid assistant", "ai")
    assert term_match("AI glasses launched", "ai")

    noise = enrich_candidate(
        {
            "title": "Telangana extends food security to eligible families",
            "summary": "Policy update for ration-card beneficiaries",
            "url": "https://example.invalid/food",
            "materiality_score": 2,
        },
        source_lane="core_glasses",
    )
    assert noise["relationship"] == "irrelevant"
    assert noise["routing_targets"] == ["reject_noise"]

    direct = enrich_candidate(
        {
            "title": "CyanBridge v2.1.1",
            "summary": "Firmware release with SDK and BLE support",
            "url": "https://github.com/example/release",
            "materiality_score": 7,
        },
        trusted_direct_source=True,
    )
    assert direct["relationship"] == "direct"
    assert "development_hacking" in direct["routing_targets"]

    rumor = enrich_candidate(
        {
            "title": "Apple reportedly targets smart glasses for 2027",
            "summary": "Supply-chain rumor",
            "url": "https://example.invalid/apple",
            "materiality_score": 5,
        },
        source_lane="core_glasses",
    )
    assert rumor["relationship"] == "speculative"
    assert "watching" in rumor["routing_targets"]
    assert rumor["publication_eligible"] is False

    optics = enrich_candidate(
        {
            "title": "New waveguide reduces ghosting in wearable displays",
            "summary": "Optical research for near-eye displays",
            "url": "https://example.invalid/optics",
            "materiality_score": 5,
        },
        source_lane="research",
        channel_hint="research",
    )
    assert optics["relationship"] == "enabling"
    assert "research_optics" in optics["routing_targets"]
    assert "deep_research" in optics["routing_targets"]

    review_types = classify_types(
        title="Hands-on smart glasses review video",
        relationship="direct",
        url="https://youtube.com/watch?v=1",
    )
    assert "review" in review_types
    assert "video" in review_types
    assert "report_card_evidence" in route_candidate("direct", review_types)

    print("knowledge-flow classifier regression checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
