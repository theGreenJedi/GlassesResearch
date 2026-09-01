#!/usr/bin/env python3
"""Compile approved model intelligence proposals into auditable draft actions.

No action produced here mutates canonical model records. The compiler turns the
second-gate-approved proposal into a deterministic repository consequence, proves
any referenced GLS IDs already exist, and blocks unresolved identity rather than
guessing. Canonical edits remain visible work for the draft PR/repository gate.
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
DEFAULT_INPUT = ROOT / "research" / "model-proposals"
DEFAULT_OUTPUT = ROOT / "research" / "model-actions"
THE_LIST = ROOT / "models" / "THE_LIST.md"
GLS_PATTERN = re.compile(r"GLS-\d{4}")


class ActuatorError(RuntimeError):
    pass


def known_gls_ids(path: Path = THE_LIST) -> set[str]:
    if not path.exists():
        raise ActuatorError(f"canonical model list missing: {path}")
    return set(GLS_PATTERN.findall(path.read_text(encoding="utf-8")))


def load_package(path: Path) -> dict[str, Any]:
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ActuatorError(f"cannot read {path.name}: {exc}") from exc
    if not isinstance(envelope, dict) or envelope.get("schema_version") != 1:
        raise ActuatorError(f"{path.name}: invalid model-proposal envelope")
    if envelope.get("state") != "model_proposal_second_gate_approved":
        raise ActuatorError(f"{path.name}: proposal is not second-gate approved")
    approved = envelope.get("approved_proposal")
    if not isinstance(approved, dict) or not isinstance(approved.get("proposal"), dict):
        raise ActuatorError(f"{path.name}: missing approved proposal")
    return envelope


def _action_id(package_id: str, proposal: dict[str, Any]) -> str:
    canonical = json.dumps(
        {"package_id": package_id, "proposal": proposal},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return "GRMA-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12].upper()


def _related_ids(proposal: dict[str, Any]) -> list[str]:
    identity = proposal.get("proposed_identity")
    if not isinstance(identity, dict):
        return []
    raw = identity.get("related_gls_ids")
    if not isinstance(raw, list):
        return []
    return sorted(set(item for item in raw if isinstance(item, str) and GLS_PATTERN.fullmatch(item)))


def compile_action(envelope: dict[str, Any], canonical_ids: set[str]) -> dict[str, Any]:
    package_id = str(envelope.get("package_id") or "")
    approved = envelope["approved_proposal"]
    proposal = approved["proposal"]
    kind = proposal.get("proposal_kind")
    conclusion = proposal.get("conclusion")
    identity = proposal.get("proposed_identity") if isinstance(proposal.get("proposed_identity"), dict) else {}
    related = _related_ids(proposal)
    unknown = [gls_id for gls_id in related if gls_id not in canonical_ids]
    if unknown:
        raise ActuatorError(f"{package_id}: proposal references unknown canonical GLS IDs: {', '.join(unknown)}")

    disposition = "blocked_unsupported"
    blocked_reason: str | None = None
    requires_gls_allocation = False
    target_gls_ids = related

    if kind == "no_change":
        disposition = "record_only_no_change"
    elif kind == "watch":
        disposition = "watch_packet"
    elif kind == "evidence_update":
        if related:
            disposition = "evidence_update_candidate"
        else:
            disposition = "blocked_unresolved_identity"
            blocked_reason = "Evidence update has no exact existing GLS target. Resolve identity before canonical application."
    elif kind == "identity_correction":
        if related:
            disposition = "identity_correction_candidate"
        else:
            disposition = "blocked_unresolved_identity"
            blocked_reason = "Identity correction has no exact existing GLS target. Canonical identity must not be guessed."
    elif kind == "lineage_change":
        edges = identity.get("identity_edges") if isinstance(identity, dict) else None
        if related and isinstance(edges, list) and edges:
            disposition = "lineage_change_candidate"
        else:
            disposition = "blocked_unresolved_identity"
            blocked_reason = "Lineage change requires existing GLS context and an evidence-backed identity edge."
    elif kind == "catalog_admission":
        acquisition = proposal.get("acquisition")
        if conclusion == "verified_new_model" and isinstance(acquisition, dict) and acquisition.get("threshold_met") is True:
            disposition = "catalog_admission_candidate"
            requires_gls_allocation = True
            target_gls_ids = []
        else:
            disposition = "blocked_admission_threshold"
            blocked_reason = "Catalog admission cannot proceed without verified new-model identity and acquisition threshold."
    elif kind == "escalation":
        disposition = "manual_escalation"
    else:
        blocked_reason = f"Unsupported proposal kind: {kind!r}"

    return {
        "schema_version": 1,
        "action_id": _action_id(package_id, proposal),
        "source_package_id": package_id,
        "source_proposal_id": approved.get("proposal_id"),
        "investigation_key": approved.get("investigation_key"),
        "proposal_revision": approved.get("proposal_updated_at"),
        "proposal_kind": kind,
        "conclusion": conclusion,
        "confidence": proposal.get("confidence"),
        "canonical_name": identity.get("canonical_name") if isinstance(identity, dict) else None,
        "target_gls_ids": target_gls_ids,
        "requires_gls_allocation": requires_gls_allocation,
        "disposition": disposition,
        "blocked_reason": blocked_reason,
        "canonical_mutation_applied": False,
        "repository_gate_required": True,
        "verified_claims": proposal.get("verified_claims", []),
        "evidence": proposal.get("evidence", []),
        "identity_edges": identity.get("identity_edges", []) if isinstance(identity, dict) else [],
        "acquisition": proposal.get("acquisition"),
        "consequences": proposal.get("consequences", []),
        "unresolved_questions": proposal.get("unresolved_questions", []),
        "watch_targets": proposal.get("watch_targets", []),
    }


def render_markdown(action: dict[str, Any]) -> str:
    targets = ", ".join(action["target_gls_ids"]) or "none"
    blocked = f"\n**Blocked:** {action['blocked_reason']}  \n" if action.get("blocked_reason") else ""
    allocation = "yes — allocate only through canonical repository review" if action["requires_gls_allocation"] else "no"
    claims = "\n".join(
        f"- **{row.get('key', 'claim')}** — {row.get('statement', '')} ({row.get('confidence', 'unknown')})"
        for row in action["verified_claims"]
        if isinstance(row, dict)
    ) or "- none"
    evidence = "\n".join(
        f"- [{row.get('source_class', 'source')}]({row.get('url', '')}) — {row.get('supports', '')}"
        for row in action["evidence"]
        if isinstance(row, dict)
    ) or "- none"
    consequences = "\n".join(
        f"- `{row.get('destination', 'unknown')}` — {row.get('reason', '')}"
        for row in action["consequences"]
        if isinstance(row, dict)
    ) or "- none"
    questions = "\n".join(f"- {item}" for item in action["unresolved_questions"]) or "- none"
    return f"""# {action['action_id']} — model intelligence action

**Disposition:** `{action['disposition']}`  
**Proposal kind:** `{action['proposal_kind']}`  
**Conclusion:** `{action['conclusion']}`  
**Confidence:** `{action['confidence']}`  
**Canonical name:** {action['canonical_name'] or 'unresolved'}  
**Existing GLS targets:** {targets}  
**Requires GLS allocation:** {allocation}  
**Canonical mutation applied:** **no**  
**Repository gate required:** **yes**  
{blocked}
> This is the deterministic consequence of a human-approved Models proposal. It is deliberately a draft action, not an invisible catalog mutation. Any canonical edit must be visible in this PR and satisfy the normal GlassesResearch validators.

## Verified claims

{claims}

## Evidence

{evidence}

## Proposed downstream consequences

{consequences}

## Unresolved questions

{questions}

## Repository application rule

- `catalog_admission_candidate`: verify acquisition/identity again, allocate a new GLS ID only through the canonical model workflow, then update all affected indexes/lineage/release/news surfaces.
- `identity_correction_candidate`: touch only the exact existing GLS targets above; preserve old aliases/history and evidence.
- `lineage_change_candidate`: apply only evidence-backed edges with exact targets.
- `evidence_update_candidate`: attach evidence to exact targets; never infer a score change from this packet alone.
- blocked/escalation/watch actions remain non-canonical until their stated uncertainty is resolved.
"""


def compile_path(path: Path, output_dir: Path, canonical_ids: set[str]) -> str | None:
    envelope = load_package(path)
    action = compile_action(envelope, canonical_ids)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{action['action_id']}.json"
    md_path = output_dir / f"{action['action_id']}.md"
    if json_path.exists() and md_path.exists():
        return None
    json_path.write_text(json.dumps(action, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(action), encoding="utf-8")
    return action["action_id"]


def compile_all(input_dir: Path, output_dir: Path, canonical_ids: set[str] | None = None) -> list[str]:
    ids = canonical_ids if canonical_ids is not None else known_gls_ids()
    if not input_dir.exists():
        return []
    created: list[str] = []
    for path in sorted(input_dir.glob("GRMP-*.json")):
        result = compile_path(path, output_dir, ids)
        if result:
            created.append(result)
    return created


def self_test() -> None:
    base = {
        "schema_version": 1,
        "package_id": "GRMP-TEST",
        "state": "model_proposal_second_gate_approved",
        "approved_proposal": {
            "proposal_id": "proposal-1",
            "investigation_key": "news:route-1",
            "proposal_updated_at": "2026-09-01T12:00:00Z",
            "proposal": {
                "proposal_kind": "identity_correction",
                "conclusion": "alias_of_existing",
                "confidence": "high",
                "proposed_identity": {
                    "canonical_name": "Existing Glasses",
                    "related_gls_ids": ["GLS-0042"],
                    "identity_edges": [],
                },
                "verified_claims": [],
                "evidence": [],
                "acquisition": None,
                "consequences": [],
                "unresolved_questions": [],
                "watch_targets": [],
            },
        },
    }
    action = compile_action(base, {"GLS-0042"})
    assert action["disposition"] == "identity_correction_candidate"
    assert action["canonical_mutation_applied"] is False

    unresolved = json.loads(json.dumps(base))
    unresolved["approved_proposal"]["proposal"]["proposed_identity"]["related_gls_ids"] = []
    assert compile_action(unresolved, set())["disposition"] == "blocked_unresolved_identity"

    admission = json.loads(json.dumps(base))
    admission["approved_proposal"]["proposal"].update({
        "proposal_kind": "catalog_admission",
        "conclusion": "verified_new_model",
        "acquisition": {"threshold_met": True},
    })
    admission["approved_proposal"]["proposal"]["proposed_identity"]["related_gls_ids"] = []
    admitted = compile_action(admission, set())
    assert admitted["disposition"] == "catalog_admission_candidate"
    assert admitted["requires_gls_allocation"] is True

    try:
        compile_action(base, set())
    except ActuatorError:
        pass
    else:
        raise AssertionError("unknown GLS references must fail closed")

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        input_dir = root / "in"
        output_dir = root / "out"
        input_dir.mkdir()
        (input_dir / "GRMP-TEST.json").write_text(json.dumps(base), encoding="utf-8")
        first = compile_all(input_dir, output_dir, {"GLS-0042"})
        second = compile_all(input_dir, output_dir, {"GLS-0042"})
        assert len(first) == 1 and second == []
    print("Model proposal actuator self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.all:
        parser.error("use --all or --self-test")
    try:
        created = compile_all(args.input, args.output)
    except ActuatorError as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"Materialized {len(created)} model action(s)" if created else "No new model actions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
