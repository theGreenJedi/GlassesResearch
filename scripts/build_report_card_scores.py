#!/usr/bin/env python3
"""Build compact six-dimension Core Report Cards for every canonical model."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
CORE_DIMENSIONS={"Discreetness":"discreetness","Camera":"camera","Visual AI":"visual_ai","Hackability":"hackability","Owner Control":"owner_control","Android Compatibility":"android_compatibility"}
LEGACY_DIMENSIONS={"Hardware":"hardware","Wearability":"wearability","Visual AI":"visual_ai","Software":"software","Display / HUD":"display_hud","Openness":"openness","Owner Control":"owner_control","Cloud Independence":"cloud_independence","Hackability":"hackability","Value":"value"}
DIRECT_LEGACY_TO_CORE={"visual_ai":"visual_ai","hackability":"hackability","owner_control":"owner_control"}
SECTION=re.compile(r"^##+\s+(GLS-\d{4})\s+[—-]\s+(.+?)\s*$"); ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"); MODEL_ROW=re.compile(r"^\|\s*(GLS-\d{4})\s*\|")
def parse_score(raw):
    if isinstance(raw,(int,float)): return float(raw) if 0<=float(raw)<=10 else "unknown"
    value=str(raw or "").strip()
    if value.upper() in {"N/A","NA"}: return "na"
    if value.lower() in {"not yet graded","unknown","—","-",""}: return "unknown"
    try: score=float(value)
    except ValueError: return "unknown"
    return score if 0<=score<=10 else "unknown"
def parse_legacy(root):
    records={}
    for path in sorted(root.rglob("*.md")):
        current=None
        for line in path.read_text(encoding="utf-8").splitlines():
            section=SECTION.match(line)
            if section:
                current=section.group(1); records.setdefault(current,{"scores":{},"sources":[]}); rel=path.relative_to(root.parent).as_posix()
                if rel not in records[current]["sources"]: records[current]["sources"].append(rel)
                continue
            if not current: continue
            row=ROW.match(line)
            if row:
                dimension=LEGACY_DIMENSIONS.get(row.group(1).strip())
                if dimension: records[current]["scores"][dimension]=parse_score(row.group(2))
    return records
def parse_model_ids(path,legacy):
    if not path: return sorted(legacy)
    ids=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        match=MODEL_ROW.match(line)
        if match: ids.append(match.group(1))
    return sorted(dict.fromkeys(ids))
def load_records(path,key):
    if not path or not path.exists(): return {}
    payload=json.loads(path.read_text(encoding="utf-8")); return {r["id"]:r.get(key,{}) for r in payload.get("records",[]) if r.get("id")}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",required=True); ap.add_argument("--models"); ap.add_argument("--capabilities"); ap.add_argument("--overrides"); ap.add_argument("--research-evidence"); ap.add_argument("--output",required=True); args=ap.parse_args()
    legacy=parse_legacy(Path(args.input_dir)); model_ids=parse_model_ids(Path(args.models) if args.models else None,legacy)
    capabilities=load_records(Path(args.capabilities) if args.capabilities else None,"capabilities"); overrides=load_records(Path(args.overrides) if args.overrides else None,"scores"); research=load_records(Path(args.research_evidence) if args.research_evidence else None,"dimensions")
    records=[]
    for model_id in model_ids:
        core={d:"unknown" for d in CORE_DIMENSIONS.values()}; meta={d:{"provenance":"unresolved","confidence":"unknown","evidence_state":"none-located"} for d in CORE_DIMENSIONS.values()}; old=legacy.get(model_id,{}); old_scores=old.get("scores",{})
        for legacy_id,core_id in DIRECT_LEGACY_TO_CORE.items():
            score=old_scores.get(legacy_id,"unknown")
            if score!="unknown": core[core_id]=score; meta[core_id]={"provenance":"legacy-report-card","confidence":"documented","evidence_state":"scored"}
        camera_state=capabilities.get(model_id,{}).get("camera",{}).get("value")
        if camera_state=="no": core["camera"]=0.0; meta["camera"]={"provenance":"finder-capability:camera=no","confidence":"documented","evidence_state":"scored"}
        elif camera_state=="na": core["camera"]="na"; meta["camera"]={"provenance":"finder-capability:camera=na","confidence":"documented","evidence_state":"scored"}
        # Research informs the card even where evidence is not yet sufficient to assign a numeric score.
        for dimension,evidence in research.get(model_id,{}).items():
            if dimension in meta and core[dimension]=="unknown":
                sources=evidence.get("sources",[]); lanes=sorted({s.get("lane","research") for s in sources})
                meta[dimension]={"provenance":"model-bound-research","confidence":"assessment-pending","evidence_state":"evidence-available","evidence_lanes":lanes,"evidence_sources":sources}
        for core_id,raw in overrides.get(model_id,{}).items():
            if core_id not in core: continue
            if isinstance(raw,dict): score=parse_score(raw.get("score")); provenance=raw.get("provenance","curated-override"); confidence=raw.get("confidence","documented")
            else: score=parse_score(raw); provenance="curated-override"; confidence="documented"
            core[core_id]=score; meta[core_id]={"provenance":provenance,"confidence":confidence,"evidence_state":"scored"}
        records.append({"id":model_id,"scores":core,"score_meta":meta,"extended_scores":old_scores,"sources":old.get("sources",[])})
    payload={"schema_version":3,"name":"GlassesResearch Core Report Card","score_min":0,"score_max":10,"unknown_semantics":"unknown means no numeric score is currently justified; score_meta distinguishes no located evidence from admitted evidence awaiting assessment","dimensions":[{"id":v,"label":k} for k,v in CORE_DIMENSIONS.items()],"extended_dimensions":[{"id":v,"label":k} for k,v in LEGACY_DIMENSIONS.items()],"records":records}
    target=Path(args.output); target.parent.mkdir(parents=True,exist_ok=True); target.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Built Core Report Cards for {len(records)} canonical models")
if __name__=="__main__": main()
