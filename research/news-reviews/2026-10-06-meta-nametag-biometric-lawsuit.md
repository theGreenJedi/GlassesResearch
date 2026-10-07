# Newsroom promotion review — Meta NameTag biometric lawsuit

<!-- news_promotion_schema: 1 -->

**Survey date:** 2026-10-06  
**Candidate window:** 2026-09-04 to 2026-09-11  
**Candidate files reviewed:** none — recovery of benchmark-source discovery miss tracked in #570  
**Reviewer:** GlassesResearch Editorial Desk

## Executive summary

- Candidates reviewed: 1 development
- Unique developments after deduplication: 1
- Publish: 1
- Watch: 0
- Archive: 0
- Superseded: 0
- Reject: 0

## Publish

### Federal complaint challenges alleged biometric uses tied to Meta NameTag

- **Scope lane:** `core_glasses`
- **Disposition:** `publish`
- **Institution test:** yes
- **Why it matters:** the filing directly concerns an unreleased face-recognition system developed for smart glasses and creates a durable privacy, bystander-consent and platform-governance record.
- **Best procedural source:** plaintiffs' counsel filing announcement identifying Alvarez v. Meta Platforms, Inc., N.D. Ill. No. 1:26-cv-10773, filed September 4, 2026.
- **Independent context:** WIRED's June NameTag code investigation and September lawsuit report; Bloomberg Law's September 4 filing report.
- **Affected models:** none — the record concerns Meta's smart-glasses platform / unreleased NameTag capability and does not establish a model-specific specification change.
- **Affected lineages / platforms / resources:** Meta smart-glasses privacy and platform governance; no lineage identity or catalog change warranted.
- **Canonical destinations:** `docs/news/articles/2026-10-06-meta-nametag-biometric-lawsuit.md`, `research/discovery-benchmark.json`, `research/discovery-sources.json`.
- **Uncertainty / contradictions:** filing and procedural facts are verified; the complaint's biometric collection and training-data claims remain allegations. Meta has disputed reporting characterizations of NameTag and described the unreleased work as exploratory.
- **Candidate IDs / intake dates:** none — #570 records the discovery miss.

## Discovery postmortem

The durable discovery configuration contained generic smart-glasses/privacy research queries but no benchmark target for WIRED's NameTag reporting and no explicit NameTag/biometric-litigation query. The September 11 story therefore had no deterministic regression fixture despite WIRED already being a benchmark publication for GlassesResearch.

Correction in this change:
- add the WIRED NameTag lawsuit as a discovery benchmark target;
- add targeted NameTag / biometric / lawsuit discovery queries so the miss is reproducible and regression-testable;
- retain the article as verified procedural research while preserving allegations as allegations.

## Canonical follow-up checklist

- [x] New models added where warranted — none warranted.
- [x] Lineage implications reviewed — none warranted.
- [x] Comparison data updated where warranted — none warranted.
- [x] Timeline implications reviewed — legal/privacy record, not a product milestone.
- [x] Community/development resources reviewed — no update warranted.
- [x] Public promotion passed the glasses-relevance gate.
- [x] Allegations and verified procedural facts separated explicitly.
- [x] Discovery regression fixture added.
