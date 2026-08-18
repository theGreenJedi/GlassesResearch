---
title: "How to Cite GlassesResearch"
description: "Stable citation guidance for GlassesResearch model records, smart-glasses timeline events, research pages, and machine-readable datasets."
---

# How to Cite GlassesResearch

GlassesResearch is designed to be linked, checked, challenged, and reused as a research map. When a specific factual claim matters, cite the underlying primary source as well as the GlassesResearch page that organizes or interprets it.

## Canonical model records

Every cataloged model has a stable `GLS-####` identifier and canonical page.

Preferred form:

> **Manufacturer Model (GLS-####)**, GlassesResearch, https://glassesresearch.org/models/catalog/gls-####/

Use the stable GLS identifier when model names, rebrands, or manufacturer labels may be ambiguous.

### Machine-ready model citations

Every canonical model has citation exports generated from the same stable identity ledger:

- BibTeX: `https://glassesresearch.org/data/citations/gls-####.bib`
- CSL-JSON: `https://glassesresearch.org/data/citations/gls-####.json`
- Citation index: `https://glassesresearch.org/data/citations/index.json`
- Aggregate canonical-model BibTeX: `https://glassesresearch.org/data/citations/glassesresearch-models.bib`

The GitHub repository also publishes a root `CITATION.cff`, allowing GitHub's **Cite this repository** control to provide standardized citation metadata for the project as a whole.

## Industry timeline events

Canonical timeline events have stable `TL-####` identifiers and permalink fragments.

Preferred form:

> **GlassesResearch Smart Glasses Industry Timeline, TL-####**, GlassesResearch, https://glassesresearch.org/docs/INDUSTRY_TIMELINE/#TL-####

For historical claims, also cite the primary source attached to the timeline event whenever practical.

## Research and technical pages

For BLE, firmware, ecosystem, lineage, Report Card, or other research pages, cite the page title and canonical GlassesResearch URL. If the page distinguishes hands-on observations from community or manufacturer evidence, preserve that distinction in your own description of the claim.

## Machine-readable datasets

The preferred reusable model endpoints are:

- Canonical aggregate model dataset: `https://glassesresearch.org/data/public/models.json`
- Flat catalog CSV: `https://glassesresearch.org/data/public/models.csv`
- Per-model bundle: `https://glassesresearch.org/data/public/models/gls-####.json`
- Per-model JSON Schema: `https://glassesresearch.org/data/public/schema.json`
- Evidence-resource registry: `https://glassesresearch.org/data/public/evidence-resources.json`

Lower-level public structured endpoints remain available:

- Canonical device catalog: `https://glassesresearch.org/data/devices.json`
- Comparison data: `https://glassesresearch.org/data/comparisons.json`
- Timeline record: `https://glassesresearch.org/timeline/events.json`
- Live timeline signals: `https://glassesresearch.org/timeline/auto-events.json`

When reproducibility matters, record the access date, schema version, and specific GLS or TL identifiers used rather than relying only on array order or display position. Claim-level `confidence` or `verified_at` values may be `null` when the underlying research has not recorded those values; do not convert missing provenance into certainty.

## Linking, embedding, and reuse

No permission is needed to link to public GlassesResearch pages. Deep links to individual canonical models, timeline events, technical research, evidence records, and comparisons are encouraged when they help readers verify a claim or continue an investigation.

A compact [embeddable model card](EMBED_GLASSESRESEARCH.md) is available for every canonical GLS model. It is static, cookie-free, and links the reader back to the canonical evidence page rather than copying an untraceable rating into another site.

The [Reference Desk](REFERENCE_DESK.md) collects the fastest paths for journalists, researchers, developers, and community writers who need stable identities, data, citations, or evidence.

Do not describe an unresolved GlassesResearch field as a verified negative. `Unknown`, `N/A`, and verified `No` are intentionally different states.

## Corrections

If a cited GlassesResearch claim appears wrong, incomplete, or superseded by stronger evidence, use the [research challenge process](/docs/RESEARCH_CHALLENGES/). Stable identifiers are intended to make corrections easier to discuss without ambiguity.
