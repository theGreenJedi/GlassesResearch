---
description: Claim-level evidence and publication limits for original observed Q-000173.
---

# Q-000173 — Why can green HUD text read differently against blue sky and green trees?

**Original observed question:** Green HUD text against a bright sky vs against trees：how big is the difference in real life?

**Original observation:** [Source](https://www.reddit.com/r/SmartGlasses/comments/1xda2xq/green_hud_text_against_a_bright_sky_vs_against/) (preserved in canonical registry; reviewed October 31, 2026). The observation is not itself device verification.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Optical see-through contrast falls with ambient illumination | [Source](https://doi.org/10.1145/3385959.3418445) | Measured HoloLens, not the observer's green HUD |
| Physical vs perceived AR contrast differs | [Source](https://www.cl.cam.ac.uk/research/rainbow/projects/ar_contrast/) | SIGGRAPH Asia 2025 controlled study; no specific sky/tree product benchmark |
| Natural scene structure can mask additive text | [Source](https://doi.org/10.1177/1541931218621294) | Controlled text readability research; no numerical field ratio for this pair |

## Uncertainty and publication gate

Canonical proposed FAQ: `docs/faq/05-displays.md#why-can-green-hud-text-read-differently-against-blue-sky-and-green-trees`. Existing single directory: `docs/faq/README.md`. The answer separates manufacturer/project assertions, independent technical studies, and community observations. **No GlassesResearch device bench test, guaranteed compatibility, or comparative performance measurement is claimed.**

**State: published after exact production proof.** Do not credit the original registry ID until this publication PR passes editorial, strict links/fragments and all CI checks, merges, the existing main Pages deployment succeeds, and the production-content-proof workflow fetches exact FAQ, directory and evidence pages. Reconcile the original registry row in a follow-up PR with canonical answer_url, publication_verified_at and claim-specific proof. Related Q IDs must not inflate the distinct URL count.

## Publication verification — 2026-10-31

[Publication PR #730](https://github.com/theGreenJedi/GlassesResearch/pull/730) merged as `67b0303687e7e20d04dc76b3ef063ec5d2f5a16c` after editorial, strict built-page links/fragments and all CI checks passed. [Main Pages deploy #41240424429](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41240424429) succeeded. [Exact production-content-proof #41240648389](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41240648389) succeeded at 2026-10-31T20:50:14Z, fetching the live FAQ (digest `b4c8addbe057`), single directory (digest `b5dfdc0a15c5`) and this evidence page (digest `26b3bfa206b5`) with exact deployed-build matches. The [canonical answer](https://glassesresearch.org/docs/faq/05-displays/#why-can-green-hud-text-read-differently-against-blue-sky-and-green-trees) has a validated directory fragment. Publication proof does **not** verify any device, app or optical performance. The canonical URL was **already credited under another registry ID**; this original observed ID is now answered without adding a new distinct URL.
