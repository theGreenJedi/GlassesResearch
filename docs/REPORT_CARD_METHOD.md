# Report Card Method

GlassesResearch Report Cards are evidence-linked technical evaluations, not sponsored rankings. They are designed to make tradeoffs visible without collapsing unlike products into a single winner.

## Core Report Card

Every canonical model receives the same compact six-dimension Core Report Card. A model does not need a long-form editorial review before it can participate in the Report Card system or the Finder.

- **Discreetness** — how closely the product presents and functions as ordinary eyewear in routine public use, including visible bulk, obvious electronics, capture indicators, and social practicality.
- **Camera** — the usefulness of the outward-facing camera system for wearer-perspective capture. Presence alone does not establish a high score; still/video capability, access, limitations, and practical capture quality matter.
- **Visual AI** — the evidence-backed ability to understand what the wearer is looking at and turn visual context into useful machine understanding.
- **Hackability** — the practical experimentation surface: BLE or wired access, SDK/API access, firmware paths, reverse-engineering potential, sideloading, exposed interfaces, and community tooling.
- **Owner Control** — how much meaningful control remains with the owner, including direct device access, replaceable AI, local processing, custom endpoints, sideloading, and freedom from a single prescribed vendor path.
- **Android Compatibility** — the depth and quality of Android support, from basic companion-app compatibility through direct SDK/device access, standard interfaces, and owner-controlled integration.

These six dimensions are the canonical shopper/developer comparison surface. Finder score filters use these same fields rather than a separate subset of specially reviewed models.

## Extended ratings

Deep research may add ratings beyond the Core Report Card when the evidence warrants them. The established extended dimensions include **Hardware, Wearability, Software, Display / HUD, Openness, Cloud Independence, and Value**. Long-form research may also add narrowly scoped measurements when useful.

Extended ratings do not determine whether a model has a Core Report Card and do not remove a model from Finder merely because deep research is incomplete.

During migration from the earlier ten-dimension Report Card, **Visual AI, Hackability, and Owner Control** carry directly into the Core Report Card because their meanings are equivalent. Broader legacy scores are preserved as extended ratings rather than silently relabeled. In particular, Wearability is not automatically converted into Discreetness, and generic Hardware is not automatically converted into Camera quality.

## Scoring scale

Scores use a 0–10 scale with letter grades as a readable shorthand. The numerical score is the primary value; the grade does not add a second hidden calculation.

A high score means the evidence strongly supports that dimension. A low score means evidence supports meaningful limitations in that dimension. **Unknown is not zero. N/A is not zero.** If evidence is insufficient, the field remains unscored. A verified absence of a camera can support a Camera score of 0; mere camera presence does not justify inventing a quality score.

## Catalog-wide cards

The Core Report Card builder emits a record for every canonical GLS model. Each of the six fields therefore exists for every model even when its current value is `unknown` or `na`. This makes missing research visible without confusing missing evidence with product failure.

Evidence-backed scores can be supplied through the curated Core Report Card override dataset. The builder preserves provenance for migrated and curated scores, allowing the catalog to become more complete incrementally without weakening the evidence standard.

## Freshness is part of the evidence

A Report Card score is not considered current merely because its page was rebuilt, the catalog was edited, or some other field for the same model was reviewed. **Freshness belongs to the evidence supporting the specific scored subject.**

Every resolved Core score can therefore carry:

- `verified_at` — the date the evidence supporting that specific judgment was last re-checked;
- `freshness` — `fresh`, `aging`, `stale`, or `unknown`;
- `max_age_days` — the routine review interval for that subject;
- `next_review_due` — the date by which routine re-verification is due;
- `age_days` — age of the score-specific verification at build time;
- `context_reviewed_at` — an optional model-level comparison-review date that may help researchers triage work but **does not** substitute for `verified_at`.

The public [Report Card Freshness dashboard](REPORT_CARD_FRESHNESS.md) reports catalog-wide research health and the prioritized refresh queue.

### Freshness states

A score is **Fresh** through the first 75% of its routine review interval, **Aging** during the final 25%, and **Stale** after that interval expires. A resolved score with no score-specific verification date has **Unknown freshness** and belongs in the refresh queue until it is explicitly re-verified.

Unscored subjects remain research gaps rather than freshness failures. They are tracked separately so hundreds of legitimate `Unknown` score cells do not drown out scores that already exist but need maintenance.

### Routine review intervals

| Core subject | Maximum routine interval |
|---|---:|
| Discreetness | 365 days |
| Camera | 365 days |
| Visual AI | 90 days |
| Hackability | 120 days |
| Owner Control | 90 days |
| Android Compatibility | 120 days |

These intervals are ceilings, not guarantees. A material hardware revision, firmware change, service change, SDK/API change, companion-app change, platform-policy change, or ownership/control change should trigger immediate re-verification of the affected subjects even if their routine deadline has not arrived.

### What counts as re-verification

Re-verification means revisiting the evidence that supports the specific score and deciding whether the judgment remains defensible. If it does, update `verified_at`. If the evidence has changed, update the score, provenance, confidence, and `verified_at` together.

A deployment timestamp, Markdown edit date, unrelated model review, or generic catalog refresh **must never be promoted into a verification date**. Curated resolved Core scores are required to carry an explicit `verified_at` date in `YYYY-MM-DD` form.

## No hidden overall weighting

GlassesResearch does **not** calculate a single weighted overall winner score. The dimensions are intentionally shown separately because different users value different properties. A developer may care most about hackability and owner control; a daily wearer may care most about discreetness; another buyer may require a camera, visual AI, and strong Android integration.

If an overall weighting system is introduced in the future, its weights and calculation must be public on this page before the resulting score is published.

## Evidence before score

Every scored judgment must be defensible from the evidence basis associated with the Report Card. Primary sources, direct measurements, reproducible experiments, manuals, firmware, regulatory records, and other authoritative evidence are preferred. Community and secondary evidence must remain clearly distinguished.

The project-wide [Evidence and Confidence Standard](EVIDENCE_STANDARD.md) governs claim status. In particular, **Personally observed** is distinct from independently reproduced **Verified** evidence, and unresolved facts remain **Unknown**.

## Field observations

First-person observations are useful when GlassesResearch actually has the device or a documented experiment. They must be labeled as field observations or personally observed evidence and identify the device context when relevant. They are never inferred from product copy and are never fabricated for devices that have not been handled.

A field observation can describe practical details that specifications miss—pairing behavior, button placement, balance, unexpected friction, visible indicators, companion-app behavior, or other reproducible quirks. It does not automatically generalize to every hardware or firmware revision.

## Lineage and owner-control emphasis

Lineage/OEM relationships, owner control, and cloud independence remain first-class research questions because branding alone does not reveal who controls the hardware/software stack or what remains usable if a vendor service disappears. Where evidence exists, Core and extended ratings should connect those judgments to the relevant lineage and technical research rather than treating each branded product as an isolated object.

## Corrections

Scores can change when stronger evidence arrives. Changes should preserve the evidence trail rather than silently rewriting history. See the [Evidence and Confidence Standard](EVIDENCE_STANDARD.md) and [research challenge process](RESEARCH_CHALLENGES.md).
