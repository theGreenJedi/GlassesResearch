#!/usr/bin/env python3
"""Validate GlassesResearch evidence-enrichment contracts without requiring third-party packages."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "research" / "evidence-claims.schema.json"
ARCH = ROOT / "research" / "EVIDENCE_ENRICHMENT_ARCHITECTURE.md"
FLOW = ROOT / "research" / "KNOWLEDGE_FLOW.md"
CARD = ROOT / "research" / "REPORT_CARD_PIPELINE.md"
def require(condition, message):
    if not condition: raise SystemExit(f"evidence-architecture: ERROR: {message}")
def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    require(schema.get("additionalProperties") is False, "claim schema must be closed")
    required = set(schema.get("required", []))
    require({"id","claim","subject","source","evidence","status","destinations"} <= required, "core claim fields missing")
    lane = schema["properties"]["evidence"]["properties"]["lane"]["enum"]
    require({"community","documentary_regulatory","manufacturer","commercial","developer","independent","gr_lab","unknown"} <= set(lane), "evidence lanes incomplete")
    targets = schema["properties"]["destinations"]["items"]["properties"]["target"]["enum"]
    require({"canonical_model","model_dossier","report_card","cross_model","research_queue","finder_comparison","public_research","editorial"} <= set(targets), "destination set incomplete")
    arch = ARCH.read_text(encoding="utf-8")
    flow = FLOW.read_text(encoding="utf-8")
    card = CARD.read_text(encoding="utf-8")
    require("Research is the umbrella" in arch and "Community Research is a subordinate" in arch, "research hierarchy missing")
    require("Contradictions are first-class" in arch, "contradiction preservation missing")
    require("Provenance travels with every claim" in arch, "provenance invariant missing")
    require("Route → Enrich → Publish/Propagate" in flow, "knowledge flow does not include enrichment")
    require("does **not** silently rewrite a score" in card, "Report Card evidence gate missing")
    print("evidence-architecture: OK")
if __name__ == "__main__": main()
