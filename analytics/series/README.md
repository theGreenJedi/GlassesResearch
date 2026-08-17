# Long-range analytics series

This directory is the durable, query-friendly analytics history for GlassesResearch.

## Purpose

`analytics/latest.*` answers **what is happening now** and contains rolling windows.
The files here answer **what happened over months** using exact source-day records.

## Layout

- `index.json` — compact list of recorded months and month-to-date summaries.
- `YYYY-MM.json` — one versioned file per month.

Each monthly file has `schema_version: 1` and keeps source dates separate:

- `google_search_console.days[YYYY-MM-DD]` stores the latest finalized Google day, including exact clicks, impressions, CTR, average position, and that day's top queries/pages.
- `cloudflare.days[YYYY-MM-DD]` stores the previous complete UTC day, including requests, HTTP visits, bytes served, and top countries.

Each source also has a `summary` derived only from the exact daily rows in that month. Google average position is weighted by impressions. Cloudflare traffic is infrastructure traffic and must not be interpreted as unique human readership.

## Retention rules

1. Historical dates are retained; a later run only replaces the same source/date key when re-collecting that exact day.
2. Google and Cloudflare dates are intentionally independent because Google finalized Search Console data trails real time while Cloudflare can close a UTC day immediately.
3. Month files are compact enough that multi-month reports require opening only the relevant month files rather than hundreds of daily snapshots.
4. `schema_version` must be incremented for breaking structural changes. Migration code should preserve prior files rather than silently rewriting history.
5. `analytics/history/` remains the raw daily report-snapshot archive. `analytics/series/` is the canonical source for long-range trend reporting.

This format is designed so a request such as **"show the analytics for the past five months"** can be answered directly from five or six monthly files with explicit completeness information.