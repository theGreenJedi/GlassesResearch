# Community outreach — OFFLINE DRY RUN ONLY

**Purpose:** Connect real community questions to already-published GlassesResearch answers without contacting, messaging, or posting to anybody. This project deliberately has **no platform-posting code, credentials, or API actions**. The pilot remains in draft PR #742, separate from the public site.

## Process (two independent human gates)

1. **Listen and match:** Existing question registry retains original thread URL, original question and published research URL. The candidate builder generates queue.md, deduplicated by discussion.
2. **GATE 1 — Review candidate questions:** A human opens the original conversation and the linked evidence; checks status (including lock/closure), dates, rules against promotional or AI content, whether others have answered, useful incremental value, and appropriate affiliation disclosure. Decide **hold**, **skip**, or **approved_for_drafting**. Approval is never automatic.
3. **Propose reply in private:** Only after explicit Gate 1 approval, a human author writes a complete, tailored answer for the original platform and places it in draft_submissions.json. Draft must stand alone; no click required. Linking to GlassesResearch is optional, only if justified and locally permitted.
4. **GATE 2 — Review proposed answer:** The offline reply packet includes the question, answer URL, approval notes and the draft. Human reviewer chooses **pending**, **request_revision**, or **accepted_for_dry_run_only**. This last status means the workflow test passed, **not permission to post**.
5. **STOP:** There is intentionally no publish phase, no scheduled job, no outreach integration, and no permission to send any messages.

## Files and responsibilities

- scripts/build_outreach_queue.py — local candidate matching, only evidence_state=published and status=answered.
- operations/outreach/queue.md — proposed matches, not verified outreach opportunities. Current queue holds 15 from 60 distinct source discussions.
- operations/outreach/candidate_decisions.json — the human Gate 1 record. **Empty initially**.
- scripts/build_outreach_drafts.py — validates both gates, fails closed on unknown/duplicate URLs, missing checks, unapproved drafts, or ungrounded answer links.
- operations/outreach/draft_submissions.json — manually proposed reply texts; **empty initially**.
- operations/outreach/draft_decisions.json — second independent review; **empty initially**.
- operations/outreach/replies_for_review.md — resulting offline packet. Shows no answers until Gate 1 passes.
- operations/outreach/outcomes.json — separate historical exclusion ledger; no actions are inferred from it.
- .github/workflows/outreach-queue-check.yml — validation on PRs, read-only permissions, with no schedule and no posting action.

## Gate 1 recorded approvals

The review ledger uses a unique **source_url** from queue.md. Valid states: hold, skip, approved_for_drafting. An approval must have a human reviewer identifier, reviewed_at date, specific notes, and all of these six explicit Boolean checks set to true:

- thread_context_reviewed
- thread_accepts_replies
- community_rules_reviewed
- added_value_confirmed
- published_answer_rechecked
- affiliation_policy_reviewed

Any unknown or unverified condition means **hold**. These fields must reflect real manual checks, not inferred verification from a crawler. They do not authorize publication.

## Gate 2 proposed replies

For approved discussions only, draft_submissions.json accepts a record with **source_url**, **answer_url** (matching the approved published answer), **author**, and **reply_body**. The reply must provide the substance in the community itself, acknowledge uncertainties, disclose affiliation when relevant, and avoid unverified hardware claims.

Reply decisions can only be pending, request_revision, or accepted_for_dry_run_only. There is no "post" state or action. Even an accepted draft stays offline.

## Reproducible local dry run

From repo root:

    python scripts/build_outreach_queue.py
    python scripts/build_outreach_drafts.py
    python -m unittest discover -s tests -p 'test_outreach_*.py'

No network access is necessary for these commands. They consume existing repository files only, and only write review artifacts in the repository working copy. Nothing is transmitted to Reddit, Stack Exchange, GitHub issues, Discord, or any other community.

## Acceptance tests before considering a real pilot

- Matching is reproducible, deduplicated, source-linked, and displays limitations.
- Human can reject/hold a candidate without a response being generated.
- Unapproved candidate, unchecked rules, or unknown answer URL blocks drafting.
- Reply review cannot publish and cannot masquerade as a community reply.
- Tests catch duplicate decisions, unverified checks, malformed/empty drafts, and forbidden publication status.
- Review a handful of cross-platform examples, then discuss policies and real-world risks **before** any posting authorization.

**Current state as of 2026-11-06:** 60 candidate discussion matches; 15 queued; 0 candidate approvals; 0 proposed replies; 0 community messages sent.
