#!/usr/bin/env python3
"""Conservative canonical-model resolver in front of the newsroom news actuator.

The publication actuator itself remains in ``newsroom_news_actuator_core``. This shim
adds exact canonical entity resolution so a strongly verified package that names an
existing model (for example, ``HTC VIVE Eagle``) can carry the corresponding GLS ID
without fuzzy matching or weakening any publication/evidence gate.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

import newsroom_news_actuator_core as core


def normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def package_text(package: dict[str, Any]) -> str:
    values: list[str] = []
    for field in ("title", "summary"):
        value = package.get(field)
        if isinstance(value, str):
            values.append(value)
    claims = package.get("claims")
    if isinstance(claims, list):
        for claim in claims:
            if isinstance(claim, dict) and isinstance(claim.get("statement"), str):
                values.append(claim["statement"])
    return normalize(" ".join(values))


def canonical_aliases(ledger: str) -> dict[str, set[str]]:
    aliases: dict[str, set[str]] = {}
    row = re.compile(r"^\|\s*(GLS-\d{4})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
    for model_id, maker, model in row.findall(ledger):
        model_norm = normalize(model)
        candidates = {normalize(f"{maker} {model}")}
        # Model-only resolution is allowed only for multi-token canonical names.
        # This keeps exact names such as "VIVE Eagle" useful while avoiding
        # dangerous single-word matches such as "Frames" or "Glasses".
        if len(model_norm.split()) >= 2:
            candidates.add(model_norm)
        for alias in candidates:
            if alias:
                aliases.setdefault(alias, set()).add(model_id)
    return aliases


def contains_phrase(haystack: str, needle: str) -> bool:
    return f" {needle} " in f" {haystack} "


def existing_gls_ids(root: Path, package: dict[str, Any]) -> list[str]:
    ledger = (root / "models" / "THE_LIST.md").read_text(encoding="utf-8")
    explicit = set(re.findall(r"\bGLS-\d{4}\b", json.dumps(package, ensure_ascii=False)))
    resolved = {model_id for model_id in explicit if model_id in ledger}

    text = package_text(package)
    for alias, model_ids in canonical_aliases(ledger).items():
        # Ambiguous canonical aliases never resolve automatically.
        if len(model_ids) == 1 and contains_phrase(text, alias):
            resolved.update(model_ids)
    return sorted(resolved)


def resolver_self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "models").mkdir(parents=True)
        (root / "models" / "THE_LIST.md").write_text(
            "| ID | Maker | Model | Era | State | Type | Access | Evidence / links |\n"
            "|---|---|---:|---:|---|---|---|---|\n"
            "| GLS-0025 | HTC | VIVE Eagle | 2025 | current | camera/audio | retail | primary |\n"
            "| GLS-0998 | Example | Twin Glasses | 2026 | current | audio | retail | primary |\n"
            "| GLS-0999 | Other | Twin Glasses | 2026 | current | audio | retail | primary |\n",
            encoding="utf-8",
        )
        vive = {
            "title": "HTC VIVE Eagle reaches U.S. retail availability",
            "summary": "VIVE Eagle is now available in the U.S.",
            "claims": [],
        }
        assert existing_gls_ids(root, vive) == ["GLS-0025"]
        ambiguous = {"title": "Twin Glasses update", "summary": "Twin Glasses changed.", "claims": []}
        assert existing_gls_ids(root, ambiguous) == []
        explicit = {"title": "Unrelated", "summary": "GLS-0998 changed.", "claims": []}
        assert existing_gls_ids(root, explicit) == ["GLS-0998"]
    print("Canonical newsroom model resolver self-test passed")


core.existing_gls_ids = existing_gls_ids

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        resolver_self_test()
    raise SystemExit(core.main())
