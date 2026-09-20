#!/usr/bin/env python3
"""Validate canonical presentation imagery before public model pages consume it."""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED = ("primary_image", "credit", "rights_basis", "retrieved_or_captured", "alt", "original_image", "normalization")
RIGHTS_BASES = {
    "original-photography",
    "licensed",
    "manufacturer-press-media",
    "manufacturer-editorial-use",
    "open-license",
    "public-domain",
}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--registry",type=Path,required=True)
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--models",type=Path)
    a=p.parse_args()
    data=json.loads(a.registry.read_text(encoding="utf-8"))
    errors=[]
    records=data.get("records",{})
    if a.models:
        import re
        canonical=set(re.findall(r"^\|\s*(GLS-\d{4})\s*\|",a.models.read_text(encoding="utf-8"),re.MULTILINE))
        registered=set(records)
        for model_id in sorted(canonical-registered):
            errors.append(f"{model_id}: missing canonical visual registry record")
        for model_id in sorted(registered-canonical):
            errors.append(f"{model_id}: visual registry record is not a canonical model")
    for model_id, record in records.items():
        state=record.get("state","missing")
        if state not in {"missing","candidate","cleared","published"}:
            errors.append(f"{model_id}: invalid state {state!r}")
            continue
        if state!="published":
            continue
        for field in REQUIRED:
            if not str(record.get(field,"")).strip():
                errors.append(f"{model_id}: published visual missing {field}")
        if not str(record.get("source_url","")).strip() and not str(record.get("original_photo_provenance","")).strip():
            errors.append(f"{model_id}: published visual needs source_url or original_photo_provenance")
        rights_basis=str(record.get("rights_basis","")).strip()
        if rights_basis not in RIGHTS_BASES:
            errors.append(f"{model_id}: published visual has unsupported rights_basis {rights_basis!r}")
        if rights_basis == "manufacturer-editorial-use":
            if not str(record.get("source_url","")).strip():
                errors.append(f"{model_id}: manufacturer-editorial-use requires source_url")
            if not str(record.get("editorial_purpose","")).strip():
                errors.append(f"{model_id}: manufacturer-editorial-use requires editorial_purpose")
        original=str(record.get("original_image",""))
        if original.startswith(("http://","https://")):
            errors.append(f"{model_id}: original_image must be locally preserved")
        elif original and not (a.root / original.lstrip("/")).exists():
            errors.append(f"{model_id}: original_image does not exist: {original}")
        image=str(record.get("primary_image",""))
        if image.startswith(("http://","https://")):
            errors.append(f"{model_id}: primary_image must be a preserved local site asset, not a hotlink")
        elif image:
            local=a.root / image.lstrip("/")
            if not local.exists():
                errors.append(f"{model_id}: primary_image does not exist: {image}")
        try_on=str(record.get("try_on_asset",""))
        if try_on:
            for field, default in (("try_on_scale", 2.25), ("try_on_y_offset", 0), ("try_on_rotation_offset", 0)):
                value=record.get(field, default)
                if not isinstance(value,(int,float)):
                    errors.append(f"{model_id}: {field} must be numeric")
            scale=record.get("try_on_scale",2.25)
            if isinstance(scale,(int,float)) and not (1.0 <= float(scale) <= 4.0):
                errors.append(f"{model_id}: try_on_scale must be between 1.0 and 4.0")
            runtime = (
                a.root / "docs/vendor/mediapipe/vision_bundle.mjs",
                a.root / "docs/vendor/mediapipe/face_landmarker.task",
            )
            if any(not path.exists() for path in runtime):
                errors.append(f"{model_id}: try_on_asset cannot publish until the self-hosted face-tracking runtime is present")
            if try_on.startswith(("http://","https://")):
                errors.append(f"{model_id}: try_on_asset must be a preserved local site asset")
            elif not (a.root / try_on.lstrip("/")).exists():
                errors.append(f"{model_id}: try_on_asset does not exist: {try_on}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"Validated model visual registry ({len(records)} records)")

if __name__=="__main__":
    main()
