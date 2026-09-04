#!/usr/bin/env python3
"""Derive canonical catalog metadata from approved catalog evidence.

The canonical model count is derived only from the unique GLS rows in
``models/THE_LIST.md``. Public pages, generated datasets, and validators should
consume this helper rather than maintain independent counts.

The catalog update date is mechanical metadata. It comes from dated canonical
admission packets and catalog corrections, never from a hand-entered homepage
value or from the wall-clock time of a site build.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
import re

EDITION_RE = re.compile(r"(\*\*Edition:\*\*\s*)(20\d{2}-\d{2}-\d{2})")
ADMISSION_SECTION_RE = re.compile(
    r"## Admit to canonical purchaser-history ledger\n(.*?)(?=\n## |\Z)",
    flags=re.S,
)
DATE_LINE_RE = re.compile(r"^Date:\s*(20\d{2}-\d{2}-\d{2})\s*$", flags=re.M)
DATE_IN_NAME_RE = re.compile(r"(20\d{2}-\d{2}-\d{2})")
CORRECTION_DATE_RE = re.compile(
    r"^\|\s*(20\d{2}-\d{2}-\d{2})\s*\|\s*GLS-\d{4}\s*\|",
    flags=re.M,
)
GLS_ID_ROW_RE = re.compile(r"^\| (GLS-\d{4}) \|", flags=re.M)
GLS_ROW_RE = re.compile(r"^\| GLS-\d{4} \|", flags=re.M)


def _validated(raw: str) -> str:
    date.fromisoformat(raw)
    return raw


def edition_from_text(text: str) -> str | None:
    match = EDITION_RE.search(text)
    return _validated(match.group(2)) if match else None


def canonical_model_ids(root: Path, the_list_text: str | None = None) -> tuple[str, ...]:
    """Return the sorted unique canonical GLS IDs from the authoritative ledger."""
    if the_list_text is None:
        the_list_text = (root / "models" / "THE_LIST.md").read_text(encoding="utf-8")
    ids = set(GLS_ID_ROW_RE.findall(the_list_text))
    return tuple(sorted(ids, key=lambda value: int(value.split("-")[1])))


def canonical_model_count(root: Path, the_list_text: str | None = None) -> int:
    """Return the one authoritative canonical model count."""
    return len(canonical_model_ids(root, the_list_text))


def canonical_event_dates(root: Path) -> list[str]:
    """Return dates of events that can change the canonical purchaser ledger."""
    dates: list[str] = []
    models = root / "models"

    for path in sorted(models.glob("THE_LIST_RECONCILIATION_*.md")):
        text = path.read_text(encoding="utf-8")
        section = ADMISSION_SECTION_RE.search(text)
        if not section or not GLS_ROW_RE.search(section.group(1)):
            continue
        explicit = DATE_LINE_RE.search(text)
        inferred = DATE_IN_NAME_RE.search(path.name)
        match = explicit or inferred
        if not match:
            raise ValueError(f"approved admission packet has no ISO date: {path}")
        dates.append(_validated(match.group(1)))

    corrections = models / "CATALOG_CORRECTIONS.md"
    if corrections.exists():
        text = corrections.read_text(encoding="utf-8")
        dates.extend(_validated(raw) for raw in CORRECTION_DATE_RE.findall(text))

    return dates


def canonical_updated_at(root: Path, the_list_text: str | None = None) -> str:
    """Return the latest evidence-backed date on which canonical catalog state changed."""
    dates = canonical_event_dates(root)
    if dates:
        return max(dates)

    if the_list_text is None:
        list_path = root / "models" / "THE_LIST.md"
        the_list_text = list_path.read_text(encoding="utf-8")
    fallback = edition_from_text(the_list_text)
    if fallback:
        return fallback
    raise ValueError("cannot derive canonical catalog update date")


def synchronize_edition(text: str, updated_at: str) -> str:
    """Replace the visible ledger Edition with the derived canonical date."""
    _validated(updated_at)
    synced, replacements = EDITION_RE.subn(rf"\g<1>{updated_at}", text, count=1)
    if replacements != 1:
        raise ValueError("THE_LIST.md Edition field missing or ambiguous")
    return synced
