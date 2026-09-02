#!/usr/bin/env python3
"""Select only low-risk, strongly evidenced news packages for automatic publication.

This is deliberately narrower than the ordinary newsroom publication queue.  A package
may bypass the repository's final human merge gate only when all of these are true:

* the semantic route is exactly ``news.publish``;
* the story is high confidence and not a privacy/policy or rumor beat;
* every claim is high-confidence and verified/corroborated, except that a high-confidence
  single-source claim is allowed when the package includes a primary source;
* evidence includes either a primary source or at least two independent source hosts.

Everything else remains in the existing human-gated newsroom path.
"""
from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from newsroom_publication_intake import normalize_package, package_id

SAFE_DESTINATIONS = {"news.publish"}
BLOCKED_BEATS = {"privacy_policy", "rumor"}
GOOD_VERIFICATIONS = {"verified", "corroborated"}


class GateError(RuntimeError):
    pass


def source_host(url: str) -> str:
    host = (urlparse(url).hostname or "").lower().rstrip(".")
    return host[4:] if host.startswith("www.") else host


def eligibility(raw: Any) -> tuple[bool, str, str | None]:
    try:
        package = normalize_package(raw)
    except Exception as exc:
        return False, f"invalid_package:{exc}", None

    pid = package_id(package)
    destinations = {route["destination"] for route in package["routes"]}
    if destinations != SAFE_DESTINATIONS:
        return False, "mixed_or_non_news_route", pid
    if package["confidence"] != "high":
        return False, "story_not_high_confidence", pid
    if package["beat"] in BLOCKED_BEATS:
        return False, f"blocked_beat:{package['beat']}", pid

    claims = package["claims"]
    if not claims:
        return False, "no_claims", pid

    sources = package["sources"]
    has_primary = any(source["source_class"] == "primary" for source in sources)
    independent_hosts = {source_host(source["url"]) for source in sources if source_host(source["url"])}
    if not has_primary and len(independent_hosts) < 2:
        return False, "insufficient_independent_evidence", pid

    for claim in claims:
        verification = claim["verification"]
        confidence = claim["confidence"]
        if confidence != "high":
            return False, f"claim_not_high_confidence:{claim['claim_id']}", pid
        if verification in GOOD_VERIFICATIONS:
            continue
        if verification == "single_source" and has_primary:
            continue
        return False, f"claim_not_publishable:{claim['claim_id']}", pid

    return True, "eligible", pid


def filter_payload(payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if payload.get("schema_version") != 1:
        raise GateError("publication queue must use schema_version 1")
    raw_packages = payload.get("packages")
    if not isinstance(raw_packages, list):
        raise GateError("publication queue packages must be a list")

    kept: list[Any] = []
    decisions: list[dict[str, Any]] = []
    eligible_ids: list[str] = []
    for raw in raw_packages:
        allowed, reason, pid = eligibility(raw)
        decisions.append({"package_id": pid, "eligible": allowed, "reason": reason})
        if allowed:
            kept.append(raw)
            if pid:
                eligible_ids.append(pid)

    filtered = {"schema_version": 1, "packages": kept}
    report = {
        "schema_version": 1,
        "eligible_count": len(kept),
        "eligible_ids": eligible_ids,
        "total_count": len(raw_packages),
        "decisions": decisions,
    }
    return filtered, report


def self_test() -> None:
    base = {
        "story_id": "story-1",
        "story_key": "example-launch",
        "title": "Example glasses launch",
        "summary": "A material launch with strong evidence.",
        "confidence": "high",
        "beat": "products",
        "claims": [{
            "claim_id": "claim-1",
            "normalized_key": "release",
            "statement": "Example Glasses launched.",
            "claim_type": "release",
            "verification": "verified",
            "confidence": "high",
        }],
        "sources": [{
            "source_id": "source-1",
            "url": "https://maker.example/product",
            "publisher": "Maker",
            "source_class": "primary",
            "published_at": "2026-09-02",
        }],
        "routes": [{
            "route_id": "route-1",
            "destination": "news.publish",
            "reason": "Material verified launch",
            "payload": {},
            "created_at": "2026-09-02T00:00:00Z",
        }],
    }
    ok, reason, _ = eligibility(base)
    assert ok and reason == "eligible"

    mixed = json.loads(json.dumps(base))
    mixed["routes"].append({
        "route_id": "route-2",
        "destination": "catalog.update",
        "reason": "Also changes catalog",
        "payload": {},
        "created_at": "2026-09-02T00:00:00Z",
    })
    assert eligibility(mixed)[1] == "mixed_or_non_news_route"

    privacy = json.loads(json.dumps(base))
    privacy["beat"] = "privacy_policy"
    assert eligibility(privacy)[1] == "blocked_beat:privacy_policy"

    weak = json.loads(json.dumps(base))
    weak["sources"][0]["source_class"] = "secondary"
    assert eligibility(weak)[1] == "insufficient_independent_evidence"

    corroborated = json.loads(json.dumps(weak))
    corroborated["sources"].append({
        "source_id": "source-2",
        "url": "https://independent.example/report",
        "publisher": "Independent",
        "source_class": "secondary",
        "published_at": "2026-09-02",
    })
    assert eligibility(corroborated)[0]

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        payload = {"schema_version": 1, "packages": [base, privacy, corroborated]}
        filtered, report = filter_payload(payload)
        assert len(filtered["packages"]) == 2
        assert report["eligible_count"] == 2
        assert len(report["eligible_ids"]) == 2
        (root / "report.json").write_text(json.dumps(report), encoding="utf-8")
    print("Newsroom automatic-publication gate self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if not args.input or not args.output or not args.report:
        parser.error("--input, --output, and --report are required unless --self-test is used")

    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise GateError("publication queue must be a JSON object")
        filtered, report = filter_payload(payload)
        args.output.write_text(json.dumps(filtered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (OSError, json.JSONDecodeError, GateError) as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"Automatic publication gate: {report['eligible_count']}/{report['total_count']} package(s) eligible")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
