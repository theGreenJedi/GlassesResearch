---
description: Claim-level evidence and publication limits for original observed Q-000113.
---

# Q-000113 — Does the community RokidAIAssistant glasses app support display-free Rokid AI Glasses Style?

**Original observed question:** Does your `glasses-app` module run on the **Rokid AI Glasses Style** (the display-free model)?

**Original observation:** [Source](https://github.com/zero2005x/RokidAIAssistant/issues/23) (preserved in canonical registry; reviewed October 31, 2026). The observation is not itself device verification.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Original Style compatibility request | [Source](https://github.com/zero2005x/RokidAIAssistant/issues/23) | A question, not evidence of support |
| Phone/glasses app and CXR SDK project architecture | [Source](https://github.com/zero2005x/RokidAIAssistant) | README does not verify Style deployment |
| Maintainer predicts battery/heat limits and declines custom build | [Source](https://github.com/zero2005x/RokidAIAssistant/issues/23#issuecomment-6059585121) | Engineering judgment; no measured runtime or explicit Style compatibility confirmation |
| Style product distinct from display-equipped Rokid Glasses | [Source](https://global.rokid.com/products/rokid-ai-glasses-style) | Vendor features do not establish third-party API access |

## Uncertainty and publication gate

Canonical proposed FAQ: `docs/faq/09-development-openness.md#does-the-community-rokidaiassistant-glasses-app-support-display-free-rokid-ai-glasses-style`. Existing single directory: `docs/faq/README.md`. The answer separates manufacturer/project assertions, independent technical studies, and community observations. **No GlassesResearch device bench test, guaranteed compatibility, or comparative performance measurement is claimed.**

**State: refreshed research and publication pending.** Do not credit the original registry ID until this publication PR passes editorial, strict links/fragments and all CI checks, merges, the existing main Pages deployment succeeds, and the production-content-proof workflow fetches exact FAQ, directory and evidence pages. Reconcile the original registry row in a follow-up PR with canonical answer_url, publication_verified_at and claim-specific proof. Related Q IDs must not inflate the distinct URL count.
