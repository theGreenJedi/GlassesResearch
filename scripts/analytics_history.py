#!/usr/bin/env python3
"""Persist exact daily analytics into month-oriented long-range series files.

The regular analytics report is optimized for "what is happening now" and
contains rolling windows. This companion script stores exact source-day metrics
so requests such as "show the last five months" can be answered from compact,
versioned monthly files without re-querying every historical snapshot.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

from analytics_report import _cf_slice, gsc_client, gsc_query
from cloudflare_rum import rum_day

SCHEMA_VERSION = 1
SERIES = Path("analytics") / "series"


def load_month(month: str) -> dict:
    path = SERIES / f"{month}.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("schema_version") == SCHEMA_VERSION:
                data.setdefault("cloudflare_web_analytics", {"days": {}, "summary": {}})
                return data
        except Exception:
            pass
    return {
        "schema_version": SCHEMA_VERSION,
        "month": month,
        "updated_at": None,
        "google_search_console": {"days": {}, "summary": {}},
        "cloudflare": {"days": {}, "summary": {}},
        "cloudflare_web_analytics": {"days": {}, "summary": {}},
    }


def gsc_rows(token: str, site: str, day: date, dimension: str, limit: int = 25) -> list[dict]:
    rows = gsc_query(token, site, day, day, [dimension], limit).get("rows", [])
    out = []
    for row in rows:
        out.append(
            {
                dimension: (row.get("keys") or [""])[0],
                "clicks": float(row.get("clicks", 0)),
                "impressions": float(row.get("impressions", 0)),
                "ctr": float(row.get("ctr", 0)),
                "position": float(row.get("position", 0)),
            }
        )
    return out


def normalized_gsc_days(rows: list[dict], start: date, end: date) -> dict[str, dict]:
    """Use Google's date dimension for actual daily totals; absent days are unknown."""
    records = {}
    for row in rows:
        keys = row.get("keys") or []
        if not keys:
            raise ValueError("Search Console date-grouped row has no date key")
        key = str(keys[0])
        day = date.fromisoformat(key)
        if not start <= day <= end:
            raise ValueError(f"Search Console returned an out-of-range day: {key}")
        clicks = float(row.get("clicks", 0))
        impressions = float(row.get("impressions", 0))
        if clicks < 0 or impressions < 0:
            raise ValueError(f"Search Console returned negative totals: {key}")
        if key in records:
            raise ValueError(f"Search Console returned duplicate date: {key}")
        # Do not store an absent or zero-only response as a verified zero day.
        if clicks == 0 and impressions == 0:
            continue
        records[key] = {
            "date": key,
            "clicks": clicks,
            "impressions": impressions,
            "ctr": clicks / impressions if impressions else 0.0,
            "position": float(row.get("position", 0)),
        }
    return records


def collect_gsc_days() -> tuple[dict[str, dict] | None, date | None, date | None, str | None]:
    """Backfill the last 90 finalized days in one date-grouped query.

    A one-day query that returns no rows is NOT evidence of zero impressions.
    The same dates are revisited daily so delayed/finalized data can correct
    historical records, without dozens of per-day API calls.
    """
    token, site, error = gsc_client()
    if error:
        return None, None, None, error
    end = date.today() - timedelta(days=2)
    start = end - timedelta(days=89)
    try:
        rows = gsc_query(token, site, start, end, ["date"], 25000).get("rows", [])
        if not rows:
            return None, start, end, "no finalized date-grouped rows returned; previous history left unchanged"
        return normalized_gsc_days(rows, start, end), start, end, None
    except Exception as exc:
        return None, start, end, str(exc)


def replace_gsc_days(records: dict[str, dict], start: date, end: date) -> int:
    """Refresh daily totals and discard previously invented zero-day records.

    Preserve previously collected per-day query/page examples when present;
    backfilled days without examples carry no claim that there were none.
    """
    touched_months = {key[:7] for key in records}
    for path in SERIES.glob("20??-??.json"):
        month = path.stem
        if start.strftime("%Y-%m") <= month <= end.strftime("%Y-%m"):
            touched_months.add(month)
    updated = 0
    for month in sorted(touched_months):
        data = load_month(month)
        dates = data["google_search_console"].setdefault("days", {})
        for key in list(dates):
            if start.isoformat() <= key <= end.isoformat() and key not in records:
                del dates[key]  # Missing from Google's dated response: unknown, NOT zero.
                updated += 1
        for key, fresh in records.items():
            if not key.startswith(month + "-"):
                continue
            previous = dates.get(key, {})
            record = {
                **fresh,
                "top_queries": previous.get("top_queries", []),
                "top_pages": previous.get("top_pages", []),
            }
            if dates.get(key) != record:
                updated += 1
            dates[key] = record
        data["google_search_console"]["summary"] = summarize_gsc(dates)
        data["updated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        SERIES.mkdir(parents=True, exist_ok=True)
        (SERIES / f"{month}.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return updated


def reconcile_gsc(records: dict[str, dict]) -> dict | None:
    """Compare newly fetched exact daily totals with the independent 28d report."""
    latest = SERIES.parent / "latest.json"
    if not latest.exists():
        return None
    try:
        report = json.loads(latest.read_text(encoding="utf-8"))
        g = report.get("google_search_console", {})
        period = g.get("rolling_28d", {})
        if not g.get("available") or not period:
            return None
        start, end = period["start"], period["end"]
        dated = [row for key, row in records.items() if start <= key <= end]
        impressions = sum(row["impressions"] for row in dated)
        clicks = sum(row["clicks"] for row in dated)
        expected_impressions = float(period["impressions"])
        expected_clicks = float(period["clicks"])
        matches = impressions == expected_impressions and clicks == expected_clicks
        return {
            "status": "match" if matches else "mismatch",
            "start": start, "end": end,
            "daily_impressions": impressions, "reported_impressions": expected_impressions,
            "daily_clicks": clicks, "reported_clicks": expected_clicks,
            "days_with_reported_data": len(dated),
            "note": "Days absent from Google's date-grouped result are unknown, not verified zeros.",
        }
    except (KeyError, TypeError, ValueError, OSError) as exc:
        return {"status": "unavailable", "reason": str(exc)}


def collect_cf_day() -> tuple[str | None, dict | None, str | None]:
    token = os.getenv("CLOUDFLARE_API_TOKEN", "").strip()
    zone = os.getenv("CLOUDFLARE_ZONE_ID", "").strip()
    day = datetime.now(timezone.utc).date() - timedelta(days=1)
    if not token or not zone:
        return day.isoformat(), None, "token/zone variable not configured"
    start = datetime.combine(day, time.min, tzinfo=timezone.utc)
    end = start + timedelta(days=1)
    try:
        raw = _cf_slice(token, zone, start, end)
        countries = []
        for row in raw.get("countries", []):
            countries.append(
                {
                    "country": row.get("dimensions", {}).get("clientCountryName") or "unknown",
                    "requests": int(row.get("count", 0)),
                    "visits": int(row.get("sum", {}).get("visits", 0)),
                }
            )
        record = {
            "date": day.isoformat(),
            "utc_window": {"start": start.isoformat(), "end": end.isoformat()},
            "requests": int(raw.get("requests", 0)),
            "visits": int(raw.get("visits", 0)),
            "bytes": int(raw.get("bytes", 0)),
            "top_countries": countries,
        }
        return day.isoformat(), record, None
    except Exception as exc:
        return day.isoformat(), None, str(exc)


def summarize_gsc(days: dict[str, dict]) -> dict:
    records = [days[k] for k in sorted(days)]
    impressions = sum(float(r.get("impressions", 0)) for r in records)
    clicks = sum(float(r.get("clicks", 0)) for r in records)
    weighted_position_n = sum(float(r.get("position", 0)) * float(r.get("impressions", 0)) for r in records)
    return {
        "days_recorded": len(records),
        "first_date": records[0]["date"] if records else None,
        "last_date": records[-1]["date"] if records else None,
        "impressions": impressions,
        "clicks": clicks,
        "ctr": (clicks / impressions) if impressions else 0.0,
        "average_position_weighted_by_impressions": (weighted_position_n / impressions) if impressions else 0.0,
    }


def summarize_cf(days: dict[str, dict]) -> dict:
    records = [days[k] for k in sorted(days)]
    return {
        "days_recorded": len(records),
        "first_date": records[0]["date"] if records else None,
        "last_date": records[-1]["date"] if records else None,
        "requests": sum(int(r.get("requests", 0)) for r in records),
        "visits": sum(int(r.get("visits", 0)) for r in records),
        "bytes": sum(int(r.get("bytes", 0)) for r in records),
    }


def summarize_rum(days: dict[str, dict]) -> dict:
    records = [days[k] for k in sorted(days)]
    return {
        "days_recorded": len(records),
        "first_date": records[0]["date"] if records else None,
        "last_date": records[-1]["date"] if records else None,
        "pageviews": sum(int(r.get("pageviews", 0)) for r in records),
        "visits": sum(int(r.get("visits", 0)) for r in records),
    }


def write_record(source: str, day_key: str, record: dict) -> Path:
    month = day_key[:7]
    data = load_month(month)
    data[source]["days"][day_key] = record
    if source == "google_search_console":
        data[source]["summary"] = summarize_gsc(data[source]["days"])
    elif source == "cloudflare_web_analytics":
        data[source]["summary"] = summarize_rum(data[source]["days"])
    else:
        data[source]["summary"] = summarize_cf(data[source]["days"])
    data["updated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    SERIES.mkdir(parents=True, exist_ok=True)
    path = SERIES / f"{month}.json"
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def update_index(gsc_reconciliation: dict | None = None) -> None:
    months = []
    for path in sorted(SERIES.glob("20??-??.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        months.append(
            {
                "month": data.get("month"),
                "google": data.get("google_search_console", {}).get("summary", {}),
                "cloudflare": data.get("cloudflare", {}).get("summary", {}),
                "cloudflare_web_analytics": data.get("cloudflare_web_analytics", {}).get("summary", {}),
            }
        )
    index = {
        "schema_version": SCHEMA_VERSION,
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "months": months,
    }
    if gsc_reconciliation is not None:
        index["google_reconciliation"] = gsc_reconciliation
    (SERIES / "index.json").write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def collect_rum_day() -> tuple[str | None, dict | None, str | None]:
    token = os.getenv("CLOUDFLARE_API_TOKEN", "").strip()
    zone = os.getenv("CLOUDFLARE_ZONE_ID", "").strip()
    day = datetime.now(timezone.utc).date() - timedelta(days=1)
    if not token or not zone:
        return day.isoformat(), None, "token/zone variable not configured"
    start = datetime.combine(day, time.min, tzinfo=timezone.utc)
    try:
        return day.isoformat(), rum_day(token, zone, start), None
    except Exception as exc:
        return day.isoformat(), None, str(exc)


def main() -> int:
    SERIES.mkdir(parents=True, exist_ok=True)
    successes = 0
    g_records, g_start, g_end, g_error = collect_gsc_days()
    reconciliation = None
    if g_records is not None:
        changed = replace_gsc_days(g_records, g_start, g_end)
        reconciliation = reconcile_gsc(g_records)
        successes += 1
        print(f"Search Console date-grouped backfill: {len(g_records)} verified days, {changed} records changed")
        if reconciliation:
            print("Search Console 28-day reconciliation: " + json.dumps(reconciliation))
            if reconciliation["status"] != "match":
                print("::warning::Search Console daily history disagrees with rolling 28-day totals", file=sys.stderr)
    elif g_error:
        print(f"Long-range GSC retention unavailable: {g_error}", file=sys.stderr)

    c_day, c_record, c_error = collect_cf_day()
    if c_record:
        write_record("cloudflare", c_day, c_record)
        successes += 1
    elif c_error:
        print(f"Long-range Cloudflare retention unavailable for {c_day}: {c_error}", file=sys.stderr)

    r_day, r_record, r_error = collect_rum_day()
    if r_record:
        write_record("cloudflare_web_analytics", r_day, r_record)
        successes += 1
    elif r_error:
        print(f"Long-range Cloudflare Web Analytics retention unavailable for {r_day}: {r_error}", file=sys.stderr)

    update_index(reconciliation)
    print(f"Long-range analytics retention updated; sources recorded: {successes}/3")
    return 0 if successes else 1


if __name__ == "__main__":
    sys.exit(main())
