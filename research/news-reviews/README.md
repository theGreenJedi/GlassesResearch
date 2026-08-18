# Research Inbox Reviews

This directory is the durable review layer for the institutional knowledge-intake system.

Raw automated intake lives in `research/news-candidates/` and `research/discovery-candidates/` on the durable `knowledge-intake` branch. Nothing in those directories is a canonical fact or a public-site publication merely because it was collected.

## Automated triage layer

The nightly editorial-triage workflow converts retained intake into persistent review state here instead of producing a throwaway Actions-only report.

It writes:

- `queue.json` — machine-readable durable triage state;
- `latest.md` — the current maintainer-facing action queue;
- `YYYY-MM-DD-auto-triage.md` — the dated triage snapshot for that Eastern-calendar day.

Automated triage may classify an item as:

- `needs_editorial_verification` — a concrete direct/enabling glasses development ready for factual review;
- `source_review` — potentially useful evidence whose source or relationship needs manual attention;
- `catalog_review` — a static manufacturer catalog/developer link that may improve model research but is not itself a news event;
- `source_monitor` — a configured standing manufacturer/source surface retained for future change detection rather than treated as a new development;
- `watching` — rumor/speculation retained without promotion;
- `adjacent_radar` — neighboring wearable/HCI material without a concrete glasses publication gate;
- `rejected_noise` — irrelevant or generic non-eyewear material that must not advance.

`source_monitor` and `catalog_review` are deliberately outside the publication lane. Their presence means the discovery system knows where to look or has found a useful static research surface; it does **not** mean something new happened. This prevents standing manufacturer homepages, SDK pages, and catalog pages from consuming the same editorial queue as actual launches, policy changes, releases, hacks, or newly established evidence.

**Automated triage never authorizes publication.** Explicit factual verification and editorial approval remain the boundary between intake and canonical GlassesResearch publication. Only a verified public publication may become eligible for Verified Research Alerts.

Existing explicit editorial decisions in the queue are preserved across later automated runs so the conveyor cannot silently erase human judgment.

## Editorial survey flow

Periodic or event-driven surveys may still group related coverage into underlying developments, check the strongest sources, and record an explicit disposition for each item or cluster.

1. Start with the durable automated queue rather than rediscovering raw intake.
2. Separate standing source monitors and catalog research from actual developments before assigning editorial effort.
3. Group duplicates, rewrites, follow-ups, and stories about the same underlying development.
4. Identify the best primary source and useful independent context.
5. Assign a scope lane: `core_glasses`, `adjacent_hci`, or `research_radar`.
6. Apply the institution test: **Will this still make GlassesResearch more useful one year from now?**
7. Assign an editorial disposition:
   - `published` — verified glasses/eyewear relevance; incorporated into canonical research;
   - `watch` — potentially important; retain for later developments;
   - `archived` — worth preserving, but no current public action;
   - `superseded` — replaced or clarified by newer evidence;
   - `rejected` — insufficiently relevant, durable, or reliable.
8. For `published`, list every canonical destination updated (model, lineage, comparison data, timeline, community/development, FAQ, glossary, etc.).
9. Preserve the completed decision so the editorial history remains auditable.

## Publication gate

Adjacent HCI material may be collected and triaged, but it does **not** go to the public site unless it has a concrete smart-glasses / AI-eyeglasses / eyewear connection. Standing source monitors and catalog-review records likewise do not enter publication merely because they are relevant. The collector has broad peripheral vision; the website remains glasses-first.

## Principle

> **Collect broadly. Triage continuously. Verify deliberately. Publish selectively. Preserve everything worth remembering.**
