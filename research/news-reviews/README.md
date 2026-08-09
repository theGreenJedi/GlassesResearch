# Research Inbox Surveys

This directory is the maintainer-facing survey layer for the institutional knowledge intake system.

Raw automated intake lives in `research/news-candidates/`. Nothing in that directory is a canonical fact or a public-site publication merely because it was collected.

Periodic surveys are performed here. A survey reads a chosen window of collected candidates (for example one week or one month), groups related items, checks the strongest sources, and records an editorial disposition for each item or cluster.

## Survey flow

1. Choose a coverage window from `research/news-candidates/`.
2. Group duplicates, rewrites, follow-ups, and stories about the same underlying development.
3. Identify the best primary source and useful independent context.
4. Assign a scope lane: `core_glasses`, `adjacent_hci`, or `research_radar`.
5. Apply the institution test: **Will this still make GlassesResearch more useful one year from now?**
6. Assign a disposition:
   - `publish` — verified glasses/eyewear relevance; promote into canonical research.
   - `watch` — potentially important; retain for later developments.
   - `archive` — worth preserving, but no current public action.
   - `superseded` — replaced or clarified by newer evidence.
   - `reject` — insufficiently relevant, durable, or reliable.
7. For `publish`, list every canonical destination that must be updated (model, lineage, comparison data, timeline, community/development, FAQ, glossary, etc.).
8. Commit the completed survey so the editorial history is preserved.

## Naming

Use a date or date range, for example:

- `2026-08-09-weekly.md`
- `2026-08-monthly.md`
- `2026-08-01_to_2026-08-15.md`

Start from `SURVEY_TEMPLATE.md`.

## Publication gate

For now, adjacent HCI material is collected and may be surveyed, but it does **not** go to the public site unless it has a concrete smart-glasses / AI-eyeglasses / eyewear connection. The collector has broad peripheral vision; the website remains glasses-first.

## Principle

> **Collect broadly. Publish selectively. Preserve everything worth remembering.**
