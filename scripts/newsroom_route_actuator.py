#!/usr/bin/env python3
"""Materialize every approved newsroom route into an auditable repository action.

Direct canonical mutation is intentionally narrow. News-only publication is handled by
`newsroom_news_actuator.py`. This dispatcher makes every other second-gate-approved
route produce a deterministic repository consequence without inventing identity,
scores, lineage, or release truth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "research" / "newsroom-packages"
ACTIONS = ROOT / "research" / "newsroom-actions"
DOSSIERS = ROOT / "research" / "newsroom-dossiers"
EVIDENCE = ROOT / "research" / "newsroom-evidence"
THE_LIST = ROOT / "models" / "THE_LIST.md"
GLS_RE = re.compile(r"^GLS-\d{4}$")

NEWS_DESTINATIONS = {"news.publish", "news.update_story"}
SUPPORTED = {
    "catalog.update",
    "lineage.update",
    "report_card.evidence",
    "finder.update",
    "release_tracker.update",
    "research.dossier",
}

OWNER = {
    "catalog.update": "model-investigator/catalog",
    "lineage.update": "lineage-specialist",
    "report_card.evidence": "report-card-evidence",
    "finder.update": "finder/comparison-data",
    "release_tracker.update": "release-tracker",
    "research.dossier": "research-desk",
}


class RouteActuatorError(RuntimeError):
    pass


def _load(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RouteActuatorError(f"cannot read {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RouteActuatorError(f"{path}: expected object")
    return payload


def _known_gls(path: Path = THE_LIST) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"\bGLS-\d{4}\b", text))


def _context(route: dict[str, Any]) -> dict[str, Any] | None:
    payload = route.get("payload")
    if not isinstance(payload, dict):
        return None
    context = payload.get("newsroom_context")
    if not isinstance(context, dict) or context.get("schema_version") != 1:
        return None
    return context


def _targets(context: dict[str, Any] | None, known_gls: set[str]) -> tuple[list[str], list[str]]:
    if not context:
        return [], []
    valid: set[str] = set()
    invalid: set[str] = set()
    entities = context.get("entities")
    if not isinstance(entities, list):
        return [], []
    for entity in entities:
        if not isinstance(entity, dict):
            continue
        value = entity.get("canonical_gls_id")
        if not isinstance(value, str) or not value:
            continue
        if not GLS_RE.fullmatch(value) or value not in known_gls:
            invalid.add(value)
        else:
            valid.add(value)
    return sorted(valid), sorted(invalid)


def _route_claims(package: dict[str, Any], context: dict[str, Any] | None) -> list[dict[str, Any]]:
    raw_claims = package.get("claims") if isinstance(package.get("claims"), list) else []
    if not context or not isinstance(context.get("claim_keys"), list):
        return [claim for claim in raw_claims if isinstance(claim, dict)]
    wanted = {str(value) for value in context["claim_keys"]}
    selected = []
    for claim in raw_claims:
        if not isinstance(claim, dict):
            continue
        key = str(claim.get("normalized_key") or "")
        if key in wanted:
            selected.append(claim)
    return selected


def _action_id(package_id: str, route: dict[str, Any], context: dict[str, Any] | None) -> str:
    canonical = json.dumps(
        {
            "package_id": package_id,
            "route_id": route.get("route_id"),
            "destination": route.get("destination"),
            "context": context,
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return "GRNA-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12].upper()


def _state(destination: str, context: dict[str, Any] | None, targets: list[str], invalid: list[str]) -> tuple[str, str]:
    if invalid:
        return "blocked", "Trusted route context contains a canonical GLS identifier that is absent from The List."
    if destination == "research.dossier":
        return "research_materialized", "Bounded research work can be materialized without asserting a canonical fact."
    if context is None:
        return "blocked", "Route predates the trusted newsroom_context contract; reprocess it rather than guessing identity."
    if destination == "catalog.update" and not targets:
        return "escalate_models", "Catalog work without an existing canonical GLS identity must return to the model investigator."
    if destination in {"lineage.update", "report_card.evidence", "finder.update", "release_tracker.update"} and not targets:
        return "blocked", "This route requires at least one existing canonical GLS target."
    if destination == "report_card.evidence":
        return "evidence_materialized", "Evidence is materialized for review; scores and yes/no fields are never inferred here."
    return "ready_for_specialist", "Exact existing canonical target(s) and evidence are available for the destination specialist."


def _record(
    envelope: dict[str, Any],
    route: dict[str, Any],
    known_gls: set[str],
) -> dict[str, Any]:
    package_id = str(envelope.get("package_id") or "").strip()
    package = envelope.get("package")
    if not package_id or not isinstance(package, dict):
        raise RouteActuatorError("invalid newsroom package envelope")
    destination = str(route.get("destination") or "")
    if destination not in SUPPORTED:
        raise RouteActuatorError(f"unsupported route destination {destination!r}")
    context = _context(route)
    targets, invalid = _targets(context, known_gls)
    state, note = _state(destination, context, targets, invalid)
    claims = _route_claims(package, context)
    sources = [source for source in package.get("sources", []) if isinstance(source, dict)]
    action_id = _action_id(package_id, route, context)
    return {
        "schema_version": 1,
        "action_id": action_id,
        "package_id": package_id,
        "route_id": str(route.get("route_id") or ""),
        "destination": destination,
        "state": state,
        "owner": OWNER[destination],
        "canonical_gls_ids": targets,
        "invalid_gls_ids": invalid,
        "story": {
            "story_id": package.get("story_id"),
            "story_key": package.get("story_key"),
            "title": package.get("title"),
            "summary": package.get("summary"),
            "confidence": package.get("confidence"),
            "beat": package.get("beat"),
        },
        "route_reason": route.get("reason"),
        "route_created_at": route.get("created_at"),
        "trusted_context": context,
        "claims": claims,
        "sources": sources,
        "disposition_note": note,
        "canonical_mutation_applied": False,
    }


def _markdown(record: dict[str, Any]) -> str:
    story = record["story"]
    targets = ", ".join(record["canonical_gls_ids"]) or "none"
    claims = "\n".join(
        f"- **{claim.get('verification', 'unknown')} / {claim.get('confidence', 'unknown')}** — {claim.get('statement', '')}"
        for claim in record["claims"]
    ) or "- No route-scoped claims were supplied."
    sources = "\n".join(
        f"- [{source.get('publisher') or source.get('url')}]({source.get('url')}) — `{source.get('source_class', 'unknown')}`"
        for source in record["sources"]
        if isinstance(source.get("url"), str) and source.get("url")
    ) or "- No evidence sources were supplied."
    return f"""# {record['action_id']} — {story.get('title') or record['destination']}

**Route:** `{record['destination']}`  
**State:** `{record['state']}`  
**Owner:** `{record['owner']}`  
**Canonical GLS target(s):** {targets}  
**Canonical mutation applied:** no

> {record['disposition_note']}

## Route reason

{record.get('route_reason') or 'No route reason supplied.'}

## Current understanding

{story.get('summary') or 'No story summary supplied.'}

## Route-scoped claims

{claims}

## Evidence sources

{sources}

## Safety boundary

This action was generated only after the newsroom's second human publication gate. It is still not permission to invent a model identity, inherit lineage facts, infer a Report Card score, or convert Unknown into a positive Finder fact. Any canonical edit must satisfy the destination's existing repository validators and the normal PR merge gate.
"""


def materialize(envelope_path: Path, known_gls: set[str], root: Path = ROOT) -> list[dict[str, Any]]:
    envelope = _load(envelope_path)
    package = envelope.get("package")
    if not isinstance(package, dict):
        raise RouteActuatorError(f"{envelope_path}: missing package")
    routes = package.get("routes")
    if not isinstance(routes, list):
        raise RouteActuatorError(f"{envelope_path}: routes must be a list")

    records: list[dict[str, Any]] = []
    for route in routes:
        if not isinstance(route, dict):
            continue
        destination = str(route.get("destination") or "")
        if destination in NEWS_DESTINATIONS:
            continue
        if destination not in SUPPORTED:
            raise RouteActuatorError(f"{envelope_path}: unsupported route {destination!r}")
        record = _record(envelope, route, known_gls)
        records.append(record)

        action_dir = root / "research" / "newsroom-actions"
        action_dir.mkdir(parents=True, exist_ok=True)
        action_json = action_dir / f"{record['action_id']}.json"
        action_md = action_dir / f"{record['action_id']}.md"
        if not action_json.exists():
            action_json.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if not action_md.exists():
            action_md.write_text(_markdown(record), encoding="utf-8")

        if record["state"] == "research_materialized":
            dossier_dir = root / "research" / "newsroom-dossiers"
            dossier_dir.mkdir(parents=True, exist_ok=True)
            dossier = dossier_dir / f"{record['action_id']}.md"
            if not dossier.exists():
                dossier.write_text(_markdown(record).replace("## Safety boundary", "## Research question\n\n" + str(record.get("route_reason") or "Resolve the bounded evidence question above.") + "\n\n## Safety boundary"), encoding="utf-8")

        if record["state"] == "evidence_materialized":
            evidence_dir = root / "research" / "newsroom-evidence"
            evidence_dir.mkdir(parents=True, exist_ok=True)
            evidence_json = evidence_dir / f"{record['action_id']}.json"
            evidence_md = evidence_dir / f"{record['action_id']}.md"
            if not evidence_json.exists():
                evidence_json.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            if not evidence_md.exists():
                evidence_md.write_text(_markdown(record), encoding="utf-8")
    return records


def process_all(package_dir: Path = PACKAGES, root: Path = ROOT, list_path: Path = THE_LIST) -> tuple[int, dict[str, int]]:
    known = _known_gls(list_path)
    count = 0
    states: dict[str, int] = {}
    for path in sorted(package_dir.glob("GRNP-*.json")):
        records = materialize(path, known, root)
        count += len(records)
        for record in records:
            state = str(record["state"])
            states[state] = states.get(state, 0) + 1
    return count, states


def self_test() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package_dir = root / "research" / "newsroom-packages"
        package_dir.mkdir(parents=True)
        model_list = root / "models" / "THE_LIST.md"
        model_list.parent.mkdir(parents=True)
        model_list.write_text("| GLS-0042 | Example | Model |\n", encoding="utf-8")
        base = {
            "schema_version": 1,
            "package_id": "GRNP-TEST",
            "state": "second_gate_approved",
            "package": {
                "story_id": "story-1",
                "story_key": "example",
                "title": "Example update",
                "summary": "Example summary",
                "confidence": "high",
                "beat": "products",
                "claims": [{"claim_id": "c1", "normalized_key": "feature", "statement": "Feature changed", "verification": "verified", "confidence": "high", "claim_type": "feature"}],
                "sources": [{"source_id": "s1", "url": "https://example.com", "publisher": "Example", "source_class": "primary"}],
                "routes": [],
            },
        }
        context = {
            "schema_version": 1,
            "story_key": "example",
            "story_title": "Example update",
            "story_confidence": "high",
            "claim_keys": ["feature"],
            "claims": [],
            "entities": [{"key": "model-example", "type": "model", "name": "Example Model", "confidence": "high", "canonical_gls_id": "GLS-0042", "aliases": []}],
        }
        base["package"]["routes"] = [
            {"route_id": "r1", "destination": "report_card.evidence", "reason": "Review evidence", "payload": {"newsroom_context": context}, "created_at": "2026-09-01T00:00:00Z"},
            {"route_id": "r2", "destination": "research.dossier", "reason": "Resolve a bounded question", "payload": {"newsroom_context": context}, "created_at": "2026-09-01T00:00:00Z"},
            {"route_id": "r3", "destination": "catalog.update", "reason": "Unknown candidate", "payload": {"newsroom_context": {**context, "entities": []}}, "created_at": "2026-09-01T00:00:00Z"},
        ]
        path = package_dir / "GRNP-TEST.json"
        path.write_text(json.dumps(base), encoding="utf-8")
        total, states = process_all(package_dir, root, model_list)
        assert total == 3
        assert states == {"evidence_materialized": 1, "research_materialized": 1, "escalate_models": 1}
        assert len(list((root / "research" / "newsroom-evidence").glob("*.json"))) == 1
        assert len(list((root / "research" / "newsroom-dossiers").glob("*.md"))) == 1
        assert len(list((root / "research" / "newsroom-actions").glob("*.json"))) == 3
        total2, states2 = process_all(package_dir, root, model_list)
        assert total2 == 3 and states2 == states
    print("Newsroom route actuator self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--package", type=Path)
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.package:
        records = materialize(args.package, _known_gls(), ROOT)
        print(f"Materialized {len(records)} route action(s).")
        return 0
    if args.all:
        total, states = process_all()
        summary = ", ".join(f"{key}={value}" for key, value in sorted(states.items())) or "none"
        print(f"Materialized {total} approved non-news route action(s): {summary}.")
        return 0
    parser.error("use --all, --package, or --self-test")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
