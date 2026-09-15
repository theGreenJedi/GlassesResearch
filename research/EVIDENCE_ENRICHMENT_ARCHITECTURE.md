# Evidence Enrichment Architecture

## Mission

GlassesResearch research inputs are not isolated articles. Community observations, documentary/regulatory records, manufacturer material, commercial evidence, developer work, independent testing, and GR lab observations form a shared evidence system that progressively improves what GlassesResearch knows about models, families, platforms, software, ownership, and unresolved questions.

**Research is the umbrella. Community Research is a subordinate evidence/source lane.** Publication is one possible output of research; it is not the terminal purpose of ingestion.

## Core graph

`Sources -> Evidence -> Claims -> Subjects -> Investigations -> Experiments -> Conclusions -> Site outputs`

A source is where information came from. Evidence is the relevant preserved observation/document. A claim is the smallest proposition that can be supported, contradicted, qualified, or left unresolved. A subject is the model/family/platform/app/manufacturer/topic the claim concerns. Investigations and experiments test unresolved claims. Conclusions record the current evidence-weighted state without destroying earlier provenance.

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
2. **Model research dossier** — living evidence, contradictions, unresolved questions, reproduction status, and research history.
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

The Scour Community task is a discovery/intake mechanism, not a truth generator. For each retained useful observation it should preserve source, date, subject candidates, atomic claim(s), evidence lane=`community`, confidence/uncertainty, and proposed destinations. High-value unresolved observations should route into Research rather than disappear after community publication.

## Documentary research contract

Document research should extract atomic claims from primary/authoritative records, preserve document identity/date/location, link claims to subjects, identify contradictions or corroboration, and route consequences to canonical review, Report Card evidence, model dossiers, cross-model knowledge, or further investigation.

## Safety rails

- Unknown stays unknown.
- Provenance travels with every claim.
- Publication never upgrades evidence strength.
- Community attribution is never rewritten as GR verification.
- Canonical facts are not overwritten merely because a newer source exists.
- Contradictions are preserved and surfaced for investigation.
- Automated enrichment may propose consequential canonical/score changes; existing deterministic authority/policy decides whether they can execute or must escalate.
- Every propagated change must be attributable and revertible.

## Commissioning test

The architecture is commissioned only when a real ingested finding can be traced end-to-end from source through claim and subject linkage, routed to at least one applicable downstream destination, validated without provenance loss, and observed to update or deliberately leave unchanged the appropriate model/research knowledge. A deliberate contradictory fixture must also prove that conflicting evidence is retained rather than silently overwritten.
