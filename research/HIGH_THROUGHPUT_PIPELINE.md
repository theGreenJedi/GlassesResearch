# High-Throughput Model Research Workflow

This workflow accelerates the Report-Card-first methodology without lowering its evidentiary standard.

## Production unit

The default production unit is **12–20 models per research batch**, preferably grouped by manufacturer or hardware lineage. Small four-model PRs are reserved for unusually difficult or heterogeneous research.

A normal batch uses one branch, one research pass, one grading pass, one editorial pass, one PR, and one merge.

## Pipeline

`Select lineage packet → harvest sources → normalize canonical facts → grade all models → audit/generate paragraphs → one PR → one merge`

### 1. Select a lineage packet

Prefer related models whose manufacturer documentation, SDKs, support pages, architecture, or product history overlap. Shared evidence may establish family architecture, but generation-specific scores still require generation-specific evidence where hardware or capabilities materially differ.

### 2. Harvest evidence in parallel

Collect the primary-source pack for the entire batch before grading individual models. Reuse verified manufacturer-level documentation instead of rediscovering the same SDK, support page, or platform architecture for each generation.

Evidence priority remains:

1. manufacturer/developer documentation and manuals
2. SDK/API/firmware/source repositories
3. regulatory or archived first-party material
4. credible independent testing
5. commercial/secondary evidence when primary material is unavailable
6. GlassesResearch hands-on observations, clearly identified as such

### 3. Normalize canonical facts

For every model, reconcile the canonical listing against the source pack before scoring. Corrections to generation, date, capabilities, state, lineage, or access are part of the same batch.

### 4. Grade as a dedicated pass

After evidence collection is complete, apply the shared catalog-wide 0–10 ruler to every model. Do not alternate repeatedly between source discovery and grading when the evidence can be harvested as a family.

- `N/A` remains reserved for genuinely inapplicable dimensions.
- `Not yet graded` means the dimension applies but evidence is insufficient.
- Unknown specifications remain unknown; speed never justifies inference.

### 5. Editorial pass in the same batch

Once the Report Cards are complete, immediately audit existing public paragraphs against them. Preserve accurate substantive prose. Rewrite only when research changes or sharpens the conclusion. Create a paragraph when none exists.

The paragraph remains an output of the evidence and Report Card, not a substitute for them.

### 6. Difficult-model queue

A poorly documented model must not block an otherwise strong batch. Move models requiring archival work, uncertain OEM identification, dead manufacturer pages, contradictory evidence, or difficult regional sourcing into a separate investigation-heavy queue. Record the reason and continue the fast/evidence-rich queue.

### 7. Repository transaction budget

For a normal 12–20 model packet:

- one working branch
- one evidence/report-card package (or one structured data set plus generated rendering)
- editorial updates in the same branch
- one PR
- one verified merge

Avoid separate PRs for source gathering, grading, and paragraph generation unless a substantive review boundary requires it.

## Structured-data direction

Report Cards should migrate toward machine-readable per-model records containing:

- stable GLS ID
- canonical identity and lineage
- ten dimension scores/statuses
- evidence notes per dimension
- primary-source URLs
- canonical corrections
- editorial audit state

Markdown tables/pages should eventually be rendered from those records so research effort is spent on evidence and judgment rather than repeated table formatting.

## Quality invariant

**Speed comes from eliminating duplicated work, not lowering the research bar.**

The common ruler, traceable evidence, canonical corrections, explicit unknowns, and evidence-derived editorial prose remain mandatory regardless of batch size.
