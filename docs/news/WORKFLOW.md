# Weekly Smart-Glasses News Workflow

This is the durable method for the weekly research task.

## Goal

Keep GlassesResearch useful as both a chronological news archive and a current canonical reference. The task is not to summarize every article. It is to detect material change, verify it, preserve fragile evidence, and update the pages that readers rely on.

## Weekly procedure

1. Read the latest `main`, this workflow, the source watchlist, latest digest, release tracker, model registry, FAQ, and affected model chapters.
2. Search the entire watchlist plus broad web/news/research queries for the preceding 14 days. The overlap catches late-indexed reports and corrections.
3. Search exact model names, companion apps, firmware/release-note pages, GitHub repositories, regulators, standards databases, and relevant non-English identifiers.
4. Deduplicate rewrites back to the earliest primary source.
5. Classify each candidate by evidence type and consequence.
6. Reject rumors without material corroboration, routine promotions, affiliate lists, and trivial variants.
7. For every accepted item, record:
   - event date and discovery date;
   - headline written by this project;
   - concise description;
   - why it matters;
   - affected models/entities;
   - source type and direct links;
   - uncertainty or contradiction;
   - repository pages that must change.
8. Archive fragile lawful-to-preserve sources when practical, with URL, retrieval date, hash, license/redistribution status, and authenticity caveat.
9. Create `docs/news/digests/YYYY-MM-DD.md` only when there is material new information.
10. Update `docs/news/README.md`, `RELEASE_TRACKER.md`, the model registry, glossary, resource pages, FAQ answers, and backlogs as required.
11. Open a reviewable GitHub pull request. Do not auto-merge unattended work.
12. If nothing material changed, do not create an empty digest or PR; report “no material update” with the searches completed.

## Consequence test

An item is material when it changes at least one of:

- what exists or can be purchased;
- a release, shipment, delay, discontinuation, recall, or region;
- a device’s capability, compatibility, security, privacy, repair, or support;
- an SDK, protocol, app, firmware, model, or open-source path;
- a component or manufacturing constraint;
- credible scientific understanding or human-factors evidence;
- a canonical claim already present in this repository.

## Pull-request checklist

- [ ] All accepted items have direct sources.
- [ ] Primary sources are preferred and independent context is separated.
- [ ] Event dates are distinguished from publication/discovery dates.
- [ ] Announcement, preorder, shipping, verification, and hands-on status are not conflated.
- [ ] Existing digests were not silently rewritten; corrections are explicit.
- [ ] Canonical pages were updated when news changed current knowledge.
- [ ] Fragile resources were archived or the reason for link-only preservation is stated.
- [ ] No placeholder or empty weekly file was created.
- [ ] Internal links and MkDocs navigation resolve.
- [ ] PR explains models/layers affected and validations performed.

## Digest template

```markdown
# Smart-Glasses Ecosystem Digest — YYYY-MM-DD

**Coverage window:**
**Evidence lane:** externally sourced unless explicitly marked
**Previous digest:**

## Executive summary

## Releases and availability

### Project-written headline
- **Event date:**
- **Discovered:**
- **Evidence:**
- **What happened:**
- **Why it matters:**
- **Affected models/entities:**
- **Sources:**
- **Uncertainty:**
- **Repository updates:**

## Software, firmware, SDKs, and security

## Components, standards, manufacturing, and regulation

## Community and preservation discoveries

## Research radar

## Corrections and changed assessments

## Immediate repository follow-ups
```
