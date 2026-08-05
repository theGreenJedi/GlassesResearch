#!/usr/bin/env python3
"""Stage repository Markdown and site assets for the GlassesResearch MkDocs site."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"

COPY_DIRS = (
    "buyers",
    "docs",
    "glossary",
    "hacking",
    "images",
    "models",
    "resources",
)
COPY_FILES = (
    "FOUNDING_CHARTER.md",
    "WHY.md",
)


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    readme = ROOT / "README.md"
    if not readme.exists():
        raise FileNotFoundError("README.md is required to build the site")
    shutil.copy2(readme, DEST / "index.md")

    for filename in COPY_FILES:
        source = ROOT / filename
        if not source.exists():
            raise FileNotFoundError(f"Required documentation file missing: {filename}")
        shutil.copy2(source, DEST / filename)

    for dirname in COPY_DIRS:
        source = ROOT / dirname
        if not source.exists():
            raise FileNotFoundError(f"Required documentation directory missing: {dirname}")
        shutil.copytree(
            source,
            DEST / dirname,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    print(f"Staged documentation at {DEST}")


if __name__ == "__main__":
    main()
