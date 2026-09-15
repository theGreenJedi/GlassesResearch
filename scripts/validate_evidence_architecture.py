#!/usr/bin/env python3
"""Validate GlassesResearch evidence-enrichment contracts, persisted claims, and model evidence indexes."""
import json
import re
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "research" / "evidence-claims.schema.json"
ARCH = ROOT / "research" / "EVIDENCE_ENRICHMENT_ARCHITECTURE.md"
FLOW = ROOT / "research" / "KNOWLEDGE_FLOW.md"
CARD = ROOT / "research" / "REPORT_CARD_PIPELINE.md"
CLAIMS = ROOT / "research" / "claims"
MODEL_EVIDENCE = ROOT / "research" / "model-evidence"
FIXTURES = ROOT / "tests" / "fixtures" / "evidence-claims"
ID_RE = re.compile(r"^GRCL-\d{4}-\d{4,}$")
def require(condition, message):
    if not condition: raise SystemExit(f"evidence-architecture: ERROR: {message}")
def validate_claim(c, schema, where):
    require(isinstance(c, dict), f"{where}: claim must be object")
    for key in schema["required"]: require(key in c, f"{where}: missing {key}")
    require(ID_RE.match(str(c["id"])), f"{where}: invalid id")
    require(c["subject"]["type"] in schema["properties"]["subject"]["properties"]["type"]["enum"], f"{where}: invalid subject type")
    require(c["evidence"]["lane"] in schema["properties"]["evidence"]["properties"]["lane"]["enum"], f"{where}: invalid evidence lane")
    require(c["evidence"]["strength"] in schema["properties"]["evidence"]["properties"]["strength"]["enum"], f"{where}: invalid evidence strength")
    require(c["status"] in schema["properties"]["status"]["enum"], f"{where}: invalid status")
    allowed_targets = set(schema["properties"]["destinations"]["items"]["properties"]["target"]["enum"])
    require(c["destinations"], f"{where}: destinations required")
    targets = [d["target"] for d in c["destinations"]]
    require(len(targets) == len(set(targets)), f"{where}: duplicate destination")
    require(set(targets) <= allowed_targets, f"{where}: invalid destination")
    if c["subject"]["type"] == "model":
        dossier = next((d for d in c["destinations"] if d["target"] == "model_dossier"), None)
        require(dossier is not None, f"{where}: retained model claim missing model_dossier destination")
        require(dossier["disposition"] != "rejected", f"{where}: retained model claim rejected from its own dossier")
    return c
def load_claims(directory, schema):
    out = {}
    for path in sorted(directory.glob("*.json")):
        c = validate_claim(json.loads(path.read_text(encoding="utf-8")), schema, path.relative_to(ROOT))
        require(c["id"] not in out, f"duplicate claim id {c['id']}")
        out[c["id"]] = c
    return out
def validate_links(claims, label):
    for cid, c in claims.items():
        for other in c.get("contradicts", []):
            require(other in claims, f"{label}: {cid} contradicts missing {other}")
            require(cid in claims[other].get("contradicts", []), f"{label}: contradiction {cid}<->{other} must be reciprocal")
        for other in c.get("supports", []): require(other in claims, f"{label}: {cid} supports missing {other}")
def validate_model_indexes(claims):
    expected = defaultdict(set)
    for cid, c in claims.items():
        if c["subject"]["type"] == "model": expected[c["subject"]["id"]].add(cid)
    actual_models = set()
    for path in sorted(MODEL_EVIDENCE.glob("*.json")):
        index = json.loads(path.read_text(encoding="utf-8"))
        model = index.get("model_id")
        require(model == path.stem, f"{path.relative_to(ROOT)}: model_id/path mismatch")
        actual_models.add(model)
        ids = [x.get("id") for x in index.get("claims", [])]
        require(len(ids) == len(set(ids)), f"{model}: duplicate indexed claim")
        require(set(ids) == expected.get(model, set()), f"{model}: model evidence index is incomplete or contains orphan references")
        require(index.get("claim_count") == len(ids), f"{model}: claim_count mismatch")
        for item in index.get("claims", []):
            source = claims[item["id"]]
            require(item.get("status") == source["status"], f"{model}/{item['id']}: status drift")
            require(item.get("evidence_lane") == source["evidence"]["lane"], f"{model}/{item['id']}: lane drift")
            require(item.get("source_reference") == source["source"]["reference"], f"{model}/{item['id']}: source drift")
    require(actual_models == set(expected), "one or more canonical model subjects lack a complete evidence index")
def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    require(schema.get("additionalProperties") is False, "claim schema must be closed")
    required = set(schema.get("required", []))
    require({"id","claim","subject","source","evidence","status","destinations"} <= required, "core claim fields missing")
    lanes = set(schema["properties"]["evidence"]["properties"]["lane"]["enum"])
    require({"community","documentary_regulatory","manufacturer","commercial","developer","independent","gr_lab","unknown"} <= lanes, "evidence lanes incomplete")
    targets = set(schema["properties"]["destinations"]["items"]["properties"]["target"]["enum"])
    require({"canonical_model","model_dossier","report_card","cross_model","research_queue","finder_comparison","public_research","editorial"} <= targets, "destination set incomplete")
    arch, flow, card = ARCH.read_text(encoding="utf-8"), FLOW.read_text(encoding="utf-8"), CARD.read_text(encoding="utf-8")
    require("Research is the umbrella" in arch and "Community Research is a subordinate" in arch, "research hierarchy missing")
    require("Contradictions are first-class" in arch, "contradiction preservation missing")
    require("Provenance travels with every claim" in arch, "provenance invariant missing")
    require("No-orphan invariant" in arch and "canonical human-facing dossier" in arch, "model-page completeness contract missing")
    require("Route → Enrich → Publish/Propagate" in flow, "knowledge flow does not include enrichment")
    require("does **not** silently rewrite a score" in card, "Report Card evidence gate missing")
    claims = load_claims(CLAIMS, schema)
    require(claims, "at least one real persisted claim required")
    require(any(c["evidence"]["lane"] == "community" for c in claims.values()), "real community claim required")
    require(any(c["evidence"]["lane"] == "documentary_regulatory" for c in claims.values()), "real documentary/regulatory claim required")
    validate_links(claims, "real claims")
    validate_model_indexes(claims)
    fixtures = load_claims(FIXTURES, schema)
    require(len(fixtures) >= 2, "contradiction fixtures required")
    validate_links(fixtures, "fixtures")
    require(any(c.get("contradicts") for c in fixtures.values()), "contradiction fixture not exercised")
    print(f"evidence-architecture: OK ({len(claims)} real claims; complete model indexes; contradiction preservation exercised)")
if __name__ == "__main__": main()
