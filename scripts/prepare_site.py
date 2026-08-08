#!/usr/bin/env python3
"""Stage repository Markdown and site assets for the GlassesResearch MkDocs site."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"

COPY_DIRS = (
    "artifacts",
    "buyers",
    "comparisons",
    "docs",
    "evidence",
    "glossary",
    "hacking",
    "images",
    "models",
    "resources",
    "timeline",
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
        ignore = shutil.ignore_patterns("__pycache__", "*.pyc")
        if dirname == "artifacts":
            ignore = shutil.ignore_patterns("__pycache__", "*.pyc", "files")
        shutil.copytree(source, DEST / dirname, ignore=ignore)

    cname = ROOT / "CNAME"
    if cname.exists():
        shutil.copy2(cname, DEST / "CNAME")

    (DEST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://glassesresearch.org/sitemap.xml\n",
        encoding="utf-8",
    )
    (DEST / "humans.txt").write_text(
        "GlassesResearch\nIndependent, privacy-first smart-glasses research.\n"
        "Repository: https://github.com/theGreenJedi/GlassesResearch\n",
        encoding="utf-8",
    )

    database_output = DEST / "data" / "devices.json"
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_device_database.py"), "--source", str(ROOT / "models" / "THE_LIST.md"), "--output", str(database_output)],
        check=True,
    )

    comparison_output = DEST / "data" / "comparisons.json"
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_comparison_engine.py"), "--schema", str(ROOT / "comparisons" / "schema.json"), "--data-dir", str(ROOT / "comparisons" / "data"), "--output", str(comparison_output)],
        check=True,
    )

    print(f"Staged documentation at {DEST}")


if __name__ == "__main__":
    main()
