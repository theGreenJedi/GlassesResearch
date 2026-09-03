#!/usr/bin/env python3
"""Import the public developing wire into durable newsroom intake.

The public wire and the institutional collector are intentionally different discovery
surfaces. This bridge makes sure useful commodity-search discoveries do not stop at
the public ticker: each current wire report is also represented as an ordinary
unverified research candidate for the existing triage/verification conveyor.

Nothing here verifies a claim or authorizes publication.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from collections import Counter
from pathlib import Path

POLICY_TERMS = (
    "privacy", "regulator", "regulation", "lawsuit", "suit", "ban", "banned",
    "security", "surveillance", "court", "legal", "law ", "policy",
)
HIGH_MATERIALITY_TERMS = (
    "launch", "launches", "launched", "release", "released", "shipping", "ships",
    "available", "availability", "preorder", "pre-order", "recall", "discontinued",
    "acquisition", "sdk", "api", "firmware", "privacy", "lawsuit", "regulator", "ban",
)
MODEL_TERMS = (
    "glasses", "specs", "ray-ban", "rayneo", "xreal", "rokid", "viture", "vuzix",
    "vive eagle", "even realities",
)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def keyword_hits(title: str) -> list[str]:
    text = title.casefold()
    return sorted({term.strip() for term in HIGH_MATERIALITY_TERMS if term in text})


def convert_item(item: dict) -> dict | None:
    if not isinstance(item, dict):
        return None
    title = str(item.get("title", "")).strip()
    url = str(item.get("url", "")).strip()
    discovery_id = str(item.get("discovery_id", "")).strip()
    if not title or not url or not discovery_id:
        return None

    text = title.casefold()
    hits = keyword_hits(title)
    is_policy = any(term in text for term in POLICY_TERMS)
    looks_model_related = any(term in text for term in MODEL_TERMS)
    source_class = str(item.get("source_class", "reputable_secondary")).strip() or "reputable_secondary"
    priority = "high" if source_class == "primary" or len(hits) >= 1 else "normal"
    materiality = 4 if priority == "high" else 3

    content_types = ["news"]
    routing_targets = ["research_news_review"]
    primary_type = "news"
    if is_policy:
        content_types.append("policy")
        routing_targets.append("policy_privacy")
        primary_type = "policy"
    if looks_model_related:
        content_types.append("model")

    publisher = str(item.get("publisher", "")).strip() or "unknown publisher"
    return {
        "id": f"wire-{discovery_id}",
        "title": title,
        "url": url,
        "source": f"Commodity news wire: {publisher}",
        "source_lane": "core_glasses",
        "published": str(item.get("published_at", "")).strip(),
        "summary": title,
        "materiality_score": materiality,
        "keyword_hits": hits,
        "status": "candidate",
        "relationship": "direct",
        "content_types": sorted(set(content_types)),
        "primary_type": primary_type,
        "routing_targets": routing_targets,
        "triage_priority": priority,
        "publication_eligible": True,
        "publication_gate_reason": "commodity-wire discovery retained for independent editorial verification",
        "disposition": "collected",
        "site_action": "none_pending_editorial_review",
        "institution_test": "review durability",
        "discovery_channel": "commodity_wire",
        "wire_status": str(item.get("status", "reported")),
        "wire_discovered_at": str(item.get("discovered_at", "")),
        "wire_source_class": source_class,
        "wire_publisher": publisher,
    }


def build_payload(wire: dict, discovered_utc: str) -> dict:
    candidates = [converted for item in wire.get("items", []) if (converted := convert_item(item))]
    relationships = Counter(str(item.get("relationship", "unknown")) for item in candidates)
    types = Counter(kind for item in candidates for kind in item.get("content_types", []))
    routes = Counter(route for item in candidates for route in item.get("routing_targets", []))
    return {
        "schema": 3,
        "discovered_utc": discovered_utc,
        "candidate_count": len(candidates),
        "precision_rejected_count": 0,
        "relationship_counts": dict(sorted(relationships.items())),
        "type_counts": dict(sorted(types.items())),
        "routing_counts": dict(sorted(routes.items())),
        "publication_policy": "wire discovery is intake only; triage, independent verification, editorial review, and canonical publication remain separate gates",
        "collector_errors": [],
        "source_surface": "data/wire-state.json",
        "candidates": candidates,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wire", type=Path, default=Path("data/wire-state.json"))
    parser.add_argument("--output", type=Path, default=Path("research/news-candidates/wire-latest.json"))
    args = parser.parse_args()

    if not args.wire.exists():
        print(f"No public wire state at {args.wire}; nothing to import.")
        return 0
    wire = json.loads(args.wire.read_text(encoding="utf-8"))
    if wire.get("schema_version") != 1 or not isinstance(wire.get("items"), list):
        raise SystemExit("Public wire state does not satisfy the expected schema")

    payload = build_payload(wire, utc_now())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Imported public wire into editorial intake: candidates={payload['candidate_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
