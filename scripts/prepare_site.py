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
    "data",
    "docs",
    "evidence",
    "glossary",
    "guides",
    "hacking",
    "images",
    "lineages",
    "models",
    "resources",
    "timeline",
)
COPY_FILES = (
    "FOUNDING_CHARTER.md",
    "WHY.md",
)

PUBLIC_SITE_EXCLUDES = (
    "comparisons/README.md",
    "docs/AI610-Notes.md",
    "docs/CONTENT_GAPS_WAVE_TWO.md",
    "docs/HOMEPAGE_DESIGN_NOTES.md",
    "docs/KISS_WORKING_NOTES.md",
    "docs/LEGACY_STRUCTURE_AUDIT.md",
    "docs/RESEARCH_AGENDA.md",
    "docs/ROADMAP_V1.md",
    "docs/SEO_DISCOVERABILITY.md",
    "docs/WEBSITE.md",
    "docs/START_HERE.md",
    "docs/news/WORKFLOW.md",
    "docs/report-cards/PROFILE_AUDIT_03_06.md",
    "docs/report-cards/SOURCES_01.md",
    "resources/CHANGE_SCOPE.md",
    "resources/PR_NOTES.md",
    "resources/VALIDATION.md",
    "timeline/README.md",
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

    for relpath in PUBLIC_SITE_EXCLUDES:
        target = DEST / relpath
        if target.exists():
            target.unlink()

    public_list = DEST / "models" / "THE_LIST.md"
    if public_list.exists():
        text = public_list.read_text(encoding="utf-8")
        text = text.replace(
            "[weekly news workflow](../docs/news/WORKFLOW.md)",
            "[weekly news coverage](../docs/news/README.md)",
        )
        public_list.write_text(text, encoding="utf-8")

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

    capability_output = DEST / "data" / "finder-capabilities.json"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_finder_capabilities.py"),
            "--models", str(ROOT / "models" / "THE_LIST.md"),
            "--comparisons", str(comparison_output),
            "--overrides", str(ROOT / "data" / "finder-capability-overrides.json"),
            "--output", str(capability_output),
        ],
        check=True,
    )

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "apply_finder_capabilities.py"),
            "--comparisons", str(comparison_output),
            "--capabilities", str(capability_output),
        ],
        check=True,
    )

    report_card_output = DEST / "data" / "report-card-scores.json"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_report_card_scores.py"),
            "--input-dir", str(ROOT / "docs" / "report-cards"),
            "--output", str(report_card_output),
        ],
        check=True,
    )

    site_status_output = DEST / "data" / "site-status.json"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_site_status.py"),
            "--devices", str(database_output),
            "--report-cards", str(report_card_output),
            "--output", str(site_status_output),
        ],
        check=True,
    )

    purchase_fallback_output = DEST / "data" / "purchase-fallbacks.json"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_purchase_fallbacks.py"),
            "--models", str(ROOT / "models" / "THE_LIST.md"),
            "--curated", str(ROOT / "data" / "purchase-sources.json"),
            "--output", str(purchase_fallback_output),
        ],
        check=True,
    )

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_model_pages.py"),
            "--data-dir", str(DEST / "data"),
            "--output-root", str(DEST),
        ],
        check=True,
    )

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_internal_model_links.py"), "--output-root", str(DEST)],
        check=True,
    )

    print(f"Staged documentation at {DEST}")


if __name__ == "__main__":
    main()
