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

SCHEMA_VERSION = 1
SERIES = Path("analytics") / "series"


def load_month(month: str) -> dict:
    path = SERIES / f"{month}.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("schema_version") == SCHEMA_VERSION:
                return data
        except Exception:
            pass
    return {
        "schema_version": SCHEMA_VERSION,
        "month": month,
        "updated_at": None,
        "google_search_console": {"days": {}, "summary": {}},
        "cloudflare": {"days": {}, "summary": {}},
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


def collect_gsc_day() -> tuple[str | None, dict | None, str | None]:
    token, site, error = gsc_client()
    if error:
        return None, None, error
    day = date.today() - timedelta(days=2)
    try:
        rows = gsc_query(token, site, day, day).get("rows", [])
        total = rows[0] if rows else {}
        record = {
            "date": day.isoformat(),
            "clicks": float(total.get("clicks", 0)),
            "impressions": float(total.get("impressions", 0)),
            "ctr": float(total.get("ctr", 0)),
            "position": float(total.get("position", 0)),
            "top_queries": gsc_rows(token, site, day, "query"),
            "top_pages": gsc_rows(token, site, day, "page"),
        }
        return day.isoformat(), record, None
    except Exception as exc:
        return day.isoformat(), None, str(exc)


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


def write_record(source: str, day_key: str, record: dict) -> Path:
    month = day_key[:7]
    data = load_month(month)
    data[source]["days"][day_key] = record
    if source == "google_search_console":
        data[source]["summary"] = summarize_gsc(data[source]["days"])
    else:
        data[source]["summary"] = summarize_cf(data[source]["days"])
    data["updated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    SERIES.mkdir(parents=True, exist_ok=True)
    path = SERIES / f"{month}.json"
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def update_index() -> None:
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
            }
        )
    index = {
        "schema_version": SCHEMA_VERSION,
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "months": months,
    }
    (SERIES / "index.json").write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    SERIES.mkdir(parents=True, exist_ok=True)
    successes = 0
    g_day, g_record, g_error = collect_gsc_day()
    if g_record:
        write_record("google_search_console", g_day, g_record)
        successes += 1
    elif g_error:
        print(f"Long-range GSC retention unavailable for {g_day}: {g_error}", file=sys.stderr)

    c_day, c_record, c_error = collect_cf_day()
    if c_record:
        write_record("cloudflare", c_day, c_record)
        successes += 1
    elif c_error:
        print(f"Long-range Cloudflare retention unavailable for {c_day}: {c_error}", file=sys.stderr)

    update_index()
    print(f"Long-range analytics retention updated; sources recorded: {successes}/2")
    return 0 if successes else 1


if __name__ == "__main__":
    sys.exit(main())
