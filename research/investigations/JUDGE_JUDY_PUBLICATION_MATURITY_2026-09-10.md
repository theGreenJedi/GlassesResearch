# Judge Judy publication-maturity mission — 2026-09-10

## Question

How can GlassesResearch reach the presentation, navigation, and publishing maturity of the strongest sites in and around the smart-glasses category without weakening the evidence model that makes GlassesResearch distinct?

This mission treats the answer as a publication-design problem, not a request for more research volume. GlassesResearch already has substantial catalog, Report Card, provenance, lineage, community, preservation, and owner-control depth. The gap is making that depth feel immediate, legible, current, and deliberately packaged for a reader who did not arrive through the repository.

## Reference set

### Direct competitors and adjacent research references

- **smartglasses.today** — benchmark for visible news velocity and a front page that feels alive. Its discovery speed is useful as a presentation benchmark; GlassesResearch must preserve the separate Verified and Across the Wire evidence lanes rather than imitate aggregator verification standards.
- **AR Compare** — benchmark for immediate buyer/comparison ergonomics and low-friction product discovery.
- **Smart Glasses Decoded** and **The Near Eye** — benchmarks for category explanation, task-based entrances, and translating a confusing market into reader jobs.
- **AI Glasses Open Database / ai-eyewear.ch** — benchmark for machine-readable provenance discipline, explicit unknowns, and research-data presentation.
- **GlassBench**, **CyanBridge**, and **VRcompare** — useful adjacent references for ecosystem mapping, owner-control/development paths, and comparison patterns.

### Authority and publishing benchmarks, not direct competitors

**WIRED, PCMag, Wareable, UploadVR, and The Verge** are not targets GlassesResearch is trying to defeat as general technology publications. They are reference implementations for mature publishing grammar: headline/deck hierarchy, story cards, feed construction, page rhythm, category architecture, mobile behavior, visual storytelling, related-content paths, and the separation of lead stories from supporting material.

## Judgment

The research substrate is already the stronger part of the product. The next maturity jump should come from editing, hierarchy, visual presentation, task-first navigation, article packaging, and visible freshness — not from adding another forest of destinations.

The governing transformation is:

> **Research institute underneath. Modern specialist publication on top. Exceptional research tool when the reader asks for it.**

## Seven remediations

### 1. Make Research & News a newsroom

The public landing must work before JavaScript enhancement and become richer when structured newsroom and wire state load. It needs a recognizable desk identity, a featured story, verified material, developing signals, topic/job entrances, archive/follow paths, and explicit evidence-state separation.

Implementation surfaces: `docs/RESEARCH_NEWS.md`, `docs/javascripts/research-news-newsroom.js`, `docs/stylesheets/research-news-newsroom.css`, `docs/stylesheets/newsroom-publication-shell.css`, and `docs/stylesheets/publication-maturity.css`.

### 2. Increase homepage hierarchy without increasing homepage inventory

Do not solve presentation problems by adding more sections. Give the lead editorial, live newsroom, Finder, events, and research exploration visibly different jobs. Keep the lead high, place the Finder before secondary event material, and make the main hero actions reader verbs rather than an institutional table of contents.

Implementation surfaces: `README.md`, `scripts/build_verified_change_surfaces.py`, `scripts/feature_community_editorial.py`, and homepage CSS.

### 3. Use task entrances as the site's first language

A visitor should not need to understand Report Cards, canonical IDs, lineages, or Extended Research before beginning a useful task. Task entrances can lead into those deeper structures after the reader has selected a goal.

Implementation surfaces: `README.md`, `docs/START_BY_NEED.md`, and `docs/COMPARISON_ENGINE.md`.

### 4. Make Finder immediate while preserving evidence semantics

Expose obvious presets such as camera-free display, prescription support, documented budget limits, local/offline operation, and direct comparison. Presets must use the same canonical filters as the full Finder, and unknown data must continue to remain unknown rather than being guessed into a match.

Implementation surfaces: `docs/COMPARISON_ENGINE.md`, `data/finder-schema.json`, and the existing generic Finder engine.

### 5. Build a visual vocabulary from evidence

Favor visuals that teach the research: bench photographs, measurements, hardware profiles, screenshots, protocol/evidence maps, relationship diagrams, and technology family trees. For the current Community Research lead, the homepage visual is a compact evidence-route diagram derived from the three attributed projects rather than generic stock art.

Implementation surfaces: `scripts/feature_community_editorial.py` and `docs/stylesheets/publication-maturity.css`. Future hands-on work should feed the same visual system with original bench material.

### 6. Package long-form articles like finished publications

Keep the article body and evidence boundary intact while adding reading time, publication/update status, desk/type, model/topic chips, evidence-state summary, related research routes, correction/challenge access, and a visible Git revision trail. Do not invent a human byline or imply hands-on verification where none exists.

Implementation surfaces: `docs/javascripts/publication-maturity.js` and `docs/stylesheets/publication-maturity.css`.

### 7. Make freshness visible and meaningful

Show publication age on fast-moving newsroom surfaces, keep the catalog's mechanical update date, expose Finder capability and price-observation dates, and retain dated editorial/verified material. A build timestamp is not evidence freshness and must not be presented as one.

Implementation surfaces: homepage wire loader, Research & News presentation, Finder freshness panel, and existing mechanical catalog-status generation.

## Evidence and authority boundary

This mission changes presentation and navigation. It does not introduce new device specifications, Report Card scores, laboratory findings, availability claims, or community findings. The Community Research feature summarizes an already published GlassesResearch editorial and continues to label the underlying work as attributed repository evidence rather than GlassesResearch laboratory verification.

No fragile external resource needed to be newly archived for this mission because the work is a presentation refactor. Existing evidence, articles, structured state, and canonical research remain the substrate.

## Success criteria

- Research & News remains useful when enhancement scripts fail and becomes a richer live desk when structured state is available.
- Homepage order reads as mission/lead/newsroom/Finder before secondary exploration.
- Finder offers obvious task presets without bypassing canonical filters or unknown semantics.
- Long-form articles surface publication metadata, evidence posture, related paths, and revision history without manufacturing authorship.
- Freshness labels derive from research/publication dates, not page-build time.
- The visual language becomes more evidence-derived rather than more decorative.
- Existing verification, provenance, corrections, preservation, and owner-control rules remain unchanged.
