#!/usr/bin/env python3
"""Build model/dimension evidence state from admitted model-bound research.

This does not convert community evidence into GlassesResearch verification and does
not invent scores. It makes admitted research available to Report Card generation
so `unknown` means unscored, not unseen.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

MODEL = re.compile(r"\bGLS-\d{4}\b")
TITLE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
ROOTS = ("research/investigations", "research/community-research", "research/claims", "docs/community-research")
DIMENSIONS = {
    "camera": ("camera", "image capture", "photo", "video"),
    "visual_ai": ("visual ai", "computer vision", "ocr", "object recognition", "visual assistant"),
    "hackability": ("reverse engineer", "reverse-engineer", "firmware", "protocol", "packet capture", "teardown", "ota", "payload", "root", "sdk"),
    "owner_control": ("owner control", "local-first", "local first", "firmware", "custom client", "unofficial client", "protocol", "offline", "self-host"),
    "android_compatibility": ("android", "apk", "adb", "android sdk"),
    "discreetness": ("discreet", "ordinary-looking", "camera-free", "camera free", "appearance", "frame design"),
}

def lane(path: Path) -> str:
    value = path.as_posix().lower()
    return "community" if "community-research" in value else "research"

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--root",required=True); ap.add_argument("--output",required=True); args=ap.parse_args()
    root=Path(args.root); records: dict[str,dict[str,list[dict]]]={}
    for rel in ROOTS:
        base=root/rel
        if not base.exists(): continue
        for path in sorted(base.rglob("*.md")):
            if path.name.lower() in {"readme.md","index.md"}: continue
            text=path.read_text(encoding="utf-8",errors="replace"); ids=sorted(set(MODEL.findall(text)))
            if not ids: continue
            low=text.lower(); tm=TITLE.search(text); title=tm.group(1).strip() if tm else path.stem.replace("_"," ")
            source={"title":title,"path":path.relative_to(root).as_posix(),"lane":lane(path)}
            for dimension, terms in DIMENSIONS.items():
                if not any(term in low for term in terms): continue
                for model_id in ids:
                    records.setdefault(model_id,{}).setdefault(dimension,[]).append(source)
    payload={"schema_version":1,"semantics":"Model-bound admitted research relevant to Report Card dimensions. Presence informs evidence state but does not itself verify a claim or assign a score.","records":[]}
    for model_id,dims in sorted(records.items()):
        payload["records"].append({"id":model_id,"dimensions":{d:{"state":"evidence-available","sources":s} for d,s in sorted(dims.items())}})
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Built research evidence state for {len(records)} models")
    return 0
if __name__=="__main__": raise SystemExit(main())
