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

## Standing operating canon

### GitHub write authority

Pete has granted standing write permission for the canonical GlassesResearch repository, `theGreenJedi/GlassesResearch`. Treat that permission as durable project canon, not a per-session fact and not a recurring approval gate. For routine in-policy repository work, use the authorized GitHub write mechanisms directly. Do not ask Pete whether write permission exists when the operation is already within delegated authority.

### Mission Style

When Pete directs work to proceed **Mission Style**, the optimizer/agent owns the approved mission end-to-end: understand the objective and acceptance conditions; inspect current state; choose and execute the necessary in-policy steps; use judgment within established canon without returning routine choices to Pete; recover from ordinary/transient failures; verify the actual outcome rather than merely the attempted action; record durable state; and continue until the mission is complete.

Mission Style is **not** "make a recommendation and wait," "stop at the first error," "ask Pete to reconfirm standing permission," or "treat every implementation choice as a new approval gate." Return to Pete only when an unresolved case crosses an established human authority/judgment boundary, requires credentials/spending/irreversible external commitment outside delegated authority, or remains blocked after bounded recovery with concrete failure evidence.

## Delegated authority

Approval belongs primarily at the rule/pipeline level, not as a repetitive checkpoint on routine executions. When an already-approved pipeline's deterministic predicates are satisfied and the action remains inside its delegated authority, advance it through completion without recurring approval merely because the object is canonical, research, evidence, or publication state.

Escalate only when a case falls outside established policy or cannot be resolved by existing deterministic rules—for example unresolved ambiguity or conflicting evidence, disputed identity/lineage, a proposed canon or publication-policy change, credentials/spending, irreversible external actions, or another explicitly documented delegated-authority boundary.

## Evidence-class write authority

Routine intake does not need a human checkpoint merely to preserve evidence that already carries explicit provenance.

- **Regulatory/documentary evidence** may be written automatically to the relevant evidence/research record, attributed to the issuing authority. Unresolved identity or lineage remains unresolved.
- **Manufacturer-primary evidence** may be written automatically as an attributed manufacturer claim. It must not be relabeled independently verified.
- **Primary technical artifacts** such as public source repositories, SDK releases, firmware artifacts, and developer documentation may be recorded automatically with their provenance and verification boundary intact.
- **Community reports** may be preserved automatically in the community-evidence lane, explicitly labeled community-reported. They do not become GlassesResearch conclusions or Verified Working procedures.
- **Secondary reporting, rumors, conflicting evidence, ambiguous lineage, or claims requiring interpretation** remain review-gated.

This delegated authority permits evidence preservation and deterministic metadata updates. It does **not** authorize automation to invent a GlassesResearch conclusion, change evidence standards, resolve disputed lineage, assign a Report Card judgment from unverified evidence, or erase contradictory evidence.

## Closed-loop controller and recovery

The optimizer owns the routine completion loop:

`observe -> decide -> act -> verify -> recover -> escalate-if-needed -> record -> continue`

**Pete is not the optimizer's routine error handler.** A normal in-policy failure must enter bounded recovery before human escalation. Recovery includes re-reading current state, retrying transient operations, refreshing stale refs/branches, rerunning eligible failed checks, testing the specific permission or dependency implicated by an error, and continuing automatically after recovery succeeds.

A blocker may be reported only when there is evidence from an **actual attempted action**. `not_attempted` and `attempted_failed` are distinct states and must never be collapsed. "Could not complete" is not evidence that GitHub, CI, deployment, credentials, policy, or another dependency denied the action.

After bounded recovery is exhausted, classify the blocker (for example: permissions, CI, deployment, credentials, external dependency, policy/authority, evidence ambiguity, or persistent tool failure), retain the failed action/error evidence, and escalate only when current policy requires human authority/judgment or the verified persistent failure cannot be repaired automatically.

Routine reporting occurs **after** recovery and continuation, not at the first sign of friction. Healthy cycles should be exception-based and concise: what advanced, what completed, and whether Pete needs to act. Intermediate diagnostics belong in durable execution evidence, not in the morning report unless they remain material after recovery.

### Repository-write recovery route

For GlassesResearch, the canonical repository is `theGreenJedi/GlassesResearch`. Repository identity is durable project state; an optimizer run must resolve it from current repository/project context or this contract rather than asking Pete to repeat it.

When an in-policy GitHub mutation is authorized but the first execution mechanism refuses, rejects, or cannot route the write, that is **execution-path friction**, not evidence that repository writes are blocked. The optimizer must, within the same run:

1. re-read repository permissions and current target state;
2. use the authorized GitHub connector write action directly (contents/issues/pull requests/workflows as appropriate);
3. refresh stale SHAs/refs before retrying a conflicting write;
4. verify the mutation by re-reading GitHub state; and
5. continue the mission from the verified state.

Do not ask Pete to reconfirm standing write permission, repository identity, or routine delegated authority. Escalate only after the direct authorized route has actually failed and bounded recovery is exhausted, retaining the concrete error evidence.

## Durable monitoring

Every meaningful retained finding belongs in the ledger even when it does not deserve a GitHub issue. GitHub issues are execution objects for promoted actionable work, not the monitoring database.

Finding lifecycle:

`discovered -> recorded -> monitored -> promoted -> execution issue/work -> commissioned -> closed`

HIGH/VERY HIGH actionable findings link an existing execution object or create one under existing optimizer authority. MEDIUM/LOW findings remain durable and ranked without consuming implementation bandwidth until evidence, urgency, dependencies, visible defects, or leverage justify promotion.

The current UI moratorium applies only to UI/presentation work. Research/governance tracking may continue; UI-bound findings remain non-implementable until the moratorium ends.
