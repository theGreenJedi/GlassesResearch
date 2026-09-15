#!/usr/bin/env python3
"""Fail if generated Report Cards omit/contradict deterministically resolved canonical facts."""
from __future__ import annotations
import argparse,json
from pathlib import Path
RESOLVERS={"camera":{"no":0.0,"na":"na"}}
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def rows(p,k): return {r["id"]:r.get(k,{}) for r in p.get("records",[]) if r.get("id")}
def val(x): return x.get("value") if isinstance(x,dict) else x
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--capabilities",required=True); ap.add_argument("--report-cards",required=True); a=ap.parse_args(); caps=rows(load(a.capabilities),"capabilities"); cards=rows(load(a.report_cards),"scores"); bad=[]; checked=0
 for mid,dimensions in caps.items():
  if mid not in cards: continue
  for dim,mapping in RESOLVERS.items():
   fact=val(dimensions.get(dim))
   if fact not in mapping: continue
   checked+=1; expected=mapping[fact]; actual=cards[mid].get(dim,"unknown")
   if actual!=expected: bad.append(f"{mid} {dim}: canonical {fact!r} requires {expected!r}; card has {actual!r}")
 if bad:
  print("Report Card reconciliation FAILED:"); [print(" -",x) for x in bad]; raise SystemExit(1)
 print(f"Report Card reconciliation OK: {checked} resolved canonical facts checked")
if __name__=="__main__": main()
