#!/usr/bin/env python3
"""Stage repository Markdown and site assets for the GlassesResearch MkDocs site."""
from __future__ import annotations
import re, shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"
COPY_DIRS = ("artifacts","buyers","comparisons","data","docs","evidence","glossary","guides","hacking","images","lineages","models","resources","timeline")
COPY_FILES = ("FOUNDING_CHARTER.md","WHY.md","CITATION.cff")
PUBLIC_SITE_EXCLUDES = ("comparisons/README.md","docs/AI610-Notes.md","docs/CONTENT_GAPS_WAVE_TWO.md","docs/HOMEPAGE_DESIGN_NOTES.md","docs/KISS_WORKING_NOTES.md","docs/LEGACY_STRUCTURE_AUDIT.md","docs/RESEARCH_AGENDA.md","docs/ROADMAP_V1.md","docs/SEO_DISCOVERABILITY.md","docs/WEBSITE.md","docs/START_HERE.md","docs/news/WORKFLOW.md","docs/report-cards/PROFILE_AUDIT_03_06.md","docs/report-cards/SOURCES_01.md","resources/CHANGE_SCOPE.md","resources/PR_NOTES.md","resources/VALIDATION.md","timeline/README.md")
PUBLIC_NARRATION_REPLACEMENTS = (
("A model entry is not complete merely because it appears in a catalog. Each GlassesResearch profile should explain, in ordinary language, **what the glasses really are, what is interesting about them, where they are strong, and what tradeoffs matter**. The structured Report Card remains useful underneath; this page is the human-readable layer.\n\nProfiles are published only when the available evidence supports something more useful than generic product description. Missing profiles are research work to be done, not invitations to manufacture filler.\n\n",""),
("Only confirmed facts are presented as positive. An unresolved field is not treated as a negative.\n\n",""),
("The [canonical catalog row](/models/THE_LIST/) is the stable identity ledger. Source links document the catalog claim; deeper specifications may have their own citations in the comparison record.\n\n",""),
("Unknown fields are deliberately preserved as unknown. To supply primary documentation or challenge a claim, use the [research challenge process](/docs/RESEARCH_CHALLENGES/).","See an error or have stronger evidence? [Submit a research challenge](/docs/RESEARCH_CHALLENGES/)."),
("W610's report card remains incomplete because direct evidence matters more here than filling blanks with assumptions.","W610 report card fields without sufficient evidence remain unscored."),)
def strip_public_infrastructure_narration():
    targets=list((DEST/"models").glob("PROFILES*.md"))+list((DEST/"models"/"catalog").glob("*.md"))+list((DEST/"guides").glob("*.md"))
    for path in targets:
        if not path.exists(): continue
        text=path.read_text(encoding="utf-8")
        for old,new in PUBLIC_NARRATION_REPLACEMENTS: text=text.replace(old,new)
        text=re.sub(r"\*\*Coverage note:\*\* (\d+) capability fields remain unknown\. That is a research status, not a product limitation\.",r"**Unknown capabilities:** \1",text)
        text=re.sub(r"This guide answers a specific search question using the GlassesResearch verified database\. Inclusion requires (.+?); unknown values never qualify\. It is a research shortlist rather than an affiliate ranking, and it changes when stronger evidence enters the database\.",r"Included models have verified \1.",text)
        text=re.sub(r"\n## Method\n\n.*?(?=\n## |\Z)","\n",text,flags=re.DOTALL)
        path.write_text(text,encoding="utf-8")
def run(*args): subprocess.run([sys.executable,*map(str,args)],check=True)
def main():
    if DEST.exists(): shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    shutil.copy2(ROOT/"README.md",DEST/"index.md")
    for f in COPY_FILES: shutil.copy2(ROOT/f,DEST/f)
    for d in COPY_DIRS:
        ignore=shutil.ignore_patterns("__pycache__","*.pyc","files") if d=="artifacts" else shutil.ignore_patterns("__pycache__","*.pyc")
        shutil.copytree(ROOT/d,DEST/d,ignore=ignore)
    for rel in PUBLIC_SITE_EXCLUDES:
        p=DEST/rel
        if p.exists(): p.unlink()
    public_list=DEST/"models"/"THE_LIST.md"
    if public_list.exists(): public_list.write_text(public_list.read_text(encoding="utf-8").replace("[weekly news workflow](../docs/news/WORKFLOW.md)","[weekly news coverage](../docs/news/README.md)"),encoding="utf-8")
    if (ROOT/"CNAME").exists(): shutil.copy2(ROOT/"CNAME",DEST/"CNAME")
    (DEST/"robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://glassesresearch.org/sitemap.xml\n",encoding="utf-8")
    (DEST/"humans.txt").write_text("GlassesResearch\nIndependent, privacy-first smart-glasses research.\nRepository: https://github.com/theGreenJedi/GlassesResearch\n",encoding="utf-8")
    database=DEST/"data"/"devices.json"; run(ROOT/"scripts/build_device_database.py","--source",ROOT/"models/THE_LIST.md","--output",database)
    comparisons=DEST/"data"/"comparisons.json"; run(ROOT/"scripts/build_comparison_engine.py","--schema",ROOT/"comparisons/schema.json","--data-dir",ROOT/"comparisons/data","--output",comparisons)
    caps=DEST/"data"/"finder-capabilities.json"; run(ROOT/"scripts/build_finder_capabilities.py","--models",ROOT/"models/THE_LIST.md","--comparisons",comparisons,"--overrides",ROOT/"data/finder-capability-overrides.json","--output",caps)
    run(ROOT/"scripts/apply_finder_capabilities.py","--comparisons",comparisons,"--capabilities",caps)
    cards=DEST/"data"/"report-card-scores.json"; run(ROOT/"scripts/build_report_card_scores.py","--input-dir",ROOT/"docs/report-cards","--models",ROOT/"models/THE_LIST.md","--capabilities",caps,"--overrides",ROOT/"data/core-report-card-overrides.json","--output",cards)
    run(ROOT/"scripts/build_site_status.py","--devices",database,"--report-cards",cards,"--output",DEST/"data/site-status.json")
    run(ROOT/"scripts/build_purchase_fallbacks.py","--models",ROOT/"models/THE_LIST.md","--curated",ROOT/"data/purchase-sources.json","--output",DEST/"data/purchase-fallbacks.json")
    run(ROOT/"scripts/build_model_pages.py","--data-dir",DEST/"data","--output-root",DEST)
    run(ROOT/"scripts/build_community_reviews.py","--reviews",ROOT/"data/community-reviews.json","--reviewers",ROOT/"data/community-reviewers.json","--devices",database,"--summary-output",DEST/"data/community-review-summary.json","--profile-root",DEST/"contributors","--index-output",DEST/"docs/COMMUNITY_REVIEWERS.md")
    run(ROOT/"scripts/build_gls_resolver.py","--devices",database,"--output-root",DEST)
    run(ROOT/"scripts/build_citation_distribution.py","--devices",database,"--scores",cards,"--output-root",DEST)
    catalog_index=DEST/"models"/"catalog"/"index.md"
    if catalog_index.exists():
        catalog_index.write_text(catalog_index.read_text(encoding="utf-8")+"\n[Resolve any GLS identifier](/gls/) · [Machine-readable GLS index](/data/gls-index.json)\n",encoding="utf-8")
    run(ROOT/"scripts/build_report_card_hub.py","--devices",database,"--scores",cards,"--aliases",ROOT/"data/lineage-aliases.json","--output",DEST/"docs/REPORT_CARD.md")
    strip_public_infrastructure_narration()
    run(ROOT/"scripts/build_internal_model_links.py","--output-root",DEST)
    run(ROOT/"scripts/build_rss_feed.py","--source",ROOT/"docs/RESEARCH_NEWS.md","--output",DEST/"feed.xml")
    print(f"Staged documentation at {DEST}")
if __name__=="__main__": main()
