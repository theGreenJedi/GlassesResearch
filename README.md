# GlassesResearch

Independent research into AI eyeglasses, smart eyewear, and open, user-controlled ecosystems.

**Knowledge over marketing. Evidence over speculation. Openness over lock-in.**

The repository I wish I had when I began.

## Mission

GlassesResearch exists to make scattered information about the W610/W6xx smart-glasses ecosystem easier to find, verify, preserve, and build upon. It will cover hardware, BLE behavior, firmware, SDKs and apps, optics, retail variants, reverse engineering, and user-controlled AI integrations.

## Principles

- **Document before modifying.** Preserve original behavior, evidence, and sources.
- **Verify claims.** Separate confirmed findings from hypotheses and open questions.
- **Attribute sources.** Credit vendors, researchers, community posts, and archived materials.
- **Prefer user control.** Explore local-first and vendor-independent integrations.
- **Avoid needless rediscovery.** Record repeatable procedures and prior results.

## Model chapters

Each glasses model receives its own self-contained chapter under [`models/`](models/README.md). Device-specific hardware, BLE research, firmware, applications, manufacturing intelligence, diagnostics, diagrams, schematics, evidence, resources, and research history remain together inside that model's hierarchy.

### Current model

- [`models/W610/`](models/W610/README.md) — dedicated W610 research chapter

Shared documents remain available for cross-model methods and repository-wide guidance.

## Repository map

- [`models/`](models/README.md) — model-specific research chapters
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

This repository is in its initial documentation phase. Early work will establish a reliable device baseline, preserve source material, and document repeatable experiments.

## Contributing

Contributions should clearly distinguish observed facts, sourced claims, interpretations, and hypotheses. Include reproduction steps whenever possible.

## Safety and legal note

Research only hardware and software you are authorized to inspect. Do not publish credentials, personal data, proprietary secrets, or material whose distribution is prohibited.
