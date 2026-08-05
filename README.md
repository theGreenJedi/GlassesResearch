# GlassesResearch

Independent research into AI eyeglasses, smart eyewear, and open, user-controlled ecosystems.

**Knowledge over marketing. Evidence over speculation. Openness over lock-in.**

The repository I wish I had when I began.

## Start here

- [`WHY.md`](WHY.md) — why this project exists and what success means
- [`docs/PROJECT_VISION.md`](docs/PROJECT_VISION.md) — what GlassesResearch is building
- [`docs/ECOSYSTEM_SCOPE.md`](docs/ECOSYSTEM_SCOPE.md) — ecosystem-wide scope and evidence lanes
- [`models/CATALOG.md`](models/CATALOG.md) — populated cross-ecosystem model registry
- [`docs/faq/README.md`](docs/faq/README.md) — 100 current smart-glasses questions and evidence-aware answers
- [`docs/REPOSITORY_LAWS.md`](docs/REPOSITORY_LAWS.md) — no orphan knowledge, no empty merges, and other operating rules
- [`docs/INVESTIGATION_WORKFLOW.md`](docs/INVESTIGATION_WORKFLOW.md) — how investigations become durable pull requests
- [`glossary/README.md`](glossary/README.md) — canonical homes for recurring organizations, components, applications, standards, and other entities
- [`models/W610/resources/RESEARCH_PORTAL.md`](models/W610/resources/RESEARCH_PORTAL.md) — annotated, clickable routes for further W610 research
- [`models/W610/QUESTIONS.md`](models/W610/QUESTIONS.md) — enter the W610 chapter through the question you are trying to answer
- [`docs/EVIDENCE_STANDARD.md`](docs/EVIDENCE_STANDARD.md) — claim status, confidence, sourcing, and correction rules
- [`models/W610/RESEARCH_BACKLOG.md`](models/W610/RESEARCH_BACKLOG.md) — the living investigation queue

## Mission

GlassesResearch exists to make scattered information across the smart-glasses ecosystem easier to find, verify, preserve, and build upon. It covers potentially hundreds of models across hardware, BLE behavior, firmware, SDKs and apps, optics, retail variants, reverse engineering, manufacturing intelligence, community resources, and user-controlled AI integrations. The W610 is the current hands-on reference device, not the repository boundary.

## Principles

- **Document before modifying.** Preserve original behavior, evidence, and sources.
- **Verify claims.** Separate confirmed findings from hypotheses and open questions.
- **Attribute sources.** Credit vendors, researchers, community posts, and archived materials.
- **Prefer user control.** Explore local-first and vendor-independent integrations.
- **Avoid needless rediscovery.** Record repeatable procedures and prior results.
- **Preserve corrections.** Mark disproven claims and retain the reasoning trail.
- **No orphan knowledge.** Give recurring entities one canonical home and link back to it.
- **No empty merges.** New structure must provide immediate value.

## Model chapters

Each glasses model receives its own self-contained chapter under [`models/`](models/README.md). Device-specific hardware, BLE research, firmware, applications, manufacturing intelligence, diagnostics, diagrams, schematics, evidence, resources, questions, chronology, genealogy, and research history remain together inside that model's hierarchy.

### Registry and current hands-on model

- [`models/CATALOG.md`](models/CATALOG.md) — cross-ecosystem registry with real starting sources
- [`models/W610/`](models/W610/README.md) — current hands-on reference chapter

Shared entities and repository-wide methods remain in canonical locations such as [`glossary/`](glossary/README.md) and [`docs/`](docs/).

## Repository map

- [`models/`](models/README.md) — model-specific research chapters and ecosystem registry
- [`AGENTS.md`](AGENTS.md) — standing directives for every future engineering session
- [`docs/ECOSYSTEM_SCOPE.md`](docs/ECOSYSTEM_SCOPE.md) — model-agnostic scope and evidence lanes
- [`docs/faq/README.md`](docs/faq/README.md) — buyer, use-case, technical, privacy, accessibility, and development FAQ
- [`glossary/`](glossary/README.md) — canonical homes for recurring entities
- [`docs/PROJECT_VISION.md`](docs/PROJECT_VISION.md) — repository mission and intended visitor experience
- [`docs/REPOSITORY_LAWS.md`](docs/REPOSITORY_LAWS.md) — daily engineering rules
- [`docs/INVESTIGATION_WORKFLOW.md`](docs/INVESTIGATION_WORKFLOW.md) — investigation and pull-request process
- [`docs/KISS_WORKING_NOTES.md`](docs/KISS_WORKING_NOTES.md) — future subject-independent framework notes that do not block GlassesResearch
- [`docs/EVIDENCE_STANDARD.md`](docs/EVIDENCE_STANDARD.md) — evidence and confidence rules
- [`docs/Hardware.md`](docs/Hardware.md) — shared physical research methods and initial notes
- [`docs/BLE.md`](docs/BLE.md) — shared discovery and protocol methodology
- [`docs/Firmware.md`](docs/Firmware.md) — firmware acquisition, preservation, and analysis guidance
- [`docs/SDK.md`](docs/SDK.md) — vendor apps, SDKs, APIs, and integration notes
- [`docs/AmazonModels.md`](docs/AmazonModels.md) — retail listings and model-family comparisons
- [`docs/ReverseEngineering.md`](docs/ReverseEngineering.md) — methodology and reproducible experiment guidance
- [`docs/AI610-Notes.md`](docs/AI610-Notes.md) — private-notebook findings prepared for public documentation
- [`docs/ResearchLog.md`](docs/ResearchLog.md) — repository-wide dated engineering notes
- [`images/`](images/) — shared photographs, screenshots, diagrams, and other visual evidence

## Evidence workflow

Visual evidence should be preserved alongside written observations rather than treated as decoration. Each photo set should have a dated folder and a short index describing what each image shows, where it came from, and whether it is original evidence or a third-party source.

Recommended naming pattern:

```text
images/YYYY-MM-DD-topic/
```

Model-specific evidence should normally be stored inside the appropriate model chapter, such as:

```text
models/W610/evidence/photos/YYYY-MM-DD-topic/
```

See [`images/README.md`](images/README.md) for naming, provenance, privacy, and cataloging guidance.

## Current status

This repository is actively converting investigations into useful, cross-linked knowledge across the smart-glasses ecosystem. The W610 chapter is the current hands-on reference implementation; the model registry provides the growth path for devices not yet physically available to maintainers.

## Contributing

Contributions should clearly distinguish observed facts, sourced claims, interpretations, hypotheses, and disproven claims. Include reproduction steps whenever possible and follow the evidence standard, repository laws, and investigation workflow.

## Safety and legal note

Research only hardware and software you are authorized to inspect. Do not publish credentials, personal data, proprietary secrets, or material whose distribution is prohibited.
