# Knowledge flow

GlassesResearch discovery is intentionally broader than publication. The intake system should behave like a curious person searching the open web, then classify and route what it finds before editorial review.

The operational sequence is:

**Discover → Classify → Triage → Verify → Route → Enrich → Publish/Propagate → Deliver**

The enrichment stage is defined by [`EVIDENCE_ENRICHMENT_ARCHITECTURE.md`](EVIDENCE_ENRICHMENT_ARCHITECTURE.md). Publication is one downstream use of evidence, not the terminal purpose of ingestion. Retained evidence can also improve canonical model data, model research dossiers, Report Card evidence, cross-model knowledge, research queues, and—once sufficiently established—structured Finder/comparison attributes.

## Relationship to smart glasses

Every candidate receives one relationship state:

- `direct` — explicitly about smart glasses, smart eyewear, or a known glasses source.
- `enabling` — optics, lenses, displays, sensors, chips, prescription technology, or another technology directly useful to smart eyewear.
- `adjacent` — neighboring wearable/HCI work that may become relevant but does not yet make a concrete glasses claim.
- `speculative` — rumor, leak, patent, concept, or future-product claim that must not silently become canonical fact.
- `irrelevant` — search noise. These items are removed from the human review queue.

## Content type

Candidates can carry more than one descriptive type:

`model · review · video · news · research · tool · sdk · hack · optics · policy · retail · teardown · community · rumor`

## Routing

Classification determines where a candidate should go next. Routing targets include model-catalog review, Report Card evidence, development/hacking, optics research, privacy/policy, retail/rebrand review, deep research, community evidence review, adjacent radar, and Watching.

Routing is not publication. A candidate may be correctly routed and still fail verification. A retained candidate that contains useful factual propositions should be normalized into provenance-bearing claims using [`evidence-claims.schema.json`](evidence-claims.schema.json). Each claim records its subject, source, evidence lane/strength, epistemic status, contradictions/corroboration, and every applicable downstream destination.

### Canonical-model routing invariant

When a retained claim resolves to a canonical model ID, it must route into that model's evidence corpus regardless of whether it is verified, contradicted, superseded, under investigation, or merely a community observation. `research/model-evidence/<MODEL_ID>.json` is the deterministic machine-readable index of all such retained model claims. The index is generated from the claims themselves; it is not a second editorial database.

Verification changes labeling and evidentiary weight, not discoverability. A model-specific claim may be rejected from canonical facts, Report Card scoring, cross-model propagation, Finder/comparison, or editorial publication and still remain discoverable in its model dossier. No retained model-specific evidence may become orphaned simply because it did not clear a verification or publication threshold.

The eventual public model page is the human-facing view of this complete corpus. It may summarize, group, filter, collapse, paginate, or rank evidence for usability, but all retained resources remain drill-down discoverable. Public rendering is a presentation concern and remains separate from the underlying evidence-completeness contract.

## Research hierarchy

**Research is the umbrella. Community Research is subordinate to Research as an evidence/source lane.** Community findings can generate or enrich broader Research while retaining their community provenance. Documentary/regulatory, manufacturer, commercial, developer, independent, and GR-lab evidence can later corroborate, qualify, contradict, or disprove the same claim without rewriting its origin.

## Durable intake

Automated collectors persist their queue on the `knowledge-intake` branch. The queue does not depend on GitHub Actions being allowed to create pull requests. Pull requests remain useful for editorial changes, but they are not the conveyor belt that keeps discoveries alive.

The public site's synthesized claims should receive only evidence appropriate to their verification/editorial status. Subscriber delivery occurs after publication, using the same model/topic relationships that routed the underlying evidence. **That threshold does not hide retained model-specific evidence from the model evidence corpus:** unverified material remains discoverable as explicitly unverified evidence rather than being promoted as verified fact. Internal enrichment may continue even when a finding is not suitable for editorial publication.

## Provenance invariant

A source observation never becomes stronger merely because it was ingested, routed, repeated, indexed, or published. Community evidence remains community evidence until separately corroborated; manufacturer claims remain manufacturer claims; GR-lab verification is recorded only after an actual reproducible GR observation. Contradictions are retained as first-class relationships rather than overwritten.
