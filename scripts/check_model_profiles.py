#!/usr/bin/env python3
"""Check editorial-profile coverage for canonical and approved pending GLS models.

Canonical coverage remains strict. Reconciliation packets may approve new GLS rows before
`sync_catalog_counts.py` mechanically inserts them into THE_LIST on main; profiles for those
approved admissions must not be treated as orphaned during the pull request that approves them.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
THE_LIST = MODELS / "THE_LIST.md"
ID_RE = re.compile(r"\bGLS-\d{4}\b")
PROFILE_HEADING_RE = re.compile(r"^##\s+(GLS-\d{4})\s+—\s+", re.MULTILINE)
ADMISSION_SECTION_RE = re.compile(r"## Admit to canonical purchaser-history ledger\n(.*?)(?=\n## |\Z)", re.S)
ROW_ID_RE = re.compile(r"^\| (GLS-\d{4}) \|", re.M)


def approved_pending_ids() -> set[str]:
    approved: set[str] = set()
    for path in MODELS.glob("THE_LIST_RECONCILIATION_*.md"):
        text = path.read_text(encoding="utf-8")
        match = ADMISSION_SECTION_RE.search(text)
        if match:
            approved.update(ROW_ID_RE.findall(match.group(1)))
    return approved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail when any canonical model lacks a profile")
    args = parser.parse_args()

    canonical_text = THE_LIST.read_text(encoding="utf-8")
    profile_files = sorted(MODELS.glob("PROFILES*.md"))
    profile_text = "\n".join(path.read_text(encoding="utf-8") for path in profile_files)

    canonical = set(ID_RE.findall(canonical_text))
    pending = approved_pending_ids() - canonical
    expected = canonical | pending
    profiled = set(PROFILE_HEADING_RE.findall(profile_text))

    missing = sorted(canonical - profiled)
    pending_missing = sorted(pending - profiled)
    extra = sorted(profiled - expected)

    print(f"Canonical models: {len(canonical)}")
    print(f"Approved pending admissions: {len(pending)}")
    print(f"Editorial profile volumes: {len(profile_files)}")
    print(f"Editorial profiles: {len(profiled)}")
    print(f"Canonical coverage: {len(canonical) - len(missing)}/{len(canonical)}")

    if missing:
        print("Missing canonical profiles:")
        for model_id in missing:
            print(f"  {model_id}")
    if pending_missing:
        print("Approved admissions missing profiles:")
        for model_id in pending_missing:
            print(f"  {model_id}")
    if extra:
        print("Profiles without canonical or approved-pending model IDs:")
        for model_id in extra:
            print(f"  {model_id}")

    if extra or pending_missing:
        return 1
    if args.strict and missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
