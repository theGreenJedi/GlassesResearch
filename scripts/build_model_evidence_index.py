#!/usr/bin/env python3
"""Build deterministic per-model evidence indexes from persisted provenance-bearing claims."""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "research" / "claims"
OUT = ROOT / "research" / "model-evidence"

def load_claims():
    claims = []
    for path in sorted(CLAIMS.glob("*.json")):
        claim = json.loads(path.read_text(encoding="utf-8"))
        claim["_path"] = str(path.relative_to(ROOT))
        claims.append(claim)
    return claims

def build():
    grouped = defaultdict(list)
    for claim in load_claims():
        subject = claim.get("subject", {})
        if subject.get("type") != "model":
            continue
        destinations = claim.get("destinations", [])
        dossier = next((d for d in destinations if d.get("target") == "model_dossier"), None)
        if dossier is None:
            raise SystemExit(f"{claim.get('id')}: model claim missing model_dossier destination")
        if dossier.get("disposition") == "rejected":
            raise SystemExit(f"{claim.get('id')}: retained model claim cannot be rejected from its own dossier")
        grouped[subject["id"]].append({
            "id": claim["id"],
            "claim": claim["claim"],
            "status": claim["status"],
            "evidence_lane": claim["evidence"]["lane"],
            "evidence_strength": claim["evidence"]["strength"],
            "source_reference": claim["source"]["reference"],
            "observed_at": claim["source"]["observed_at"],
            "claim_path": claim["_path"],
            "dossier_disposition": dossier["disposition"],
            "dossier_reference": dossier.get("reference"),
            "supports": claim.get("supports", []),
            "contradicts": claim.get("contradicts", [])
        })
    OUT.mkdir(parents=True, exist_ok=True)
    expected = set()
    for model_id, items in grouped.items():
        items.sort(key=lambda x: (x["observed_at"], x["id"]), reverse=True)
        lanes = defaultdict(int); statuses = defaultdict(int)
        for item in items:
            lanes[item["evidence_lane"]] += 1; statuses[item["status"]] += 1
        payload = {
            "schema_version": 1,
            "model_id": model_id,
            "claim_count": len(items),
            "counts_by_evidence_lane": dict(sorted(lanes.items())),
            "counts_by_status": dict(sorted(statuses.items())),
            "claims": items
        }
        path = OUT / f"{model_id}.json"
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        expected.add(path.name)
    for path in OUT.glob("*.json"):
        if path.name not in expected:
            path.unlink()
    print(f"model-evidence: built {len(grouped)} model indexes from {sum(len(v) for v in grouped.values())} claims")

if __name__ == "__main__": build()
