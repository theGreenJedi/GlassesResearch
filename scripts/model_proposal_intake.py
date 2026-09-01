#!/usr/bin/env python3
"""Ingest second-gate-approved glasses-models proposals into GlassesResearch.

The intake is intentionally non-canonical. It validates and snapshots the exact
approved proposal revision so repository automation can compile a reviewable
action without giving either Worker authority to mutate the catalog directly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "research" / "model-proposals"
DEFAULT_URL = "https://glassesresearch.org/api/newsroom/model-proposals"

PROPOSAL_KINDS = {
    "catalog_admission",
    "identity_correction",
    "lineage_change",
    "evidence_update",
    "watch",
    "escalation",
    "no_change",
}
CONCLUSIONS = {
    "new_model_candidate",
    "verified_new_model",
    "variant_of_existing",
    "alias_of_existing",
    "oem_rebadge_of_existing",
    "regional_variant",
    "lineage_relationship",
    "insufficient_evidence",
    "contradictory_evidence",
    "not_a_distinct_model",
    "noise",
}
CONSEQUENCES = {
    "catalog.admit_candidate",
    "catalog.correct_identity",
    "lineage.link",
    "lineage.split_candidate",
    "lineage.merge_candidate",
    "finder.evidence",
    "report_card.evidence",
    "release_tracker.update",
    "news.update_story",
    "alerts.consider",
    "research.dossier",
    "watch.continue",
}
CONFIDENCE = {"low", "medium", "high"}
GLS_ID = re.compile(r"^GLS-\d{4}$")


class IntakeError(RuntimeError):
    pass


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IntakeError(f"{field} must be a non-empty string")
    return value.strip()


def _optional_text(value: Any) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _strings(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise IntakeError(f"{field} must be a string list")
    return sorted(set(item.strip() for item in value if item.strip()))


def _http_url(value: Any, field: str) -> str:
    url = _text(value, field)
    if not url.startswith(("https://", "http://")):
        raise IntakeError(f"{field} must be HTTP(S)")
    return url


def _object(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{field} must be an object")
    return value


def normalize_queue_item(raw: Any) -> dict[str, Any]:
    item = _object(raw, "proposal queue item")
    proposal_id = _text(item.get("proposal_id"), "proposal_id")
    investigation_id = _text(item.get("investigation_id"), "investigation_id")
    investigation_key = _text(item.get("investigation_key"), "investigation_key")
    proposal_updated_at = _text(item.get("proposal_updated_at"), "proposal_updated_at")
    reviewed_at = _text(item.get("reviewed_at"), "reviewed_at")
    proposal = _object(item.get("proposal"), "proposal")

    if proposal.get("version") != "glassesresearch-model-proposal.v1":
        raise IntakeError(f"{proposal_id}: unsupported proposal version")
    if _text(proposal.get("investigation_key"), "proposal.investigation_key") != investigation_key:
        raise IntakeError(f"{proposal_id}: investigation key mismatch")

    conclusion = _text(proposal.get("conclusion"), "proposal.conclusion")
    if conclusion not in CONCLUSIONS:
        raise IntakeError(f"{proposal_id}: invalid conclusion {conclusion!r}")
    confidence = _text(proposal.get("confidence"), "proposal.confidence")
    if confidence not in CONFIDENCE:
        raise IntakeError(f"{proposal_id}: invalid confidence {confidence!r}")
    kind = _text(proposal.get("proposal_kind"), "proposal.proposal_kind")
    if kind not in PROPOSAL_KINDS:
        raise IntakeError(f"{proposal_id}: invalid proposal kind {kind!r}")

    identity = _object(proposal.get("proposed_identity"), "proposal.proposed_identity")
    related_ids = _strings(identity.get("related_gls_ids"), "proposal.proposed_identity.related_gls_ids")
    for gls_id in related_ids:
        if not GLS_ID.fullmatch(gls_id):
            raise IntakeError(f"{proposal_id}: invalid GLS id {gls_id!r}")
    aliases = _strings(identity.get("aliases"), "proposal.proposed_identity.aliases")

    identifiers_raw = identity.get("identifiers")
    if not isinstance(identifiers_raw, list):
        raise IntakeError(f"{proposal_id}: identifiers must be a list")
    identifiers: list[dict[str, str]] = []
    for index, raw_identifier in enumerate(identifiers_raw):
        identifier = _object(raw_identifier, f"identifiers[{index}]")
        conf = _text(identifier.get("confidence"), f"identifiers[{index}].confidence")
        if conf not in CONFIDENCE:
            raise IntakeError(f"{proposal_id}: invalid identifier confidence")
        identifiers.append({
            "kind": _text(identifier.get("kind"), f"identifiers[{index}].kind"),
            "value": _text(identifier.get("value"), f"identifiers[{index}].value"),
            "confidence": conf,
        })
    identifiers.sort(key=lambda row: (row["kind"], row["value"]))

    evidence_raw = proposal.get("evidence")
    if not isinstance(evidence_raw, list):
        raise IntakeError(f"{proposal_id}: evidence must be a list")
    evidence: list[dict[str, str]] = []
    evidence_urls: set[str] = set()
    for index, raw_evidence in enumerate(evidence_raw):
        source = _object(raw_evidence, f"evidence[{index}]")
        url = _http_url(source.get("url"), f"evidence[{index}].url")
        conf = _text(source.get("confidence"), f"evidence[{index}].confidence")
        if conf not in CONFIDENCE:
            raise IntakeError(f"{proposal_id}: invalid evidence confidence")
        evidence_urls.add(url)
        evidence.append({
            "url": url,
            "source_class": _text(source.get("source_class"), f"evidence[{index}].source_class"),
            "supports": _text(source.get("supports"), f"evidence[{index}].supports"),
            "confidence": conf,
        })
    evidence.sort(key=lambda row: row["url"])

    claims_raw = proposal.get("verified_claims")
    if not isinstance(claims_raw, list):
        raise IntakeError(f"{proposal_id}: verified_claims must be a list")
    claims: list[dict[str, Any]] = []
    for index, raw_claim in enumerate(claims_raw):
        claim = _object(raw_claim, f"verified_claims[{index}]")
        urls = [_http_url(url, f"verified_claims[{index}].source_urls") for url in _strings(claim.get("source_urls"), f"verified_claims[{index}].source_urls")]
        if any(url not in evidence_urls for url in urls):
            raise IntakeError(f"{proposal_id}: verified claim cites evidence not carried by proposal")
        conf = _text(claim.get("confidence"), f"verified_claims[{index}].confidence")
        if conf not in CONFIDENCE:
            raise IntakeError(f"{proposal_id}: invalid claim confidence")
        claims.append({
            "key": _text(claim.get("key"), f"verified_claims[{index}].key"),
            "statement": _text(claim.get("statement"), f"verified_claims[{index}].statement"),
            "confidence": conf,
            "source_urls": urls,
        })
    claims.sort(key=lambda row: row["key"])

    consequences_raw = proposal.get("consequences")
    if not isinstance(consequences_raw, list):
        raise IntakeError(f"{proposal_id}: consequences must be a list")
    consequences: list[dict[str, Any]] = []
    for index, raw_consequence in enumerate(consequences_raw):
        consequence = _object(raw_consequence, f"consequences[{index}]")
        destination = _text(consequence.get("destination"), f"consequences[{index}].destination")
        if destination not in CONSEQUENCES:
            raise IntakeError(f"{proposal_id}: unsupported consequence {destination!r}")
        payload = consequence.get("payload", {})
        if not isinstance(payload, dict):
            raise IntakeError(f"{proposal_id}: consequence payload must be an object")
        consequences.append({
            "destination": destination,
            "reason": _text(consequence.get("reason"), f"consequences[{index}].reason"),
            "payload": payload,
        })
    consequences.sort(key=lambda row: row["destination"])

    edges_raw = identity.get("identity_edges")
    if not isinstance(edges_raw, list):
        raise IntakeError(f"{proposal_id}: identity_edges must be a list")
    edges: list[dict[str, Any]] = []
    for index, raw_edge in enumerate(edges_raw):
        edge = _object(raw_edge, f"identity_edges[{index}]")
        urls = [_http_url(url, f"identity_edges[{index}].evidence_urls") for url in _strings(edge.get("evidence_urls"), f"identity_edges[{index}].evidence_urls")]
        if any(url not in evidence_urls for url in urls):
            raise IntakeError(f"{proposal_id}: identity edge cites evidence not carried by proposal")
        conf = _text(edge.get("confidence"), f"identity_edges[{index}].confidence")
        if conf not in CONFIDENCE:
            raise IntakeError(f"{proposal_id}: invalid identity-edge confidence")
        edges.append({
            "left_key": _text(edge.get("left_key"), f"identity_edges[{index}].left_key"),
            "relationship": _text(edge.get("relationship"), f"identity_edges[{index}].relationship"),
            "right_key": _text(edge.get("right_key"), f"identity_edges[{index}].right_key"),
            "confidence": conf,
            "status": _text(edge.get("status"), f"identity_edges[{index}].status"),
            "evidence_urls": urls,
        })
    edges.sort(key=lambda row: (row["left_key"], row["relationship"], row["right_key"]))

    acquisition_raw = proposal.get("acquisition")
    acquisition: dict[str, Any] | None = None
    if acquisition_raw is not None:
        acquisition_obj = _object(acquisition_raw, "proposal.acquisition")
        source_urls = [_http_url(url, "proposal.acquisition.source_urls") for url in _strings(acquisition_obj.get("source_urls"), "proposal.acquisition.source_urls")]
        if any(url not in evidence_urls for url in source_urls):
            raise IntakeError(f"{proposal_id}: acquisition cites evidence not carried by proposal")
        threshold = acquisition_obj.get("threshold_met")
        if not isinstance(threshold, bool):
            raise IntakeError(f"{proposal_id}: acquisition.threshold_met must be boolean")
        acquisition = {
            "state": _text(acquisition_obj.get("state"), "proposal.acquisition.state"),
            "threshold_met": threshold,
            "source_urls": source_urls,
            "note": _text(acquisition_obj.get("note"), "proposal.acquisition.note"),
        }

    if kind == "catalog_admission" and not (
        conclusion == "verified_new_model" and acquisition and acquisition["threshold_met"] is True
    ):
        raise IntakeError(f"{proposal_id}: catalog admission lacks verified identity/acquisition threshold")
    if kind != "no_change" and not evidence:
        raise IntakeError(f"{proposal_id}: material proposal requires evidence")

    requires_review = proposal.get("requires_human_review")
    if not isinstance(requires_review, bool):
        raise IntakeError(f"{proposal_id}: requires_human_review must be boolean")

    normalized_proposal = {
        "version": "glassesresearch-model-proposal.v1",
        "investigation_key": investigation_key,
        "conclusion": conclusion,
        "confidence": confidence,
        "proposal_kind": kind,
        "proposed_identity": {
            "canonical_name": _optional_text(identity.get("canonical_name")),
            "aliases": aliases,
            "related_gls_ids": related_ids,
            "identifiers": identifiers,
            "identity_edges": edges,
        },
        "acquisition": acquisition,
        "evidence": evidence,
        "verified_claims": claims,
        "consequences": consequences,
        "unresolved_questions": _strings(proposal.get("unresolved_questions"), "proposal.unresolved_questions"),
        "watch_targets": _strings(proposal.get("watch_targets"), "proposal.watch_targets"),
        "requires_human_review": requires_review,
        "created_at": _text(proposal.get("created_at"), "proposal.created_at"),
    }
    return {
        "proposal_id": proposal_id,
        "investigation_id": investigation_id,
        "investigation_key": investigation_key,
        "proposal_updated_at": proposal_updated_at,
        "reviewed_at": reviewed_at,
        "proposal": normalized_proposal,
    }


def package_id(item: dict[str, Any]) -> str:
    canonical = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "GRMP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12].upper()


def _markdown(pid: str, item: dict[str, Any], source_url: str) -> str:
    p = item["proposal"]
    identity = p["proposed_identity"]["canonical_name"] or "unresolved identity"
    related = ", ".join(p["proposed_identity"]["related_gls_ids"]) or "none"
    evidence = "\n".join(f"- [{row['source_class']}]({row['url']}) — {row['supports']} ({row['confidence']})" for row in p["evidence"]) or "- none"
    claims = "\n".join(f"- **{row['key']}** — {row['statement']} ({row['confidence']})" for row in p["verified_claims"]) or "- none"
    consequences = "\n".join(f"- `{row['destination']}` — {row['reason']}" for row in p["consequences"]) or "- none"
    unresolved = "\n".join(f"- {row}" for row in p["unresolved_questions"]) or "- none"
    return f"""# {pid} — {identity}

**State:** exact current Models proposal revision approved at the human proposal gate; not canonical  
**Proposal kind:** `{p['proposal_kind']}`  
**Conclusion:** `{p['conclusion']}`  
**Confidence:** `{p['confidence']}`  
**Related GLS IDs:** {related}  
**Proposal ID:** `{item['proposal_id']}`  
**Investigation:** `{item['investigation_key']}`  
**Queue source:** {source_url}

> Human approval authorizes repository intake of this proposal. It does not allocate a GLS ID, mutate canonical identity, change a score, or publish a fact by itself. Those consequences must remain visible in the repository draft/PR.

## Verified claims

{claims}

## Evidence

{evidence}

## Proposed consequences

{consequences}

## Unresolved questions

{unresolved}
"""


def ingest(payload: dict[str, Any], output_dir: Path, source_url: str) -> list[str]:
    if payload.get("schema_version") != 1:
        raise IntakeError("model proposal queue must use schema_version 1")
    raw = payload.get("proposals")
    if not isinstance(raw, list):
        raise IntakeError("model proposal queue proposals must be a list")
    output_dir.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    for raw_item in raw:
        item = normalize_queue_item(raw_item)
        pid = package_id(item)
        json_path = output_dir / f"{pid}.json"
        md_path = output_dir / f"{pid}.md"
        if json_path.exists() and md_path.exists():
            continue
        envelope = {
            "schema_version": 1,
            "package_id": pid,
            "state": "model_proposal_second_gate_approved",
            "source_queue": source_url,
            "ingested_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "approved_proposal": item,
        }
        json_path.write_text(json.dumps(envelope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        md_path.write_text(_markdown(pid, item, source_url), encoding="utf-8")
        created.append(pid)
    return created


def self_test() -> None:
    evidence_url = "https://example.com/identity"
    fixture = {
        "schema_version": 1,
        "proposals": [{
            "proposal_id": "proposal-1",
            "investigation_id": "inv-1",
            "investigation_key": "news:route-1",
            "proposal_updated_at": "2026-09-01T12:00:00Z",
            "reviewed_at": "2026-09-01T12:01:00Z",
            "proposal": {
                "version": "glassesresearch-model-proposal.v1",
                "investigation_key": "news:route-1",
                "conclusion": "alias_of_existing",
                "confidence": "high",
                "proposal_kind": "identity_correction",
                "proposed_identity": {
                    "canonical_name": "Example Glasses",
                    "aliases": ["Example AI Glasses"],
                    "related_gls_ids": ["GLS-0042"],
                    "identifiers": [],
                    "identity_edges": [],
                },
                "acquisition": None,
                "evidence": [{"url": evidence_url, "source_class": "primary", "supports": "same product identity", "confidence": "high"}],
                "verified_claims": [{"key": "identity", "statement": "The names refer to the same model.", "confidence": "high", "source_urls": [evidence_url]}],
                "consequences": [{"destination": "catalog.correct_identity", "reason": "Record verified alias", "payload": {}}],
                "unresolved_questions": [],
                "watch_targets": [],
                "requires_human_review": True,
                "created_at": "2026-09-01T12:00:00Z",
            },
        }],
    }
    item = normalize_queue_item(fixture["proposals"][0])
    assert item["proposal"]["proposed_identity"]["related_gls_ids"] == ["GLS-0042"]
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory)
        first = ingest(fixture, output, "https://example.com/model-proposals")
        second = ingest(fixture, output, "https://example.com/model-proposals")
        assert len(first) == 1 and second == []
        assert (output / f"{first[0]}.json").exists()
    print("Model proposal intake self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-url", default=DEFAULT_URL)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise IntakeError("model proposal queue must be an object")
        created = ingest(payload, args.output, args.source_url)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"Ingested {len(created)} approved model proposal(s)" if created else "No new approved model proposals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
