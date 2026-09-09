# GlassesResearch Optimizer Pipeline

The GlassesResearch optimizer is an execution pipeline, not a presentation-only recommendation list.

## Priority grades

Every meaningful optimizer finding receives a priority grade independently of its pipeline state:

- **VERY HIGH** — material user/research value, reliability, evidence integrity, freshness, coverage, or leverage; strong evidence; actionable now; risk and effort are justified by the expected gain. Enters the active execution pipeline by default.
- **HIGH** — clearly worthwhile and well-supported, with meaningful expected value and acceptable implementation risk/effort. Enters the active execution pipeline when actionable and not blocked by a higher-order dependency.
- **MEDIUM** — useful but not currently important enough to consume implementation bandwidth. Retain in the monitored backlog and promote if new evidence, urgency, dependencies, visible defects, or leverage materially increase its value.
- **LOW** — marginal, speculative, duplicative, disproportionately costly, or weakly evidenced. Preserve only when it may become useful later; otherwise retire with a concise disposition.

Priority is not permanence. Each optimizer run should regrade findings when conditions change. A MEDIUM item can become VERY HIGH after a visible failure; a HIGH item can fall to MEDIUM after another change solves most of the problem.

Only **VERY HIGH** and **HIGH** findings are active implementation priorities by default. MEDIUM and LOW findings belong in future monitoring rather than the construction queue.

## Pipeline states

Priorities should move through explicit states:

`identified -> investigated -> constructed -> PR -> green -> outcome-verified -> merge-qualified -> merged/live`

An item may also be marked `blocked`, `deferred`, `disproven`, or `retired`. Those dispositions should remain visible in the execution ledger so useful findings are not silently lost between optimizer runs.

Priority grade and pipeline state are separate dimensions. For example, a VERY HIGH item can be `blocked`, while a MEDIUM item can be `investigated` but intentionally left out of construction.

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
4. Grade or regrade each finding as VERY HIGH, HIGH, MEDIUM, or LOW using expected value, evidence strength, urgency, implementation risk, and effort.
5. Keep VERY HIGH/HIGH findings in the active execution queue; keep MEDIUM/LOW findings in a concise ranked monitoring backlog unless promoted by changed conditions.
6. Reuse or refresh existing issues/PRs instead of duplicating them.
7. Construct worthwhile independent active improvements and validate them.
8. Advance green, outcome-verified, non-authority-sensitive work through merge when the promotion gate is satisfied.
9. Re-check the live/resulting site after merge when the change affects public or operational behavior.
10. Preserve blocked, deferred, disproven, retired, and monitored findings with concise dispositions.

## Evidence and trust invariants

The pipeline never weakens GlassesResearch evidence standards for speed. Unknown stays unknown. Hands-on, primary-source, commercial, community, inferred, hypothesis, disproven, and unknown evidence lanes remain distinct. The optimizer must not add tracking, cookies, affiliate incentives, keyword stuffing, backlink schemes, fabricated freshness, or unverified claims merely to advance a priority.

The purpose of the pipeline is faster validated progress on the work that matters most, not lower standards or indiscriminate implementation.
