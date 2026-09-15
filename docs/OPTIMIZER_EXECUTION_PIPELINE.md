# Optimizer Execution Pipeline

This document is the durable handoff for the GlassesResearch optimizer. It prevents useful findings from disappearing between runs and prevents the same recommendation from being rediscovered without execution.

## Source of truth

The machine-readable institutional memory is [`research/OPTIMIZER_LEDGER.yaml`](../research/OPTIMIZER_LEDGER.yaml). Before proposing or advancing optimizer work, reconcile the run against that ledger: update an equivalent existing subject rather than duplicating it, regrade when conditions materially change, and retain disposition/history when work is demoted, superseded, commissioned, or closed.

The ledger is internal and is **not** a public Research page. It may incubate subjects that later graduate into public Research.

## Research graduation

**Research is the umbrella. Community Research is subordinate to Research as a source/evidence lane.** A subject may graduate into Research because GlassesResearch needs to investigate it or because GlassesResearch is actively investigating it; completion is not a prerequisite.

Canonical research states are:

`needs_investigation -> under_investigation -> findings_established`

Community, documentary/regulatory, manufacturer, commercial, GR-lab, inferred, hypothesis, disproven, and unknown evidence remain distinguishable. A community-originated finding can become a broader GlassesResearch research subject and later gain documentary or independent GR-lab evidence without rewriting its provenance.

## Promotion rule

Lifecycle:

`identified -> investigated -> constructed -> PR -> green -> outcome-verified -> merge-qualified -> merged/live`

A normal reversible change becomes merge-qualified only when all three are proven:

1. it works as intended against the stated acceptance goal;
2. all required CI/build/test/validation checks relevant to the change are green; and
3. the resulting site/repository still functions as intended after integration/build, including affected user-facing behavior, publication paths, research surfaces, and operational workflows.

Green CI is necessary but not sufficient. Outcome verification is part of the gate.

After merge, verify the live/public result when applicable and record the disposition in the pipeline/ledger.

## Commissioning interpretation

A merge proves code integration; it does not prove the mission succeeded. Treat `implemented`, `integrated`, `commissioned`, and `operational` as distinct states. **Built means commissioned. Operational means commissioned and observably continuing to work.**

## Delegated authority

Approval belongs primarily at the rule/pipeline level, not as a repetitive checkpoint on routine executions. When an already-approved pipeline's deterministic predicates are satisfied and the action remains inside its delegated authority, advance it through completion without recurring approval merely because the object is canonical, research, evidence, or publication state.

Escalate only when a case falls outside established policy or cannot be resolved by existing deterministic rules—for example unresolved ambiguity or conflicting evidence, disputed identity/lineage, a proposed canon or publication-policy change, credentials/spending, irreversible external actions, or another explicitly documented delegated-authority boundary.

## Durable monitoring

Every meaningful retained finding belongs in the ledger even when it does not deserve a GitHub issue. GitHub issues are execution objects for promoted actionable work, not the monitoring database.

Finding lifecycle:

`discovered -> recorded -> monitored -> promoted -> execution issue/work -> commissioned -> closed`

HIGH/VERY HIGH actionable findings link an existing execution object or create one under existing optimizer authority. MEDIUM/LOW findings remain durable and ranked without consuming implementation bandwidth until evidence, urgency, dependencies, visible defects, or leverage justify promotion.

The current UI moratorium applies only to UI/presentation work. Research/governance tracking may continue; UI-bound findings remain non-implementable until the moratorium ends.
