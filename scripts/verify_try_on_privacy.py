#!/usr/bin/env python3
"""Fail the public build if the camera try-on shell regresses its privacy boundary."""
from __future__ import annotations
import argparse, re
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--script",type=Path,required=True)
    a=p.parse_args()
    text=a.script.read_text(encoding="utf-8")
    errors=[]
    if re.search(r"https?://",text):
        errors.append("try-on script contains a remote URL")
    if "audio: false" not in text:
        errors.append("try-on camera request must explicitly disable audio")
    for required in ("getUserMedia", "track.stop()", "pagehide", "MEDIAPIPE_MODULE = '/vendor/", "FACE_MODEL = '/vendor/"):
        if required not in text:
            errors.append(f"try-on privacy contract missing {required!r}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Try-on privacy shell validated: same-origin runtime paths, audio disabled, camera shutdown hooks present")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
