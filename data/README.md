# GlassesResearch Data

GlassesResearch publishes machine-readable research alongside the human-readable site. The public dataset is generated from the same validated catalog, comparison, Finder, Report Card, evidence, ecosystem, and lineage sources used to build the site; it is not a separate stronger source of claims.

The human-facing entry point is the [GlassesResearch Open Smart-Glasses Dataset](../dataset/index.md).

## Canonical public exports

- `/data/public/models.json` — aggregate canonical model dataset.
- `/data/public/models.csv` — flat catalog-oriented export for spreadsheets and analysis.
- `/data/public/models/gls-####.json` — one canonical bundle for each active stable model ID.
- `/data/public/lineages.json` — validated family/branch context for mapped canonical models.
- `/data/public/relationships.json` — stable `GLR-*` lineage relationship records and evidence paths.
- `/data/public/manifest.json` — content-addressed dataset version, counts, license, semantics, and file checksums.
- `/data/public/SHA256SUMS.txt` — SHA-256 checksum inventory for the complete current export.
- `/data/public/releases/grd-.../` — content-addressed copy of the current core aggregate release.
- `/data/public/schema.json` — JSON Schema for each per-model bundle.
- `/data/public/evidence-resources.json` — stable evidence-resource registry included beside the model export.

The existing lower-level endpoints remain public:

- `/data/devices.json` — canonical identity/catalog records.
- `/data/comparisons.json` — normalized field-by-field comparison research.
- `/data/finder-capabilities.json` — four-state Finder capability matrix.
- `/data/report-card-scores.json` — extracted Report Card dimensions.
- `/data/lineage-index.json` — identity/relationship-only lineage intelligence used internally by search, Finder, community evidence, and the open dataset.
- `/data/ecosystem-relations.json` — evidence-backed ecosystem graph.

## Provenance semantics

A claim in the public model export carries its recorded evidence state and source list. The schema also has `confidence` and `verified_at` fields so future research can record those values at claim level. Existing records do not receive invented confidence or dates: where the underlying claim does not yet contain them, those fields are `null`.

Relationship records retain their existing evidence, provenance, confidence, and status. Finder capabilities retain their own provenance. Lineage context is identity/relationship information only: family membership, predecessors, successors, aliases, and rebrands never transfer specifications, firmware behavior, verification status, community observations, or Report Card scores between models.

## Stable identity and versioning

Model identity is anchored to permanent `GLS-####` identifiers. Retired identifiers are not reused. Lineage relationships use stable `GLR-*` identifiers so the relationship itself can be cited or challenged.

Each complete public export receives a content-derived `GRD-*` version. The version is calculated from SHA-256 checksums of the generated export; unchanged content therefore retains the same dataset version. `manifest.json` and `SHA256SUMS.txt` let a consumer prove exactly which release was used.

## Reuse

The JSON export is intended for software, research notebooks, search tools, archival work, journalism, retrieval systems, and downstream analysis. The CSV export is intentionally narrower and contains identity plus canonical public paths; richer claim provenance remains in JSON.

When citing a factual claim, prefer the underlying source in addition to the GlassesResearch model or relationship record. `Unknown`, `N/A`, and a verified negative remain different states.
