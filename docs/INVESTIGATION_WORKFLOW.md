# Investigation Workflow

Investigations are the engine that grows GlassesResearch.

## Investigation record

Each investigation should have a stable identifier and a dedicated page, for example:

```text
models/W610/investigations/002-ble-reconnaissance.md
```

The page should contain:

- **Question:** What are we trying to learn?
- **Scope:** Which model, revision, software version, or artifact is included?
- **Status:** Planning, collecting, analyzing, verified, published, superseded, or blocked.
- **Evidence:** What was captured, observed, measured, or sourced?
- **Findings:** What does the evidence directly support?
- **Current conclusion:** What do we presently believe, with confidence and caveats?
- **Disproven paths:** What was tested and rejected?
- **Affected knowledge:** Which glossary, timeline, model, resource, component, firmware, photo, or procedure pages changed?
- **Next questions:** What should be investigated next?

## Pull-request workflow

1. Start from current `main`.
2. Create a branch named for the investigation or coherent change.
3. Gather and preserve evidence before writing strong conclusions.
4. Update every affected canonical page; do not leave discoveries isolated in the investigation narrative.
5. Add new directories only when they are immediately populated.
6. Check every internal and external link.
7. Compare the branch against `main` and confirm no unrelated changes.
8. Open a pull request with a title that states the question answered or capability established.
9. Merge only after the pull request itself clearly explains the evidence, findings, limitations, and remaining work.

## Cross-link checklist

For every newly discovered entity, ask whether it needs links to:

- model chapters;
- investigations;
- glossary pages;
- resources;
- organizations or people;
- components;
- applications or firmware;
- BLE identifiers;
- evidence photographs or captures;
- timeline events;
- diagrams or procedures.

If the entity appears repeatedly, give it a canonical glossary page.

## Completion standard

An investigation is ready to merge when:

- it answers a real question or materially narrows the unknowns;
- the evidence and source quality are visible;
- uncertainty is labeled honestly;
- all new directories contain useful content;
- linkable resources are hyperlinked and annotated;
- repeated entities have canonical homes;
- related pages have been updated;
- the pull request can be understood a year later without relying on chat history.

## After merging

Record new open questions in the backlog or GitHub Issues. Improve the general workflow only when the investigation exposed a real deficiency. Then begin the next investigation.
