#!/usr/bin/env python3
"""Pull Editorial-authorized GlassesResearch newsroom packages into repository intake.

This script deliberately does not publish canonical claims. It creates durable,
idempotent package records that repository automation or a maintainer can turn into
validated canonical edits. The newsroom Worker therefore needs no GitHub write token.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = "https://glassesresearch.org/api/newsroom/publication-queue"
DEFAULT_OUTPUT = ROOT / "research" / "newsroom-packages"

# Compatibility token only. The operating model changed to one explicit Editorial
# approval followed by machine-prepared draft work and the final repository PR gate.
# Keep the historical envelope value so already-ingested packages and actuators remain
# interoperable; do not interpret this string as a current second human approval step.
AUTHORIZED_ENVELOPE_STATE = "second_gate_approved"

ALLOWED_DESTINATIONS = {
    "news.publish",
    "news.update_story",
    "catalog.update",
    "lineage.update",
    "report_card.evidence",
    "finder.update",
    "release_tracker.update",
    "research.dossier",
}


class IntakeError(RuntimeError):
    pass


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IntakeError(f"{field} must be a non-empty string")
    return value.strip()


def _one_line(value: Any, field: str) -> str:
    return " ".join(_text(value, field).split())


def _string(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def _http_url(value: Any, field: str) -> str:
    url = _text(value, field)
    if not (url.startswith("https://") or url.startswith("http://")):
        raise IntakeError(f"{field} must be HTTP(S)")
    return url


def _load_url(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "GlassesResearch-newsroom-intake/1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except Exception as exc:  # pragma: no cover - network failures are operational
        raise IntakeError(f"cannot fetch publication queue: {exc}") from exc
    if not isinstance(payload, dict):
        raise IntakeError("publication queue must be a JSON object")
    return payload


def _load_file(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IntakeError(f"cannot read publication queue fixture: {exc}") from exc
    if not isinstance(payload, dict):
        raise IntakeError("publication queue fixture must be a JSON object")
    return payload


def normalize_package(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise IntakeError("package must be an object")

    story_id = _one_line(raw.get("story_id"), "package.story_id")
    story_key = _one_line(raw.get("story_key"), "package.story_key")
    title = _one_line(raw.get("title"), "package.title")
    summary = _text(raw.get("summary"), "package.summary")
    confidence = _one_line(raw.get("confidence"), "package.confidence")
    beat = _one_line(raw.get("beat"), "package.beat")

    raw_claims = raw.get("claims")
    if not isinstance(raw_claims, list):
        raise IntakeError(f"{story_key}: claims must be a list")
    claims: list[dict[str, Any]] = []
    for index, claim in enumerate(raw_claims):
        if not isinstance(claim, dict):
            raise IntakeError(f"{story_key}: claims[{index}] must be an object")
        claims.append(
            {
                "claim_id": _one_line(claim.get("claim_id"), f"claims[{index}].claim_id"),
                "normalized_key": _one_line(claim.get("normalized_key"), f"claims[{index}].normalized_key"),
                "statement": _text(claim.get("statement"), f"claims[{index}].statement"),
                "claim_type": _one_line(claim.get("claim_type"), f"claims[{index}].claim_type"),
                "verification": _one_line(claim.get("verification"), f"claims[{index}].verification"),
                "confidence": _one_line(claim.get("confidence"), f"claims[{index}].confidence"),
            }
        )

    raw_sources = raw.get("sources")
    if not isinstance(raw_sources, list) or not raw_sources:
        raise IntakeError(f"{story_key}: sources must contain at least one source")
    sources: list[dict[str, Any]] = []
    for index, source in enumerate(raw_sources):
        if not isinstance(source, dict):
            raise IntakeError(f"{story_key}: sources[{index}] must be an object")
        sources.append(
            {
                "source_id": _one_line(source.get("source_id"), f"sources[{index}].source_id"),
                "url": _http_url(source.get("url"), f"sources[{index}].url"),
                "publisher": _string(source.get("publisher")) or "Unknown publisher",
                "source_class": _one_line(source.get("source_class"), f"sources[{index}].source_class"),
                "published_at": _string(source.get("published_at")) or None,
            }
        )

    raw_routes = raw.get("routes")
    if not isinstance(raw_routes, list) or not raw_routes:
        raise IntakeError(f"{story_key}: routes must contain at least one approved route")
    routes: list[dict[str, Any]] = []
    for index, route in enumerate(raw_routes):
        if not isinstance(route, dict):
            raise IntakeError(f"{story_key}: routes[{index}] must be an object")
        destination = _one_line(route.get("destination"), f"routes[{index}].destination")
        if destination not in ALLOWED_DESTINATIONS:
            raise IntakeError(f"{story_key}: unsupported publication route {destination!r}")
        payload = route.get("payload", {})
        if not isinstance(payload, dict):
            raise IntakeError(f"{story_key}: routes[{index}].payload must be an object")
        routes.append(
            {
                "route_id": _one_line(route.get("route_id"), f"routes[{index}].route_id"),
                "destination": destination,
                "reason": _text(route.get("reason"), f"routes[{index}].reason"),
                "payload": payload,
                "created_at": _one_line(route.get("created_at"), f"routes[{index}].created_at"),
            }
        )

    routes.sort(key=lambda item: item["route_id"])
    claims.sort(key=lambda item: item["claim_id"])
    sources.sort(key=lambda item: item["source_id"])
    return {
        "story_id": story_id,
        "story_key": story_key,
        "title": title,
        "summary": summary,
        "confidence": confidence,
        "beat": beat,
        "claims": claims,
        "sources": sources,
        "routes": routes,
    }


def package_id(package: dict[str, Any]) -> str:
    canonical = json.dumps(package, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12].upper()
    return f"GRNP-{digest}"


def _markdown(package_id_value: str, package: dict[str, Any], source_url: str) -> str:
    routes = "\n".join(
        f"- `{route['destination']}` — {route['reason']}" for route in package["routes"]
    )
    claims = "\n".join(
        f"- **{claim['verification']} / {claim['confidence']}** — {claim['statement']}"
        for claim in package["claims"]
    ) or "- No semantic claims were supplied."
    sources = "\n".join(
        f"- [{source['publisher']}]({source['url']}) — `{source['source_class']}`"
        for source in package["sources"]
    )
    return f"""# {package_id_value} — {package['title']}

**State:** authorized by the Editorial research pipeline; not yet canonical publication  
**Story key:** `{package['story_key']}`  
**Beat:** `{package['beat']}`  
**Confidence:** `{package['confidence']}`  
**Queue source:** {source_url}

> This package is an authorized draft input, not proof that the canonical repository was changed. Exact destination mapping, evidence checks, repository validation, and final PR review remain mandatory before publication.

## Current understanding

{package['summary']}

## Authorized semantic routes

{routes}

## Claims

{claims}

## Evidence sources

{sources}

## Repository application checklist

- [ ] Map every authorized route to exact canonical repository path(s).
- [ ] Verify source strength and claim wording against the underlying evidence.
- [ ] Update every materially affected canonical layer, not only the public digest.
- [ ] Produce/update the durable `research/news-reviews/` editorial record.
- [ ] Satisfy `scripts/verify_news_promotion.py` and the normal repository validation suite.
- [ ] Merge through the normal GlassesResearch PR path before treating the change as published.
"""


def ingest(payload: dict[str, Any], output_dir: Path, source_url: str) -> list[str]:
    if payload.get("schema_version") != 1:
        raise IntakeError("publication queue must use schema_version 1")
    raw_packages = payload.get("packages")
    if not isinstance(raw_packages, list):
        raise IntakeError("publication queue packages must be a list")

    output_dir.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    for raw in raw_packages:
        package = normalize_package(raw)
        pid = package_id(package)
        json_path = output_dir / f"{pid}.json"
        markdown_path = output_dir / f"{pid}.md"
        if json_path.exists() and markdown_path.exists():
            continue

        envelope = {
            "schema_version": 1,
            "package_id": pid,
            "state": AUTHORIZED_ENVELOPE_STATE,
            "source_queue": source_url,
            "ingested_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "package": package,
        }
        json_path.write_text(json.dumps(envelope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        markdown_path.write_text(_markdown(pid, package, source_url), encoding="utf-8")
        created.append(pid)
    return created


def self_test() -> None:
    fixture = {
        "schema_version": 1,
        "packages": [
            {
                "story_id": "story-1",
                "story_key": "example-glasses-launch",
                "title": "Example glasses launch",
                "summary": "A material launch supported by a primary source.",
                "confidence": "high",
                "beat": "products",
                "claims": [
                    {
                        "claim_id": "claim-1",
                        "normalized_key": "release",
                        "statement": "Example Glasses launched.",
                        "claim_type": "release",
                        "verification": "verified",
                        "confidence": "high",
                    }
                ],
                "sources": [
                    {
                        "source_id": "source-1",
                        "url": "https://example.com/glasses",
                        "publisher": "Example",
                        "source_class": "primary",
                        "published_at": "2026-09-01",
                    }
                ],
                "routes": [
                    {
                        "route_id": "route-1",
                        "destination": "news.publish",
                        "reason": "Material launch",
                        "payload": {"canonical_paths": ["docs/RESEARCH_NEWS.md"]},
                        "created_at": "2026-09-01T00:00:00Z",
                    }
                ],
            }
        ],
    }
    normalized = normalize_package(fixture["packages"][0])
    assert package_id(normalized) == package_id(normalized)
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory)
        first = ingest(fixture, output, "https://example.com/queue")
        second = ingest(fixture, output, "https://example.com/queue")
        assert len(first) == 1 and second == []
        envelope = json.loads((output / f"{first[0]}.json").read_text(encoding="utf-8"))
        assert envelope["state"] == AUTHORIZED_ENVELOPE_STATE
        markdown = (output / f"{first[0]}.md").read_text(encoding="utf-8")
        assert "authorized by the Editorial research pipeline" in markdown
        assert "second human publication gate" not in markdown
        assert "not yet canonical publication" in markdown
    print("Newsroom publication intake self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    try:
        payload = _load_file(args.input) if args.input else _load_url(args.url)
        created = ingest(payload, args.output, args.url if not args.input else str(args.input))
    except IntakeError as exc:
        print(f"ERROR: {exc}")
        return 1

    if created:
        print(f"Ingested {len(created)} Editorial-authorized newsroom package(s): {', '.join(created)}")
    else:
        print("No new Editorial-authorized newsroom draft packages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
