#!/usr/bin/env python3
"""Extract per-model GlassesResearch Report Card scores from report-card Markdown."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DIMENSIONS = {
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
SECTION = re.compile(r"^##+\s+(GLS-\d{4})\s+[—-]\s+(.+?)\s*$")
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")


def parse_score(raw: str):
    value = raw.strip()
    if value.upper() in {"N/A", "NA"}:
        return "na"
    if value.lower() in {"not yet graded", "unknown", "—", "-", ""}:
        return "unknown"
    try:
        score = float(value)
    except ValueError:
        return "unknown"
    return score if 0 <= score <= 10 else "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    root = Path(args.input_dir)
    records: dict[str, dict] = {}
    for path in sorted(root.rglob("*.md")):
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            section = SECTION.match(line)
            if section:
                current = section.group(1)
                records.setdefault(current, {"id": current, "scores": {}, "sources": []})
                rel = path.relative_to(root.parent).as_posix()
                if rel not in records[current]["sources"]:
                    records[current]["sources"].append(rel)
                continue
            if not current:
                continue
            row = ROW.match(line)
            if not row:
                continue
            label, raw_score = row.group(1).strip(), row.group(2).strip()
            dimension = DIMENSIONS.get(label)
            if not dimension:
                continue
            records[current]["scores"][dimension] = parse_score(raw_score)

    payload = {
        "schema_version": 1,
        "score_min": 0,
        "score_max": 10,
        "unknown_semantics": "unknown and N/A never satisfy a minimum-score filter",
        "dimensions": [{"id": v, "label": k} for k, v in DIMENSIONS.items()],
        "records": sorted(records.values(), key=lambda r: r["id"]),
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Extracted Report Card scores for {len(records)} models")


if __name__ == "__main__":
    main()
