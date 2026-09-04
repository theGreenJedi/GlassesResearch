# GlassesResearch scheduler manifest

This file is the canonical human-readable map of recurring GitHub Actions work in `theGreenJedi/GlassesResearch`.

The scheduling rule is **few clocks, explicit chains**. Event-driven handoffs are primary when one stage logically depends on another. Cron schedules are retained as dead-man backstops or for genuinely independent maintenance work. Verification, editorial, publication, and owner-control gates are not weakened by scheduler simplification.

## Newsroom conveyor

| Stage | Workflow | Primary trigger | Cron/backstop | Concurrency | Notes |
|---|---|---|---|---|---|
| Public discovery wire | `search-wire.yml` | independent discovery clock | every 30 minutes | `search-wire-writer` | Unverified discovery only. A visible wire change explicitly dispatches knowledge intake. |
| High-recall intake | `hourly-news-intake.yml` | dispatch from a changed public wire | `17 * * * *` | `knowledge-intake-writer` | Collects institutional sources, ordinary web, and current wire. The hourly clock is a dead-man fallback. |
| Editorial triage | `daily-news-verification.yml` | successful intake / approved upstream workflow completion | 11:55 PM Eastern DST-aware backstop | `knowledge-intake-writer` | Precision gate. Failed upstream runs do not authorize triage. |
| Publication relay | `newsroom-publication-after-triage.yml` | successful editorial triage | none | `newsroom-publication-after-triage` | Relay only; it cannot publish content itself. |
| Strongly verified publication intake | `newsroom-publication-intake.yml` | dispatch from publication relay | `47 * * * *` | `newsroom-publication-intake` | Bounded auto-publication and all existing verification gates remain unchanged. Hourly cron is a dead-man fallback. |

### Expected flow

`wire change → intake → successful triage → publication relay → strongly verified publication intake`

If the wire does not visibly change, the hourly intake fallback still collects institutional and ordinary-web candidates. If an event handoff is missed, the downstream backstop clocks recover the conveyor without requiring Pete to click anything.

## Independent recurring maintenance

All times below are UTC unless explicitly described otherwise.

| Workflow | Cadence | Purpose |
|---|---|---|
| `cloudflare-analytics-test.yml` | `10 6 * * *` | Daily analytics/Cloudflare contract check. |
| `analytics-report.yml` | `15 7 * * *` | Daily analytics report refresh. |
| `timeline-watch.yml` | `17 9 * * *` | Daily living-industry-timeline update. |
| `purchase-link-health.yml` | `29 9 * * *` | Daily purchase-link health pass; deliberately staggered away from timeline work. |
| `daily-site-link-review.yml` | `37 10 * * *` | Daily whole-site link review. |
| `model-discovery-audit.yml` | `20 4 * * *` / `20 5 * * *` | 12:20 AM Eastern, DST-aware dual-UTC schedule with in-workflow gating. |
| `daily-news-collector.yml` | `51 3 * * *` / `51 4 * * *` | 11:51 PM Eastern institutional-intake backstop, DST-aware. |
| `daily-news-verification.yml` | `55 3 * * *` / `55 4 * * *` | 11:55 PM Eastern editorial-triage backstop, DST-aware. |
| `weekly-research-report.yml` | `45 17 * * 5` / `45 18 * * 5` | Friday 1:45 PM Eastern research report, DST-aware. |

## Scheduler policy

1. Do not add a new cron merely because another workflow sometimes starts late. Prefer an explicit event handoff plus one sensible dead-man backstop.
2. Do not schedule unrelated repository-writing maintenance jobs on the same minute when an adjacent minute is available.
3. A workflow that writes `main`, a durable automation branch, or a publication surface must declare a concurrency group appropriate to that writer.
4. Wire/discovery material remains unverified regardless of scheduler path. Scheduler changes never bypass editorial or verification gates.
5. Publication remains bounded by the existing strong-verification gate and canonical-path validation. A faster or more reliable trigger does not imply broader authority.
6. DST-sensitive local-time jobs may use two UTC cron entries only when the workflow gates on the active Eastern offset.
7. When adding or changing a recurring workflow, update this manifest in the same PR.

## Why the newsroom is arranged this way

The previous layout independently polled strongly verified publication intake six times per hour while also using an event-driven post-triage relay. It also relied on a repository push as an implicit wire-to-intake handoff, even though machine-authored GitHub pushes are not a good orchestration primitive. The current layout makes the dependency chain explicit and keeps clocks as recovery mechanisms rather than the primary control plane.
