#!/usr/bin/env python3
"""Build compact six-dimension Core Report Cards for every canonical model.

The Core Report Card is intentionally small enough to power the Finder across the
entire catalog. Existing deep Report Card dimensions are preserved as extended
scores. Unknown remains unknown; this builder never turns missing evidence into a
negative or an invented score.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CORE_DIMENSIONS = {
    "Discreetness": "discreetness",
    "Camera": "camera",
    "Visual AI": "visual_ai",
    "Hackability": "hackability",
    "Owner Control": "owner_control",
    "Android Compatibility": "android_compatibility",
}
LEGACY_DIMENSIONS = {
    "Hardware": "hardware",
    "Wearability": "wearability",
    "Visual AI": "visual_ai",
    "Software": "software",
    "Display / HUD": "display_hud",
    "Openness": "openness",
    "Owner Control": "owner_control",
    "Cloud Independence": "cloud_independence",
    "Hackability": "hackability",
    "Value": "value",
}
DIRECT_LEGACY_TO_CORE = {
    "visual_ai": "visual_ai",
    "hackability": "hackability",
    "owner_control": "owner_control",
}
SECTION = re.compile(r"^##+\s+(GLS-\d{4})\s+[—-]\s+(.+?)\s*$")
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")
MODEL_ROW = re.compile(r"^\|\s*(GLS-\d{4})\s*\|")


def parse_score(raw: object):
    if isinstance(raw, (int, float)):
        score = float(raw)
        return score if 0 <= score <= 10 else "unknown"
    value = str(raw or "").strip()
    if value.upper() in {"N/A", "NA"}:
        return "na"
    if value.lower() in {"not yet graded", "unknown", "—", "-", ""}:
        return "unknown"
    try:
        score = float(value)
    except ValueError:
        return "unknown"
    return score if 0 <= score <= 10 else "unknown"


def parse_legacy(root: Path) -> dict[str, dict]:
    records: dict[str, dict] = {}
    for path in sorted(root.rglob("*.md")):
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            section = SECTION.match(line)
            if section:
                current = section.group(1)
                records.setdefault(current, {"scores": {}, "sources": []})
                rel = path.relative_to(root.parent).as_posix()
                if rel not in records[current]["sources"]:
                    records[current]["sources"].append(rel)
                continue
            if not current:
                continue
            row = ROW.match(line)
            if not row:
                continue
            dimension = LEGACY_DIMENSIONS.get(row.group(1).strip())
            if dimension:
                records[current]["scores"][dimension] = parse_score(row.group(2))
    return records


def parse_model_ids(path: Path | None, legacy: dict[str, dict]) -> list[str]:
    if not path:
        return sorted(legacy)
    ids = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MODEL_ROW.match(line)
        if match:
            ids.append(match.group(1))
    return sorted(dict.fromkeys(ids))


def load_capabilities(path: Path | None) -> dict[str, dict]:
    if not path or not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        record["id"]: record.get("capabilities", {})
        for record in payload.get("records", [])
        if record.get("id")
    }


def load_overrides(path: Path | None) -> dict[str, dict]:
    if not path or not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        record["id"]: record.get("scores", {})
        for record in payload.get("records", [])
        if record.get("id")
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--models")
    ap.add_argument("--capabilities")
    ap.add_argument("--overrides")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    legacy = parse_legacy(Path(args.input_dir))
    model_ids = parse_model_ids(Path(args.models) if args.models else None, legacy)
    capabilities = load_capabilities(Path(args.capabilities) if args.capabilities else None)
    overrides = load_overrides(Path(args.overrides) if args.overrides else None)

    records = []
    for model_id in model_ids:
        core = {dimension: "unknown" for dimension in CORE_DIMENSIONS.values()}
        meta = {
            dimension: {"provenance": "unresolved", "confidence": "unknown"}
            for dimension in CORE_DIMENSIONS.values()
        }
        old = legacy.get(model_id, {})
        old_scores = old.get("scores", {})

        # Only semantically identical old dimensions migrate automatically.
        for legacy_id, core_id in DIRECT_LEGACY_TO_CORE.items():
            score = old_scores.get(legacy_id, "unknown")
            if score != "unknown":
                core[core_id] = score
                meta[core_id] = {
                    "provenance": "legacy-report-card",
                    "confidence": "documented",
                }

        # A verified absence of a camera is enough to score Camera at zero.
        # Presence alone is not enough to invent image-quality/usefulness ratings.
        camera_state = capabilities.get(model_id, {}).get("camera", {}).get("value")
        if camera_state == "no":
            core["camera"] = 0.0
            meta["camera"] = {
                "provenance": "finder-capability:camera=no",
                "confidence": "documented",
            }
        elif camera_state == "na":
            core["camera"] = "na"
            meta["camera"] = {
                "provenance": "finder-capability:camera=na",
                "confidence": "documented",
            }

        # Curated evidence-backed Core scores have final precedence.
        for core_id, raw in overrides.get(model_id, {}).items():
            if core_id not in core:
                continue
            if isinstance(raw, dict):
                score = parse_score(raw.get("score"))
                provenance = raw.get("provenance", "curated-override")
                confidence = raw.get("confidence", "documented")
            else:
                score = parse_score(raw)
                provenance = "curated-override"
                confidence = "documented"
            core[core_id] = score
            meta[core_id] = {"provenance": provenance, "confidence": confidence}

        records.append({
            "id": model_id,
            "scores": core,
            "score_meta": meta,
            "extended_scores": old_scores,
            "sources": old.get("sources", []),
        })

    payload = {
        "schema_version": 2,
        "name": "GlassesResearch Core Report Card",
        "score_min": 0,
        "score_max": 10,
        "unknown_semantics": "unknown and N/A never satisfy a minimum-score filter",
        "dimensions": [{"id": value, "label": label} for label, value in CORE_DIMENSIONS.items()],
        "extended_dimensions": [{"id": value, "label": label} for label, value in LEGACY_DIMENSIONS.items()],
        "records": records,
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built Core Report Cards for {len(records)} canonical models")


if __name__ == "__main__":
    main()
