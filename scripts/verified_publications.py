#!/usr/bin/env python3
"""Validate and publish the explicit Verified Research Alerts publication ledger.

The ledger is the editorial authorization boundary between public research and mail.
Discovery candidates and Watching items are deliberately outside this path.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "data" / "verified-publications.json"
RESEARCH_NEWS = ROOT / "docs" / "RESEARCH_NEWS.md"
SITE_ORIGIN = "https://glassesresearch.org"
TOPICS = {
    "hacks_development",
    "firmware_software",
    "hardware_teardown",
    "privacy_policy",
    "release_availability",
    "research_science",
    "standards_regulation",
}
DATE_HEADING = re.compile(r"^###\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4}\s+—\s+.+?)(?:\s+\{#[^}]+\})?\s*$")
SECTION = re.compile(r"^##\s+(.+?)(?:\s+\{#[^}]+\})?\s*$")
ID_RE = re.compile(r"^gr-\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)?$")


class ValidationError(RuntimeError):
    pass


def load_manifest(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read publication manifest: {exc}") from exc
    if payload.get("schema_version") != 1:
        raise ValidationError("verified-publications.json must use schema_version 1")
    if not isinstance(payload.get("publications"), list):
        raise ValidationError("verified-publications.json publications must be a list")
    return payload


def public_headings() -> tuple[dict[str, str], set[str]]:
    text = RESEARCH_NEWS.read_text(encoding="utf-8")
    section = ""
    headings: dict[str, str] = {}
    watching: set[str] = set()
    for raw in text.splitlines():
        section_match = SECTION.match(raw)
        if section_match:
            section = section_match.group(1).strip()
            continue
        heading_match = DATE_HEADING.match(raw)
        if not heading_match:
            continue
        heading = heading_match.group(1).strip()
        headings[heading] = section
        if section.lower() == "watching":
            watching.add(heading)
    return headings, watching


def validate(path: Path) -> dict:
    manifest = load_manifest(path)
    headings, watching = public_headings()
    publications = manifest["publications"]
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_headings: set[str] = set()

    for idx, item in enumerate(publications):
        label = f"publications[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue

        publication_id = str(item.get("id", ""))
        if not ID_RE.fullmatch(publication_id):
            errors.append(f"{label}.id is not a stable gr-YYYY-MM-DD-slug identifier")
        if publication_id in seen_ids:
            errors.append(f"duplicate publication id: {publication_id}")
        seen_ids.add(publication_id)

        if item.get("state") != "verified":
            errors.append(f"{publication_id or label}: state must be verified")
        if not isinstance(item.get("dispatch"), bool):
            errors.append(f"{publication_id or label}: dispatch must be true or false")

        source_heading = str(item.get("source_heading", "")).strip()
        if not source_heading:
            errors.append(f"{publication_id or label}: source_heading is required")
        elif source_heading not in headings:
            errors.append(f"{publication_id}: source_heading is not a dated heading in docs/RESEARCH_NEWS.md")
        elif source_heading in watching:
            errors.append(f"{publication_id}: Watching items cannot enter the verified publication ledger")
        if source_heading in seen_headings:
            errors.append(f"duplicate source_heading in manifest: {source_heading}")
        seen_headings.add(source_heading)

        for field in ("title", "summary"):
            value = str(item.get(field, "")).strip()
            if not value:
                errors.append(f"{publication_id or label}: {field} is required")

        canonical_url = str(item.get("canonical_url", "")).strip()
        if not canonical_url.startswith(SITE_ORIGIN + "/"):
            errors.append(f"{publication_id or label}: canonical_url must stay on {SITE_ORIGIN}")

        published_at = str(item.get("published_at", "")).strip()
        if not DATE_RE.fullmatch(published_at):
            errors.append(f"{publication_id or label}: published_at must be YYYY-MM-DD or an explicit UTC timestamp")

        for field in ("models", "brands_lineages", "topics"):
            value = item.get(field)
            if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
                errors.append(f"{publication_id or label}: {field} must be a list of non-empty strings")
        unknown_topics = set(item.get("topics") or []) - TOPICS
        if unknown_topics:
            errors.append(f"{publication_id or label}: unknown topics: {', '.join(sorted(unknown_topics))}")

    alertable_headings = {heading for heading in headings if heading not in watching}
    missing = sorted(alertable_headings - seen_headings)
    if missing:
        errors.append(
            "Every dated non-Watching Research & News item must have an explicit publication-ledger disposition; missing: "
            + " | ".join(missing)
        )

    if errors:
        raise ValidationError("\n".join(errors))

    dispatched = sum(bool(item["dispatch"]) for item in publications)
    print(
        f"Verified publication ledger valid: {len(publications)} public items, "
        f"{dispatched} dispatch-enabled, {len(watching)} Watching headings excluded."
    )
    return manifest


def request_json(url: str, *, method: str = "GET", token: str | None = None, payload: dict | None = None) -> dict:
    headers = {"User-Agent": "GlassesResearch-verified-publication-bridge/1.0"}
    data = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=25) as response:
        body = response.read().decode("utf-8")
        return json.loads(body or "{}")


def publish(manifest: dict, endpoint: str, token: str) -> None:
    enabled = [item for item in manifest["publications"] if item["dispatch"]]
    if not enabled:
        print("No dispatch-enabled verified publications.")
        return

    for item in enabled:
        payload = {
            key: item[key]
            for key in (
                "id",
                "title",
                "canonical_url",
                "summary",
                "models",
                "brands_lineages",
                "topics",
                "published_at",
            )
        }
        last_error: Exception | None = None
        for attempt in range(1, 6):
            try:
                result = request_json(endpoint, method="POST", token=token, payload=payload)
                if result.get("ok") is not True:
                    raise RuntimeError(f"publisher returned non-success response: {result}")
                print(f"Published alert event accepted: {item['id']}")
                break
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
                last_error = exc
                if attempt == 5:
                    raise RuntimeError(f"Failed publishing {item['id']} after 5 attempts: {exc}") from exc
                time.sleep(attempt * 3)
        else:
            raise RuntimeError(f"Failed publishing {item['id']}: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--publish", action="store_true", help="POST dispatch-enabled entries after validation")
    parser.add_argument("--endpoint", default="https://alerts.glassesresearch.org/published")
    args = parser.parse_args()

    try:
        manifest = validate(args.manifest)
        if args.publish:
            token = os.environ.get("PUBLISH_TOKEN", "").strip()
            if not token:
                raise ValidationError("PUBLISH_TOKEN is required for --publish")
            health = request_json("https://alerts.glassesresearch.org/health")
            if health.get("ok") is not True or health.get("service") != "verified-research-alerts":
                raise ValidationError(f"Verified Research Alerts Worker health check failed: {health}")
            print("Verified Research Alerts Worker health check passed.")
            publish(manifest, args.endpoint, token)
    except (ValidationError, RuntimeError, urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
