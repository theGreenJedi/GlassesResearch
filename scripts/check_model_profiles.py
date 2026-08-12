#!/usr/bin/env python3
"""Check that every canonical GLS model eventually receives a useful editorial profile.

This guard is intentionally non-failing while the 121-model editorial pass is in progress.
Use --strict once coverage reaches 100% to make missing profiles a CI failure.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THE_LIST = ROOT / "models" / "THE_LIST.md"
PROFILES = ROOT / "models" / "PROFILES.md"
ID_RE = re.compile(r"\bGLS-\d{4}\b")
PROFILE_HEADING_RE = re.compile(r"^##\s+(GLS-\d{4})\s+—\s+", re.MULTILINE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail when any canonical model lacks a profile")
    args = parser.parse_args()

    canonical_text = THE_LIST.read_text(encoding="utf-8")
    profile_text = PROFILES.read_text(encoding="utf-8")

    canonical = sorted(set(ID_RE.findall(canonical_text)))
    profiled = sorted(set(PROFILE_HEADING_RE.findall(profile_text)))

    missing = sorted(set(canonical) - set(profiled))
    extra = sorted(set(profiled) - set(canonical))

    print(f"Canonical models: {len(canonical)}")
    print(f"Editorial profiles: {len(profiled)}")
    print(f"Coverage: {len(profiled)}/{len(canonical)}")

    if missing:
        print("Missing profiles:")
        for model_id in missing:
            print(f"  {model_id}")

    if extra:
        print("Profiles without canonical model IDs:")
        for model_id in extra:
            print(f"  {model_id}")
        return 1

    if args.strict and missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
