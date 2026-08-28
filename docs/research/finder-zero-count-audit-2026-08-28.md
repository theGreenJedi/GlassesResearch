# Finder zero-result audit — 2026-08-28

Issue: #382

## Rule

A Finder filter showing zero matches is not automatically a claim that no matching product exists. Classify zero-result states as:

- `true-zero` — canonical data contains no verified match and no unresolved records relevant to the filter.
- `coverage-zero` — the zero is caused by missing or unresolved evidence/normalization.
- `frontend-zero` — canonical data supports a match but Finder semantics suppress or misclassify it.
- `data-pipeline-zero` — source data contains the needed fact but generation/staging drops or corrupts it.

Unknown remains unknown and never becomes `no` merely to remove a zero.

## Current capability zeros

The repeatable capability audit on main identified four zero-verified-match fields. All four are `coverage-zero`, not safe `true-zero` conclusions:

| Filter | Classification | Existing research lead |
|---|---|---|
| Adjustable diopter | `coverage-zero` | VITURE Pro/One-family primary documentation describes per-eye myopia adjustment; canonical mapping still needs promotion. |
| Live video / streaming | `coverage-zero` | Ray-Ban's official FAQ documents Facebook/Instagram live broadcasting for Ray-Ban Meta Gen 1; canonical mapping still needs promotion. |
| Transcription | `coverage-zero` | Even G2 primary support material explicitly discusses transcribed text; field semantics should be pinned before promotion. |
| Navigation | `coverage-zero` | Even G2 primary support documentation describes real-time turn-by-turn Navigate; canonical mapping still needs promotion. |

These leads were recorded on #382 on 2026-08-27. They are research targets, not automatic capability claims.

## Buying and price filters

The previous audit script covered capability filters only. Issue #382 also calls out buying-source and price zeros, so the audit now covers every ordinary Finder schema filter.

Current canonical input inspection shows:

- `Under $100` is a `coverage-zero`: `data/price-observations.json` has no usable current observation at or below $100; its lowest recorded current price is $249. The absence of a sub-$100 observation is not evidence that no cataloged model can be acquired under $100.
- `Major retailer` is a `coverage-zero`: the purchase-source schema supports `major_retailer`, but current curated purchase records contain no source tagged with that type.
- `Optical retailer` is a `coverage-zero`: the purchase-source schema supports `optical_retailer`, but current curated purchase records contain no source tagged with that type.
- Manufacturer, Amazon, secondary-market, used-condition, available-new, and the $250/$500/$1,000 thresholds have canonical data capable of producing nonzero matches.

The buying-source zeros are therefore normalization/evidence work, not frontend defects and not verified assertions of absence.

## Frontend and pipeline findings

Issue #381 was the confirmed `frontend-zero` class defect: `no_display` could be synthesized from lack of a positive display claim when canonical state was unknown. That semantics defect has already been corrected.

No additional `frontend-zero` or `data-pipeline-zero` defect is established by this audit. The Finder consistency workflow is green on current main, including staged-site generation and the zero-count observability step.

## Automation change

`scripts/audit_finder_zero_counts.py` now audits all ordinary Finder filter types rather than capability fields only: capability, available-new purchase state, purchase source, condition, and price ceiling. It uses the issue taxonomy directly for zero states: unresolved data produces `coverage-zero`; only a fully resolved zero can be called `true-zero`.

The script remains diagnostic. It does not manufacture product claims or fail merely because a legitimate coverage gap exists.

## Disposition

As of this audit, every identified current zero-result class has a disposition. Remaining work is evidence acquisition/normalization in the proper product lanes, not an unexplained Finder-zero defect. Future zeros remain observable in CI and should be handled under the same taxonomy.
