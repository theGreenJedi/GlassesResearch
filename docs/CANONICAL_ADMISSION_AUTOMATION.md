# Canonical Admission Automation

GlassesResearch uses automation to remove repetitive approval work without delegating ambiguous research judgment.

The canonical catalog is a real-world smart-glasses identity ledger. A clean admission says only that a distinct smart-glasses model has a sufficiently stable identity and credible evidence that real hardware exists or existed beyond a concept/render. Public purchasability is metadata, not an admission threshold. It does not make the product good, current everywhere, independently tested, open, private, repairable, supported, or recommended.

## The boring-certainty lane

A model may receive a GLS ID automatically only when every deterministic gate passes:

1. The Models investigator has current canonical catalog context and concludes `verified_new_model` with `high` confidence.
2. The proposal has no existing GLS target, identity edge, unresolved question, contradictory evidence, merge/split question, alias/rebadge question, or other unresolved identity relationship.
3. The device has credible evidence of real hardware: documented production, deployment, field/pilot use, paid acquisition, enterprise/developer procurement, or another direct real-world hardware path. Concepts, rumors, renders, and unnamed/insufficiently evidenced devices do not qualify.
4. The real-world existence path is supported by high-confidence primary, retailer, regulatory, or independently attributable evidence carried in the proposal.
5. The proposal supplies a complete structured canonical row: maker, model, exact evidence era, lifecycle state, type, access basis, and source URL. Lifecycle and access are separate facts; for example `deployed` + `closed/internal` or `current` + `retail`.
6. The row source is evidence establishing the qualifying real-world hardware path.
7. The current ledger has neither the exact maker/model nor the same acquisition source attached to an existing canonical row.
8. The generated reconciliation packet, conservative profile, synchronized ledger, strict profile coverage, public device database, site build, link checks, and required PR checks all pass.
9. The `main` commit used for GLS allocation is still current immediately before merge.

If any condition fails, the automation does nothing canonical. The candidate remains ordinary research/review work.

## Scope of this lane

This admission lane itself does not perform:

- removals or retirements;
- alias, rebadge, merge, split, or disputed lineage decisions;
- identity corrections to existing GLS records;
- admissions with uncertain identity, source, form factor, real-world existence, or product boundary;
- Report Card scoring;
- promotion between provenance/evidence classes;
- privacy, openness, owner-control, cloud-independence, durability, support, value, or hands-on conclusions.

That scope boundary does **not** create a blanket human-approval requirement for those categories. They may be handled by another already-approved deterministic pipeline when one exists. A case escalates only when its governing pipeline cannot resolve the evidence/judgment, the case falls outside delegated authority, or the governing policy itself would need to change.

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
