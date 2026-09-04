#!/usr/bin/env python3
"""Promote unusually clean model-admission actions into canonical reconciliation packets.

This is intentionally narrower than the general model proposal actuator. It only acts
on evidence-backed, high-confidence, verified-new-model findings that crossed the
purchaser-history acquisition threshold and carry a fully structured catalog row.
Anything ambiguous remains a draft action for repository review.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "research" / "model-actions"
MODELS = ROOT / "models"
THE_LIST = MODELS / "THE_LIST.md"
AUTO_PROFILES = MODELS / "PROFILES_AUTO_ADMISSIONS.md"
GLS_RE = re.compile(r"\bGLS-(\d{4})\b")
SAFE_SOURCE_CLASSES = {"primary", "retailer", "oem_odm", "certification"}
REQUIRED_ROW_FIELDS = ("maker", "model", "state", "type", "access", "source_url")


class AdmissionError(RuntimeError):
    pass


def _clean_cell(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise AdmissionError(f"catalog row {label} must be a string")
    text = " ".join(value.replace("|", "/").split())
    if not text or len(text) > 240:
        raise AdmissionError(f"catalog row {label} is empty or too long")
    return text


def _existing_numbers() -> set[int]:
    numbers: set[int] = set()
    for path in [THE_LIST, *MODELS.glob("THE_LIST_RECONCILIATION_*.md")]:
        if path.exists():
            numbers.update(int(value) for value in GLS_RE.findall(path.read_text(encoding="utf-8")))
    return numbers


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
        raise AdmissionError(f"{path.name}: invalid model action")
    return value


def _catalog_row(action: dict[str, Any]) -> dict[str, str] | None:
    for consequence in action.get("consequences", []):
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


def _eligible(action: dict[str, Any]) -> tuple[bool, str, dict[str, str] | None]:
    if action.get("disposition") != "catalog_admission_candidate":
        return False, "not a catalog admission candidate", None
    if action.get("proposal_kind") != "catalog_admission" or action.get("conclusion") != "verified_new_model":
        return False, "identity/admission state is not canonical-safe", None
    if action.get("confidence") != "high":
        return False, "requires high confidence", None
    acquisition = action.get("acquisition")
    if not isinstance(acquisition, dict) or acquisition.get("threshold_met") is not True:
        return False, "purchaser-history threshold not met", None
    if action.get("target_gls_ids"):
        return False, "new admission unexpectedly targets an existing GLS id", None
    if action.get("identity_edges"):
        return False, "identity edges require explicit repository review", None
    if action.get("unresolved_questions"):
        return False, "unresolved questions remain", None

    evidence = action.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return False, "no evidence", None
    high_urls = {
        item.get("url") for item in evidence
        if isinstance(item, dict)
        and item.get("confidence") == "high"
        and item.get("source_class") in SAFE_SOURCE_CLASSES
        and isinstance(item.get("url"), str)
    }
    acquisition_urls = {
        url for url in acquisition.get("source_urls", []) if isinstance(url, str)
    }
    if not high_urls.intersection(acquisition_urls):
        return False, "acquisition is not backed by high-confidence primary/commercial evidence", None

    try:
        row = _catalog_row(action)
    except AdmissionError as exc:
        return False, str(exc), None
    if row is None:
        return False, "structured catalog_row payload missing", None
    if row["source_url"] not in high_urls or row["source_url"] not in acquisition_urls:
        return False, "catalog row source is not the verified acquisition source", None
    return True, "eligible", row


def _date(action: dict[str, Any]) -> str:
    revision = action.get("proposal_revision")
    if isinstance(revision, str) and re.match(r"^20\d{2}-\d{2}-\d{2}", revision):
        return revision[:10]
    raise AdmissionError("eligible admission requires a dated proposal revision")


def _packet(gls_id: str, action: dict[str, Any], row: dict[str, str]) -> str:
    date = _date(action)
    evidence = action.get("evidence", [])
    evidence_lines = "\n".join(
        f"- {item.get('url')} — {item.get('supports', '')} ({item.get('source_class')}, {item.get('confidence')})"
        for item in evidence if isinstance(item, dict)
    )
    claims = "\n".join(
        f"- **{item.get('key', 'claim')}** — {item.get('statement', '')} ({item.get('confidence', 'unknown')})"
        for item in action.get("verified_claims", []) if isinstance(item, dict)
    ) or "- none"
    return f"""# Automatic canonical reconciliation — {row['maker']} {row['model']}

Date: {date}
Source action: `{action.get('action_id')}`
Investigation: `{action.get('investigation_key')}`

This packet was generated by the bounded canonical model-admission actuator. The upstream Models finding established a high-confidence distinct identity, a purchaser-history acquisition path, no unresolved identity questions or edges, and a structured catalog row whose source is carried by the admissible evidence packet.

## Admit to canonical purchaser-history ledger

| ID | Maker | Model | State | Type | Access | Evidence |
|---|---|---|---|---|---|---|
| {gls_id} | {row['maker']} | {row['model']} | {row['state']} | {row['type']} | {row['access']} | {row['source_url']} |

## Admission boundary

Admission establishes identity and documented acquisition only. It does not infer Report Card scores, owner control, openness, privacy behavior, cloud independence, durability, or hands-on performance beyond the verified claims below.

## Verified claims

{claims}

## Evidence

{evidence_lines}

## Automation safety

- conclusion: `verified_new_model`
- confidence: `high`
- acquisition threshold: met
- existing GLS targets: none
- unresolved questions: none
- identity edges: none
- catalog row source: verified acquisition evidence

Canonical propagation remains subject to the normal catalog consistency, profile coverage, and public device-database validators.
"""


def _profile(gls_id: str, action: dict[str, Any], row: dict[str, str], packet_name: str) -> str:
    claims = [
        item.get("statement") for item in action.get("verified_claims", [])
        if isinstance(item, dict) and isinstance(item.get("statement"), str)
    ]
    summary = " ".join(claims[:3]) or "No additional product claims are promoted by this admission."
    return f"""
## {gls_id} — {row['maker']} {row['model']}

**Canonical admission profile.** {row['maker']} {row['model']} crossed the purchaser-history threshold through a verified acquisition route. This initial profile intentionally carries only admission-safe identity/acquisition evidence; Report Card scoring and broader operational claims remain unscored until their evidence is separately reviewed.

{summary}

Sources: [canonical reconciliation]({packet_name}) · [acquisition source]({row['source_url']})
"""


def compile_all(input_dir: Path = DEFAULT_INPUT) -> list[str]:
    used = _existing_numbers()
    created: list[str] = []
    profile_text = AUTO_PROFILES.read_text(encoding="utf-8") if AUTO_PROFILES.exists() else "# Automatic Canonical Admission Profiles\n\nThese conservative profiles are generated only for bounded, evidence-clean automatic catalog admissions.\n"

    for path in sorted(input_dir.glob("GRMA-*.json")):
        action = _load(path)
        eligible, reason, row = _eligible(action)
        if not eligible or row is None:
            continue
        action_id = str(action.get("action_id") or path.stem)
        if action_id in profile_text:
            continue
        gls_id = _next_gls(used)
        date = _date(action)
        safe_action = re.sub(r"[^A-Za-z0-9_-]+", "-", action_id).strip("-")[:48]
        packet_name = f"THE_LIST_RECONCILIATION_{date}_AUTO_{safe_action}.md"
        packet_path = MODELS / packet_name
        if packet_path.exists():
            continue
        packet_path.write_text(_packet(gls_id, action, row), encoding="utf-8")
        profile_text += _profile(gls_id, action, row, packet_name) + f"\n<!-- source-action: {action_id} -->\n"
        created.append(gls_id)

    if created:
        AUTO_PROFILES.write_text(profile_text, encoding="utf-8")
    return created


def self_test() -> None:
    action = {
        "schema_version": 1,
        "action_id": "GRMA-TEST",
        "investigation_key": "news:route-1",
        "proposal_revision": "2026-09-03T12:00:00Z",
        "proposal_kind": "catalog_admission",
        "conclusion": "verified_new_model",
        "confidence": "high",
        "target_gls_ids": [],
        "disposition": "catalog_admission_candidate",
        "verified_claims": [{"key": "identity", "statement": "Maker Model is a distinct product.", "confidence": "high"}],
        "evidence": [{"url": "https://maker.example/model", "source_class": "primary", "supports": "product and paid order route", "confidence": "high"}],
        "identity_edges": [],
        "acquisition": {"state": "paid_purchase", "threshold_met": True, "source_urls": ["https://maker.example/model"]},
        "consequences": [{"destination": "catalog.admit_candidate", "reason": "verified distinct purchasable model", "payload": {"catalog_row": {"maker": "Maker", "model": "Model", "state": "current", "type": "camera/audio AI glasses", "access": "retail", "source_url": "https://maker.example/model"}}}],
        "unresolved_questions": [],
    }
    ok, _, row = _eligible(action)
    assert ok and row and row["maker"] == "Maker"
    blocked = json.loads(json.dumps(action))
    blocked["unresolved_questions"] = ["Is this a rebadge?"]
    assert _eligible(blocked)[0] is False
    blocked = json.loads(json.dumps(action))
    blocked["consequences"][0]["payload"] = {}
    assert _eligible(blocked)[0] is False
    print("Canonical model admission actuator self-test passed")


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
    print(f"Created {len(created)} canonical admission(s): {', '.join(created)}" if created else "No canonical-safe model admissions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
