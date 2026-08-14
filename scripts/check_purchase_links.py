#!/usr/bin/env python3
"""Check Glasses Finder purchase links and maintain a health ledger.

This checker intentionally does not delete or rewrite purchase-source records. It records
reachability/freshness separately so the public UI can suppress bad routes while preserving
history and a replacement queue can be reviewed before any canonical URL changes.
"""

from __future__ import annotations

import argparse
import json
import socket
import ssl
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PURCHASE_PATH = ROOT / "data" / "purchase-sources.json"
HEALTH_PATH = ROOT / "data" / "purchase-link-health.json"
QUEUE_PATH = ROOT / "research" / "purchase-link-replacement-queue.md"

USER_AGENT = "GlassesResearch-LinkHealth/1.0 (+https://glassesresearch.org/)"
TIMEOUT = 18


@dataclass
class CheckResult:
    model_id: str
    label: str
    url: str
    source_type: str
    status: str
    http_status: int | None
    final_url: str | None
    checked_at: str
    elapsed_ms: int
    note: str = ""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def classify(code: int | None, original: str, final_url: str | None, error: str = "") -> tuple[str, str]:
    if code is None:
        return "unreachable", error or "No HTTP response"
    if 200 <= code < 300:
        if final_url and final_url.rstrip("/") != original.rstrip("/"):
            return "redirected", "Reached a different final URL; review exact-model match"
        return "reachable", ""
    if code in (401, 403, 405, 429):
        return "blocked_or_rate_limited", f"HTTP {code}; retailer may block automated checks"
    if code in (404, 410):
        return "dead", f"HTTP {code}"
    if 300 <= code < 400:
        return "redirected", f"HTTP {code}"
    if 500 <= code < 600:
        return "temporary_failure", f"HTTP {code}"
    return "unknown", f"HTTP {code}"


def check_url(record: dict) -> CheckResult:
    url = record["url"]
    start = time.monotonic()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.5",
            "Accept-Language": "en-US,en;q=0.8",
        },
        method="GET",
    )
    code = None
    final_url = None
    error = ""
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as response:
            code = response.getcode()
            final_url = response.geturl()
            response.read(2048)
    except urllib.error.HTTPError as exc:
        code = exc.code
        final_url = exc.geturl()
        error = str(exc)
    except (urllib.error.URLError, TimeoutError, socket.timeout, ssl.SSLError) as exc:
        error = str(exc)
    elapsed = int((time.monotonic() - start) * 1000)
    status, note = classify(code, url, final_url, error)
    return CheckResult(
        model_id=record["model_id"],
        label=record.get("label", record.get("retailer", "Purchase source")),
        url=url,
        source_type=record.get("source_type", "unknown"),
        status=status,
        http_status=code,
        final_url=final_url,
        checked_at=utc_now(),
        elapsed_ms=elapsed,
        note=note,
    )


def load_purchase_records() -> list[dict]:
    data = json.loads(PURCHASE_PATH.read_text(encoding="utf-8"))
    flat: list[dict] = []
    for i, model in enumerate(data.get("records", [])):
        model_id = model.get("id")
        if not model_id:
            raise SystemExit(f"purchase model record {i} missing id")
        sources = model.get("sources", [])
        if not isinstance(sources, list):
            raise SystemExit(f"purchase model record {model_id} has non-list sources")
        for j, source in enumerate(sources):
            if not source.get("url"):
                raise SystemExit(f"purchase source {model_id}[{j}] missing url")
            flat.append({"model_id": model_id, **source})
    return flat


def write_health(results: list[CheckResult]) -> None:
    summary: dict[str, int] = {}
    for result in results:
        summary[result.status] = summary.get(result.status, 0) + 1
    payload = {
        "schema_version": 1,
        "generated_at": utc_now(),
        "meaning": "Automated reachability/freshness ledger. It does not by itself prove exact-model inventory or price accuracy.",
        "summary": dict(sorted(summary.items())),
        "records": [asdict(r) for r in results],
    }
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    HEALTH_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_queue(results: list[CheckResult]) -> None:
    needs_review = [r for r in results if r.status not in {"reachable", "blocked_or_rate_limited"}]
    lines = [
        "# Purchase Link Replacement Queue",
        "",
        f"Generated: {utc_now()}",
        "",
        "This queue is generated from the purchase-link health checker. Canonical purchase URLs are never silently replaced or deleted by the checker.",
        "",
        "`blocked_or_rate_limited` routes stay out of this queue because many retailers intentionally reject bots even when their shopper pages work. Those routes require separate periodic human/browser verification.",
        "",
    ]
    if not needs_review:
        lines.append("No automated replacement candidates on this run.\n")
    else:
        lines += [
            "| Model | Source | State | HTTP | Current URL | Action |",
            "|---|---|---|---:|---|---|",
        ]
        for r in sorted(needs_review, key=lambda x: (x.model_id, x.label)):
            action = {
                "dead": "Find replacement or durable marketplace search",
                "unreachable": "Retry, then search replacement if persistent",
                "redirected": "Verify final page still matches exact model",
                "temporary_failure": "Retry later",
                "unknown": "Review manually",
            }.get(r.status, "Review manually")
            lines.append(
                f"| {r.model_id} | {r.label} | {r.status} | {r.http_status or ''} | {r.url} | {action} |"
            )
        lines.append("")
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Check only the first N source URLs (0 = all)")
    parser.add_argument("--delay", type=float, default=0.35, help="Delay between requests")
    args = parser.parse_args()

    records = load_purchase_records()
    if args.limit:
        records = records[: args.limit]

    results = []
    for idx, record in enumerate(records, 1):
        result = check_url(record)
        results.append(result)
        print(f"[{idx}/{len(records)}] {result.model_id} {result.label}: {result.status} ({result.http_status})")
        if idx < len(records) and args.delay:
            time.sleep(args.delay)

    write_health(results)
    write_queue(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
