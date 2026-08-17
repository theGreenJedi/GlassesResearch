#!/usr/bin/env python3
"""Build a page/query Search Console opportunity report for evidence-led optimization."""
from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import quote

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

OUT = Path("analytics")


def token() -> str:
    info = json.loads(os.environ["GOOGLE_SEARCH_CONSOLE_CREDENTIALS"])
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    creds.refresh(Request())
    return creds.token


def query_rows(access_token: str, site: str, start: date, end: date) -> list[dict]:
    endpoint = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + quote(site, safe="")
        + "/searchAnalytics/query"
    )
    response = requests.post(
        endpoint,
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "type": "web",
            "dataState": "final",
            "dimensions": ["page", "query"],
            "rowLimit": 25000,
        },
        timeout=45,
    )
    response.raise_for_status()
    return response.json().get("rows", [])


def main() -> int:
    site = os.environ["GOOGLE_SEARCH_CONSOLE_SITE_URL"].strip()
    end = date.today() - timedelta(days=2)
    start = end - timedelta(days=27)
    rows = []
    for row in query_rows(token(), site, start, end):
        keys = row.get("keys") or ["", ""]
        rows.append({
            "page": keys[0],
            "query": keys[1],
            "clicks": float(row.get("clicks", 0)),
            "impressions": float(row.get("impressions", 0)),
            "ctr": float(row.get("ctr", 0)),
            "position": float(row.get("position", 0)),
        })

    # Prioritize relevant queries already close enough that better content,
    # titles, internal links, and external citations could plausibly move them.
    opportunities = sorted(
        (r for r in rows if r["impressions"] > 0 and r["position"] <= 30),
        key=lambda r: (r["position"] > 10, -r["impressions"], r["position"]),
    )

    payload = {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "rows": rows,
        "opportunities": opportunities,
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "search-opportunities.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# GlassesResearch Search Opportunities",
        "",
        f"Google Search Console page/query pairs for **{start.isoformat()} → {end.isoformat()}**.",
        "",
        "> This is an evidence tool, not a keyword-chasing list. Improve a page only when the query genuinely matches the research the page should contain.",
        "",
        "## Page-one and near-page-one opportunities",
        "",
        "| Page | Query | Impressions | Clicks | CTR | Position |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for r in opportunities[:50]:
        page = r["page"].replace("|", "\\|")
        query = r["query"].replace("|", "\\|")
        lines.append(f"| {page} | {query} | {r['impressions']:g} | {r['clicks']:g} | {r['ctr']*100:.2f}% | {r['position']:.1f} |")
    if not opportunities:
        lines.append("| _No qualifying rows yet_ | | | | | |")
    lines += [
        "",
        "## How to use this report",
        "",
        "1. Prefer pages already ranking in positions 4–20 with meaningful impressions.",
        "2. Confirm the query matches the page's real subject before changing anything.",
        "3. Improve evidence, clarity, title/description, and internal links rather than adding filler.",
        "4. Re-measure after Google has had time to recrawl and retest the page.",
        "",
    ]
    (OUT / "search-opportunities.md").write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
