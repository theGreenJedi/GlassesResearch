# Living Smart-Glasses Industry Timeline

This directory is the canonical data layer for the GlassesResearch industry timeline.

The timeline is designed as a citable research product, not a decorative chronology. Every canonical event has a stable `TL-####` identifier, date/state, category, significance score, evidence class, sources, and optional links to device records. The website renders the graph and prose from the same data.

## Event states

- `occurred` — the event happened and is supported by evidence.
- `announced` — a future event or milestone has been publicly announced by a primary source.
- `delayed` — an announced event did not occur on the original schedule.
- `cancelled` — an announced event was cancelled.
- `provisional` — an automatically discovered signal awaiting promotion to the canonical record.

Announced events remain visibly distinct from occurred history. They are never silently rewritten; later changes are recorded as state changes or follow-up events.

## Significance

- **5 — industry-changing**: defining platform, category, or market event.
- **4 — major**: prominent main-graph milestone.
- **3 — important**: retained in the canonical timeline and visible with normal filters.
- **2 — minor**: useful detailed chronology; normally suppressed from the uncluttered main view.
- **1 — routine**: retained only when historically useful.

## Automation

`.github/workflows/timeline-watch.yml` runs a conservative primary-source watcher. It reads `sources.json`, discovers smart-glasses/XR-relevant entries from configured feeds, deduplicates them, assigns only a provisional significance score, and writes `auto-events.json`.

Automatically discovered records **do not become canonical history merely because they were found**. The website can show them as a clearly marked live-signal layer. Promotion into `events.json` requires a stable event ID and evidence review.

This preserves two goals at once: the timeline keeps up with the industry automatically, while the canonical graph remains trustworthy enough to cite.
