#!/usr/bin/env python3
"""Persist provenance-bounded evidence authorized by automated triage.

This actuator records evidence; it never publishes a GlassesResearch conclusion,
changes a Report Card score, resolves lineage, or promotes a claim to Verified.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
QUEUE=ROOT/"research/news-reviews/queue.json"
OUT=ROOT/"research/delegated-evidence"

LANES={
 "regulatory":"documentary_regulatory",
 "manufacturer_primary":"manufacturer",
 "primary_artifact":"developer",
 "community":"community",
}
ACTIONS={"record_attributed_evidence","record_community_signal"}

def materialize(queue_path:Path=QUEUE,out:Path=OUT)->int:
    payload=json.loads(queue_path.read_text(encoding="utf-8"))
    out.mkdir(parents=True,exist_ok=True)
    count=0
    for item in payload.get("candidates",[]):
        if not isinstance(item,dict) or not item.get("evidence_write_authorized"):
            continue
        action=str(item.get("evidence_write_scope",""))
        klass=str(item.get("evidence_class","unknown"))
        if action not in ACTIONS or klass not in LANES:
            continue
        url=str(item.get("url","")).strip()
        title=str(item.get("title","")).strip()
        if not url or not title:
            continue
        key=hashlib.sha256(url.encode()).hexdigest()[:16]
        record={
          "schema_version":1,
          "id":"GRDE-"+key.upper(),
          "claim":title,
          "summary":str(item.get("summary","")).strip(),
          "source":{"reference":url,"publisher":str(item.get("source","")).strip() or None,
                    "observed_at":str(item.get("last_seen_utc") or item.get("intake_discovered_utc") or "")},
          "evidence":{"class":klass,"lane":LANES[klass],
                      "attribution_required":True},
          "relationship":item.get("relationship"),
          "content_types":item.get("content_types",[]),
          "routing_targets":item.get("routing_targets",[]),
          "automation":{"action":action,"gr_conclusion_authorized":False,
                        "canonical_mutation_authorized":(klass == "regulatory" and "Research & News" in item.get("routing_targets", []))},
        }
        target=out/f"{record['id']}.json"
        rendered=json.dumps(record,indent=2,ensure_ascii=False)+"\n"
        if not target.exists() or target.read_text(encoding="utf-8")!=rendered:
            target.write_text(rendered,encoding="utf-8"); count+=1
    return count

def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root=Path(d); q=root/"queue.json"; o=root/"out"
        q.write_text(json.dumps({"candidates":[
          {"title":"FCC smart glasses filing","url":"https://fcc.gov/x","evidence_write_authorized":True,
           "evidence_write_scope":"record_attributed_evidence","evidence_class":"regulatory","relationship":"direct"},
          {"title":"Rumor","url":"https://example.com/x","evidence_write_authorized":False,
           "evidence_write_scope":"queue_for_review","evidence_class":"secondary","relationship":"speculative"}]}))
        assert materialize(q,o)==1
        files=list(o.glob("*.json")); assert len(files)==1
        r=json.loads(files[0].read_text()); assert r["evidence"]["lane"]=="documentary_regulatory"
        assert r["automation"]["gr_conclusion_authorized"] is False
        assert materialize(q,o)==0
    print("delegated evidence actuator self-test passed")

def main():
    p=argparse.ArgumentParser(); p.add_argument("--self-test",action="store_true"); a=p.parse_args()
    if a.self_test: self_test(); return
    print(f"Materialized {materialize()} delegated evidence record(s).")
if __name__=="__main__": main()
