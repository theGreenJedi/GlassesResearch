#!/usr/bin/env python3
"""Fail when the public release tracker stops receiving verified review.

This checks only the tracker's declared manual-review date. It does not infer
that product release states are correct merely because other newsroom feeds
are fresh.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

LAST_CHECKED_RE = re.compile(r"(?im)^\s*(?:\*\*)?Last checked(?:\*\*)?\s*:\s*(\d{4}-\d{2}-\d{2})\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("tracker", type=Path)
    parser.add_argument("--max-age-days", type=int, default=7)
    parser.add_argument(
        "--today",
        type=dt.date.fromisoformat,
        help="Override UTC today (YYYY-MM-DD) for deterministic tests.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_age_days < 0:
        raise SystemExit("--max-age-days must be >= 0")

    text = args.tracker.read_text(encoding="utf-8")
    match = LAST_CHECKED_RE.search(text)
    if not match:
        raise SystemExit(
            f"{args.tracker}: missing a standalone 'Last checked: YYYY-MM-DD' line"
        )

    checked = dt.date.fromisoformat(match.group(1))
    today = args.today or dt.datetime.now(dt.timezone.utc).date()
    age = (today - checked).days

    if age < 0:
        raise SystemExit(
            f"{args.tracker}: Last checked {checked} is {abs(age)} day(s) in the future"
        )
    if age > args.max_age_days:
        raise SystemExit(
            f"{args.tracker}: release-status review is {age} days old "
            f"(maximum {args.max_age_days}); reverify the tracker before updating the date"
        )

    print(
        f"{args.tracker}: release-status review age {age} day(s) "
        f"(maximum {args.max_age_days})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
