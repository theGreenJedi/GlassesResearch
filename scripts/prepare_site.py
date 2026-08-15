#!/usr/bin/env python3
"""Stage repository Markdown and site assets for the GlassesResearch MkDocs site."""

from __future__ import annotations

import re
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

# Public presentation should show the result of the research system, not narrate
# the machinery that produced it. Internal methodology remains in the repository.
PUBLIC_NARRATION_REPLACEMENTS = (
    (
        "A model entry is not complete merely because it appears in a catalog. Each GlassesResearch profile should explain, in ordinary language, **what the glasses really are, what is interesting about them, where they are strong, and what tradeoffs matter**. The structured Report Card remains useful underneath; this page is the human-readable layer.\n\nProfiles are published only when the available evidence supports something more useful than generic product description. Missing profiles are research work to be done, not invitations to manufacture filler.\n\n",
        "",
    ),
    (
        "Only confirmed facts are presented as positive. An unresolved field is not treated as a negative.\n\n",
        "",
    ),
    (
        "The [canonical catalog row](/models/THE_LIST/) is the stable identity ledger. Source links document the catalog claim; deeper specifications may have their own citations in the comparison record.\n\n",
        "",
    ),
    (
        "Unknown fields are deliberately preserved as unknown. To supply primary documentation or challenge a claim, use the [research challenge process](/docs/RESEARCH_CHALLENGES/).",
        "See an error or have stronger evidence? [Submit a research challenge](/docs/RESEARCH_CHALLENGES/).",
    ),
    (
        "W610's report card remains incomplete because direct evidence matters more here than filling blanks with assumptions.",
        "W610 report card fields without sufficient evidence remain unscored.",
    ),
)


def strip_public_infrastructure_narration() -> None:
    """Remove editorial/build-process narration from visitor-facing presentation pages."""
    targets = []
    targets.extend((DEST / "models").glob("PROFILES*.md"))
    targets.extend((DEST / "models" / "catalog").glob("*.md"))
    targets.extend((DEST / "guides").glob("*.md"))

    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in PUBLIC_NARRATION_REPLACEMENTS:
            text = text.replace(old, new)

        # Generated model pages should state the coverage result directly rather
        # than explaining the epistemic policy that created it.
        text = re.sub(
            r"\*\*Coverage note:\*\* (\d+) capability fields remain unknown\. That is a research status, not a product limitation\.",
            r"**Unknown capabilities:** \1",
            text,
        )

        # Search-intent guides should lead with the selection itself, not explain
        # the database pipeline. Keep the criteria visible and useful.
        text = re.sub(
            r"This guide answers a specific search question using the GlassesResearch verified database\. Inclusion requires (.+?); unknown values never qualify\. It is a research shortlist rather than an affiliate ranking, and it changes when stronger evidence enters the database\.",
            r"Included models have verified \1.",
            text,
        )
        text = re.sub(r"\n## Method\n\n.*?(?=\n## |\Z)", "\n", text, flags=re.DOTALL)

        path.write_text(text, encoding="utf-8")


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

    strip_public_infrastructure_narration()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_internal_model_links.py"), "--output-root", str(DEST)],
        check=True,
    )

    print(f"Staged documentation at {DEST}")


if __name__ == "__main__":
    main()
