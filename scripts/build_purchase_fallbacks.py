#!/usr/bin/env python3
"""Generate durable secondary-market search fallbacks for every canonical GLS model.

These are search routes, not inventory claims. Curated exact retailer/manufacturer sources
remain in purchase-sources.json; this output only guarantees that a shopper can continue
looking for any model, especially discontinued hardware.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote_plus

ROW = re.compile(r"^\| (GLS-\d{4}) \| ([^|]+) \| ([^|]+) \|")


def models(path: Path):
    out = []
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        out.append({"id": m.group(1).strip(), "maker": m.group(2).strip(), "model": m.group(3).strip()})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True)
    ap.add_argument("--curated", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    curated_data = json.loads(Path(args.curated).read_text(encoding="utf-8"))
    curated = {r["id"]: r.get("sources", []) for r in curated_data.get("records", [])}
    records = []
    for model in models(Path(args.models)):
        sources = curated.get(model["id"], [])
        has_ebay = any("ebay." in str(s.get("url", "")).lower() for s in sources)
        fallback = None
        if not has_ebay:
            query = quote_plus(f'{model["maker"]} {model["model"]} smart glasses')
            fallback = {
                "source_type": "secondary_market",
                "retailer": "eBay",
                "label": "eBay exact-model search",
                "condition": "used",
                "url": f"https://www.ebay.com/sch/i.html?_nkw={query}",
                "availability": "search",
                "exact_model_confidence": "search",
                "generated": True,
                "note": "Durable discovery fallback; search results are not guaranteed to match the exact model and must be checked by the shopper."
            }
        records.append({"id": model["id"], "fallback": fallback})

    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "meaning": "Generated secondary-market discovery fallbacks; not inventory claims.",
        "records": records,
    }
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated fallback records for {len(records)} models")


if __name__ == "__main__":
    main()
