---
description: "Attributed Mentra App account-switch deep-link hotfix and launcher regression repairs, with staging and device-verification limits."
---

# Mentra App: account-switch link hotfix and Home launcher regression

**Research note: October 24, 2026 (U.S. Eastern)**

**Across the Wire · Upstream developer evidence · Not independently tested by GlassesResearch**

## Account-link handling: unintended account replacement

[MentraOS PR #4947](https://github.com/Mentra-Community/MentraOS/pull/4947), opened October 24 and **merged to staging October 25 at 00:31 UTC** (October 24 evening Eastern), documents an account-isolation defect in the Mentra phone companion app. According to the upstream developer, opening certain password-reset or signup-confirmation deep links could replace an already signed-in phone session with the account represented by the link **without the owner's explicit approval**. The PR says that data subsequently generated on the phone could then be associated with that other account.

The developer reports that the affected reset-link path existed on the 3.2 main branch as well as the 3.3 release candidate; that is a **code-branch observation, not proof of a particular installed production build or of exploitation**. The upstream fix ignores session tokens in password-reset links, requires confirmation before switching to a different account through signup links, and avoids recording sensitive link fragments in deep-link logs. The PR reports 138 tests passing across 13 suites and a clean compile, but explicitly identifies a device-test gap for the deep-link scenario.

**Status boundary:** A merged staging fix is not evidence that a consumer update has been distributed or installed. GlassesResearch has not reproduced the behavior, audited deployed app versions, or established that any user account was compromised. This is a material **owner-control and privacy** lead to track through production release and independent device testing.

## Home launcher: adding an app could hide existing apps

[MentraOS PR #4943](https://github.com/Mentra-Community/MentraOS/pull/4943), **merged October 24 at 03:10 UTC** (October 23 evening Eastern), describes a separate launcher-state defect. On a phone without a previously saved Home layout, choosing **Add to Home** from All Apps could save the drawer's off-screen grid coordinates as the Home layout, making the existing Home apps disappear from the visible slots. The report also says the Miniapp Developer shortcut could remain available in All Apps when its setting was off.

The upstream repair uses the rendered Home order when no saved layout exists and applies the developer-shortcut visibility setting across launcher lists. The developer reports 149 passing tests across 18 suites and a clean compile. The PR does **not** establish physical-device regression coverage for the exact Add to Home failure. The existing apps were reportedly displaced off-screen rather than deleted; the report does not justify a claim of lost app data.

**Research disposition:** Preserve both upstream changes as attributed software evidence. Track whether the account-link fix reaches a released consumer app and whether the launcher repair is independently reproduced. Do not change a hardware Report Card, mark a device secure, or describe either fix as a production rollout on the basis of a staging merge.

## Primary sources and evidence limits

- [MentraOS PR #4947 — Stop email links from switching the signed-in account](https://github.com/Mentra-Community/MentraOS/pull/4947), opened October 24, merged October 25 UTC.
- [MentraOS PR #4943 — Keep Home apps when adding from All Apps](https://github.com/Mentra-Community/MentraOS/pull/4943), opened and merged October 24 UTC.

The dates, defect descriptions, fixes, test counts, and branch statuses above come from public upstream pull-request records. They are **not GlassesResearch hands-on verification**, independent security testing, or evidence of end-user rollout.
