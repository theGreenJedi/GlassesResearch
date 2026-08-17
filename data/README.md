# GlassesResearch Data

GlassesResearch publishes machine-readable research alongside the human-readable site. The public dataset is generated from the same validated catalog, comparison, Finder, Report Card, evidence, and ecosystem sources used to build the site; it is not a separate stronger source of claims.

## Canonical public exports

- `/data/public/models.json` — aggregate canonical model dataset.
- `/data/public/models.csv` — flat catalog-oriented export for spreadsheets and analysis.
- `/data/public/models/gls-####.json` — one canonical bundle for each active stable model ID.
- `/data/public/schema.json` — JSON Schema for each per-model bundle.
- `/data/public/evidence-resources.json` — stable evidence-resource registry included beside the model export.

The existing lower-level endpoints remain public:

- `/data/devices.json` — canonical identity/catalog records.
- `/data/comparisons.json` — normalized field-by-field comparison research.
- `/data/finder-capabilities.json` — four-state Finder capability matrix.
- `/data/report-card-scores.json` — extracted Report Card dimensions.
- `/data/ecosystem-relations.json` — evidence-backed ecosystem graph.

## Provenance semantics

A claim in the public model export carries its recorded evidence state and source list. The schema also has `confidence` and `verified_at` fields so future research can record those values at claim level. Existing records do not receive invented confidence or dates: where the underlying claim does not yet contain them, those fields are `null`.

Relationship records retain their existing evidence, provenance, confidence, and status. Finder capabilities retain their own provenance. These layers are kept distinct because a generated convenience bundle must not erase where a conclusion came from.

## Stable identity and versioning

Model identity is anchored to permanent `GLS-####` identifiers. Retired identifiers are not reused. The export and per-model schema carry their own `schema_version`; consumers should key on stable IDs and schema versions rather than array position.

## Reuse

The JSON export is intended for software, research notebooks, search tools, archival work, and downstream analysis. The CSV export is intentionally narrower and contains identity plus canonical public paths; richer claim provenance remains in JSON.

When citing a factual claim, prefer the underlying source in addition to the GlassesResearch model record. `Unknown`, `N/A`, and a verified negative remain different states.
