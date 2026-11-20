#!/usr/bin/env python3
"""Read-only AI discovery measurement; citations, referrals and crawls never summed."""
import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
REFS = {"ChatGPT": ("chatgpt.com", "chat.openai.com"),
        "Perplexity": ("perplexity.ai",),
        "Claude": ("claude.ai",),
        "Copilot": ("copilot.microsoft.com",),
        "Gemini": ("gemini.google.com",)}
BOTS = {"OAI-SearchBot": "search", "ChatGPT-User": "user retrieval",
        "GPTBot": "training", "PerplexityBot": "search",
        "Perplexity-User": "user retrieval", "Claude-SearchBot": "search",
        "Claude-User": "user retrieval", "ClaudeBot": "training",
        "bingbot": "general search", "Googlebot": "general search"}
EXPORTS = {"bing_ai": "citation appearances", "google_ai": "AI link impressions"}

def matches(host, domain):
    host = host.lower().strip().rstrip(".")
    return host == domain or host.endswith("." + domain)

def browser_referrals(latest):
    if not latest.get("cloudflare_web_analytics", {}).get("available"):
        return {"status": "unavailable", "platform_pageviews": None}
    period = latest["cloudflare_web_analytics"].get("rolling_7d", {})
    if "referrers" not in period:
        return {"status": "unavailable", "platform_pageviews": None}
    counts = {p: 0 for p in REFS}
    for row in period["referrers"]:
        for p, domains in REFS.items():
            if any(matches(row.get("referrer", ""), d) for d in domains):
                counts[p] += int(row["pageviews"])
    return {"status": "partial", "start": period.get("start"), "end": period.get("end"),
            "platform_pageviews": counts, "note": "Lower bounds from returned top referrers; zero is not evidence of absence."}

def cloudflare_query(token, zone, start, end, clauses):
    base = ('datetime_geq: ' + json.dumps(start) + ', datetime_lt: ' + json.dumps(end)
            + ', requestSource: "eyeball", clientRequestHTTPHost: "glassesresearch.org"')
    parts = []
    for i, clause in enumerate(clauses):
        parts.append(f'q{i}: httpRequestsAdaptiveGroups(limit: 1, filter: {{{base}, {clause}}}) {{ count }}')
    query = "{ viewer { zones(filter: {zoneTag: " + json.dumps(zone) + "}) {" + " ".join(parts) + "} } }"
    response = requests.post("https://api.cloudflare.com/client/v4/graphql",
                             headers={"Authorization": "Bearer " + token},
                             json={"query": query}, timeout=35)
    if not response.ok:
        return {"status": "unavailable", "reason": f"HTTP {response.status_code}", "counts": None}
    data = response.json()
    if data.get("errors"):
        return {"status": "unavailable", "reason": "GraphQL rejected query; check plan, permissions or schema", "counts": None}
    zones = data.get("data", {}).get("viewer", {}).get("zones", [])
    if len(zones) != 1:
        return {"status": "unavailable", "reason": "No matching zone", "counts": None}
    result = []
    for i in range(len(clauses)):
        rows = zones[0].get(f"q{i}")
        if not isinstance(rows, list) or len(rows) > 1:
            return {"status": "unavailable", "reason": "Unexpected aggregate response", "counts": None}
        result.append(int(rows[0]["count"]) if rows else 0)
    return {"status": "observed", "counts": result}

def edge_metrics(start, end):
    token = os.getenv("CLOUDFLARE_API_TOKEN", "").strip()
    zone = os.getenv("CLOUDFLARE_ZONE_ID", "").strip()
    sources = {
        "crawler_requests": {bot: "userAgent_like: " + json.dumps("%" + bot + "%") for bot in BOTS},
        "referrer_requests": {p: "OR: [" + ", ".join(
            '{clientRefererHost: ' + json.dumps(d) + '}, {clientRefererHost_like: ' + json.dumps("%." + d) + "}"
            for d in domains) + "]" for p, domains in REFS.items()}
    }
    output = {}
    for name, clauses in sources.items():
        if not token or not zone:
            result = {"status": "unavailable", "reason": "Missing configured credentials", "counts": None}
        else:
            try:
                result = cloudflare_query(token, zone, start, end, list(clauses.values()))
            except (requests.RequestException, ValueError, KeyError, TypeError):
                result = {"status": "unavailable", "reason": "Transport or response decoding error", "counts": None}
        if result["counts"] is not None:
            result["counts"] = dict(zip(clauses, result["counts"]))
        output[name] = result
    return output

def export_metrics(path):
    # Explicitly normalized totals, not raw user exports. Preserve date window and
    # attribution; missing inputs are null, never zero. Do not sum across sources.
    payload = json.loads(path.read_text()) if path and path.exists() else {}
    result = {}
    for key, unit in EXPORTS.items():
        item = payload.get(key)
        if item is None:
            result[key] = {"status": "awaiting_export", "unit": unit, "total": None}
            continue
        if not isinstance(item.get("total"), int) or isinstance(item["total"], bool) or item["total"] < 0:
            raise ValueError(f"{key}: expected nonnegative integer total")
        start = datetime.strptime(item["start"], "%Y-%m-%d")
        end = datetime.strptime(item["end"], "%Y-%m-%d")
        if end < start:
            raise ValueError(f"{key}: reversed date range")
        result[key] = {"status": "provided_export", "unit": unit, "total": item["total"],
                       "start": item["start"], "end": item["end"]}
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exports", type=Path)
    parser.add_argument("--output", type=Path, default=Path("build/agentic-discovery.json"))
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(days=7)
    iso = lambda d: d.isoformat().replace("+00:00", "Z")
    latest = json.loads((ROOT / "analytics/latest.json").read_text())
    report = {"schema_version": 1, "generated_at": iso(end), "edge_window": {"start": iso(start), "end": iso(end)},
              "browser_referrals": browser_referrals(latest),
              "edge": {"status": "not_requested"} if args.offline else edge_metrics(iso(start), iso(end)),
              "publisher_exports": export_metrics(args.exports),
              "crawler_roles": BOTS, "limitations": [
                  "Crawler user agents are self-reported; request counts are sampled estimates, not citations or people.",
                  "Edge referral counts include requests, not visits; direct or stripped referrals are not measured.",
                  "Browser referrers are lower bounds from a limited report; no UTM capture is claimed.",
                  "Google AI impressions are not citation counts; publisher exports are not automatically fetched.",
                  "No platform-wide citation totals are inferred from controlled experiments."]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
