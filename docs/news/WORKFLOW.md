# Smart-Glasses News Collection and Promotion Workflow

GlassesResearch treats news as an **input to the research institution**, not the final product. The goal is to detect material change quickly, verify it, preserve evidence, and update the durable pages readers rely on.

## Cadence

- **Daily:** automated discovery gathers potentially material ecosystem developments into `research/news-candidates/`.
- **As needed:** important developments are reviewed and promoted immediately into canonical research.
- **Periodic synthesis:** public news digests summarize meaningful changes without turning the site into a noisy ticker.

The candidate store is repository-side intake and is not itself a public factual record.

## Daily collector coverage

The collector searches broadly across:

- smart-glasses and AI-glasses news queries;
- known manufacturers, retailers, and technology lineages;
- manufacturer newsrooms and release pages;
- SDKs, firmware, GitHub releases, companion apps, and developer platforms;
- display, optical, AI, chipset, battery, connectivity, accessibility, privacy, security, and standards developments that can materially affect the ecosystem;
- OEM/ODM, retail-rebrand, regulatory, certification, and supply-chain developments.

The source and query map lives in `research/news-collector-sources.json` and should expand as the ecosystem expands.

## Candidate review procedure

1. Read the latest `main`, candidate intake, [The List](../../models/THE_LIST.md), lineage pages, model registry, comparison data, timeline, community/development hub, FAQ, and affected model chapters.
2. Trace each candidate back to the best available primary source; use independent reporting for context, contradictions, and cases where primary material is unavailable.
3. Deduplicate rewrites and syndication.
4. Distinguish announcement, preorder, shipping, hands-on verification, firmware rollout, discontinuation, and rumor.
5. Reject routine promotions, affiliate lists, SEO rewrites, trivial color/style variants, and rumors without material corroboration.
6. For accepted items, record event date, discovery date, source type, affected models/lineages, what changed, uncertainty, and which canonical pages must change.
7. Preserve fragile lawful-to-preserve evidence when practical.
8. Promote the finding into durable research rather than leaving it only as a news item.

## Materiality / consequence test

An item is newsworthy when it materially changes at least one of:

- what exists or can be purchased;
- a model launch, preorder, shipment, delay, discontinuation, recall, or regional availability;
- a technology lineage, rebrand relationship, compatibility relationship, or ecosystem boundary;
- a device's capability, compatibility, security, privacy, repair, support, accessibility, or user control;
- an SDK, API, protocol, app, firmware, model, open-source project, or developer path;
- a meaningful AI, software, hardware, optics, display, chipset, battery, sensor, connectivity, or manufacturing development likely to influence smart glasses;
- a component or supply-chain constraint;
- credible scientific or human-factors evidence;
- a canonical claim already present in this repository.

## Promotion destinations

A verified development should update every durable layer it materially affects:

- `models/THE_LIST.md` for new or materially changed purchasable models;
- `models/<Model>/` for model-specific research;
- `lineages/` for lineage membership, evolution, shared technology, compatibility, pros/cons, current models, and use cases;
- comparison data when new comparable facts become available;
- timeline data for significant milestones;
- `resources/COMMUNITY_AND_DEVELOPMENT.md` for community/developer ecosystem changes;
- release tracker and public digest when useful to readers;
- glossary, FAQ, artifacts, evidence corpus, buyer guidance, and research pages where relevant.

A single event can update several of these at once.

## Review and publication rule

The automated collector may open a pull request containing **raw candidates only**. Those files are not canonical facts and should not be treated as publication-ready research.

Canonical updates require evidence review. Important developments may be promoted immediately; lower-priority items can be synthesized periodically. Empty public digests are not created.

## Pull-request checklist for promoted news

- [ ] Accepted claims have direct sources.
- [ ] Primary sources are preferred and independent context is separated.
- [ ] Event dates are distinguished from publication/discovery dates.
- [ ] Announcement, preorder, shipping, verification, and hands-on status are not conflated.
- [ ] New models were checked against The List and relevant lineage pages.
- [ ] Lineage implications were evaluated explicitly.
- [ ] Canonical model/comparison/timeline/community pages were updated when knowledge changed.
- [ ] Fragile resources were archived or a link-only preservation choice was made deliberately.
- [ ] Existing public digests were not silently rewritten; corrections are explicit.
- [ ] Internal links and MkDocs navigation resolve.
- [ ] PR explains which models, lineages, and research layers changed and why.

## Public digest template

```markdown
# Smart-Glasses Ecosystem Digest — YYYY-MM-DD

**Coverage window:**
**Evidence lane:** externally sourced unless explicitly marked
**Previous digest:**

## Executive summary

## New models, releases, and availability

### Project-written headline
- **Event date:**
- **Discovered:**
- **Evidence:**
- **What happened:**
- **Why it matters:**
- **Affected models / lineages:**
- **Sources:**
- **Uncertainty:**
- **Canonical research updated:**

## Lineage developments

## Software, firmware, SDKs, AI, and security

## Hardware, optics, components, standards, manufacturing, and regulation

## Community and preservation discoveries

## Corrections and changed assessments
```
