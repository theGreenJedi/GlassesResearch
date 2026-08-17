#!/usr/bin/env python3
"""Fail when internal narration leaks publicly or visitor-facing capability contracts drift."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / ".site-src"

ALLOWED = {
    "docs/ABOUT.md",
    "docs/RESEARCH_STANDARDS.md",
    "docs/CONTRIBUTE.md",
}

BANNED = (
    "## What belongs here",
    "## Editorial rules",
    "## Coverage backlog",
    "## Publication rule",
    "## Weekly output",
    "## Standing rule",
    "## Current phase:",
    "verification priorities",
    "highest priority",
    "The priority now is",
    "future work should primarily",
    "do not create a placeholder",
    "add the actual resource, not a sentence",
)

# These are not prose-style preferences. They are visitor-facing contracts that
# must remain explicit because multiple pages describe the same systems.
REQUIRED_CONTRACTS = {
    "docs/REPORT_CARD.md": (
        "Core Report Cards — one for every canonical model in the catalog.",
        "They add depth; they do not define catalog coverage.",
        "## Extended Research",
    ),
    "docs/TOOLS.md": (
        "Price-band controls and Report Card minimum-score filters are planned",
        "six-subject Core Report Cards for every canonical model",
        "Extended Research",
    ),
    "docs/GLASSES_FINDER.md": (
        "## Current capability contract",
        "Price-band/range controls and Report Card minimum-score filters are planned",
        "## Implementation status",
    ),
    "docs/COMPARISON_ENGINE.md": (
        "**Current live controls:**",
        "**Planned controls:** price-band/range filtering and Report Card minimum-score thresholds.",
    ),
}


def main() -> int:
    failures = []
    for path in SITE.rglob("*.md"):
        rel = path.relative_to(SITE).as_posix()
        if rel in ALLOWED:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        lower = text.lower()
        for phrase in BANNED:
            if phrase.lower() in lower:
                failures.append((rel, f"banned narration: {phrase}"))

    for rel, phrases in REQUIRED_CONTRACTS.items():
        path = SITE / rel
        if not path.exists():
            failures.append((rel, "missing visitor-facing contract page"))
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in phrases:
            if phrase not in text:
                failures.append((rel, f"missing capability/coverage contract: {phrase}"))

    if failures:
        print("Public editorial audit failed:")
        for rel, issue in failures:
            print(f"- {rel}: {issue}")
        return 1

    print("Public editorial and capability-contract audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
