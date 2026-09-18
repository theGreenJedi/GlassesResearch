#!/usr/bin/env python3
"""Cloudflare Web Analytics / RUM collector.

This module deliberately keeps browser-side Web Analytics separate from
Cloudflare edge HTTP analytics. RUM is account-scoped and records page loads
reported by the browser beacon rather than every request reaching the zone.
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

import requests

GRAPHQL_ENDPOINT = "https://api.cloudflare.com/client/v4/graphql"
API_ENDPOINT = "https://api.cloudflare.com/client/v4"


class CloudflareRumError(RuntimeError):
    pass


def _headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _graphql(token: str, query: str, variables: dict) -> dict:
    response = requests.post(
        GRAPHQL_ENDPOINT,
        headers=_headers(token),
        json={"query": query, "variables": variables},
        timeout=45,
    )
    response.raise_for_status()
    body = response.json()
    if body.get("errors"):
        raise CloudflareRumError(
            "; ".join(error.get("message", "GraphQL error") for error in body["errors"])
        )
    return body.get("data", {})


def _zone_metadata(token: str, zone_id: str) -> tuple[str, str]:
    """Return account ID and zone hostname using the already-configured zone."""
    configured_account = os.getenv("CLOUDFLARE_ACCOUNT_ID", "").strip()
    configured_host = os.getenv("CLOUDFLARE_ANALYTICS_HOST", "").strip()

    response = requests.get(
        f"{API_ENDPOINT}/zones/{zone_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if response.ok:
        body = response.json()
        result = body.get("result") or {}
        account = result.get("account") or {}
        account_id = configured_account or str(account.get("id") or "").strip()
        host = configured_host or str(result.get("name") or "").strip()
        if account_id and host:
            return account_id, host

    if configured_account and configured_host:
        return configured_account, configured_host

    detail = ""
    try:
        body = response.json()
        errors = body.get("errors") or []
        detail = "; ".join(str(item.get("message", "")) for item in errors if item.get("message"))
    except Exception:
        detail = response.text[:300]
    raise CloudflareRumError(
        "unable to resolve Cloudflare account/host from the configured zone"
        + (f": {detail}" if detail else "")
        + "; configure CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_ANALYTICS_HOST if the token lacks Zone Read"
    )


def _rum_query(
    token: str,
    account_id: str,
    host: str,
    start: str,
    end: str,
    *,
    bot_filter: bool = True,
) -> dict:
    bot_clause = "bot: 0" if bot_filter else ""
    query = f"""query WebAnalytics(
      $accountTag: string,
      $start: Time,
      $end: Time,
      $host: string
    ) {{
      viewer {{
        accounts(filter: {{accountTag: $accountTag}}) {{
          totals: rumPageloadEventsAdaptiveGroups(
            limit: 1
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
          }}
          paths: rumPageloadEventsAdaptiveGroups(
            limit: 25
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ requestPath }}
          }}
          referrers: rumPageloadEventsAdaptiveGroups(
            limit: 20
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ refererHost }}
          }}
          countries: rumPageloadEventsAdaptiveGroups(
            limit: 20
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ countryName }}
          }}
          devices: rumPageloadEventsAdaptiveGroups(
            limit: 15
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ deviceType }}
          }}
          browsers: rumPageloadEventsAdaptiveGroups(
            limit: 15
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ userAgentBrowser }}
          }}
          operatingSystems: rumPageloadEventsAdaptiveGroups(
            limit: 15
            orderBy: [count_DESC]
            filter: {{
              datetime_geq: $start
              datetime_lt: $end
              requestHost: $host
              {bot_clause}
            }}
          ) {{
            count
            sum {{ visits }}
            dimensions {{ userAgentOS }}
          }}
        }}
      }}
    }}"""
    variables = {
        "accountTag": account_id,
        "start": start,
        "end": end,
        "host": host,
    }
    data = _graphql(token, query, variables)
    accounts = data.get("viewer", {}).get("accounts", [])
    if not accounts:
        raise CloudflareRumError("Cloudflare returned no matching account for Web Analytics")
    return accounts[0]


def _metric_rows(rows: list[dict], dimension: str, key: str) -> list[dict]:
    result = []
    for row in rows or []:
        result.append(
            {
                key: row.get("dimensions", {}).get(dimension) or "",
                "pageviews": int(row.get("count", 0)),
                "visits": int(row.get("sum", {}).get("visits", 0)),
            }
        )
    return result


def rum_period(token: str, zone_id: str, hours: int) -> dict:
    account_id, host = _zone_metadata(token, zone_id)
    end_dt = datetime.now(timezone.utc).replace(microsecond=0)
    start_dt = end_dt - timedelta(hours=hours)
    start = start_dt.isoformat().replace("+00:00", "Z")
    end = end_dt.isoformat().replace("+00:00", "Z")

    bot_filter_applied = True
    try:
        raw = _rum_query(token, account_id, host, start, end, bot_filter=True)
    except CloudflareRumError as exc:
        # Older/plan-specific schemas may omit the bot field. RUM still comes
        # from the browser beacon, so fall back rather than losing the dataset.
        if "bot" not in str(exc).lower():
            raise
        raw = _rum_query(token, account_id, host, start, end, bot_filter=False)
        bot_filter_applied = False

    totals = (raw.get("totals") or [{}])[0]
    return {
        "start": start_dt.isoformat(),
        "end": end_dt.isoformat(),
        "host": host,
        "pageviews": int(totals.get("count", 0)),
        "visits": int(totals.get("sum", {}).get("visits", 0)),
        "bot_filter_applied": bot_filter_applied,
        "paths": _metric_rows(raw.get("paths", []), "requestPath", "path"),
        "referrers": _metric_rows(raw.get("referrers", []), "refererHost", "referrer"),
        "countries": _metric_rows(raw.get("countries", []), "countryName", "country"),
        "devices": _metric_rows(raw.get("devices", []), "deviceType", "device"),
        "browsers": _metric_rows(raw.get("browsers", []), "userAgentBrowser", "browser"),
        "operating_systems": _metric_rows(
            raw.get("operatingSystems", []), "userAgentOS", "operating_system"
        ),
    }


def rum_day(token: str, zone_id: str, day_start: datetime) -> dict:
    """Collect an exact UTC day for long-range retention."""
    if day_start.tzinfo is None:
        day_start = day_start.replace(tzinfo=timezone.utc)
    end = day_start + timedelta(days=1)
    account_id, host = _zone_metadata(token, zone_id)
    start_s = day_start.isoformat().replace("+00:00", "Z")
    end_s = end.isoformat().replace("+00:00", "Z")

    bot_filter_applied = True
    try:
        raw = _rum_query(token, account_id, host, start_s, end_s, bot_filter=True)
    except CloudflareRumError as exc:
        if "bot" not in str(exc).lower():
            raise
        raw = _rum_query(token, account_id, host, start_s, end_s, bot_filter=False)
        bot_filter_applied = False

    totals = (raw.get("totals") or [{}])[0]
    return {
        "date": day_start.date().isoformat(),
        "utc_window": {"start": day_start.isoformat(), "end": end.isoformat()},
        "host": host,
        "pageviews": int(totals.get("count", 0)),
        "visits": int(totals.get("sum", {}).get("visits", 0)),
        "bot_filter_applied": bot_filter_applied,
        "top_paths": _metric_rows(raw.get("paths", []), "requestPath", "path"),
        "top_referrers": _metric_rows(raw.get("referrers", []), "refererHost", "referrer"),
        "top_countries": _metric_rows(raw.get("countries", []), "countryName", "country"),
        "top_devices": _metric_rows(raw.get("devices", []), "deviceType", "device"),
    }
