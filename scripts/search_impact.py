#!/usr/bin/env python3
"""Measure evidence-led search interventions against fixed Search Console baselines."""
from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

OUT = Path("analytics")
MANIFEST = OUT / "search-interventions.json"
SCHEMA_VERSION = 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="validate the intervention manifest without calling Search Console",
    )
    return parser.parse_args()


def load_manifest() -> dict:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"unsupported search intervention schema: {payload.get('schema_version')!r}")
    interventions = payload.get("interventions")
    if not isinstance(interventions, list) or not interventions:
        raise ValueError("search intervention manifest must contain at least one intervention")

    seen_ids: set[str] = set()
    for intervention in interventions:
        intervention_id = intervention.get("id")
        if not isinstance(intervention_id, str) or not intervention_id.strip():
            raise ValueError("every search intervention needs a stable id")
        if intervention_id in seen_ids:
            raise ValueError(f"duplicate search intervention id: {intervention_id}")
        seen_ids.add(intervention_id)

        changed = date.fromisoformat(intervention["date"])
        baseline_start = date.fromisoformat(intervention["baseline_start"])
        baseline_end = date.fromisoformat(intervention["baseline_end"])
        if baseline_start > baseline_end:
            raise ValueError(f"{intervention_id}: baseline_start is after baseline_end")
        if baseline_end >= changed:
            raise ValueError(f"{intervention_id}: baseline must end before the intervention date")

        post_days = int(intervention.get("post_days", 28))
        if post_days < 7 or post_days > 90:
            raise ValueError(f"{intervention_id}: post_days must be between 7 and 90")

        targets = intervention.get("targets")
        if not isinstance(targets, list) or not targets:
            raise ValueError(f"{intervention_id}: at least one target is required")
        for target in targets:
            page = target.get("page")
            queries = target.get("queries")
            if not isinstance(page, str) or not page.startswith("https://glassesresearch.org/"):
                raise ValueError(f"{intervention_id}: target page must be a canonical GlassesResearch URL")
            if not isinstance(queries, list) or not queries or not all(isinstance(q, str) and q.strip() for q in queries):
                raise ValueError(f"{intervention_id}: every target needs one or more exact queries")

    return payload


def token() -> str:
    info = json.loads(os.environ["GOOGLE_SEARCH_CONSOLE_CREDENTIALS"])
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    creds.refresh(Request())
    return creds.token


def query_rows(access_token: str, site: str, start: date, end: date, page: str) -> list[dict]:
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
            "dimensionFilterGroups": [
                {
                    "groupType": "and",
                    "filters": [
                        {
                            "dimension": "page",
                            "operator": "equals",
                            "expression": page,
                        }
                    ],
                }
            ],
            "rowLimit": 25000,
        },
        timeout=45,
    )
    response.raise_for_status()
    rows = []
    for row in response.json().get("rows", []):
        keys = row.get("keys") or [page, ""]
        rows.append(
            {
                "page": keys[0],
                "query": keys[1],
                "clicks": float(row.get("clicks", 0)),
                "impressions": float(row.get("impressions", 0)),
                "ctr": float(row.get("ctr", 0)),
                "position": float(row.get("position", 0)),
            }
        )
    return rows


def aggregate(rows: list[dict], queries: list[str]) -> dict:
    wanted = {q.strip().casefold() for q in queries}
    matched = [row for row in rows if row["query"].strip().casefold() in wanted]
    impressions = sum(row["impressions"] for row in matched)
    clicks = sum(row["clicks"] for row in matched)
    position = None
    if impressions > 0:
        position = sum(row["position"] * row["impressions"] for row in matched) / impressions
    return {
        "queries": queries,
        "matched_rows": len(matched),
        "clicks": clicks,
        "impressions": impressions,
        "ctr": clicks / impressions if impressions else 0.0,
        "position": position,
    }


def fmt_number(value: float) -> str:
    return f"{value:g}"


def fmt_ctr(value: float) -> str:
    return f"{value * 100:.2f}%"


def fmt_position(value: float | None) -> str:
    return "—" if value is None else f"{value:.1f}"


def build_report(manifest: dict, access_token: str, site: str) -> tuple[dict, str]:
    final_through = date.today() - timedelta(days=2)
    cache: dict[tuple[str, date, date], list[dict]] = {}

    def rows_for(page: str, start: date, end: date) -> list[dict]:
        key = (page, start, end)
        if key not in cache:
            cache[key] = query_rows(access_token, site, start, end, page)
        return cache[key]

    output_interventions = []
    for intervention in manifest["interventions"]:
        changed = date.fromisoformat(intervention["date"])
        baseline_start = date.fromisoformat(intervention["baseline_start"])
        baseline_end = date.fromisoformat(intervention["baseline_end"])
        post_days = int(intervention.get("post_days", 28))
        planned_post_end = changed + timedelta(days=post_days - 1)
        observed_post_end = min(final_through, planned_post_end)
        observed_days = max(0, (observed_post_end - changed).days + 1)
        post_complete = final_through >= planned_post_end

        target_results = []
        for target in intervention["targets"]:
            baseline = aggregate(
                rows_for(target["page"], baseline_start, baseline_end),
                target["queries"],
            )
            if observed_days:
                post = aggregate(
                    rows_for(target["page"], changed, observed_post_end),
                    target["queries"],
                )
            else:
                post = {
                    "queries": target["queries"],
                    "matched_rows": 0,
                    "clicks": 0.0,
                    "impressions": 0.0,
                    "ctr": 0.0,
                    "position": None,
                }

            comparison = None
            if post_complete:
                position_improvement = None
                if baseline["position"] is not None and post["position"] is not None:
                    position_improvement = baseline["position"] - post["position"]
                comparison = {
                    "impressions_change": post["impressions"] - baseline["impressions"],
                    "clicks_change": post["clicks"] - baseline["clicks"],
                    "ctr_change_points": (post["ctr"] - baseline["ctr"]) * 100,
                    "position_improvement": position_improvement,
                }

            target_results.append(
                {
                    **target,
                    "baseline": baseline,
                    "post": post,
                    "comparison": comparison,
                }
            )

        output_interventions.append(
            {
                "id": intervention["id"],
                "date": intervention["date"],
                "pull_request": intervention.get("pull_request"),
                "title": intervention.get("title"),
                "baseline_start": intervention["baseline_start"],
                "baseline_end": intervention["baseline_end"],
                "post_start": intervention["date"],
                "post_end_planned": planned_post_end.isoformat(),
                "post_end_observed": observed_post_end.isoformat() if observed_days else None,
                "post_days_planned": post_days,
                "post_days_observed": observed_days,
                "post_complete": post_complete,
                "targets": target_results,
            }
        )

    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "search_console_final_through": final_through.isoformat(),
        "principle": manifest.get("principle"),
        "interventions": output_interventions,
    }

    lines = [
        "# GlassesResearch Search Impact",
        "",
        f"Google Search Console finalized data through **{final_through.isoformat()}**.",
        "",
        "> This report measures evidence-led research changes. It is not a ranking target, keyword quota, or instruction to optimize irrelevant queries.",
        "",
    ]
    for intervention in output_interventions:
        lines += [
            f"## {intervention['id']} — PR #{intervention['pull_request']}",
            "",
            f"**{intervention['title']}**",
            "",
            f"Baseline: **{intervention['baseline_start']} → {intervention['baseline_end']}**. "
            f"Post window: **{intervention['post_start']} → {intervention['post_end_planned']}**.",
            "",
        ]
        if intervention["post_complete"]:
            lines.append("Status: **comparison ready** — the complete post-intervention window is finalized.")
        elif intervention["post_days_observed"]:
            lines.append(
                f"Status: **collecting** — {intervention['post_days_observed']}/{intervention['post_days_planned']} finalized post-intervention days available."
            )
        else:
            lines.append("Status: **waiting for finalized post-intervention Search Console data**.")
        lines += [
            "",
            "| Page / exact query | Baseline impressions | Baseline clicks | Baseline CTR | Baseline position | Post impressions | Post clicks | Post CTR | Post position |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for target in intervention["targets"]:
            query_label = ", ".join(f"`{q}`" for q in target["queries"])
            page_label = target["page"].removeprefix("https://glassesresearch.org") or "/"
            baseline = target["baseline"]
            post = target["post"]
            lines.append(
                f"| {page_label}<br>{query_label} | {fmt_number(baseline['impressions'])} | {fmt_number(baseline['clicks'])} | "
                f"{fmt_ctr(baseline['ctr'])} | {fmt_position(baseline['position'])} | {fmt_number(post['impressions'])} | "
                f"{fmt_number(post['clicks'])} | {fmt_ctr(post['ctr'])} | {fmt_position(post['position'])} |"
            )
        lines += [
            "",
            "Interpretation rule: do not judge the intervention until the planned post window is complete. A ranking change without useful impressions/clicks is not treated as success by itself.",
            "",
        ]

    return payload, "\n".join(lines)


def main() -> int:
    args = parse_args()
    manifest = load_manifest()
    if args.validate_only:
        print(f"validated {len(manifest['interventions'])} search intervention(s)")
        return 0

    site = os.environ["GOOGLE_SEARCH_CONSOLE_SITE_URL"].strip()
    payload, markdown = build_report(manifest, token(), site)
    OUT.mkdir(exist_ok=True)
    (OUT / "search-impact.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    (OUT / "search-impact.md").write_text(markdown + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
