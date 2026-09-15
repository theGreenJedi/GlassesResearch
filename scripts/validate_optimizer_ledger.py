#!/usr/bin/env python3
"""Validate the durable GlassesResearch optimizer/research ledger."""
from __future__ import annotations
import datetime as dt
import pathlib
import re
import sys
import yaml
ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research" / "OPTIMIZER_LEDGER.yaml"
GRADES = {"VERY_HIGH", "HIGH", "MEDIUM", "LOW"}
STATES = {"discovered", "recorded", "monitored", "promoted", "execution", "commissioned", "closed"}
RESEARCH_STATES = {"needs_investigation", "under_investigation", "findings_established"}
ID_RE = re.compile(r"^OPT-\d{4}-\d{3,}$")
ISSUE_RE = re.compile(r"^#\d+$")
def fail(msg):
    print(f"optimizer-ledger: ERROR: {msg}", file=sys.stderr); raise SystemExit(1)
def as_date(v, field, fid):
    if isinstance(v, dt.datetime): return v.date()
    if isinstance(v, dt.date): return v
    if isinstance(v, str):
        try: return dt.date.fromisoformat(v)
        except ValueError: pass
    fail(f"{fid}: {field} must be an ISO date")
def main():
    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1: fail("invalid root/schema_version")
    policy = data.get("policy") or {}
    if policy.get("public_surface") is not False: fail("ledger must remain internal")
    graduation = policy.get("research_graduation") or {}
    if set(graduation.get("states") or []) != RESEARCH_STATES: fail("canonical research states missing")
    if "Community Research is subordinate to Research" not in str(graduation.get("community_research", "")): fail("Community Research must remain subordinate to Research")
    findings = data.get("findings")
    if not isinstance(findings, list): fail("findings must be a list")
    seen = set()
    for f in findings:
        fid = str(f.get("id", ""))
        if not ID_RE.match(fid) or fid in seen: fail(f"invalid/duplicate id {fid!r}")
        seen.add(fid)
        if not str(f.get("title", "")).strip(): fail(f"{fid}: title required")
        if f.get("grade") not in GRADES: fail(f"{fid}: invalid grade")
        if f.get("state") not in STATES: fail(f"{fid}: invalid state")
        first, last = as_date(f.get("first_seen"), "first_seen", fid), as_date(f.get("last_reviewed"), "last_reviewed", fid)
        if last < first: fail(f"{fid}: last_reviewed predates first_seen")
        if not str(f.get("source", "")).strip(): fail(f"{fid}: source/reference required")
        if not str(f.get("rationale", "")).strip() or not str(f.get("evidence_strength", "")).strip(): fail(f"{fid}: rationale/evidence_strength required")
        if f.get("research_state") is not None and f.get("research_state") not in RESEARCH_STATES: fail(f"{fid}: invalid research_state")
        related = f.get("related", [])
        if not isinstance(related, list): fail(f"{fid}: related must be list")
        if f.get("grade") in {"HIGH", "VERY_HIGH"} and f.get("state") in {"promoted", "execution", "commissioned", "closed"} and not any(ISSUE_RE.match(str(x)) for x in related): fail(f"{fid}: promoted HIGH/VERY_HIGH requires execution issue")
    print(f"optimizer-ledger: OK ({len(findings)} findings, {len(seen)} unique ids)")
    return 0
if __name__ == "__main__": raise SystemExit(main())
