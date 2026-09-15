#!/usr/bin/env python3
"""Build Core Report Cards by reconciling canonical facts, research and scored evidence."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
CORE_DIMENSIONS={"Discreetness":"discreetness","Camera":"camera","Visual AI":"visual_ai","Hackability":"hackability","Owner Control":"owner_control","Android Compatibility":"android_compatibility"}
LEGACY_DIMENSIONS={"Hardware":"hardware","Wearability":"wearability","Visual AI":"visual_ai","Software":"software","Display / HUD":"display_hud","Openness":"openness","Owner Control":"owner_control","Cloud Independence":"cloud_independence","Hackability":"hackability","Value":"value"}
DIRECT_LEGACY_TO_CORE={"visual_ai":"visual_ai","hackability":"hackability","owner_control":"owner_control"}
SECTION=re.compile(r"^##+\s+(GLS-\d{4})\s+[—-]\s+(.+?)\s*$"); ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"); MODEL_ROW=re.compile(r"^\|\s*(GLS-\d{4})\s*\|"); MODEL=re.compile(r"\bGLS-\d{4}\b")
RESEARCH_ROOTS=("research/investigations","research/community-research","research/claims","docs/community-research")
RESEARCH_TERMS={"camera":("camera","image capture","photo","video"),"visual_ai":("visual ai","computer vision","ocr","object recognition","visual assistant"),"hackability":("reverse engineer","reverse-engineer","firmware","protocol","packet capture","teardown","ota","payload","root","sdk"),"owner_control":("owner control","local-first","local first","firmware","custom client","unofficial client","protocol","offline","self-host"),"android_compatibility":("android","apk","adb","android sdk"),"discreetness":("discreet","ordinary-looking","camera-free","camera free","appearance","frame design")}
# Canonical facts that deterministically resolve a score. Extend this table as dimensions acquire factual resolvers.
CAPABILITY_RESOLVERS={"camera":{"no":0.0,"na":"na"}}
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
        m=MODEL_ROW.match(line)
        if m: ids.append(m.group(1))
    return sorted(dict.fromkeys(ids))
def load_records(path,key):
    if not path or not path.exists(): return {}
    payload=json.loads(path.read_text(encoding="utf-8")); return {r["id"]:r.get(key,{}) for r in payload.get("records",[]) if r.get("id")}
def scan_research(repo_root):
    records={}
    for rel in RESEARCH_ROOTS:
        base=repo_root/rel
        if not base.exists(): continue
        for path in sorted(base.rglob("*.md")):
            if path.name.lower() in {"readme.md","index.md"}: continue
            text=path.read_text(encoding="utf-8",errors="replace"); ids=sorted(set(MODEL.findall(text))); low=text.lower()
            if not ids: continue
            lane="community" if "community-research" in path.as_posix().lower() else "research"; source={"title":path.stem.replace("_"," "),"path":path.relative_to(repo_root).as_posix(),"lane":lane}
            for dimension,terms in RESEARCH_TERMS.items():
                if any(term in low for term in terms):
                    for model_id in ids: records.setdefault(model_id,{}).setdefault(dimension,{"state":"evidence-available","sources":[]})["sources"].append(source)
    return records
def capability_value(raw): return raw.get("value") if isinstance(raw,dict) else raw
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",required=True); ap.add_argument("--models"); ap.add_argument("--capabilities"); ap.add_argument("--overrides"); ap.add_argument("--research-evidence"); ap.add_argument("--output",required=True); args=ap.parse_args()
    input_dir=Path(args.input_dir); legacy=parse_legacy(input_dir); model_ids=parse_model_ids(Path(args.models) if args.models else None,legacy); capabilities=load_records(Path(args.capabilities) if args.capabilities else None,"capabilities"); overrides=load_records(Path(args.overrides) if args.overrides else None,"scores"); research=load_records(Path(args.research_evidence),"dimensions") if args.research_evidence else scan_research(input_dir.parents[1]); records=[]
    for model_id in model_ids:
        core={d:"unknown" for d in CORE_DIMENSIONS.values()}; meta={d:{"provenance":"unresolved","confidence":"unknown","evidence_state":"none-located"} for d in CORE_DIMENSIONS.values()}; old=legacy.get(model_id,{}); old_scores=old.get("scores",{})
        for legacy_id,core_id in DIRECT_LEGACY_TO_CORE.items():
            score=old_scores.get(legacy_id,"unknown")
            if score!="unknown": core[core_id]=score; meta[core_id]={"provenance":"legacy-report-card","confidence":"documented","evidence_state":"scored"}
        # Canonical factual resolvers outrank absence/unknown and prevent known hardware facts regressing to unknown.
        for dimension,mapping in CAPABILITY_RESOLVERS.items():
            value=capability_value(capabilities.get(model_id,{}).get(dimension))
            if value in mapping: core[dimension]=mapping[value]; meta[dimension]={"provenance":f"finder-capability:{dimension}={value}","confidence":"documented","evidence_state":"scored"}
        for dimension,evidence in research.get(model_id,{}).items():
            if dimension in meta and core[dimension]=="unknown":
                sources=evidence.get("sources",[]); meta[dimension]={"provenance":"model-bound-research","confidence":"assessment-pending","evidence_state":"evidence-available","evidence_lanes":sorted({s.get("lane","research") for s in sources}),"evidence_sources":sources}
        for core_id,raw in overrides.get(model_id,{}).items():
            if core_id not in core: continue
            if isinstance(raw,dict): score=parse_score(raw.get("score")); provenance=raw.get("provenance","curated-override"); confidence=raw.get("confidence","documented")
            else: score=parse_score(raw); provenance="curated-override"; confidence="documented"
            # Overrides may score judgment dimensions, but cannot contradict deterministic canonical facts.
            canonical=capability_value(capabilities.get(model_id,{}).get(core_id)); resolved=CAPABILITY_RESOLVERS.get(core_id,{}).get(canonical,None)
            if resolved is not None and score!=resolved: raise SystemExit(f"{model_id} {core_id}: override {score!r} contradicts canonical {canonical!r} -> {resolved!r}")
            core[core_id]=score; meta[core_id]={"provenance":provenance,"confidence":confidence,"evidence_state":"scored"}
        records.append({"id":model_id,"scores":core,"score_meta":meta,"extended_scores":old_scores,"sources":old.get("sources",[])})
    payload={"schema_version":3,"name":"GlassesResearch Core Report Card","score_min":0,"score_max":10,"unknown_semantics":"unknown means no numeric score is currently justified; score_meta distinguishes no located evidence from admitted evidence awaiting assessment","dimensions":[{"id":v,"label":k} for k,v in CORE_DIMENSIONS.items()],"extended_dimensions":[{"id":v,"label":k} for k,v in LEGACY_DIMENSIONS.items()],"records":records}
    target=Path(args.output); target.parent.mkdir(parents=True,exist_ok=True); target.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Built Core Report Cards for {len(records)} canonical models")
if __name__=="__main__": main()
