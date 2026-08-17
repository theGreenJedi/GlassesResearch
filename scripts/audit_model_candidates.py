#!/usr/bin/env python3
"""Validate the model-candidate ledger and report discovery coverage.

This audit complements catalog consistency. Catalog checks prove that known canonical
models are coherent; this ledger makes discovered but not-yet-canonical models
visible and forces an explicit disposition.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "model-candidates.json"
CATALOG = ROOT / "models" / "CATALOG.md"
THE_LIST = ROOT / "models" / "THE_LIST.md"
NEWS_DIR = ROOT / "research" / "news-candidates"
ALLOWED = {"untriaged", "in-scope", "out-of-scope", "duplicate-rebrand", "needs-evidence", "cataloged"}
UNRESOLVED = {"untriaged", "in-scope", "needs-evidence"}


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def load() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def news_leads(ledger: dict) -> list[dict]:
    known_urls = {
        src["url"].split("#", 1)[0].rstrip("/")
        for item in ledger.get("candidates", [])
        for src in item.get("sources", [])
        if src.get("url")
    }
    leads: list[dict] = []
    if not NEWS_DIR.exists():
        return leads
    for path in sorted(NEWS_DIR.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for item in payload.get("candidates", []):
            if item.get("scope_lane") != "core_glasses":
                continue
            url = str(item.get("url", "")).split("#", 1)[0].rstrip("/")
            if url and url not in known_urls:
                leads.append({"date": path.stem, "title": item.get("title", ""), "url": url})
    return leads


def audit() -> tuple[list[str], list[str], dict]:
    payload = load()
    errors: list[str] = []
    warnings: list[str] = []
    items = payload.get("candidates", [])
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(items, list):
        return ["candidates must be an array"], warnings, {}

    ids: set[str] = set()
    canonical_text = THE_LIST.read_text(encoding="utf-8")
    registry_text = norm(CATALOG.read_text(encoding="utf-8"))
    today = dt.date.today()
    counts = {state: 0 for state in sorted(ALLOWED)}
    oldest_unresolved: tuple[int, str] | None = None

    for i, item in enumerate(items):
        prefix = f"candidate[{i}]"
        cid = item.get("candidate_id")
        if not cid or cid in ids:
            errors.append(f"{prefix}: candidate_id missing or duplicate: {cid!r}")
        else:
            ids.add(cid)
        status = item.get("status")
        if status not in ALLOWED:
            errors.append(f"{prefix}: invalid status {status!r}")
            continue
        counts[status] += 1
        for field in ("maker", "model", "category", "discovered_at", "rationale"):
            if not item.get(field):
                errors.append(f"{prefix}: missing {field}")
        try:
            discovered = dt.date.fromisoformat(item.get("discovered_at", ""))
        except ValueError:
            errors.append(f"{prefix}: invalid discovered_at")
            discovered = today
        if status in UNRESOLVED:
            age = (today - discovered).days
            if oldest_unresolved is None or age > oldest_unresolved[0]:
                oldest_unresolved = (age, str(cid))
        sources = item.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{prefix}: at least one discovery source is required")
        else:
            for source in sources:
                if not str(source.get("url", "")).startswith(("https://", "http://")):
                    errors.append(f"{prefix}: invalid source URL")
        canonical_id = item.get("canonical_id")
        if canonical_id and canonical_id not in canonical_text:
            errors.append(f"{prefix}: canonical_id {canonical_id} is absent from THE_LIST.md")
        if status == "cataloged" and not canonical_id:
            errors.append(f"{prefix}: cataloged candidates require canonical_id")
        if item.get("registry_entry") and norm(str(item.get("model", ""))) not in registry_text:
            errors.append(f"{prefix}: registry_entry=true but model is absent from models/CATALOG.md")

    leads = news_leads(payload)
    if leads:
        warnings.append(f"{len(leads)} core-glasses news intake item(s) are not represented by a ledger source URL; review as discovery leads")
    metrics = {
        "total": len(items),
        "counts": counts,
        "open": sum(counts[s] for s in UNRESOLVED),
        "oldest_unresolved_days": oldest_unresolved[0] if oldest_unresolved else None,
        "oldest_unresolved_id": oldest_unresolved[1] if oldest_unresolved else None,
        "unmatched_news_leads": len(leads),
        "news_leads": leads[-20:],
    }
    return errors, warnings, metrics


def markdown(metrics: dict, warnings: list[str]) -> str:
    lines = ["## Model discovery coverage", "", f"Ledger candidates: **{metrics.get('total', 0)}**", f"Open candidates: **{metrics.get('open', 0)}**"]
    if metrics.get("oldest_unresolved_days") is not None:
        lines.append(f"Oldest unresolved: **{metrics['oldest_unresolved_id']}** ({metrics['oldest_unresolved_days']} days)")
    lines.append(f"Unmatched core-glasses news leads: **{metrics.get('unmatched_news_leads', 0)}**")
    lines.append("")
    for state, count in metrics.get("counts", {}).items():
        lines.append(f"- {state}: {count}")
    if warnings:
        lines += ["", "### Review warnings"] + [f"- {w}" for w in warnings]
    leads = metrics.get("news_leads", [])
    if leads:
        lines += ["", "### Recent unmatched discovery leads"]
        for lead in leads[-10:]:
            lines.append(f"- {lead['date']}: [{lead['title']}]({lead['url']})")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-summary", action="store_true")
    args = parser.parse_args()
    errors, warnings, metrics = audit()
    for err in errors:
        print(f"ERROR: {err}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    print(json.dumps({k: v for k, v in metrics.items() if k != "news_leads"}, indent=2))
    if args.github_summary:
        import os
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            Path(summary).write_text(markdown(metrics, warnings), encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
