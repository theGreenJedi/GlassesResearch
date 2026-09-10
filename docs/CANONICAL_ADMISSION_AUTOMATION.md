# Canonical Admission Automation

GlassesResearch uses automation to remove repetitive approval work without delegating ambiguous research judgment.

The canonical catalog is a purchaser-history identity ledger. A clean admission says only that a distinct smart-glasses product has a sufficiently stable identity and crossed a documented acquisition threshold. It does not make the product good, current everywhere, independently tested, open, private, repairable, supported, or recommended.

## The boring-certainty lane

A model may receive a GLS ID automatically only when every deterministic gate passes:

1. The Models investigator has current canonical catalog context and concludes `verified_new_model` with `high` confidence.
2. The proposal has no existing GLS target, identity edge, unresolved question, contradictory evidence, merge/split question, alias/rebadge question, or other unresolved identity relationship.
3. The device crossed purchaser history through paid purchase, paid preorder, paid crowdfunding, or documented enterprise/developer procurement that actually makes hardware obtainable.
4. The acquisition route is supported by high-confidence primary or retailer evidence carried in the proposal.
5. The proposal supplies a complete structured canonical row: maker, model, exact acquisition era, state, type, access basis, and source URL.
6. The row source is the same evidence that establishes the qualifying acquisition path.
7. The current ledger has neither the exact maker/model nor the same acquisition source attached to an existing canonical row.
8. The generated reconciliation packet, conservative profile, synchronized ledger, strict profile coverage, public device database, site build, link checks, and required PR checks all pass.
9. The `main` commit used for GLS allocation is still current immediately before merge.

If any condition fails, the automation does nothing canonical. The candidate remains ordinary research/review work.

## What is deliberately not automatic

The lane does not automatically perform:

- removals or retirements;
- alias, rebadge, merge, split, or disputed lineage decisions;
- identity corrections to existing GLS records;
- admissions with uncertain era, source, form factor, acquisition status, or product boundary;
- Report Card scoring;
- promotion between provenance/evidence classes;
- privacy, openness, owner-control, cloud-independence, durability, support, value, or hands-on conclusions.

Those are judgment-bearing decisions and remain subject to the normal authority-sensitive review path.

## Stable-ID race safety

GLS IDs are allocated from a snapshot of current `main`. The automatic workflow records that exact base commit before allocation. After the candidate PR passes checks, the workflow fetches `main` again. If the base changed for any reason, the PR is closed and its branch is discarded. The next scheduled run starts over against the new canonical ledger.

The automation never rebases a preallocated GLS ID across a moving canonical base.

## Audit trail

Every automatic admission leaves the same durable artifacts expected from a manually researched admission:

- the source model-proposal package;
- an `AUTO` dated reconciliation packet recording the gate proof and evidence;
- a conservative admission profile;
- the mechanically synchronized canonical row and derived catalog metadata;
- the GitHub pull request and CI history.

The mechanism is intentionally auditable. Automation removes the redundant click, not the evidence trail.
