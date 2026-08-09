#!/usr/bin/env python3
"""Fail when internal editorial/process narration leaks into public research pages."""

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
                failures.append((rel, phrase))

    if failures:
        print("Public editorial audit failed:")
        for rel, phrase in failures:
            print(f"- {rel}: {phrase}")
        return 1

    print("Public editorial audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
