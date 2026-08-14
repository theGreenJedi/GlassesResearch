#!/usr/bin/env python3
"""Build the Glasses Finder four-state capability matrix.

Every canonical GLS model receives every shopper-facing capability field with one of:
yes, no, unknown, na. Explicit comparison data and curated overrides win. Conservative
category-derived positives are allowed; absence of evidence never becomes `no`.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CAPABILITIES = [
    "prescription_support", "progressive_lenses", "ordinary_optician", "adjustable_diopter",
    "camera", "photo_capture", "video_recording", "live_video",
    "speakers", "microphones", "phone_calls", "music",
    "display", "full_color_display", "binocular_display", "no_display",
    "ai_assistant", "visual_ai", "translation", "transcription", "navigation",
    "bluetooth", "ble", "wifi", "sdk_api", "open_source", "custom_ai",
    "offline_operation", "self_hostable",
]

YES = {True, "yes", "true", "supported", "available"}
NO = {False, "no", "false", "none", "unsupported"}


def state(value):
    if value is None:
        return None
    if isinstance(value, str):
        v = value.strip().lower()
        if v in YES:
            return "yes"
        if v in NO:
            return "no"
        if v in {"n/a", "na", "not applicable"}:
            return "na"
    if value is True:
        return "yes"
    if value is False:
        return "no"
    return None


def parse_models(path: Path):
    rows = []
    pat = re.compile(r"^\| (GLS-\d{4}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|")
    for line in path.read_text(encoding="utf-8").splitlines():
        m = pat.match(line)
        if not m:
            continue
        rows.append({
            "id": m.group(1).strip(), "maker": m.group(2).strip(), "model": m.group(3).strip(),
            "era": m.group(4).strip(), "state": m.group(5).strip(), "type": m.group(6).strip(),
        })
    return rows


def comparison_map(path: Path):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r.get("id"): r for r in data.get("records", []) if r.get("id")}


def explicit_from_comparison(record, field):
    fields = (record or {}).get("fields", {})
    aliases = {
        "prescription_support": ["prescription_support"],
        "progressive_lenses": ["progressive_lenses"],
        "ordinary_optician": ["ordinary_optician"],
        "adjustable_diopter": ["adjustable_diopter"],
        "camera": ["camera", "camera_present"],
        "photo_capture": ["photo_capture", "photos"],
        "video_recording": ["video_recording"],
        "live_video": ["live_video", "streaming"],
        "speakers": ["speakers"],
        "microphones": ["microphones"],
        "phone_calls": ["phone_calls"],
        "music": ["music"],
        "display": ["display_present"],
        "full_color_display": ["full_color_display"],
        "binocular_display": ["binocular_display"],
        "ai_assistant": ["ai_assistant"],
        "visual_ai": ["visual_ai"],
        "translation": ["translation"],
        "transcription": ["transcription"],
        "navigation": ["navigation"],
        "bluetooth": ["bluetooth"],
        "ble": ["ble"],
        "wifi": ["wifi"],
        "sdk_api": ["sdk_api", "sdk", "api"],
        "open_source": ["open_source"],
        "custom_ai": ["custom_ai"],
        "offline_operation": ["offline_operation"],
        "self_hostable": ["self_hostable"],
    }
    for candidate in aliases.get(field, [field]):
        entry = fields.get(candidate)
        if not entry or entry.get("evidence") == "unknown":
            continue
        s = state(entry.get("value"))
        if s:
            return s, "comparison"
    return None, None


def category_positive(model, field):
    t = model["type"].lower()
    positives = {
        "camera": "camera" in t,
        "photo_capture": "camera" in t,
        "speakers": "audio" in t,
        "microphones": "audio" in t or "camera" in t,
        "display": any(x in t for x in ("display", "ar", "xr", "monocular")),
    }
    if field in positives and positives[field]:
        return "yes", "catalog-type"
    if field == "no_display" and "audio" in t and not any(x in t for x in ("display", "ar", "xr", "monocular")):
        return "yes", "catalog-type"
    return None, None


def load_overrides(path: Path):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["id"]: r.get("capabilities", {}) for r in data.get("records", [])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True)
    ap.add_argument("--comparisons", required=True)
    ap.add_argument("--overrides", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    models = parse_models(Path(args.models))
    comparisons = comparison_map(Path(args.comparisons))
    overrides = load_overrides(Path(args.overrides))
    out = []
    for model in models:
        caps = {}
        for field in CAPABILITIES:
            value, provenance = explicit_from_comparison(comparisons.get(model["id"]), field)
            if not value:
                value, provenance = category_positive(model, field)
            override = overrides.get(model["id"], {}).get(field)
            if override:
                if isinstance(override, str):
                    value, provenance = override, "curated-override"
                else:
                    value = override.get("value", value)
                    provenance = override.get("provenance", "curated-override")
            caps[field] = {"value": value or "unknown", "provenance": provenance or "unresolved"}
        if caps["display"]["value"] == "yes":
            caps["no_display"] = {"value": "no", "provenance": "logical-inverse"}
        elif caps["no_display"]["value"] == "yes":
            caps["display"] = {"value": "no", "provenance": "logical-inverse"}
        out.append({**model, "capabilities": caps})

    payload = {
        "schema_version": 1,
        "semantics": "yes/no/unknown/na; absence of evidence never becomes no",
        "capability_fields": CAPABILITIES,
        "records": out,
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(out)} Finder capability records to {target}")


if __name__ == "__main__":
    main()
