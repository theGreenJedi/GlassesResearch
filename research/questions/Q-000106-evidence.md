# Q-000106 — RayNeo iO and MentraOS roadmap

Research reviewed: 2026-10-24. Genuine observed question from [MentraOS issue #4841](https://github.com/Mentra-Community/MentraOS/issues/4841), opened 2026-10-17 and recorded by question discovery on 2026-10-21. This is one observed question, not a synthetic FAQ prompt.

**Question:** Is RayNeo iO support being considered for the MentraOS roadmap?

**Disposition:** The public support request is confirmed. No maintainer acceptance, committed roadmap date, shipped adapter, or working iOS compatibility is established by the sources reviewed. Published answer: `docs/faq/09-development-openness.md`, merged in PR #682. Live page verified against the deployed source digest on 2026-10-24.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| RayNeo iO support requested on 2026-10-17 | [MentraOS #4841](https://github.com/Mentra-Community/MentraOS/issues/4841), public third-party issue in upstream project | Requester is not speaking for maintainers; issue open with no maintainer response as reviewed. |
| RayNeo iO absent from supported product list | [Official MentraOS compatibility page](https://mentraglass.com/os), manufacturer/project-controlled primary source | Page is time-sensitive; absence does not establish a permanent refusal. |
| Generic pluggable OEM adapter is proposed | [MentraOS #3017](https://github.com/Mentra-Community/MentraOS/issues/3017), upstream engineering proposal | Generic interface plan does not establish an implemented RayNeo iO adapter. |
| Independent iO projects exist | [Turbo-IO](https://github.com/Turbo1123/Turbo-IO) and [Spare io](https://github.com/owenc1122/spare-io), third-party repositories referenced by issue #4841 | No independent GlassesResearch validation of their behavior, license compatibility or MentraOS support. |

## Uncertainty and recheck trigger

If a Mentra maintainer responds to #4841, the supported-device list changes, or a tested RayNeo iO adapter ships, re-evaluate this time-sensitive answer. Do not equate a user feature request, experimental independent implementation, or generic adapter roadmap with official support. No physical-device verification was performed.

## Publication verification — 2026-10-24

Merged editorial PR: [#682](https://github.com/theGreenJedi/GlassesResearch/pull/682). Production revision: `3b2458071f92e86cd181b2971b59ed29d23108c2` (PR #683, which repaired the nested README route proof and added FAQ canaries). [Production content proof run #40063314178](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40063314178) succeeded at 2026-10-24T04:42:32Z, fetching the public FAQ route with a cache-busting request and confirming its exact build content digest (c8d957287e00). The Practical Answers index `/docs/faq/` also passed with digest `765a87516754`. No independent device testing is implied by this publication proof.
