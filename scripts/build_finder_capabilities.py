#!/usr/bin/env python3
"""Build the Glasses Finder four-state capability matrix.

Every canonical GLS model receives every shopper-facing capability field with one of:
yes, no, unknown, na. Explicit comparison data and curated overrides win. Conservative
category-derived facts are allowed only when the catalog type itself establishes them;
absence of evidence never becomes `no`.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

CAPABILITIES = [
    "prescription_support", "progressive_lenses", "ordinary_optician", "adjustable_diopter",
    "camera", "no_camera", "photo_capture", "video_recording", "live_video",
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
    if field == "no_camera":
        entry = fields.get("camera_count")
        if entry and entry.get("evidence") != "unknown":
            try:
                return ("yes" if int(entry.get("value")) == 0 else "no"), "comparison"
            except (TypeError, ValueError):
                pass
        camera = fields.get("camera") or fields.get("camera_present")
        camera_state = state(camera.get("value")) if camera and camera.get("evidence") != "unknown" else None
        if camera_state in {"yes", "no"}:
            return ("no" if camera_state == "yes" else "yes"), "comparison"
    for candidate in aliases.get(field, [field]):
        entry = fields.get(candidate)
        if not entry or entry.get("evidence") == "unknown":
            continue
        s = state(entry.get("value"))
        if s:
            return s, "comparison"
    return None, None


def category_fact(model, field):
    """Return only facts that are encoded by the canonical product type itself.

    This intentionally stays conservative. For example, `audio` establishes that a
    product is audio-capable and lacks a display/camera when the type contains no such
    modifier. A generic `display` type does *not* establish that there is no camera,
    because several AR/display products include environmental cameras without encoding
    that detail in the short type label.
    """
    t = model["type"].strip().lower()
    has_camera = "camera" in t
    has_audio = "audio" in t
    has_display = any(x in t for x in ("display", " ar", "ar ", "xr", "monocular", "hud"))
    pure_audio_family = has_audio and not has_camera and not has_display
    camera_audio_nodisplay = has_camera and has_audio and not has_display
    camera_only_nodisplay = has_camera and not has_audio and not has_display

    positives = {
        "camera": has_camera,
        "photo_capture": has_camera,
        "speakers": has_audio,
        "microphones": has_audio or has_camera,
        "music": has_audio,
        "display": has_display,
        "no_display": pure_audio_family or camera_audio_nodisplay or camera_only_nodisplay,
    }
    if positives.get(field):
        return "yes", "catalog-type"

    # Definitive negatives only where the type taxonomy excludes the capability.
    if pure_audio_family and field in {"camera", "photo_capture", "video_recording", "live_video", "display", "full_color_display", "binocular_display"}:
        return "no", "catalog-type-negative"
    if pure_audio_family and field == "no_camera":
        return "yes", "catalog-type"
        return "no", "catalog-type-negative"
    if (camera_audio_nodisplay or camera_only_nodisplay) and field in {"display", "full_color_display", "binocular_display"}:
        return "no", "catalog-type-negative"
    if has_display and field == "no_display":
        return "no", "catalog-type-negative"
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
    summary = Counter()
    for model in models:
        caps = {}
        for field in CAPABILITIES:
            value, provenance = explicit_from_comparison(comparisons.get(model["id"]), field)
            if not value:
                value, provenance = category_fact(model, field)
            override = overrides.get(model["id"], {}).get(field)
            if override:
                if isinstance(override, str):
                    value, provenance = override, "curated-override"
                else:
                    value = override.get("value", value)
                    provenance = override.get("provenance", "curated-override")
            final = value or "unknown"
            caps[field] = {"value": final, "provenance": provenance or "unresolved"}
            summary[final] += 1
        if caps["camera"]["value"] == "yes":
            caps["no_camera"] = {"value": "no", "provenance": "logical-inverse"}
        elif caps["no_camera"]["value"] == "yes":
            caps["camera"] = {"value": "no", "provenance": "logical-inverse"}
        if caps["display"]["value"] == "yes":
            caps["no_display"] = {"value": "no", "provenance": "logical-inverse"}
        elif caps["no_display"]["value"] == "yes":
            caps["display"] = {"value": "no", "provenance": "logical-inverse"}
        out.append({**model, "capabilities": caps})

    payload = {
        "schema_version": 1,
        "semantics": "yes/no/unknown/na; negatives are emitted only from explicit evidence, curated overrides, logical inverse, or definitive canonical type",
        "capability_fields": CAPABILITIES,
        "summary": dict(summary),
        "records": out,
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(out)} Finder capability records to {target}; states={dict(summary)}")


if __name__ == "__main__":
    main()
