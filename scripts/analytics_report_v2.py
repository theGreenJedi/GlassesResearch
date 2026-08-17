#!/usr/bin/env python3
"""Generate the consolidated GlassesResearch analytics snapshot.

Google Search Console is the primary external-discovery signal. Cloudflare Zone
Analytics is supporting infrastructure telemetry and must not be interpreted as
human readership.
"""
from __future__ import annotations

import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

OUT = Path("analytics")
HISTORY = OUT / "history"


def delta(cur, prev):
    return None if prev == 0 else (cur - prev) / prev * 100.0


def fmt_delta(v):
    return "n/a" if v is None else f"{v:+.1f}%"


def gsc_token():
    raw = os.environ["GOOGLE_SEARCH_CONSOLE_CREDENTIALS"]
    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    creds.refresh(Request())
    return creds.token


def gsc_query(token, site, start, end, dimension=None, row_limit=25000):
    url = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + quote(site, safe="")
        + "/searchAnalytics/query"
    )
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "type": "web",
        "dataState": "final",
        "rowLimit": row_limit,
    }
    if dimension:
        body["dimensions"] = [dimension]
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}"},
        json=body,
        timeout=45,
    )
    r.raise_for_status()
    return r.json().get("rows", [])


def gsc_period(token, site, start, end):
    totals = gsc_query(token, site, start, end, row_limit=1)
    t = totals[0] if totals else {}
    result = {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "clicks": float(t.get("clicks", 0)),
        "impressions": float(t.get("impressions", 0)),
        "ctr": float(t.get("ctr", 0)),
        "position": float(t.get("position", 0)),
    }
    for dimension, key, limit in [
        ("query", "top_queries", 25),
        ("page", "top_pages", 25),
        ("country", "countries", 15),
        ("device", "devices", 10),
    ]:
        rows = gsc_query(token, site, start, end, dimension, limit)
        result[key] = [
            {
                dimension: (r.get("keys") or [""])[0],
                "clicks": float(r.get("clicks", 0)),
                "impressions": float(r.get("impressions", 0)),
                "ctr": float(r.get("ctr", 0)),
                "position": float(r.get("position", 0)),
            }
            for r in rows
        ]
    return result


def collect_gsc():
    site = os.getenv("GOOGLE_SEARCH_CONSOLE_SITE_URL", "").strip()
    raw = os.getenv("GOOGLE_SEARCH_CONSOLE_CREDENTIALS", "").strip()
    if not site or not raw:
        return {"available": False, "error": "credentials/site variable not configured"}
    try:
        token = gsc_token()
        end = date.today() - timedelta(days=2)
        cur_start = end - timedelta(days=6)
        prev_end = cur_start - timedelta(days=1)
        prev_start = prev_end - timedelta(days=6)
        month_start = end - timedelta(days=27)
        return {
            "available": True,
            "property": site,
            "latest_final_date": end.isoformat(),
            "current_7d": gsc_period(token, site, cur_start, end),
            "previous_7d": gsc_period(token, site, prev_start, prev_end),
            "rolling_28d": gsc_period(token, site, month_start, end),
        }
    except Exception as exc:
        return {"available": False, "error": str(exc), "property": site}


def cf_rest_period(token, zone, hours):
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(hours=hours)
    url = f"https://api.cloudflare.com/client/v4/zones/{zone}/analytics/dashboard"
    r = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
        params={
            "since": start.isoformat().replace("+00:00", "Z"),
            "until": end.isoformat().replace("+00:00", "Z"),
            "continuous": "false",
        },
        timeout=45,
    )
    r.raise_for_status()
    payload = r.json()
    if not payload.get("success", False):
        raise RuntimeError(json.dumps(payload.get("errors", [])))
    totals = payload.get("result", {}).get("totals", {})
    requests_block = totals.get("requests", {})
    bandwidth = totals.get("bandwidth", {})
    uniques = totals.get("uniques", {})
    pageviews = totals.get("pageviews", {})
    countries = requests_block.get("country", {}) or {}
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "requests": int(requests_block.get("all", 0) or 0),
        "cached_requests": int(requests_block.get("cached", 0) or 0),
        "uncached_requests": int(requests_block.get("uncached", 0) or 0),
        "bytes": int(bandwidth.get("all", 0) or 0),
        "cached_bytes": int(bandwidth.get("cached", 0) or 0),
        "uniques": int(uniques.get("all", 0) or 0),
        "pageviews": int(pageviews.get("all", 0) or 0),
        "countries": sorted(
            ({"country": k, "requests": int(v)} for k, v in countries.items()),
            key=lambda x: x["requests"],
            reverse=True,
        )[:15],
        "source": "Cloudflare Zone Analytics REST API",
    }


def collect_cloudflare():
    token = os.getenv("CLOUDFLARE_API_TOKEN", "").strip()
    zone = os.getenv("CLOUDFLARE_ZONE_ID", "").strip()
    if not token or not zone:
        return {"available": False, "error": "token/zone variable not configured"}
    try:
        return {
            "available": True,
            "rolling_24h": cf_rest_period(token, zone, 24),
            "rolling_7d": cf_rest_period(token, zone, 24 * 7),
            "note": "Infrastructure telemetry; includes automated clients and owner/development traffic.",
        }
    except Exception as exc:
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
    lines = [
        "# GlassesResearch Analytics — Latest",
        "",
        f"Generated automatically: **{report['generated_at']}**",
        "",
        "> **Interpretation rule:** Google Search Console is the primary external-discovery signal. Cloudflare traffic is infrastructure telemetry and must not be treated as a count of human readers.",
        "",
        "## Executive summary",
        "",
    ]
    g = report["google_search_console"]
    if g.get("available"):
        cur, prev, month = g["current_7d"], g["previous_7d"], g["rolling_28d"]
        lines += [
            f"- **Google, latest final 7 days ({cur['start']} → {cur['end']}):** {cur['impressions']:g} impressions, {cur['clicks']:g} clicks, {cur['ctr']*100:.2f}% CTR, average position {cur['position']:.1f}.",
            f"- **7-day change:** impressions {fmt_delta(delta(cur['impressions'], prev['impressions']))}; clicks {fmt_delta(delta(cur['clicks'], prev['clicks']))}.",
            f"- **Rolling 28 days:** {month['impressions']:g} impressions, {month['clicks']:g} clicks, {month['ctr']*100:.2f}% CTR, average position {month['position']:.1f}.",
        ]
        if cur["clicks"] > 0 and prev["clicks"] == 0:
            lines.append("- **Milestone:** first organic Google clicks appeared after a zero-click prior week.")
        lines += ["", "## Google — top queries", "", md_table(cur["top_queries"], "query"), "## Google — top pages", "", md_table(cur["top_pages"], "page")]
    else:
        lines.append(f"- **Google Search Console unavailable:** {g.get('error', 'unknown error')}")

    c = report["cloudflare"]
    lines += ["", "## Cloudflare edge traffic", ""]
    if c.get("available"):
        d = c["rolling_24h"]
        cache_pct = (d["cached_requests"] / d["requests"] * 100.0) if d["requests"] else 0.0
        lines += [
            f"- Rolling 24h: **{d['requests']:,} requests**, **{d['uniques']:,} network uniques**, **{d['pageviews']:,} pageviews**, **{d['bytes']/1024/1024:.1f} MB** served.",
            f"- Cache: **{d['cached_requests']:,} requests ({cache_pct:.1f}%)** served from cache.",
            "- These figures may include bots, scanners, crawlers and owner/development traffic; do **not** equate them with unique human readers.",
            "",
            "### Top countries by request count",
            "",
            "| Country | Requests |",
            "|---|---:|",
        ]
        for row in d["countries"][:10]:
            lines.append(f"| {row['country']} | {row['requests']:,} |")
    else:
        lines.append(f"- **Cloudflare API unavailable:** {c.get('error', 'unknown error')}")

    lines += [
        "",
        "## What to watch",
        "",
        "1. First and subsequent organic Google clicks.",
        "2. Queries/pages moving toward average position 10 or better.",
        "3. Impressions growing week-over-week without sacrificing relevance.",
        "4. Cloudflare traffic only as supporting infrastructure/security context, not readership proof.",
        "",
        "_Generated by `.github/workflows/analytics-report.yml`._",
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
    return 0 if g_or_c(report) else 1


def g_or_c(report):
    return report["google_search_console"].get("available") or report["cloudflare"].get("available")


if __name__ == "__main__":
    raise SystemExit(main())
