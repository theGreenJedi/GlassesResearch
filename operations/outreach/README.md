# Community outreach — return line (review-only pilot)

**Purpose:** connect public questions we've already discovered to answers already published by GlassesResearch. This adds distribution, **not** another content-production target.

The existing `research/questions/registry.json` records the original Reddit, GitHub, and Stack Exchange thread URLs as observations. `scripts/build_outreach_queue.py` uses only records that are marked answered/published, groups multiple matching questions from the same discussion, and produces a review queue at `operations/outreach/queue.md`. No new searches, platform credentials, or external interactions occur.

Run manually from the repository root:

```bash
python scripts/build_outreach_queue.py
python -m unittest discover -s tests -p 'test_outreach_queue.py'
```

This pilot is intentionally **not scheduled**. Before scheduling it, verify stable generation and review whether the extra automation is useful. Do not interpret queue creation as evidence that any community was contacted.

## Conduct / approval gate

A candidate can be `new`, `reviewed`, `skipped`, or `posted` in `outcomes.json`. Only a person authorized to speak for GlassesResearch may publish a response. The script **cannot** publish responses. A candidate may be old, closed, irrelevant, or already resolved by other participants. Even an exact published answer may be stale or poorly matched to the questioner's situation.

Keep replies useful **without requiring the reader to click**. Disclose affiliation when relevant. Never flood threads with links, send unsolicited DMs, or bypass subreddit/forum rules. Source questions are not an invitation to market. Staff must inspect the actual thread and the latest evidence and adapt the response accordingly.

## Recording results

The human log `outcomes.json` is never overwritten by the generator. Example entry:

```json
{"source_url":"https://www.reddit.com/r/SmartGlasses/comments/example/","status":"skipped","reason":"thread closed","reviewed_at":"2026-11-06"}
```

For real published replies, separately record the public reply URL and posted date after verifying the post exists. `posted` or `skipped` source URLs are omitted on regeneration. Never count queued candidates as actual outreach.

Analytics evaluation should track confirmed referral visits and substantive conversations separately from search impressions, Cloudflare edge requests, and unverified automatic notifications.
