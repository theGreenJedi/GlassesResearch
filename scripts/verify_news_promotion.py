#!/usr/bin/env python3
"""Validate canonical destination assessments for schema-marked news reviews."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "news_promotion_schema: 1"
DISPOSITION = re.compile(r"\*\*Disposition:\*\*\s*\`?publish\`?", re.I)
FIELDS = {
    "affected models": re.compile(r"^- \*\*Affected models:\*\*\s*(.+)$", re.I | re.M),
    "affected ecosystem": re.compile(r"^- \*\*Affected lineages / platforms / resources:\*\*\s*(.+)$", re.I | re.M),
    "canonical destinations": re.compile(r"^- \*\*Canonical destinations:\*\*\s*(.+)$", re.I | re.M),
}
PATH = re.compile(r"\`([^\`]+)\`")
NONE = re.compile(r"^none\s*[—-]\s*\S.+$", re.I)


def publish_blocks(text: str) -> list[str]:
    headings = list(re.finditer(r"^###\s+", text, re.M))
    blocks = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.start():end]
        if DISPOSITION.search(block):
            blocks.append(block)
    return blocks


def validate_text(text: str, label: str) -> list[str]:
    if MARKER not in text:
        return []
    errors = []
    for number, block in enumerate(publish_blocks(text), 1):
        values = {}
        for name, pattern in FIELDS.items():
            match = pattern.search(block)
            if not match or not match.group(1).strip():
                errors.append(f"{label}: publish block {number} missing {name}")
            else:
                values[name] = match.group(1).strip()
        destination = values.get("canonical destinations")
        if destination and not NONE.match(destination):
            paths = PATH.findall(destination)
            if not paths:
                errors.append(f"{label}: publish block {number} destinations must be backtick-wrapped paths or none — rationale")
            for raw in paths:
                candidate = (ROOT / raw).resolve()
                try:
                    candidate.relative_to(ROOT)
                except ValueError:
                    errors.append(f"{label}: destination escapes repository: {raw}")
                    continue
                if not candidate.exists():
                    errors.append(f"{label}: unresolved canonical destination: {raw}")
            if paths and all(path.startswith("docs/news/digests/") for path in paths):
                errors.append(f"{label}: public digest alone is not a canonical research destination")
        for name in ("affected models", "affected ecosystem"):
            value = values.get(name)
            if value and value.lower().startswith("none") and not NONE.match(value):
                errors.append(f"{label}: {name} needs none — rationale")
    return errors


def review_files() -> list[Path]:
    paths = []
    for directory in (ROOT / "research/news-reviews", ROOT / "research/inbox"):
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            if "TEMPLATE" not in path.name and path.name != "README.md":
                paths.append(path)
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    errors = []
    for path in review_files():
        errors.extend(validate_text(path.read_text(encoding="utf-8"), path.relative_to(ROOT).as_posix()))
    if args.self_test:
        valid = (ROOT / "tests/fixtures/news-promotion-valid.md").read_text(encoding="utf-8")
        invalid = (ROOT / "tests/fixtures/news-promotion-invalid.md").read_text(encoding="utf-8")
        errors.extend(validate_text(valid, "valid fixture"))
        if not validate_text(invalid, "invalid fixture"):
            errors.append("invalid fixture unexpectedly passed")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("News promotion destination validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
