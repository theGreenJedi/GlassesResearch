#!/usr/bin/env python3
"""Discover real smart-glasses questions and maintain the canonical question registry.

This job deliberately discovers; it does not manufacture answers. Search Console is
an owned first-party sensor. Optional external question feeds can be supplied as JSON
via QUESTION_DISCOVERY_FEEDS once a source is approved for automated collection.
"""
from __future__ import annotations

import json, os, re, sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
import requests

REGISTRY = Path("research/questions/registry.json")
REPORT_JSON = Path("analytics/question-discovery.json")
REPORT_MD = Path("analytics/question-discovery.md")
QUESTION_WORDS = ("who ","what ","when ","where ","why ","how ","can ","could ","do ","does ","did ","is ","are ","will ","would ","should ","which ")
SMART_TERMS = ("smart glass","ai glass","ar glass","wearable","ray-ban meta","ray ban meta","spectacles","inmo","rokid","vuzix","realwear","solos","brilliant","even realities","myvu","heycyan")

def norm(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", " ", s.casefold()).strip()
    return re.sub(r"\s+", " ", s)

def looks_like_question(s: str) -> bool:
    n=norm(s)
    return (s.strip().endswith("?") or n.startswith(QUESTION_WORDS)) and any(t in n for t in SMART_TERMS)

def gsc_token():
    raw=os.getenv("GOOGLE_SEARCH_CONSOLE_CREDENTIALS","").strip()
    site=os.getenv("GOOGLE_SEARCH_CONSOLE_SITE_URL","").strip()
    if not raw or not site: return None,site
    from google.auth.transport.requests import Request
    from google.oauth2 import service_account
    creds=service_account.Credentials.from_service_account_info(json.loads(raw),scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    creds.refresh(Request()); return creds.token,site

def gsc_questions():
    token,site=gsc_token()
    if not token: return []
    end=date.today()-timedelta(days=2); start=end-timedelta(days=27)
    endpoint="https://searchconsole.googleapis.com/webmasters/v3/sites/"+quote(site,safe="")+"/searchAnalytics/query"
    r=requests.post(endpoint,headers={"Authorization":f"Bearer {token}"},json={"startDate":start.isoformat(),"endDate":end.isoformat(),"type":"web","dataState":"final","dimensions":["query"],"rowLimit":25000},timeout=45)
    r.raise_for_status()
    out=[]
    for row in r.json().get("rows",[]):
        q=(row.get("keys") or [""])[0].strip()
        if looks_like_question(q):
            out.append({"question":q,"source":"google_search_console","observed_at":end.isoformat(),"metrics":{"clicks":float(row.get("clicks",0)),"impressions":float(row.get("impressions",0)),"ctr":float(row.get("ctr",0)),"position":float(row.get("position",0))}})
    return out

def external_questions():
    out=[]
    for url in [x.strip() for x in os.getenv("QUESTION_DISCOVERY_FEEDS","").split(",") if x.strip()]:
        try:
            r=requests.get(url,timeout=30); r.raise_for_status(); payload=r.json()
            rows=payload if isinstance(payload,list) else payload.get("questions",[])
            for item in rows:
                q=item if isinstance(item,str) else item.get("question","")
                if q and looks_like_question(q): out.append({"question":q,"source":url,"observed_at":date.today().isoformat()})
        except Exception as exc:
            print(f"question feed unavailable {url}: {exc}",file=sys.stderr)
    return out

def load_registry():
    if REGISTRY.exists(): return json.loads(REGISTRY.read_text())
    return {"schema_version":1,"principle":"The registry grows only from questions people actually ask. It has no target size and no ceiling.","next_id":1,"questions":[]}

def main():
    reg=load_registry(); now=datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    by_norm={q["normalized"]:q for q in reg["questions"]}; new=[]; observations=0
    for obs in gsc_questions()+external_questions():
        observations+=1; n=norm(obs["question"])
        if n in by_norm:
            item=by_norm[n]; item.setdefault("observations",[]).append(obs); item["last_observed"]=obs["observed_at"]
            if obs["question"] not in item.setdefault("variants",[]): item["variants"].append(obs["question"])
            continue
        qid=f"Q-{reg['next_id']:06d}"; reg["next_id"]+=1
        item={"id":qid,"canonical_question":obs["question"],"normalized":n,"variants":[obs["question"]],"status":"observed","first_observed":obs["observed_at"],"last_observed":obs["observed_at"],"observations":[obs],"answer_url":None,"evidence_state":"unresearched"}
        reg["questions"].append(item); by_norm[n]=item; new.append(item)
    reg["updated_at"]=now; REGISTRY.parent.mkdir(parents=True,exist_ok=True); REGISTRY.write_text(json.dumps(reg,indent=2,sort_keys=True)+"\n")
    payload={"generated_at":now,"observations":observations,"new_questions":len(new),"registry_size":len(reg["questions"]),"questions":new}
    REPORT_JSON.parent.mkdir(exist_ok=True); REPORT_JSON.write_text(json.dumps(payload,indent=2)+"\n")
    lines=["# Question Discovery — Latest","",f"Generated: **{now}**","",f"- Observations processed: **{observations}**",f"- New materially distinct questions: **{len(new)}**",f"- Canonical registry size: **{len(reg['questions'])}**","","## Newly surfaced questions",""]
    lines += [f"- **{q['id']}** — {q['canonical_question']}" for q in new] or ["_No new questions surfaced in this run._"]
    lines += ["","> Discovery is not publication. New questions require duplicate review, evidence research, and the normal GlassesResearch evidence standard before an answer is published.",""]
    REPORT_MD.write_text("\n".join(lines))
    print(REPORT_MD.read_text()); return 0

if __name__=="__main__": raise SystemExit(main())
