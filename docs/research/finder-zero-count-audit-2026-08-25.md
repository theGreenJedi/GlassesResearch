# Finder zero-count audit — 2026-08-25

Status: active audit, not a publication claim.

## Why this exists

Several Finder categories currently show zero matches. A zero may be legitimate, but it may also mean the capability matrix is dominated by `unknown`, a frontend inference path is wrong, or the underlying research coverage has not yet reached that field. Unknown must never be silently converted into no.

## Audit method

For each Finder filter, separate four questions:

1. How many canonical records are `yes`, `no`, `unknown`, and `na` in the generated capability matrix?
2. How many additional frontend matches come only from inference aliases?
3. For zero-match filters, are there known real-world products that suggest a research-coverage gap rather than a true zero?
4. Does the filter depend on purchase/price/report-card data instead of the capability matrix?

## First confirmed finding

`No display` had an unsafe frontend fallback (`!display`) that could turn unresolved display evidence into an inferred positive for `no_display`. Issue #381 and its proposed fix isolate that defect. The generated capability builder itself remains conservative and explicitly states that absence of evidence never becomes `no`.

## Filters requiring explicit zero-result review

Priority order:

- Progressive lenses
- Ordinary optician compatible
- Adjustable diopter
- Live video / streaming
- Full-color display
- Binocular display
- Navigation
- Open source
- Custom / replaceable AI
- Local / offline operation
- Self-hostable
- Purchase-source and price filters that display zero

For each of these, record whether zero is: `true-zero`, `coverage-zero`, `frontend-zero`, or `data-pipeline-zero`.

## Scope boundary

This audit does not add inferred product claims and does not change canon. Any product-level correction requires evidence in the appropriate research lane before the canonical matrix changes.
