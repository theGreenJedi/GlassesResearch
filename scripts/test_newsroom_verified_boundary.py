#!/usr/bin/env python3
"""Regression coverage for the Research & News verified/wire boundary."""
from __future__ import annotations

import tempfile
from pathlib import Path

import verified_changes


def test_dated_across_the_wire_heading_is_non_verified() -> None:
    newsroom = """# Research & News

## Current Desk

### September 30, 2026 — Future reported item

**Across the Wire · Reported.**

Discovery only; this has not been independently verified.

### September 30, 2026 — Verified item

Verified evidence-backed change.
"""
    original = verified_changes.RESEARCH_NEWS
    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "RESEARCH_NEWS.md"
            path.write_text(newsroom, encoding="utf-8")
            verified_changes.RESEARCH_NEWS = path
            headings, non_verified = verified_changes.public_headings()
    finally:
        verified_changes.RESEARCH_NEWS = original

    wire = "September 30, 2026 — Future reported item"
    verified = "September 30, 2026 — Verified item"
    assert wire in headings
    assert wire in non_verified, "dated Across the Wire items must never enter the GRE ledger"
    assert verified in headings
    assert verified not in non_verified, "ordinary dated newsroom items must remain GRE-gated"


if __name__ == "__main__":
    test_dated_across_the_wire_heading_is_non_verified()
    print("Newsroom verified/wire regression test passed.")
