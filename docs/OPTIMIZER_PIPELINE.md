# GlassesResearch Optimizer Pipeline

The GlassesResearch optimizer is an execution pipeline, not a presentation-only recommendation list.

## Pipeline states

Priorities should move through explicit states:

`identified -> investigated -> constructed -> PR -> green -> outcome-verified -> merge-qualified -> merged/live`

An item may also be marked `blocked`, `deferred`, `disproven`, or `retired`. Those dispositions should remain visible in the execution ledger so useful findings are not silently lost between optimizer runs.

## Merge-promotion gate

A proposed change qualifies for subsequent merge when all three conditions are satisfied:

1. **Works as intended.** Investigation and implementation demonstrate that the proposal actually satisfies its stated acceptance goal.
2. **Required checks are green.** The CI, build, test, validation, evidence, link, publication, or other checks relevant to the change pass.
3. **The resulting site/repository still functions as intended.** The affected user-facing surfaces, research outputs, publication paths, data products, and operational workflows are verified after integration/build.

Green CI is necessary but not sufficient. The optimizer must also verify the actual resulting behavior.

For ordinary reversible site and repository improvements, there is no blanket PR-review-only bottleneck. Once the three-part promotion gate is proven, the proposal is merge-qualified under standing optimizer authority.

## Authority-sensitive exception

Technical success cannot establish every research or authority judgment. Explicit Pete + ChatGPT review remains required before merge for changes such as:

- canonical model admissions, removals, or disputed identity decisions;
- Report Card scores or scoring-policy changes;
- promotion between evidence/provenance lanes;
- disputed or consequential lineage conclusions;
- material changes to project canon or editorial/publication authority;
- credentials, spending, external commitments, or irreversible actions;
- comparable decisions where a green build cannot prove that the underlying judgment is appropriate.

These changes may still be fully constructed and validated before review; they simply do not become merge-qualified from technical checks alone.

## Optimizer run behavior

Each optimizer run should:

1. Review the live site, repository state, open issues/PRs, and the prior optimizer execution ledger before proposing work.
2. Survey relevant external smart-glasses, XR, optics, vendor, research, news, database, comparison, developer, enthusiast, and adjacent sources when they can reveal meaningful improvements.
3. Add new opportunities to the durable pipeline rather than replacing the prior list.
4. Re-rank active work by expected value, evidence strength, implementation risk, and effort.
5. Reuse or refresh existing issues/PRs instead of duplicating them.
6. Construct worthwhile independent improvements and validate them.
7. Advance green, outcome-verified, non-authority-sensitive work through merge when the promotion gate is satisfied.
8. Re-check the live/resulting site after merge when the change affects public or operational behavior.
9. Preserve blocked, deferred, disproven, and lower-ranked findings with concise dispositions.

## Evidence and trust invariants

The pipeline never weakens GlassesResearch evidence standards for speed. Unknown stays unknown. Hands-on, primary-source, commercial, community, inferred, hypothesis, disproven, and unknown evidence lanes remain distinct. The optimizer must not add tracking, cookies, affiliate incentives, keyword stuffing, backlink schemes, fabricated freshness, or unverified claims merely to advance a priority.

The purpose of the pipeline is faster validated progress, not lower standards.
