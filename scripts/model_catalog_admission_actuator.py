#!/usr/bin/env python3
"""Automatically admit only evidence-clean, unambiguous model proposals.

This actuator consumes repository-ingested GlassesResearch model-proposal envelopes.
It is intentionally much narrower than the general proposal/action pipeline. A
proposal is eligible only when the upstream investigator already resolved a
high-confidence distinct identity, the purchaser-history threshold is met, the
proposal explicitly does not require human review, no identity edge/target/question
remains, and a complete catalog row is tied to the same high-confidence acquisition
evidence.

Anything ambiguous fails closed and remains ordinary review work.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "research" / "model-proposals"
MODELS = ROOT / "models"
THE_LIST = MODELS / "THE_LIST.md"
AUTO_PROFILES = MODELS / "PROFILES_AUTO_ADMISSIONS.md"
GLS_RE = re.compile(r"\bGLS-(\d{4})\b")
EXACT_ERA_RE = re.compile(r"^20\d{2}$")
SAFE_ACQUISITION_SOURCE_CLASSES = {"primary", "retailer"}
QUALIFYING_ACQUISITION_STATES = {
    "paid_purchase",
    "paid_preorder",
    "paid_crowdfunding",
    "enterprise_procurement",
    "developer_procurement",
}
REQUIRED_ROW_FIELDS = (
    "maker",
    "model",
    "era",
    "state",
    "type",
    "access",
    "source_url",
)


class AdmissionError(RuntimeError):
    pass


def _clean_cell(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise AdmissionError(f"catalog row {label} must be a string")
    text = " ".join(value.replace("|", "/").split())
    if not text or len(text) > 240:
        raise AdmissionError(f"catalog row {label} is empty or too long")
    return text


def _normal(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _existing_numbers() -> set[int]:
    numbers: set[int] = set()
    paths = [THE_LIST, MODELS / "CATALOG_CORRECTIONS.md", *MODELS.glob("THE_LIST_RECONCILIATION_*.md")]
    for path in paths:
        if path.exists():
            numbers.update(int(value) for value in GLS_RE.findall(path.read_text(encoding="utf-8")))
    return numbers


def _existing_catalog() -> tuple[set[tuple[str, str]], set[str]]:
    identities: set[tuple[str, str]] = set()
    source_urls: set[str] = set()
    if not THE_LIST.exists():
        raise AdmissionError(f"canonical model list missing: {THE_LIST}")
    for line in THE_LIST.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| GLS-\d{4} \|", line):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 8:
            continue
        identities.add((_normal(parts[1]), _normal(parts[2])))
        source_urls.update(re.findall(r"https?://[^)\s|]+", parts[7]))
    return identities, source_urls


def _next_gls(used: set[int]) -> str:
    number = max(used or {0}) + 1
    while number in used:
        number += 1
    used.add(number)
    return f"GLS-{number:04d}"


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdmissionError(f"cannot read {path.name}: {exc}") from exc
    if not isinstance(value, dict) or value.get("schema_version") != 1:
        raise AdmissionError(f"{path.name}: invalid model-proposal envelope")
    if value.get("state") != "model_proposal_second_gate_approved":
        raise AdmissionError(f"{path.name}: proposal is not repository-authorized")
    approved = value.get("approved_proposal")
    if not isinstance(approved, dict) or not isinstance(approved.get("proposal"), dict):
        raise AdmissionError(f"{path.name}: approved proposal missing")
    return value


def _catalog_row(proposal: dict[str, Any]) -> dict[str, str] | None:
    for consequence in proposal.get("consequences", []):
        if not isinstance(consequence, dict) or consequence.get("destination") != "catalog.admit_candidate":
            continue
        payload = consequence.get("payload")
        if not isinstance(payload, dict):
            continue
        row = payload.get("catalog_row")
        if not isinstance(row, dict):
            continue
        return {field: _clean_cell(row.get(field), field) for field in REQUIRED_ROW_FIELDS}
    return None


def _eligible(
    envelope: dict[str, Any],
    existing_identities: set[tuple[str, str]],
    existing_sources: set[str],
) -> tuple[bool, str, dict[str, str] | None]:
    approved = envelope["approved_proposal"]
    proposal = approved["proposal"]

    if proposal.get("proposal_kind") != "catalog_admission" or proposal.get("conclusion") != "verified_new_model":
        return False, "not a verified catalog admission", None
    if proposal.get("confidence") != "high":
        return False, "automatic admission requires high confidence", None
    if proposal.get("requires_human_review") is not False:
        return False, "upstream proposal requires human review", None

    identity = proposal.get("proposed_identity")
    if not isinstance(identity, dict):
        return False, "proposed identity missing", None
    if identity.get("related_gls_ids"):
        return False, "proposal targets an existing GLS identity", None
    if identity.get("identity_edges"):
        return False, "identity relationship requires judgment", None
    if proposal.get("unresolved_questions"):
        return False, "unresolved questions remain", None

    acquisition = proposal.get("acquisition")
    if not isinstance(acquisition, dict) or acquisition.get("threshold_met") is not True:
        return False, "purchaser-history threshold not met", None
    if acquisition.get("state") not in QUALIFYING_ACQUISITION_STATES:
        return False, "acquisition state is not eligible for the automatic lane", None

    evidence = proposal.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return False, "no evidence", None
    high_urls = {
        item.get("url")
        for item in evidence
        if isinstance(item, dict)
        and item.get("confidence") == "high"
        and item.get("source_class") in SAFE_ACQUISITION_SOURCE_CLASSES
        and isinstance(item.get("url"), str)
    }
    acquisition_urls = {
        url for url in acquisition.get("source_urls", []) if isinstance(url, str)
    }
    if not high_urls.intersection(acquisition_urls):
        return False, "acquisition lacks high-confidence primary/retailer evidence", None

    try:
        row = _catalog_row(proposal)
    except AdmissionError as exc:
        return False, str(exc), None
    if row is None:
        return False, "structured catalog_row payload missing", None
    if not EXACT_ERA_RE.fullmatch(row["era"]):
        return False, "automatic admission requires an exact four-digit acquisition era", None
    if row["source_url"] not in high_urls or row["source_url"] not in acquisition_urls:
        return False, "catalog row source is not the verified acquisition source", None

    if (_normal(row["maker"]), _normal(row["model"])) in existing_identities:
        return False, "exact maker/model already exists in current canonical catalog", None
    if row["source_url"] in existing_sources:
        return False, "acquisition source is already attached to a canonical row", None

    canonical_name = identity.get("canonical_name")
    if not isinstance(canonical_name, str) or not canonical_name.strip():
        return False, "canonical identity name missing", None
    if _normal(row["model"]) not in _normal(canonical_name) and _normal(canonical_name) not in _normal(row["model"]):
        return False, "catalog-row model and canonical identity disagree", None

    state = row["state"].casefold()
    if "announced" in state or "reservation" in state:
        return False, "catalog row still describes a non-acquisition state", None

    return True, "eligible", row


def _proposal_date(envelope: dict[str, Any]) -> str:
    revision = envelope.get("approved_proposal", {}).get("proposal_updated_at")
    if isinstance(revision, str) and re.match(r"^20\d{2}-\d{2}-\d{2}", revision):
        return revision[:10]
    raise AdmissionError("eligible admission requires a dated proposal revision")


def _packet(gls_id: str, envelope: dict[str, Any], row: dict[str, str]) -> str:
    approved = envelope["approved_proposal"]
    proposal = approved["proposal"]
    evidence = proposal.get("evidence", [])
    evidence_lines = "\n".join(
        f"- {item.get('url')} — {item.get('supports', '')} ({item.get('source_class')}, {item.get('confidence')})"
        for item in evidence if isinstance(item, dict)
    )
    claims = "\n".join(
        f"- **{item.get('key', 'claim')}** — {item.get('statement', '')} ({item.get('confidence', 'unknown')})"
        for item in proposal.get("verified_claims", []) if isinstance(item, dict)
    ) or "- none"
    date = _proposal_date(envelope)
    return f"""# Automatic canonical reconciliation — {row['maker']} {row['model']}

Date: {date}  
Source package: `{envelope.get('package_id')}`  
Source proposal: `{approved.get('proposal_id')}`  
Investigation: `{approved.get('investigation_key')}`

This packet was generated by the bounded automatic canonical-admission lane. The upstream Models finding established a high-confidence distinct identity, a qualifying purchaser-history acquisition path, no existing GLS target, no identity relationship, no unresolved question, and a complete catalog row tied to the same high-confidence acquisition evidence.

## Admit to canonical purchaser-history ledger

| ID | Maker | Model | Era | State | Type | Access | Evidence |
|---|---|---|---:|---|---|---|---|
| {gls_id} | {row['maker']} | {row['model']} | {row['era']} | {row['state']} | {row['type']} | {row['access']} | {row['source_url']} |

## Admission boundary

Admission establishes stable identity and documented acquisition history only. It does **not** infer Report Card scores, owner control, openness, privacy behavior, cloud independence, durability, support quality, or hands-on performance.

## Verified claims carried by the proposal

{claims}

## Evidence carried by the proposal

{evidence_lines}

## Automatic-lane proof

- conclusion: `verified_new_model`
- confidence: `high`
- upstream human-review flag: `false`
- acquisition state: `{proposal.get('acquisition', {}).get('state')}`
- purchaser-history threshold: met
- existing GLS targets: none
- identity edges: none
- unresolved questions: none
- catalog-row era: exact
- catalog-row source: same high-confidence acquisition evidence
- current exact maker/model duplicate: none
- current exact source duplicate: none

Canonical propagation remains subject to the normal catalog consistency, strict profile coverage, public device-database, site-build, link, and CI validators. If `main` moves before merge, the automation abandons the candidate and retries from fresh canonical state rather than racing stable-ID allocation.
"""


def _profile(gls_id: str, envelope: dict[str, Any], row: dict[str, str], packet_name: str) -> str:
    proposal = envelope["approved_proposal"]["proposal"]
    claims = [
        item.get("statement") for item in proposal.get("verified_claims", [])
        if isinstance(item, dict) and isinstance(item.get("statement"), str)
    ]
    summary = " ".join(claims[:3]) or "No additional product claims are promoted by this admission."
    return f"""
## {gls_id} — {row['maker']} {row['model']}

**Automatic canonical admission profile.** {row['maker']} {row['model']} crossed the purchaser-history threshold through a high-confidence acquisition route and passed the bounded no-ambiguity admission gate. This initial profile intentionally carries only admission-safe identity/acquisition evidence; Report Card scoring and broader operational claims remain unscored until separately established.

{summary}

Sources: [canonical reconciliation]({packet_name}) · [acquisition source]({row['source_url']})
"""


def compile_all(input_dir: Path = DEFAULT_INPUT) -> list[str]:
    used = _existing_numbers()
    existing_identities, existing_sources = _existing_catalog()
    created: list[str] = []
    profile_text = (
        AUTO_PROFILES.read_text(encoding="utf-8")
        if AUTO_PROFILES.exists()
        else "# Automatic Canonical Admission Profiles\n\nThese conservative profiles are generated only for evidence-clean admissions that pass the bounded automatic lane.\n"
    )

    if not input_dir.exists():
        return []

    for path in sorted(input_dir.glob("GRMP-*.json")):
        envelope = _load(path)
        eligible, _, row = _eligible(envelope, existing_identities, existing_sources)
        if not eligible or row is None:
            continue
        package_id = str(envelope.get("package_id") or path.stem)
        marker = f"<!-- source-package: {package_id} -->"
        if marker in profile_text:
            continue

        gls_id = _next_gls(used)
        date = _proposal_date(envelope)
        safe_package = re.sub(r"[^A-Za-z0-9_-]+", "-", package_id).strip("-")[:48]
        packet_name = f"THE_LIST_RECONCILIATION_{date}_AUTO_{safe_package}.md"
        packet_path = MODELS / packet_name
        if packet_path.exists():
            continue

        packet_path.write_text(_packet(gls_id, envelope, row), encoding="utf-8")
        profile_text += _profile(gls_id, envelope, row, packet_name) + f"\n{marker}\n"
        existing_identities.add((_normal(row["maker"]), _normal(row["model"])))
        existing_sources.add(row["source_url"])
        created.append(gls_id)

    if created:
        AUTO_PROFILES.write_text(profile_text, encoding="utf-8")
    return created


def self_test() -> None:
    proposal = {
        "version": "glassesresearch-model-proposal.v1",
        "investigation_key": "news:route-1",
        "proposal_kind": "catalog_admission",
        "conclusion": "verified_new_model",
        "confidence": "high",
        "requires_human_review": False,
        "proposed_identity": {
            "canonical_name": "Maker Model",
            "aliases": [],
            "related_gls_ids": [],
            "identifiers": [],
            "identity_edges": [],
        },
        "acquisition": {
            "state": "paid_purchase",
            "threshold_met": True,
            "source_urls": ["https://maker.example/model"],
            "note": "Manufacturer accepts an order for the device.",
        },
        "evidence": [{
            "url": "https://maker.example/model",
            "source_class": "primary",
            "supports": "named product and device order route",
            "confidence": "high",
        }],
        "verified_claims": [{
            "key": "identity",
            "statement": "Maker Model is a distinct purchasable product.",
            "confidence": "high",
            "source_urls": ["https://maker.example/model"],
        }],
        "consequences": [{
            "destination": "catalog.admit_candidate",
            "reason": "verified distinct purchasable model",
            "payload": {
                "catalog_row": {
                    "maker": "Maker",
                    "model": "Model",
                    "era": "2026",
                    "state": "current",
                    "type": "camera/audio smart glasses",
                    "access": "retail",
                    "source_url": "https://maker.example/model",
                }
            },
        }],
        "unresolved_questions": [],
        "watch_targets": [],
        "created_at": "2026-09-10T12:00:00Z",
    }
    envelope = {
        "schema_version": 1,
        "package_id": "GRMP-TEST",
        "state": "model_proposal_second_gate_approved",
        "approved_proposal": {
            "proposal_id": "proposal-1",
            "investigation_id": "investigation-1",
            "investigation_key": "news:route-1",
            "proposal_updated_at": "2026-09-10T12:00:00Z",
            "reviewed_at": "2026-09-10T12:00:00Z",
            "proposal": proposal,
        },
    }
    ok, _, row = _eligible(envelope, set(), set())
    assert ok and row and row["maker"] == "Maker"

    blocked = json.loads(json.dumps(envelope))
    blocked["approved_proposal"]["proposal"]["unresolved_questions"] = ["Is this a rebadge?"]
    assert _eligible(blocked, set(), set())[0] is False

    blocked = json.loads(json.dumps(envelope))
    blocked["approved_proposal"]["proposal"]["requires_human_review"] = True
    assert _eligible(blocked, set(), set())[0] is False

    blocked = json.loads(json.dumps(envelope))
    blocked["approved_proposal"]["proposal"]["consequences"][0]["payload"]["catalog_row"]["era"] = "≤2026"
    assert _eligible(blocked, set(), set())[0] is False

    assert _eligible(envelope, {("maker", "model")}, set())[0] is False
    assert _eligible(envelope, set(), {"https://maker.example/model"})[0] is False
    print("Bounded automatic canonical-admission actuator self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.all:
        parser.error("use --all or --self-test")
    try:
        created = compile_all(args.input)
    except AdmissionError as exc:
        print(f"ERROR: {exc}")
        return 1
    if created:
        print(f"Created {len(created)} bounded automatic canonical admission(s): {', '.join(created)}")
    else:
        print("No evidence-clean automatic canonical admissions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
