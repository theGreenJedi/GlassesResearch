#!/usr/bin/env python3
"""Persist automated triage for GlassesResearch durable knowledge intake.

Triage is descriptive, not publication authority. Explicit editorial decisions are
preserved; automation never marks a candidate published or alert-eligible.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[1]
INTAKE_DIRS = (ROOT / "research/news-candidates", ROOT / "research/discovery-candidates")
REVIEWS_DIR = ROOT / "research/news-reviews"
QUEUE_PATH = REVIEWS_DIR / "queue.json"
LATEST_PATH = REVIEWS_DIR / "latest.md"
FINAL_DISPOSITIONS = {"published", "watch", "archived", "superseded", "rejected"}
PRIORITY_ORDER = {"high": 0, "normal": 1, "low": 2}
STATE_ORDER = {
    "needs_editorial_verification": 0,
    "source_review": 1,
    "catalog_review": 2,
    "source_monitor": 3,
    "watching": 4,
    "adjacent_radar": 5,
    "rejected_noise": 6,
}

# "Prescription" is useful eyewear vocabulary but also produces broad-web noise.
# These checks stop ordinary medication/pharmacy pages from consuming editorial
# verification capacity while retaining genuine optical/enabling evidence.
PHARMACY_NOISE_TERMS = (
    "pharmacy", "drugstore", "prescriptions", "prescription delivery",
    "refill", "refills", "medication", "medications", "medicine",
)
STRONG_ENABLING_TERMS = (
    "waveguide", "microled", "micro-oled", "micro oled", "optics", "optical",
    "lens", "lenses", "retinal", "holographic", "camera module", "snapdragon ar1",
    "display engine", "eye tracking", "gaze tracking", "near-eye display",
    "near eye display",
)
DIRECT_CONTEXT_TERMS = (
    "smart glasses", "smartglasses", "ai glasses", "ar glasses", "smart eyewear",
    "ai eyewear", "ar eyewear", "camera glasses", "audio glasses", "display glasses",
)


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lookback-days", type=int, default=14)
    parser.add_argument("--verify-reachability", action="store_true")
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--workers", type=int, default=12)
    return parser.parse_args()


def parse_stamp(value: str) -> dt.datetime | None:
    if not value:
        return None
    try:
        stamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return (stamp if stamp.tzinfo else stamp.replace(tzinfo=dt.timezone.utc)).astimezone(dt.timezone.utc)
    except ValueError:
        return None


def file_stamp(path: pathlib.Path) -> dt.datetime | None:
    match = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
    if not match:
        return None
    try:
        return dt.datetime.fromisoformat(match.group(1)).replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def candidate_id(item: dict) -> str:
    value = str(item.get("id", "")).strip()
    if value:
        return value
    return hashlib.sha256(str(item.get("url", "")).encode()).hexdigest()[:16]


def normalized_url(item: dict) -> str:
    """Stable review identity for the same source URL across collector IDs."""
    raw = str(item.get("url", "")).strip()
    if not raw:
        return ""
    try:
        parts = urlsplit(raw)
        path = parts.path.rstrip("/") or "/"
        return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))
    except ValueError:
        return raw


def review_key(item: dict) -> str:
    return normalized_url(item) or candidate_id(item)


def haystack(item: dict) -> str:
    return " ".join(str(item.get(field, "")) for field in ("title", "summary", "url")).lower()


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def generic_pharmacy_noise(item: dict) -> bool:
    if str(item.get("relationship", "")) != "enabling":
        return False
    text = haystack(item)
    return contains_any(text, PHARMACY_NOISE_TERMS) and not contains_any(text, STRONG_ENABLING_TERMS + DIRECT_CONTEXT_TERMS)


def strong_enabling_context(item: dict) -> bool:
    return contains_any(haystack(item), STRONG_ENABLING_TERMS + DIRECT_CONTEXT_TERMS)


def standing_source_watch(item: dict) -> bool:
    """A configured source surface is a monitor, not a newly discovered event."""
    title = str(item.get("title", "")).strip().lower()
    source = str(item.get("source", "")).strip().lower()
    return (
        source == "manufacturer-watch"
        or title.startswith("manufacturer/source watch:")
        or title.startswith("manufacturer catalog watch:")
    )


def catalog_discovery_lead(item: dict) -> bool:
    """A crawled manufacturer link is catalog research, not news publication work."""
    if standing_source_watch(item):
        return False
    title = str(item.get("title", "")).strip().lower()
    channel = str(item.get("discovery_channel", "")).strip().lower()
    return channel == "manufacturer_catalog" or title.startswith("manufacturer catalog lead:")


def load_existing() -> dict[str, dict]:
    try:
        payload = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {
        review_key(item): item
        for item in payload.get("candidates", [])
        if isinstance(item, dict) and review_key(item)
    }


def prefer_new(new: dict, old: dict) -> bool:
    """Prefer higher-priority/material candidates, then the newest observation."""
    new_rank = (PRIORITY_ORDER.get(str(new.get("triage_priority", "low")), 9), -int(new.get("materiality_score", 0) or 0))
    old_rank = (PRIORITY_ORDER.get(str(old.get("triage_priority", "low")), 9), -int(old.get("materiality_score", 0) or 0))
    if new_rank != old_rank:
        return new_rank < old_rank
    new_stamp = parse_stamp(str(new.get("intake_discovered_utc", "")))
    old_stamp = parse_stamp(str(old.get("intake_discovered_utc", "")))
    return bool(new_stamp and (old_stamp is None or new_stamp >= old_stamp))


def collect(cutoff: dt.datetime) -> tuple[dict[str, dict], int]:
    found: dict[str, dict] = {}
    file_count = 0
    for directory in INTAKE_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            stamp = parse_stamp(str(payload.get("discovered_utc", ""))) or file_stamp(path)
            if stamp and stamp < cutoff:
                continue
            file_count += 1
            for item in payload.get("candidates", []):
                if not isinstance(item, dict) or not str(item.get("url", "")).strip():
                    continue
                record = dict(item)
                record["id"] = candidate_id(record)
                record["intake_file"] = str(path.relative_to(ROOT))
                record["intake_discovered_utc"] = stamp.isoformat() if stamp else ""
                key = review_key(record)
                prior = found.get(key)
                if prior is None or prefer_new(record, prior):
                    found[key] = record
    return found, file_count


def check_url(url: str, timeout: float) -> dict:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "GlassesResearch-editorial-triage/2.2"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return {"status": "reachable" if 200 <= response.status < 400 else "review", "result": str(response.status)}
    except urllib.error.HTTPError as exc:
        return {"status": "review", "result": str(exc.code)}
    except Exception as exc:
        return {"status": "unreachable", "result": type(exc).__name__}


def should_check_source(item: dict) -> bool:
    if standing_source_watch(item) or catalog_discovery_lead(item):
        return False
    relationship = str(item.get("relationship", ""))
    if relationship == "direct":
        return True
    return relationship == "enabling" and strong_enabling_context(item) and not generic_pharmacy_noise(item)


def source_checks(incoming: dict[str, dict], config: argparse.Namespace, now: dt.datetime) -> dict[str, dict]:
    if not config.verify_reachability:
        return {}
    actionable = {key: item for key, item in incoming.items() if should_check_source(item)}
    if not actionable:
        return {}
    results: dict[str, dict] = {}
    workers = max(1, min(config.workers, 24, len(actionable)))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(check_url, str(item.get("url", "")), config.timeout): key for key, item in actionable.items()}
        for future in as_completed(futures):
            key = futures[future]
            result = future.result()
            result["checked_utc"] = now.isoformat()
            results[key] = result
    return results


def state_for(item: dict, source: dict) -> str:
    relationship = str(item.get("relationship", ""))
    types = set(item.get("content_types", []) or [])
    if relationship == "irrelevant":
        return "rejected_noise"
    if relationship == "speculative" or "rumor" in types:
        return "watching"
    if relationship == "adjacent":
        return "adjacent_radar"
    if generic_pharmacy_noise(item):
        return "rejected_noise"
    if standing_source_watch(item):
        return "source_monitor"
    if catalog_discovery_lead(item):
        return "catalog_review"
    if relationship == "enabling" and not strong_enabling_context(item):
        return "source_review"
    if relationship in {"direct", "enabling"}:
        return "source_review" if source.get("status") in {"review", "unreachable"} else "needs_editorial_verification"
    return "source_review"


automated_state = state_for


def preserve_editorial(record: dict, prior: dict | None) -> None:
    if not prior:
        record.update({"editorial_disposition": "pending", "editorial_notes": "", "publication_authorized": False})
        return
    for field in ("first_seen_utc", "editorial_disposition", "editorial_notes", "publication_authorized", "resolved_utc", "canonical_destinations"):
        if field in prior:
            record[field] = prior[field]


preserve_editorial_fields = preserve_editorial


def build(config: argparse.Namespace) -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    incoming, file_count = collect(now - dt.timedelta(days=config.lookback_days))
    existing = load_existing()
    checks = source_checks(incoming, config, now)
    records: list[dict] = []

    for key, item in incoming.items():
        prior = existing.get(key)
        record = dict(item)
        preserve_editorial(record, prior)
        record.setdefault("first_seen_utc", record.get("intake_discovered_utc") or now.isoformat())
        record["last_seen_utc"] = record.get("intake_discovered_utc") or now.isoformat()
        source = checks.get(key) or dict((prior or {}).get("source_check", {"status": "not_checked", "result": "", "checked_utc": ""}))
        record["source_check"] = source
        disposition = str(record.get("editorial_disposition", "pending"))
        if disposition in FINAL_DISPOSITIONS:
            record["triage_state"] = f"editorial_{disposition}"
        else:
            record["editorial_disposition"] = "pending"
            record["publication_authorized"] = False
            record["triage_state"] = state_for(record, source)
        record["publication_gate"] = (
            "authorized" if bool(record.get("publication_authorized")) and disposition == "published"
            else "blocked_pending_editorial_verification" if record["triage_state"] in {"needs_editorial_verification", "source_review"}
            else "not_publication_eligible"
        )
        records.append(record)

    incoming_keys = set(incoming)
    for key, prior in existing.items():
        if key not in incoming_keys and str(prior.get("editorial_disposition", "pending")) in FINAL_DISPOSITIONS:
            records.append(prior)

    records.sort(key=lambda item: (
        0 if str(item.get("editorial_disposition", "pending")) == "pending" else 1,
        STATE_ORDER.get(str(item.get("triage_state", "")), 9),
        PRIORITY_ORDER.get(str(item.get("triage_priority", "low")), 9),
        -int(item.get("materiality_score", 0) or 0),
        str(item.get("title", "")).lower(),
    ))
    return {
        "schema": 4,
        "generated_utc": now.isoformat(),
        "lookback_days": config.lookback_days,
        "intake_files_inspected": file_count,
        "candidate_count": len(records),
        "state_counts": dict(sorted(Counter(str(x.get("triage_state", "unknown")) for x in records).items())),
        "priority_counts": dict(sorted(Counter(str(x.get("triage_priority", "unknown")) for x in records).items())),
        "publication_rule": "Automated triage never authorizes publication; factual publication requires explicit editorial verification.",
        "candidates": records,
    }


def esc(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def markdown(queue: dict) -> str:
    lines = [
        "# Automated editorial triage — latest", "", f"Generated: `{queue['generated_utc']}`", "",
        f"- Intake files inspected: **{queue['intake_files_inspected']}**",
        f"- Candidates retained in this review window/history: **{queue['candidate_count']}**",
        "- **Publication authority: none.** This is triage state, not factual verification or publication approval.",
        "", "## Queue state", "",
    ]
    lines += [f"- `{state}`: {count}" for state, count in queue.get("state_counts", {}).items()]
    lines += ["", "## Action queue", "", "| Priority | State | Relationship | Candidate | Source check | Routes |", "|---|---|---|---|---|---|"]
    for item in [x for x in queue.get("candidates", []) if x.get("editorial_disposition", "pending") == "pending"][:250]:
        source = item.get("source_check", {}) or {}
        source_text = source.get("status", "not_checked") + (f" ({source['result']})" if source.get("result") else "")
        lines.append("| {p} | {s} | {r} | [{t}]({u}) | {c} | {routes} |".format(
            p=esc(item.get("triage_priority", "low")), s=esc(item.get("triage_state", "")), r=esc(item.get("relationship", "")),
            t=esc(item.get("title", ""))[:140], u=str(item.get("url", "")), c=esc(source_text),
            routes=esc(", ".join(item.get("routing_targets", []) or [])),
        ))
    lines += [
        "", "## Meaning of states", "",
        "- `needs_editorial_verification` — a concrete direct/enabling development ready for factual review.",
        "- `source_review` — potentially relevant, but the source or enabling relationship needs manual attention.",
        "- `catalog_review` — a static manufacturer catalog/developer link that can improve model research but is not a news event.",
        "- `source_monitor` — a configured standing source surface retained for future change detection, not a new editorial event.",
        "- `watching` — rumor/speculation; retain without public promotion.",
        "- `adjacent_radar` — neighboring wearable/HCI material without a concrete glasses publication gate.",
        "- `rejected_noise` — irrelevant or generic non-eyewear material that should not advance.", "",
        "Only an explicitly published/authorized editorial record may feed canonical publication and Verified Research Alerts.", "",
    ]
    return "\n".join(lines)


def write(queue: dict) -> None:
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    text = markdown(queue)
    LATEST_PATH.write_text(text, encoding="utf-8")
    day = dt.datetime.fromisoformat(queue["generated_utc"]).astimezone(ZoneInfo("America/New_York")).date().isoformat()
    (REVIEWS_DIR / f"{day}-auto-triage.md").write_text(text, encoding="utf-8")


def main() -> int:
    config = args()
    if config.lookback_days < 1 or config.workers < 1:
        raise SystemExit("lookback-days and workers must be >= 1")
    queue = build(config)
    write(queue)
    print(json.dumps({"candidate_count": queue["candidate_count"], "state_counts": queue["state_counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
