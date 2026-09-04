#!/usr/bin/env python3
"""Build generated homepage research-status metrics."""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import UTC, datetime
from pathlib import Path

from catalog_metadata import canonical_model_count, canonical_updated_at

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def generated_at() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    moment = datetime.fromtimestamp(int(epoch), UTC) if epoch else datetime.now(UTC)
    return moment.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def display_date(raw_date: str) -> str:
    parsed = datetime.strptime(raw_date, "%Y-%m-%d")
    return f"{parsed.strftime('%b')} {parsed.day}, {parsed.year}"


def render_homepage(path: str, payload: dict) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    replacements = {
        "models": f"{payload['canonical_model_count']:,}",
        "report-cards": f"{payload['scored_report_card_count']:,}",
        "freshness": display_date(payload["catalog_updated_at"]),
    }

    for stat, value in replacements.items():
        pattern = re.compile(
            rf'(<strong\s+data-site-stat="{re.escape(stat)}">).*?(</strong>)',
            re.DOTALL,
        )
        text, count = pattern.subn(rf"\g<1>{value}\g<2>", text, count=1)
        if count != 1:
            raise SystemExit(
                f"homepage status invariant failed: expected one data-site-stat={stat!r}, found {count}"
            )

    target.write_text(text, encoding="utf-8")
    print(
        "Rendered homepage status from the canonical ledger payload: "
        f"{replacements['models']} models, {replacements['report-cards']} Report Cards, "
        f"updated {replacements['freshness']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", required=True)
    parser.add_argument("--report-cards", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--homepage",
        help="Optional staged homepage to render with the generated canonical metrics.",
    )
    args = parser.parse_args()

    devices = load(args.devices)
    report_cards = load(args.report_cards)
    records = devices.get("records", [])
    device_count = devices.get("record_count")
    if not isinstance(device_count, int):
        device_count = len(records)
    if device_count != len(records):
        raise SystemExit(
            f"device count invariant failed: record_count={device_count}, records={len(records)}"
        )

    # models/THE_LIST.md is the only authority for the canonical count. The
    # generated device database must agree with it or the build stops rather
    # than publishing a second, conflicting number.
    model_count = canonical_model_count(ROOT)
    if device_count != model_count:
        raise SystemExit(
            "canonical model count drift: "
            f"THE_LIST.md={model_count}, generated devices.json={device_count}"
        )

    scored = 0
    for record in report_cards.get("records", []):
        scores = record.get("scores", {})
        if any(isinstance(value, (int, float)) for value in scores.values()):
            scored += 1

    payload = {
        "schema_version": 3,
        "canonical_model_count": model_count,
        "catalog_updated_at": canonical_updated_at(ROOT),
        "scored_report_card_count": scored,
        "generated_at": generated_at(),
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.homepage:
        render_homepage(args.homepage, payload)

    print(
        f"Built site status for {model_count} canonical models; "
        f"catalog updated {payload['catalog_updated_at']}; {scored} scored Report Cards"
    )


if __name__ == "__main__":
    main()
