# Q-000116 — Does the Even R1 ring work with MentraOS on G2?

**Observed wording:** “But the ring doesn't work with MentraOS right?” Quoted in [MentraOS issue #3042](https://github.com/Mentra-Community/MentraOS/issues/3042) from a community launch discussion. Canonical registry entry Q-000116 preserves the GitHub issue URL; this is one observed question, not a newly manufactured prompt. Reviewed 2026-10-25.

**Disposition:** Partially supported according to the project's own issue; **full reliable R1 control cannot be verified**. Do not confuse G2 hardware support with R1 ring support. Do not infer that an open tracking issue means every aspect is broken or that the proposed fix has shipped.

## Claim-level provenance

| Claim | Source / class | Boundary |
| --- | --- | --- |
| Even G2 glasses work with the Mentra phone app | [Mentra help: Does MentraOS support Even G2?](https://mentrahelp.zendesk.com/hc/en-us/articles/46816258641556-Does-MentraOS-support-Even-Realities-G2-glasses), updated Aug 26, 2026 — primary developer support | Does not list R1 ring compatibility or ring gesture guarantees. |
| Some R1 support exists, but pairing/discoverability and app open/switch control have been reported problematic | [MentraOS issue #3042](https://github.com/Mentra-Community/MentraOS/issues/3042), opened June 1, 2026 — project-maintained issue incorporating attributed user reports | Project issue remains open as checked Oct 25; scope and goals are not proof of release or device-level reproduction. |
| Ring may show as connected yet fail to control G2 in the official app | [Even Realities G2/R1 troubleshooting](https://support.evenrealities.com/hc/en-us/articles/17131158230159-G2-and-R1-Are-Connected-in-the-App-but-R1-Cannot-Control-G2) — manufacturer support | Even's own app, **not** a MentraOS fix or demonstration of MentraOS ring support. |
| R1 connection problems are reported by some G2 owners | [Independent owner report and discussion](https://www.reddit.com/r/EvenRealities/comments/1s9qt8u/connection_issues/) (April 1, 2026) — firsthand community report | Reports largely concern the native Even app; no population-level failure rate, not proof of MentraOS behavior. |

## Verification boundary and publication gate

No GlassesResearch G2/R1 bench work, exact app/firmware test matrix, or independent confirmation of all Mentra ring gestures. Answer must be phrased as **partial / uncertain**, not simply “yes” or “no.” Proposed FAQ: `docs/faq/09-development-openness.md#does-the-even-r1-ring-work-with-mentraos-on-even-g2`. The registry must remain **observed** until the answer is merged, passes CI, and is verified on the live site. Do not mark this question published based on a PR alone.
