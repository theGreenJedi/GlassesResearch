#!/usr/bin/env python3
"""Validate the canonical GRE verified-change ledger and derive publication payloads.

GRE events are the durable identity for verified changes. Discovery candidates and
Watching items never enter this ledger. Subscriber-delivery payloads remain backward
compatible with the existing gr-YYYY-MM-DD-* publication IDs and alert-match terms.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHANGES = ROOT / "data" / "verified-changes.json"
RESEARCH_NEWS = ROOT / "docs" / "RESEARCH_NEWS.md"
THE_LIST = ROOT / "models" / "THE_LIST.md"
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
CHANGE_TYPES = {
    "catalog_admission",
    "software_release",
    "firmware_change",
    "hardware_change",
    "availability_change",
    "policy_change",
    "research_release",
    "relationship_change",
    "correction",
}
GRE_RE = re.compile(r"^GRE-\d{6}$")
PUBLICATION_RE = re.compile(r"^gr-\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$")
GLS_RE = re.compile(r"^GLS-\d{4}$")
GLR_RE = re.compile(r"^GLR-[0-9A-F]{12}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)?$")
DATE_HEADING = re.compile(r"^###\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4}\s+—\s+.+?)(?:\s+\{#[^}]+\})?\s*$")
SECTION = re.compile(r"^##\s+(.+?)(?:\s+\{#[^}]+\})?\s*$")


class ValidationError(RuntimeError):
    pass


def load(path: Path = DEFAULT_CHANGES) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read verified-change ledger: {exc}") from exc
    if payload.get("schema_version") != 1:
        raise ValidationError("verified-changes.json must use schema_version 1")
    if not isinstance(payload.get("events"), list):
        raise ValidationError("verified-changes.json events must be a list")
    return payload


def public_headings() -> tuple[dict[str, str], set[str]]:
    section = ""
    headings: dict[str, str] = {}
    watching: set[str] = set()
    for raw in RESEARCH_NEWS.read_text(encoding="utf-8").splitlines():
        section_match = SECTION.match(raw)
        if section_match:
            section = section_match.group(1).strip()
            continue
        heading_match = DATE_HEADING.match(raw)
        if not heading_match:
            continue
        heading = heading_match.group(1).strip()
        headings[heading] = section
        if section.casefold() == "watching":
            watching.add(heading)
    return headings, watching


def canonical_model_ids() -> set[str]:
    return set(re.findall(r"\bGLS-\d{4}\b", THE_LIST.read_text(encoding="utf-8")))


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


def validate(path: Path = DEFAULT_CHANGES) -> dict[str, Any]:
    payload = load(path)
    events = payload["events"]
    headings, watching = public_headings()
    canonical = canonical_model_ids()
    errors: list[str] = []
    seen_event_ids: set[str] = set()
    seen_publication_ids: set[str] = set()
    seen_headings: set[str] = set()
    event_ids_in_order: list[str] = []

    for idx, event in enumerate(events):
        label = f"events[{idx}]"
        if not isinstance(event, dict):
            errors.append(f"{label} must be an object")
            continue
        event_id = str(event.get("id", ""))
        event_ids_in_order.append(event_id)
        if not GRE_RE.fullmatch(event_id):
            errors.append(f"{label}.id must match GRE-000000")
        if event_id in seen_event_ids:
            errors.append(f"duplicate GRE id: {event_id}")
        seen_event_ids.add(event_id)
        if event.get("state") != "verified":
            errors.append(f"{event_id or label}: state must be verified")
        if event.get("change_type") not in CHANGE_TYPES:
            errors.append(f"{event_id or label}: unsupported change_type {event.get('change_type')!r}")
        verified_at = str(event.get("verified_at", ""))
        if not DATE_RE.fullmatch(verified_at):
            errors.append(f"{event_id or label}: verified_at must be YYYY-MM-DD or an explicit UTC timestamp")
        previous_state = str(event.get("previous_state", "")).strip()
        new_state = str(event.get("new_state", "")).strip()
        if not previous_state or not new_state:
            errors.append(f"{event_id or label}: previous_state and new_state are required")
        elif previous_state == new_state:
            errors.append(f"{event_id or label}: previous_state and new_state must differ")

        affected = event.get("affected")
        if not isinstance(affected, dict):
            errors.append(f"{event_id or label}: affected must be an object")
            affected = {}
        model_ids = affected.get("model_ids", [])
        relationship_ids = affected.get("relationship_ids", [])
        if not _string_list(model_ids):
            errors.append(f"{event_id or label}: affected.model_ids must be a list of strings")
            model_ids = []
        if not _string_list(relationship_ids):
            errors.append(f"{event_id or label}: affected.relationship_ids must be a list of strings")
            relationship_ids = []
        if len(model_ids) != len(set(model_ids)):
            errors.append(f"{event_id or label}: affected.model_ids contains duplicates")
        if len(relationship_ids) != len(set(relationship_ids)):
            errors.append(f"{event_id or label}: affected.relationship_ids contains duplicates")
        for model_id in model_ids:
            if not GLS_RE.fullmatch(model_id) or model_id not in canonical:
                errors.append(f"{event_id or label}: affected model is not canonical: {model_id}")
        for relationship_id in relationship_ids:
            if not GLR_RE.fullmatch(relationship_id):
                errors.append(f"{event_id or label}: invalid relationship id: {relationship_id}")

        evidence_urls = event.get("evidence_urls")
        if not _string_list(evidence_urls) or not evidence_urls:
            errors.append(f"{event_id or label}: evidence_urls must contain at least one URL")
        else:
            for url in evidence_urls:
                if not (url.startswith("https://") or url.startswith("http://")):
                    errors.append(f"{event_id or label}: evidence URL must be HTTP(S): {url}")

        publication = event.get("publication")
        if not isinstance(publication, dict):
            errors.append(f"{event_id or label}: publication must be an object")
            publication = {}
        publication_id = str(publication.get("id", ""))
        if not PUBLICATION_RE.fullmatch(publication_id):
            errors.append(f"{event_id or label}: publication.id is invalid")
        if publication_id in seen_publication_ids:
            errors.append(f"duplicate publication id: {publication_id}")
        seen_publication_ids.add(publication_id)
        if not isinstance(publication.get("dispatch"), bool):
            errors.append(f"{event_id or label}: publication.dispatch must be true or false")
        heading = str(publication.get("source_heading", "")).strip()
        if not heading:
            errors.append(f"{event_id or label}: publication.source_heading is required")
        elif heading not in headings:
            errors.append(f"{event_id}: source_heading is not a dated heading in docs/RESEARCH_NEWS.md")
        elif heading in watching:
            errors.append(f"{event_id}: Watching items cannot become GRE events")
        if heading in seen_headings:
            errors.append(f"duplicate source_heading: {heading}")
        seen_headings.add(heading)
        for field in ("title", "summary"):
            if not str(publication.get(field, "")).strip():
                errors.append(f"{event_id or label}: publication.{field} is required")
        canonical_url = str(publication.get("canonical_url", "")).strip()
        if not canonical_url.startswith(SITE_ORIGIN + "/"):
            errors.append(f"{event_id or label}: publication.canonical_url must stay on {SITE_ORIGIN}")
        published_at = str(publication.get("published_at", "")).strip()
        if not DATE_RE.fullmatch(published_at):
            errors.append(f"{event_id or label}: publication.published_at must be a date or UTC timestamp")
        if PUBLICATION_RE.fullmatch(publication_id) and DATE_RE.fullmatch(published_at):
            if publication_id[3:13] != published_at[:10]:
                errors.append(f"{event_id}: publication ID date and published_at date disagree")

        alert = event.get("alert_match")
        if not isinstance(alert, dict):
            errors.append(f"{event_id or label}: alert_match must be an object")
            alert = {}
        for field in ("models", "brands_lineages", "topics"):
            if not _string_list(alert.get(field, [])):
                errors.append(f"{event_id or label}: alert_match.{field} must be a list of strings")
        unknown_topics = set(alert.get("topics") or []) - TOPICS
        if unknown_topics:
            errors.append(f"{event_id or label}: unknown alert topics: {', '.join(sorted(unknown_topics))}")
        alert_models = {value.casefold() for value in alert.get("models") or []}
        for model_id in model_ids:
            if model_id.casefold() not in alert_models:
                errors.append(f"{event_id}: affected canonical model {model_id} must also be an alert-match model")

    if event_ids_in_order != sorted(event_ids_in_order):
        errors.append("GRE events must remain ordered by stable event ID")
    alertable_headings = {heading for heading in headings if heading not in watching}
    missing = sorted(alertable_headings - seen_headings)
    if missing:
        errors.append("Every dated non-Watching Research & News item needs one GRE event; missing: " + " | ".join(missing))
    extra = sorted(seen_headings - alertable_headings)
    if extra:
        errors.append("GRE events reference non-alertable headings: " + " | ".join(extra))

    if errors:
        raise ValidationError("\n".join(errors))
    dispatched = sum(bool(event["publication"]["dispatch"]) for event in events)
    print(
        f"Verified change ledger valid: {len(events)} GRE events, {dispatched} dispatch-enabled, "
        f"{len(watching)} Watching headings excluded."
    )
    return payload


def publication_manifest(payload: dict[str, Any]) -> dict[str, Any]:
    publications = []
    for event in payload["events"]:
        publication = event["publication"]
        alert = event["alert_match"]
        publications.append({
            "id": publication["id"],
            "event_id": event["id"],
            "state": "verified",
            "dispatch": publication["dispatch"],
            "source_heading": publication["source_heading"],
            "title": publication["title"],
            "canonical_url": publication["canonical_url"],
            "summary": publication["summary"],
            "models": list(alert["models"]),
            "brands_lineages": list(alert["brands_lineages"]),
            "topics": list(alert["topics"]),
            "published_at": publication["published_at"],
        })
    return {
        "schema_version": 1,
        "derived_from": "data/verified-changes.json",
        "publications": publications,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changes", type=Path, default=DEFAULT_CHANGES)
    parser.add_argument("--publication-output", type=Path)
    args = parser.parse_args()
    try:
        payload = validate(args.changes)
    except ValidationError as exc:
        print(str(exc))
        return 1
    if args.publication_output:
        args.publication_output.parent.mkdir(parents=True, exist_ok=True)
        args.publication_output.write_text(json.dumps(publication_manifest(payload), indent=2) + "\n", encoding="utf-8")
        print(f"Derived publication manifest: {args.publication_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
