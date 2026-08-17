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
    "index.md": (
        "Find glasses",
        "Research a model",
        "Explore ecosystem",
    ),
    "docs/REPORT_CARD.md": (
        "Core Report Cards — one for every canonical model in the catalog.",
        "They add depth; they do not define catalog coverage.",
        "## Extended Research",
    ),
    "docs/TOOLS.md": (
        "verified price ceilings",
        "Report Card minimum scores",
        "six-subject Core Report Cards for every canonical model",
        "Extended Research",
    ),
    "docs/GLASSES_FINDER.md": (
        "## Current capability contract",
        "verified price-ceiling filters",
        "Report Card minimum-score filters",
        "shortlist checkboxes",
        "- No camera",
        "- Under $1,000",
        "- Used okay",
        "## Implementation status",
    ),
    "docs/COMPARISON_ENGINE.md": (
        "**Current live controls:**",
        "verified price ceilings",
        "Report Card minimum-score thresholds",
        "shortlist checkboxes",
    ),
}

FORBIDDEN_CONTRACTS = {
    "docs/GLASSES_FINDER.md": (
        "First-person camera",
        "Specialist retailer",
        "New / refurbished / used",
    ),
}

# Public capability claims must also remain anchored to the implementation. This
# prevents a later editorial edit from claiming a control that the Finder no
# longer ships, or source changes from silently outrunning the visitor contract.
SOURCE_CONTRACTS = {
    "docs/javascripts/glasses-finder-v3.js": (
        "price-observations.json",
        "filter.type === 'price_max'",
        "data-score-enable",
        "report-card-scores.json",
    ),
    "docs/javascripts/finder-shortlist.js": (
        "data-shortlist-id",
        "data-compare-selected",
        "Compare selected",
    ),
    "docs/javascripts/model-knowledge-flow.js": (
        "Follow this model",
        "Continue researching",
        "#verified-research-alerts",
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

    for rel, phrases in FORBIDDEN_CONTRACTS.items():
        path = SITE / rel
        if not path.exists():
            failures.append((rel, "missing visitor-facing contract page"))
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in phrases:
            if phrase in text:
                failures.append((rel, f"phantom capability/control in public contract: {phrase}"))

    for rel, phrases in SOURCE_CONTRACTS.items():
        path = ROOT / rel
        if not path.exists():
            failures.append((rel, "missing shipped-capability source"))
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in phrases:
            if phrase not in text:
                failures.append((rel, f"missing shipped-capability marker: {phrase}"))

    if failures:
        print("Public editorial audit failed:")
        for rel, issue in failures:
            print(f"- {rel}: {issue}")
        return 1

    print("Public editorial and capability-contract audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())