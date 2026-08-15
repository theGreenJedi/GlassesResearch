# Institutional Knowledge Intake and Promotion Workflow

GlassesResearch treats news as an **input to the research institution**, not the final product. The intake system observes broadly across smart glasses and adjacent wearable human-computer interfaces, preserves potentially useful developments, and publishes selectively.

> **Collect broadly. Publish selectively. Preserve everything worth remembering.**
>
> **We strive to be complete in collection, but selective in publication.**

## Cadence

- **Daily at 11:59 PM Eastern (America/New_York):** automated discovery gathers potentially material developments into `research/news-candidates/`. The workflow handles both EST and EDT automatically.
- **Periodic inbox survey:** maintainers review accumulated candidates through `research/inbox/`.
- **Durable editorial record:** completed decisions are retained in `research/news-reviews/`.
- **As needed:** important glasses-related developments are promoted into canonical research.
- **Periodic synthesis:** public news digests summarize meaningful changes without turning the site into a noisy ticker.

**Daily research intake occurs at 11:59 PM Eastern. Collection is automatic; review and publication remain deliberate human editorial processes.** GitHub Actions schedules in UTC, so the workflow carries both UTC equivalents of 11:59 PM Eastern and activates only the one matching the current `America/New_York` offset. Manual workflow dispatch remains available for testing or exceptional runs.

The candidate store is repository-side intake and is not itself a public factual record.

## Collection scope

### Core: smart glasses and eyewear

The collector searches known manufacturers, models, lineages, SDKs, firmware, developer ecosystems, components, standards, privacy/security developments, retail rebrands, regulatory records, and relevant reporting.

### Adjacent HCI radar

The collector also watches developments that may shape the future of wearable computing, including:

- brain-computer and neural interfaces;
- EMG/sEMG and wrist-based input;
- gesture, hand, eye, and gaze tracking;
- retinal, holographic, microLED, micro-OLED, and waveguide displays;
- wearable AI, ambient/spatial computing, hearables, haptics, biosensors, and accessibility interfaces;
- low-power edge AI processors, connectivity, OpenXR, Android XR, UWB, and Bluetooth LE Audio.

Adjacent HCI collection does **not** expand the public website's scope automatically. It gives the institution peripheral vision and a historical record.

## Scope lanes

Every candidate receives one of three lanes:

- **`core_glasses`** — directly relevant to smart glasses/eyewear. Eligible for public promotion after verification and editorial review.
- **`adjacent_hci`** — relevant to wearable HCI but without a concrete glasses connection yet. Retained for research radar; not eligible for public promotion yet.
- **`research_radar`** — potentially useful ecosystem evidence requiring later context or classification.

## Publication gate

**Collection is not publication.**

For now, an item may be promoted to the public GlassesResearch site only when it materially pertains to smart glasses / AI eyeglasses / eyewear research. Adjacent HCI items remain collected and searchable in the research inbox until a concrete glasses connection exists or the project's public scope is deliberately changed.

No automated collector output becomes a canonical claim by itself.

## Dispositions

Every new item begins as **`collected`**. During later review it may become:

- **`watch`** — retain and revisit if related developments occur;
- **`archived`** — worth preserving, but no current public action;
- **`published`** — verified and incorporated into canonical research;
- **`superseded`** — replaced or clarified by newer evidence;
- **`rejected`** — not sufficiently relevant, durable, or reliable.

These dispositions preserve an editorial history instead of silently discarding intake.

## Institution test

For every retained candidate ask:

> **Will this still make GlassesResearch more useful one year from now?**

The answer does not need to be yes immediately. Some items are deliberately retained as `watch` because their significance may only become clear later.

## Where surveys happen

Raw intake remains in `research/news-candidates/`. The working survey layer lives in `research/inbox/`. Completed editorial decisions live in `research/news-reviews/`.

For each survey session:

1. Choose a candidate date range (weekly, monthly, or any useful window).
2. Copy `research/inbox/INBOX_TEMPLATE.md` to a dated inbox survey file.
3. Group duplicate coverage and follow-up stories into underlying developments.
4. Verify promising developments against the strongest available sources.
5. Assign each development exactly one disposition: publish, watch, archive, superseded, or reject.
6. Record why the decision was made and which candidate IDs were considered.
7. For publish decisions, identify every canonical repository destination that needs an update.
8. Move the completed decision record into `research/news-reviews/` or reproduce it there as the durable editorial record.

This makes it possible to return months or years later and see not only what was published, but what the institution observed and how it evaluated it at the time.

## Candidate review procedure

1. Survey accumulated intake rather than assuming every daily item needs action.
2. Trace promising candidates to the best available primary source; use independent reporting for context and contradictions.
3. Deduplicate rewrites and syndication.
4. Distinguish announcement, preorder, shipping, hands-on verification, firmware rollout, discontinuation, rumor, and research finding.
5. Reject routine promotions, affiliate lists, SEO rewrites, trivial variants, and unsupported rumors.
6. For accepted items, record event date, discovery date, source type, affected models/lineages, what changed, uncertainty, and which canonical pages must change.
7. Preserve fragile lawful-to-preserve evidence when practical.
8. Promote verified glasses-related findings into durable research rather than leaving them only as news items.

## Materiality / consequence test

An item is potentially material when it changes at least one of:

- what exists or can be purchased;
- a model launch, preorder, shipment, delay, discontinuation, recall, or regional availability;
- a technology lineage, rebrand relationship, compatibility relationship, or ecosystem boundary;
- a device's capability, compatibility, security, privacy, repair, support, accessibility, or user control;
- an SDK, API, protocol, app, firmware, model, open-source project, or developer path;
- a meaningful AI, software, hardware, optics, display, chipset, battery, sensor, connectivity, or manufacturing development likely to influence smart glasses;
- an adjacent wearable-HCI development that may later become relevant to glasses;
- credible scientific or human-factors evidence;
- a canonical claim already present in this repository.

## Promotion destinations

A verified glasses-related development should update every durable layer it materially affects:

- `models/THE_LIST.md` for new or materially changed purchasable models;
- `models/<Model>/` for model-specific research;
- `lineages/` for lineage membership, evolution, shared technology, compatibility, pros/cons, current models, and use cases;
- comparison data when new comparable facts become available;
- timeline data for significant milestones;
- `resources/COMMUNITY_AND_DEVELOPMENT.md` for community/developer ecosystem changes;
- release tracker and public digest when useful to readers;
- glossary, FAQ, artifacts, evidence corpus, buyer guidance, and research pages where relevant.

A single event can update several of these at once.

Every new review uses `news_promotion_schema: 1`. A `publish` disposition must name affected models, affected lineages/platforms/resources, and resolvable canonical repository destinations. When a category or destination is genuinely unaffected, record `none —` followed by a concrete rationale. Public digest publication alone is not a substitute for canonical promotion. Other dispositions retain their existing requirements. The validator applies incrementally to schema-marked reviews, so historical editorial records remain intact.

## Review and publication rule

The automated intake workflow may open a pull request containing **raw candidates only**. Those files are research-inbox material, not canonical facts and not publication-ready content.

Canonical updates require evidence review. Adjacent HCI material remains internal research radar until it becomes concretely relevant to smart glasses or the editorial scope is deliberately broadened.

## Pull-request checklist for promoted news

- [ ] Accepted claims have direct sources.
- [ ] Primary sources are preferred and independent context is separated.
- [ ] Event dates are distinguished from publication/discovery dates.
- [ ] Announcement, preorder, shipping, verification, and hands-on status are not conflated.
- [ ] New models were checked against The List and relevant lineage pages.
- [ ] Lineage implications were evaluated explicitly.
- [ ] Public promotion passed the glasses-relevance gate.
- [ ] Canonical model/comparison/timeline/community pages were updated when knowledge changed.
- [ ] Fragile resources were archived or a link-only preservation choice was made deliberately.
- [ ] Existing public digests were not silently rewritten; corrections are explicit.
- [ ] Internal links and MkDocs navigation resolve.
- [ ] PR explains which models, lineages, and research layers changed and why.
