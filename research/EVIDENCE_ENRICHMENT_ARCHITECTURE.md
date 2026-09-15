# Evidence Enrichment Architecture

## Mission

GlassesResearch research inputs are not isolated articles. Community observations, documentary/regulatory records, manufacturer material, commercial evidence, developer work, independent testing, and GR lab observations form a shared evidence system that progressively improves what GlassesResearch knows about models, families, platforms, software, ownership, and unresolved questions.

**Research is the umbrella. Community Research is a subordinate evidence/source lane.** Publication is one possible output of research; it is not the terminal purpose of ingestion.

## Core graph

`Sources -> Evidence -> Claims -> Subjects -> Investigations -> Experiments -> Conclusions -> Site outputs`

A source is where information came from. Evidence is the relevant preserved observation/document. A claim is the smallest proposition that can be supported, contradicted, qualified, or left unresolved. A subject is the model/family/platform/app/manufacturer/topic the claim concerns. Investigations and experiments test unresolved claims. Conclusions record the current evidence-weighted state without destroying earlier provenance.

## Model-page completeness contract

For a canonical model, its public model page is ultimately the canonical human-facing dossier for that model. **Every retained model-specific evidence resource must be discoverable from that model page regardless of verification state.** Verification controls labeling and evidentiary weight; it does not control whether retained useful evidence is findable.

If W610 accumulates 100 retained community observations, all 100 remain addressable from the W610 dossier. The page may summarize, group, filter, collapse, paginate, or rank them for usability, but it must not silently discard the underlying 100 resources. A reader must be able to drill from synthesis to the retained evidence and its provenance.

Model-page evidence includes, when present:
- community observations and owner reports;
- documentary/regulatory findings;
- manufacturer claims;
- commercial/availability evidence;
- developer/SDK/protocol findings;
- independent reporting/testing;
- GR lab observations and measurements;
- contradictions and superseded claims;
- unresolved research questions and active investigations.

Each retained item carries its source, date, evidence lane, status/strength, claim, and relevant investigation or conclusion. Community evidence never acquires a verified label merely because it appears on a model page.

The model page therefore becomes progressively richer over the lifetime of the model rather than remaining a frozen article. Its synthesis and Report Card are views over the accumulated dossier; the underlying evidence corpus remains independently discoverable.

**No-orphan invariant:** once useful model-specific evidence is retained, it must have a durable subject link and a model-dossier disposition. It may be rejected from canonical facts, scoring, cross-model propagation, or synthesized editorial conclusions, but it may not disappear merely because it is unverified.

Public model pages may expose retained unverified/community/contradicted material **as evidence**, with explicit provenance/status labels. That is distinct from publishing those claims as verified editorial conclusions. The UI renderer must preserve that distinction when implemented after the UI moratorium.

## Evidence lanes

- `community` — owner/developer/community reports. Valuable leads; not independent GR verification.
- `documentary_regulatory` — FCC/regulatory filings, manuals, court records, standards, archived documentation.
- `manufacturer` — first-party product/support/marketing claims.
- `commercial` — retailer, distributor, availability and price evidence.
- `developer` — SDK/API/repository/protocol/tooling evidence, with first-party/community distinction preserved.
- `independent` — credible third-party testing/reporting.
- `gr_lab` — reproducible GlassesResearch hands-on observation or measurement.
- `inferred` / `hypothesis` / `unknown` / `disproven` — explicit epistemic states; never silently promoted to fact.

## Claim destinations

A useful claim can inform more than one destination while remaining one provenance-bearing claim:

1. **Canonical model data** — identity, aliases, lineage, capabilities, compatibility, availability and other canonical facts when evidence is strong enough.
2. **Model research dossier** — living evidence, contradictions, unresolved questions, reproduction status, and research history. For model-specific retained evidence this destination is mandatory; its public model page is the eventual human-facing view of this corpus.
3. **Report Card evidence** — evidence may support/reopen a dimension; it does not silently rewrite a score.
4. **Cross-model knowledge** — family/platform/app/chipset/manufacturer findings can attach once and affect multiple models through explicit relationships.
5. **Research queue** — unresolved or consequential claims can become `needs_investigation` or `under_investigation` subjects and generate documentary or lab work.
6. **Finder/comparison attributes** — only sufficiently established structured conclusions become decision attributes; presentation is downstream and remains subject to UI policy.
7. **Editorial/public Research** — publishable synthesis may be generated from the evidence package without becoming the canonical evidence store.

## Contradictions are first-class

Do not collapse conflicting evidence into a single convenient value. Preserve, for example:

`manufacturer claim -> community observations -> independent test -> GR measurement`

A conclusion may state which evidence currently deserves the most weight, but competing claims remain attributable and inspectable. New evidence can supersede a conclusion without erasing history.

## Enrichment lifecycle

`ingested -> normalized -> subject-linked -> claim-extracted -> evidence-graded -> routed -> investigated -> concluded -> propagated -> commissioned`

Propagation means the conclusion has been considered against every applicable destination: canonical data, model dossier, Report Card, cross-model relationships, research queue, structured decision attributes, and public research/editorial output. `not_applicable` is a valid destination disposition; silent omission is not.

## Promotion thresholds

- Community repetition increases research priority; repetition alone does not create verified fact.
- Documentary/manufacturer evidence can establish what a party documented or claimed; it does not prove real-world performance unless the proposition is inherently documentary.
- Independent and GR-lab evidence can strengthen behavioral/performance conclusions when method and identity are adequate.
- Canonical mutations require evidence appropriate to the field and must preserve uncertainty where identity/generation/lineage remains disputed.
- Report Card changes require traceable evidence and explicit score rationale.
- Cross-model propagation requires an explicit shared relationship; never infer family/platform applicability from visual similarity or branding alone.

## Scour Community contract

The Scour Community task is a discovery/intake mechanism, not a truth generator. For each retained useful observation it should preserve source, date, subject candidates, atomic claim(s), evidence lane=`community`, confidence/uncertainty, and proposed destinations. High-value unresolved observations should route into Research rather than disappear after community publication. When the subject resolves to a canonical model, the claim must route to that model's dossier even when every other destination rejects it.

## Documentary research contract

Document research should extract atomic claims from primary/authoritative records, preserve document identity/date/location, link claims to subjects, identify contradictions or corroboration, and route consequences to canonical review, Report Card evidence, model dossiers, cross-model knowledge, or further investigation. Model-specific documentary evidence remains discoverable in the model dossier even when it merely corroborates an already-established fact.

## Safety rails

- Unknown stays unknown.
- Provenance travels with every claim.
- Publication never upgrades evidence strength.
- Community attribution is never rewritten as GR verification.
- Canonical facts are not overwritten merely because a newer source exists.
- Contradictions are preserved and surfaced for investigation.
- Automated enrichment may propose consequential canonical/score changes; existing deterministic authority/policy decides whether they can execute or must escalate.
- Every propagated change must be attributable and revertible.
- Retained model-specific evidence cannot become orphaned because it failed verification or publication thresholds.

## Commissioning test

The architecture is commissioned only when a real ingested finding can be traced end-to-end from source through claim and subject linkage, routed to at least one applicable downstream destination, validated without provenance loss, and observed to update or deliberately leave unchanged the appropriate model/research knowledge. A deliberate contradictory fixture must also prove that conflicting evidence is retained rather than silently overwritten.

Model-page completeness is commissioned only when an accumulation fixture proves that multiple retained claims for one canonical model all resolve into its dossier index, including unverified, contradicted, superseded, and established evidence, with no retained claim silently omitted. Public rendering/presentation of that index is a separate UI commissioning step and remains subject to the UI moratorium.
