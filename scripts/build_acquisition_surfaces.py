#!/usr/bin/env python3
"""Build crawlable, evidence-aware ownership surfaces for canonical models."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

BAD_HEALTH = {"dead", "unreachable", "redirected"}
NEW_SOURCE_TYPES = {"manufacturer", "amazon", "major_retailer", "optical_retailer", "specialist_retailer"}


def load(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def https_url(value: object) -> bool:
    try:
        parsed = urlparse(str(value or ""))
        return parsed.scheme == "https" and bool(parsed.netloc)
    except ValueError:
        return False


def health_map(payload: dict) -> dict[tuple[str, str], str]:
    return {
        (str(row.get("model_id", "")), str(row.get("url", ""))): str(row.get("status", "unknown"))
        for row in payload.get("records", [])
    }


def usable(source: dict, model_id: str, health: dict[tuple[str, str], str]) -> bool:
    if source.get("availability") == "unavailable":
        return False
    if not https_url(source.get("url")):
        return False
    return health.get((model_id, str(source.get("url"))), "unknown") not in BAD_HEALTH


def classify(record: dict, sources: list[dict], health: dict[tuple[str, str], str]) -> dict:
    model_id = str(record["id"])
    viable = [source for source in sources if usable(source, model_id, health)]
    official = next((s for s in viable if s.get("source_type") == "manufacturer" and s.get("exact_model_confidence") == "high"), None)
    new = next((s for s in viable if s.get("source_type") in NEW_SOURCE_TYPES and s.get("condition") == "new" and s.get("availability") == "available" and s.get("exact_model_confidence") == "high"), None)
    secondary = [s for s in viable if s.get("source_type") == "secondary_market"]
    historical = [s for s in sources if s.get("availability") == "unavailable"]

    if new:
        state = "current_new_route_known"
    elif official:
        state = "official_identity_known"
    elif secondary:
        state = "secondary_route_only"
    elif historical or "discontinu" in str(record.get("state", "")).lower():
        state = "discontinued_or_historical"
    else:
        state = "no_verified_acquisition_route"

    return {
        "id": model_id,
        "maker": record.get("maker"),
        "model": record.get("model"),
        "state": state,
        "official": official,
        "buy_new": new,
        "secondary_routes": secondary,
        "second_life_path": f"/second-life/{model_id.lower()}/",
    }


def link(label: str, source: dict | None) -> str | None:
    if not source:
        return None
    return f"[{label}]({source['url']})"


def ownership_markdown(acq: dict) -> str:
    actions: list[str] = []
    official = link("Official", acq.get("official"))
    new = acq.get("buy_new")
    if official:
        actions.append(official)
    if new and (not acq.get("official") or new.get("url") != acq["official"].get("url")):
        actions.append(link("Buy New", new) or "")
    actions.append(f"[Second Life]({acq['second_life_path']})")

    state_text = {
        "current_new_route_known": "A verified current new-product route is recorded.",
        "official_identity_known": "The exact official model page is known; current purchase availability is not verified.",
        "secondary_route_only": "No verified current new-product route is recorded.",
        "discontinued_or_historical": "No verified current new-product route is recorded; historical or discontinued acquisition evidence exists.",
        "no_verified_acquisition_route": "No verified acquisition route is currently known.",
    }[acq["state"]]
    return "\n## Ownership\n\n" + state_text + "\n\n" + " · ".join(a for a in actions if a) + "\n"


def fresh_listing(item: dict, model_id: str, now: datetime) -> bool:
    if item.get("status") != "active" or item.get("model_id") not in {None, model_id}:
        return False
    if not https_url(item.get("url")):
        return False
    stamp = item.get("last_verified_at") or item.get("verified_at")
    try:
        verified = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
        if verified.tzinfo is None:
            verified = verified.replace(tzinfo=timezone.utc)
        verified = verified.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return False
    try:
        ttl = float(item.get("fresh_for_hours", 0))
    except (TypeError, ValueError):
        return False
    age = (now - verified).total_seconds()
    return ttl > 0 and age >= 0 and age <= ttl * 3600


def second_life_page(acq: dict, listings: list[dict], now: datetime) -> str:
    current = [item for item in listings if fresh_listing(item, acq["id"], now)]
    title = f"{acq['maker']} {acq['model']} — Second Life"
    description = f"Recently verified Second Life listings for {acq['maker']} {acq['model']} smart glasses."
    if current:
        rows = []
        for item in current:
            price = f" · {item.get('price')}" if item.get("price") else ""
            verified = item.get("last_verified_at") or item.get("verified_at")
            rows.append(f"- **{item.get('condition', 'Unknown condition')}**{price} · {item.get('source', 'Source')} · verified {verified} · [View listing]({item['url']})")
        body = "\n".join(rows)
    else:
        body = "No recently verified listings right now."
    return f'''---\ntitle: "{title}"\ndescription: "{description}"\nmodel_id: "{acq['id']}"\n---\n\n# {title}\n\n{body}\n\n[Back to model](/models/catalog/{acq['id'].lower()}/)\n'''


def coverage_markdown(records: list[dict]) -> str:
    counts: dict[str, int] = {}
    for row in records:
        counts[row["state"]] = counts.get(row["state"], 0) + 1
    lines = ["# Acquisition coverage", "", "Current catalog ownership-path coverage generated from canonical purchase evidence.", "", "| State | Models |", "|---|---:|"]
    for state in ("current_new_route_known", "official_identity_known", "secondary_route_only", "discontinued_or_historical", "no_verified_acquisition_route"):
        lines.append(f"| {state.replace('_', ' ')} | {counts.get(state, 0)} |")
    lines.extend(["", "Missing routes are research debt, not permission to guess.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", type=Path, required=True)
    parser.add_argument("--purchase-sources", type=Path, required=True)
    parser.add_argument("--health", type=Path, required=True)
    parser.add_argument("--second-life", type=Path)
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    args = parser.parse_args()

    devices = load(args.devices, {"records": []}).get("records", [])
    purchases = load(args.purchase_sources, {"records": []})
    health = health_map(load(args.health, {"records": []}))
    source_by_id = {str(row.get("id")): row.get("sources", []) for row in purchases.get("records", [])}
    acquisitions = [classify(record, source_by_id.get(str(record["id"]), []), health) for record in devices]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"schema_version": 1, "records": acquisitions}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.coverage.parent.mkdir(parents=True, exist_ok=True)
    args.coverage.write_text(coverage_markdown(acquisitions), encoding="utf-8")

    listings = load(args.second_life, {"listings": []}).get("listings", []) if args.second_life else []
    now = datetime.now(timezone.utc)
    for acq in acquisitions:
        model_page = args.site_root / "models" / "catalog" / acq["id"].lower() / "index.md"
        if model_page.exists():
            text = model_page.read_text(encoding="utf-8")
            if "\n## Ownership\n" not in text:
                model_page.write_text(text.rstrip() + "\n" + ownership_markdown(acq), encoding="utf-8")
        sl_page = args.site_root / "second-life" / acq["id"].lower() / "index.md"
        sl_page.parent.mkdir(parents=True, exist_ok=True)
        sl_page.write_text(second_life_page(acq, listings, now), encoding="utf-8")

    print(f"Built acquisition state for {len(acquisitions)} canonical models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
