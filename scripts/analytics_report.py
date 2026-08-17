#!/usr/bin/env python3
"""Generate a single GlassesResearch analytics snapshot.

Inputs come from GitHub Actions secrets/variables.  Search Console is the
primary discovery signal. Cloudflare HTTP analytics is included as a secondary
infrastructure signal and is deliberately labelled as such so request traffic
is never mistaken for human readership.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

import requests

OUT = Path("analytics")
HISTORY = OUT / "history"


def pct_delta(current: float, previous: float):
    if previous == 0:
        return None
    return (current - previous) / previous * 100.0


def fmt_delta(value):
    if value is None:
        return "n/a"
    return f"{value:+.1f}%"


def gsc_client():
    raw = os.getenv("GOOGLE_SEARCH_CONSOLE_CREDENTIALS", "").strip()
    site = os.getenv("GOOGLE_SEARCH_CONSOLE_SITE_URL", "").strip()
    if not raw or not site:
        return None, site, "credentials/site variable not configured"
    try:
        from google.auth.transport.requests import Request
        from google.oauth2 import service_account
        info = json.loads(raw)
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
        )
        creds.refresh(Request())
        return creds.token, site, None
    except Exception as exc:
        return None, site, f"authentication failed: {exc}"


def gsc_query(token, site, start, end, dimensions=None, row_limit=25000):
    endpoint = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + quote(site, safe="")
        + "/searchAnalytics/query"
    )
    payload = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "type": "web",
        "dataState": "final",
        "rowLimit": row_limit,
    }
    if dimensions:
        payload["dimensions"] = dimensions
    r = requests.post(
        endpoint,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=45,
    )
    r.raise_for_status()
    return r.json()


def gsc_period(token, site, start, end):
    total_rows = gsc_query(token, site, start, end).get("rows", [])
    total = total_rows[0] if total_rows else {}
    result = {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "clicks": float(total.get("clicks", 0)),
        "impressions": float(total.get("impressions", 0)),
        "ctr": float(total.get("ctr", 0)),
        "position": float(total.get("position", 0)),
    }
    for dimension, key, limit in [
        ("query", "top_queries", 25),
        ("page", "top_pages", 25),
        ("country", "countries", 15),
        ("device", "devices", 10),
    ]:
        rows = gsc_query(token, site, start, end, [dimension], limit).get("rows", [])
        result[key] = [
            {
                dimension: (row.get("keys") or [""])[0],
                "clicks": float(row.get("clicks", 0)),
                "impressions": float(row.get("impressions", 0)),
                "ctr": float(row.get("ctr", 0)),
                "position": float(row.get("position", 0)),
            }
            for row in rows
        ]
    return result


def collect_gsc():
    token, site, error = gsc_client()
    if error:
        return {"available": False, "error": error}
    # Google's final Search Console data normally trails real time. Query
    # through two days ago so comparisons are made from final data only.
    end = date.today() - timedelta(days=2)
    current_start = end - timedelta(days=6)
    previous_end = current_start - timedelta(days=1)
    previous_start = previous_end - timedelta(days=6)
    month_start = end - timedelta(days=27)
    try:
        current = gsc_period(token, site, current_start, end)
        previous = gsc_period(token, site, previous_start, previous_end)
        month = gsc_period(token, site, month_start, end)
        return {
            "available": True,
            "property": site,
            "latest_final_date": end.isoformat(),
            "current_7d": current,
            "previous_7d": previous,
            "rolling_28d": month,
        }
    except Exception as exc:
        return {"available": False, "error": str(exc), "property": site}


def cf_query(token, zone, start, end):
    query = """query Analytics($zoneTag: string, $filter: filter) {
      viewer { zones(filter: {zoneTag: $zoneTag}) {
        totals: httpRequestsAdaptiveGroups(limit: 1, filter: $filter) {
          count sum { visits edgeResponseBytes }
        }
        countries: httpRequestsAdaptiveGroups(limit: 15, filter: $filter, orderBy: [count_DESC]) {
          count sum { visits } dimensions { clientCountryName }
        }
        paths: httpRequestsAdaptiveGroups(limit: 25, filter: $filter, orderBy: [count_DESC]) {
          count sum { visits } dimensions { clientRequestPath }
        }
        userAgents: httpRequestsAdaptiveGroups(limit: 25, filter: $filter, orderBy: [count_DESC]) {
          count sum { visits } dimensions { userAgent }
        }
      }}
    }"""
    payload = {
        "query": query,
        "variables": {
            "zoneTag": zone,
            "filter": {
                "datetime_geq": start,
                "datetime_lt": end,
                "requestSource": "eyeball",
            },
        },
    }
    r = requests.post(
        "https://api.cloudflare.com/client/v4/graphql",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=45,
    )
    r.raise_for_status()
    body = r.json()
    if body.get("errors"):
        raise RuntimeError("; ".join(e.get("message", "GraphQL error") for e in body["errors"]))
    zones = body.get("data", {}).get("viewer", {}).get("zones", [])
    if not zones:
        raise RuntimeError("Cloudflare returned no matching zone")
    return zones[0]


def cf_period(token, zone, hours):
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(hours=hours)
    z = cf_query(token, zone, start.isoformat().replace("+00:00", "Z"), end.isoformat().replace("+00:00", "Z"))
    totals = (z.get("totals") or [{}])[0]
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "requests": int(totals.get("count", 0)),
        "visits": int(totals.get("sum", {}).get("visits", 0)),
        "bytes": int(totals.get("sum", {}).get("edgeResponseBytes", 0)),
        "countries": [
            {
                "country": r.get("dimensions", {}).get("clientCountryName") or "unknown",
                "requests": int(r.get("count", 0)),
                "visits": int(r.get("sum", {}).get("visits", 0)),
            }
            for r in z.get("countries", [])
        ],
        "paths": [
            {
                "path": r.get("dimensions", {}).get("clientRequestPath") or "",
                "requests": int(r.get("count", 0)),
                "visits": int(r.get("sum", {}).get("visits", 0)),
            }
            for r in z.get("paths", [])
        ],
        "user_agents": [
            {
                "user_agent": r.get("dimensions", {}).get("userAgent") or "",
                "requests": int(r.get("count", 0)),
                "visits": int(r.get("sum", {}).get("visits", 0)),
            }
            for r in z.get("userAgents", [])
        ],
    }


def collect_cloudflare():
    token = os.getenv("CLOUDFLARE_API_TOKEN", "").strip()
    zone = os.getenv("CLOUDFLARE_ZONE_ID", "").strip()
    if not token or not zone:
        return {"available": False, "error": "token/zone variable not configured"}
    try:
        return {
            "available": True,
            "rolling_24h": cf_period(token, zone, 24),
            "rolling_7d": cf_period(token, zone, 24 * 7),
            "note": "HTTP edge analytics; includes automated clients and is not a human-reader count.",
        }
    except Exception as exc:
        # Never prevent the Search Console report from being generated just
        # because the Cloudflare token has lost analytics.read permission.
        return {"available": False, "error": str(exc)}


def md_table(rows, key):
    if not rows:
        return "_No rows yet._\n"
    out = ["| Item | Clicks | Impressions | CTR | Position |", "|---|---:|---:|---:|---:|"]
    for r in rows[:10]:
        item = str(r.get(key, "")).replace("|", "\\|")
        out.append(
            f"| {item} | {r['clicks']:g} | {r['impressions']:g} | {r['ctr']*100:.2f}% | {r['position']:.1f} |"
        )
    return "\n".join(out) + "\n"


def render(report):
    generated = report["generated_at"]
    lines = [
        "# GlassesResearch Analytics — Latest",
        "",
        f"Generated automatically: **{generated}**",
        "",
        "> **Interpretation rule:** Google Search Console is the primary external-discovery signal. Cloudflare HTTP traffic is infrastructure traffic and must not be treated as a count of human readers.",
        "",
    ]
    g = report["google_search_console"]
    if g.get("available"):
        cur, prev, month = g["current_7d"], g["previous_7d"], g["rolling_28d"]
        lines += [
            "## Executive summary",
            "",
            f"- **Google, latest final 7 days ({cur['start']} → {cur['end']}):** {cur['impressions']:g} impressions, {cur['clicks']:g} clicks, {cur['ctr']*100:.2f}% CTR, average position {cur['position']:.1f}.",
            f"- **7-day change:** impressions {fmt_delta(pct_delta(cur['impressions'], prev['impressions']))}; clicks {fmt_delta(pct_delta(cur['clicks'], prev['clicks']))}.",
            f"- **Rolling 28 days:** {month['impressions']:g} impressions, {month['clicks']:g} clicks, {month['ctr']*100:.2f}% CTR, average position {month['position']:.1f}.",
        ]
        if cur["clicks"] > 0 and prev["clicks"] == 0:
            lines.append("- **Milestone:** organic Google clicks appeared after a previous zero-click week.")
        lines += ["", "## Google — top queries", "", md_table(cur["top_queries"], "query"), "## Google — top pages", "", md_table(cur["top_pages"], "page")]
    else:
        lines += ["## Executive summary", "", f"- **Google Search Console unavailable:** {g.get('error', 'unknown error')}", ""]

    c = report["cloudflare"]
    lines += ["## Cloudflare edge traffic", ""]
    if c.get("available"):
        d = c["rolling_24h"]
        lines += [
            f"- Rolling 24h: **{d['requests']:,} requests**, **{d['visits']:,} HTTP visits**, **{d['bytes']/1024/1024:.1f} MB** served.",
            "- These figures can contain bots, scanners, crawlers and owner/development traffic; do **not** equate them with unique human readers.",
            "",
            "### Top countries by request count",
            "",
            "| Country | Requests | HTTP visits |",
            "|---|---:|---:|",
        ]
        for row in d["countries"][:10]:
            lines.append(f"| {row['country']} | {row['requests']:,} | {row['visits']:,} |")
        lines.append("")
    else:
        lines += [
            f"- **Cloudflare API unavailable:** {c.get('error', 'unknown error')}",
            "- The report still succeeds with Search Console data. Restore a token with Zone Analytics Read permission to re-enable this section.",
            "",
        ]

    lines += [
        "## What to watch",
        "",
        "1. First and subsequent organic Google clicks.",
        "2. Queries/pages moving toward average position 10 or better.",
        "3. Impressions growing week-over-week without sacrificing relevance.",
        "4. Cloudflare traffic only as supporting infrastructure/security context, not as readership proof.",
        "",
        "_This file is generated by `.github/workflows/analytics-report.yml`._",
    ]
    return "\n".join(lines) + "\n"


def main():
    report = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "google_search_console": collect_gsc(),
        "cloudflare": collect_cloudflare(),
    }
    OUT.mkdir(exist_ok=True)
    HISTORY.mkdir(parents=True, exist_ok=True)
    (OUT / "latest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (OUT / "latest.md").write_text(render(report), encoding="utf-8")
    stamp = datetime.now(timezone.utc).date().isoformat()
    (HISTORY / f"{stamp}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print((OUT / "latest.md").read_text(encoding="utf-8"))
    # Only fail when both sources are unavailable; partial reports are useful.
    if not report["google_search_console"].get("available") and not report["cloudflare"].get("available"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
