#!/usr/bin/env python3
"""Validate the model-candidate ledger and report discovery coverage."""
from __future__ import annotations
import argparse, datetime as dt, json, os, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "model-candidates.json"
CATALOG = ROOT / "models" / "CATALOG.md"
THE_LIST = ROOT / "models" / "THE_LIST.md"
RECON = ROOT / "models" / "THE_LIST_RECONCILIATION_2026-08-17.md"
NEWS_DIR = ROOT / "research" / "news-candidates"
ALLOWED = {"untriaged","in-scope","out-of-scope","duplicate-rebrand","needs-evidence","cataloged"}
UNRESOLVED = {"untriaged","in-scope","needs-evidence"}
def norm(v:str)->str: return re.sub(r"[^a-z0-9]+"," ",v.lower()).strip()
def load(): return json.loads(LEDGER.read_text(encoding="utf-8"))
def news_leads(ledger):
    known={s["url"].split("#",1)[0].rstrip("/") for i in ledger.get("candidates",[]) for s in i.get("sources",[]) if s.get("url")}; out=[]
    if not NEWS_DIR.exists(): return out
    for p in sorted(NEWS_DIR.glob("*.json")):
        try: data=json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        for i in data.get("candidates",[]):
            if i.get("scope_lane")!="core_glasses": continue
            u=str(i.get("url","")).split("#",1)[0].rstrip("/")
            if u and u not in known: out.append({"date":p.stem,"title":i.get("title",""),"url":u})
    return out
def audit():
    payload=load(); errors=[]; warnings=[]; items=payload.get("candidates",[])
    if payload.get("schema_version")!=1: errors.append("schema_version must be 1")
    if not isinstance(items,list): return ["candidates must be an array"],warnings,{}
    ids=set(); canonical_text=THE_LIST.read_text(encoding="utf-8") + "\n" + (RECON.read_text(encoding="utf-8") if RECON.exists() else "")
    registry_text=norm(CATALOG.read_text(encoding="utf-8")); today=dt.date.today(); counts={s:0 for s in sorted(ALLOWED)}; oldest=None
    for n,item in enumerate(items):
        pre=f"candidate[{n}]"; cid=item.get("candidate_id")
        if not cid or cid in ids: errors.append(f"{pre}: candidate_id missing or duplicate: {cid!r}")
        else: ids.add(cid)
        status=item.get("status")
        if status not in ALLOWED: errors.append(f"{pre}: invalid status {status!r}"); continue
        counts[status]+=1
        for f in ("maker","model","category","discovered_at","rationale"):
            if not item.get(f): errors.append(f"{pre}: missing {f}")
        try: discovered=dt.date.fromisoformat(item.get("discovered_at",""))
        except ValueError: errors.append(f"{pre}: invalid discovered_at"); discovered=today
        if status in UNRESOLVED:
            age=(today-discovered).days
            if oldest is None or age>oldest[0]: oldest=(age,str(cid))
        sources=item.get("sources")
        if not isinstance(sources,list) or not sources: errors.append(f"{pre}: at least one discovery source is required")
        else:
            for s in sources:
                if not str(s.get("url","")).startswith(("https://","http://")): errors.append(f"{pre}: invalid source URL")
        canonical_id=item.get("canonical_id")
        if canonical_id and canonical_id not in canonical_text: errors.append(f"{pre}: canonical_id {canonical_id} is absent from THE_LIST/reconciliation")
        if status=="cataloged" and not canonical_id: errors.append(f"{pre}: cataloged candidates require canonical_id")
        if item.get("registry_entry") and norm(str(item.get("model",""))) not in registry_text:
            # Family rows may intentionally enumerate models in aliases/notes rather than exact table cell text.
            aliases=[norm(str(a)) for a in item.get("aliases",[]) if a]
            if not any(a and a in registry_text for a in aliases): errors.append(f"{pre}: registry_entry=true but model is absent from models/CATALOG.md")
    leads=news_leads(payload)
    if leads: warnings.append(f"{len(leads)} core-glasses news intake item(s) are not represented by a ledger source URL; review as discovery leads")
    metrics={"total":len(items),"counts":counts,"open":sum(counts[s] for s in UNRESOLVED),"oldest_unresolved_days":oldest[0] if oldest else None,"oldest_unresolved_id":oldest[1] if oldest else None,"unmatched_news_leads":len(leads),"news_leads":leads[-20:]}
    return errors,warnings,metrics
def markdown(m,w):
    lines=["## Model discovery coverage","",f"Ledger candidates: **{m.get('total',0)}**",f"Open candidates: **{m.get('open',0)}**"]
    if m.get("oldest_unresolved_days") is not None: lines.append(f"Oldest unresolved: **{m['oldest_unresolved_id']}** ({m['oldest_unresolved_days']} days)")
    lines += [f"Unmatched core-glasses news leads: **{m.get('unmatched_news_leads',0)}**",""]+[f"- {s}: {c}" for s,c in m.get("counts",{}).items()]
    if w: lines += ["","### Review warnings"]+[f"- {x}" for x in w]
    return "\n".join(lines)+"\n"
def main():
    p=argparse.ArgumentParser(); p.add_argument("--github-summary",action="store_true"); a=p.parse_args(); e,w,m=audit()
    for x in e: print("ERROR:",x)
    for x in w: print("WARNING:",x)
    print(json.dumps({k:v for k,v in m.items() if k!="news_leads"},indent=2))
    if a.github_summary and os.environ.get("GITHUB_STEP_SUMMARY"): Path(os.environ["GITHUB_STEP_SUMMARY"]).write_text(markdown(m,w),encoding="utf-8")
    return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
