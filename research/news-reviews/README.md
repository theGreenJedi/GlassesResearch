# Research Inbox Reviews

This directory is the durable review layer for the institutional knowledge-intake system.

Raw automated intake lives in `research/news-candidates/` and `research/discovery-candidates/` on the durable `knowledge-intake` branch. Nothing in those directories is a canonical fact or a public-site publication merely because it was collected.

## Automated triage layer

The nightly editorial-triage workflow now converts retained intake into persistent review state here instead of producing a throwaway Actions-only report.

It writes:

- `queue.json` — machine-readable durable triage state;
- `latest.md` — the current maintainer-facing action queue;
- `YYYY-MM-DD-auto-triage.md` — the dated triage snapshot for that Eastern-calendar day.

Automated triage may classify an item as:

- `needs_editorial_verification` — direct/enabling glasses material ready for factual review;
- `source_review` — potentially useful material whose source needs manual attention;
- `watching` — rumor/speculation retained without promotion;
- `adjacent_radar` — neighboring wearable/HCI material without a concrete glasses publication gate;
- `rejected_noise` — irrelevant material that must not advance.

**Automated triage never authorizes publication.** Explicit factual verification and editorial approval remain the boundary between intake and canonical GlassesResearch publication. Only a verified public publication may become eligible for Verified Research Alerts.

Existing explicit editorial decisions in the queue are preserved across later automated runs so the conveyor cannot silently erase human judgment.

## Editorial survey flow

Periodic or event-driven surveys may still group related coverage into underlying developments, check the strongest sources, and record an explicit disposition for each item or cluster.

1. Start with the durable automated queue rather than rediscovering raw intake.
2. Group duplicates, rewrites, follow-ups, and stories about the same underlying development.
3. Identify the best primary source and useful independent context.
4. Assign a scope lane: `core_glasses`, `adjacent_hci`, or `research_radar`.
5. Apply the institution test: **Will this still make GlassesResearch more useful one year from now?**
6. Assign an editorial disposition:
   - `published` — verified glasses/eyewear relevance; incorporated into canonical research;
   - `watch` — potentially important; retain for later developments;
   - `archived` — worth preserving, but no current public action;
   - `superseded` — replaced or clarified by newer evidence;
   - `rejected` — insufficiently relevant, durable, or reliable.
7. For `published`, list every canonical destination updated (model, lineage, comparison data, timeline, community/development, FAQ, glossary, etc.).
8. Preserve the completed decision so the editorial history remains auditable.

## Publication gate

Adjacent HCI material may be collected and triaged, but it does **not** go to the public site unless it has a concrete smart-glasses / AI-eyeglasses / eyewear connection. The collector has broad peripheral vision; the website remains glasses-first.

## Principle

> **Collect broadly. Triage continuously. Verify deliberately. Publish selectively. Preserve everything worth remembering.**
