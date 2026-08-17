# Knowledge flow

GlassesResearch discovery is intentionally broader than publication. The intake system should behave like a curious person searching the open web, then classify and route what it finds before editorial review.

The operational sequence is:

**Discover → Classify → Triage → Verify → Route → Publish → Deliver**

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

Routing is not publication. A candidate may be correctly routed and still fail verification.

## Durable intake

Automated collectors persist their queue on the `knowledge-intake` branch. The queue does not depend on GitHub Actions being allowed to create pull requests. Pull requests remain useful for editorial changes, but they are not the conveyor belt that keeps discoveries alive.

The public site should receive only verified, editorially appropriate outcomes. Subscriber delivery occurs after publication, using the same model/topic relationships that routed the underlying evidence.
