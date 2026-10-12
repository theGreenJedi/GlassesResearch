# MentraOS community engineering: miniapp update consent and pairing ownership

**Across the Wire · Community-reported · October 11, 2026 · Not independently verified by GlassesResearch**

**Published:** October 12, 2026

Two upstream MentraOS pull requests raise owner-control and privacy questions relevant to smart-glasses interoperability. These are repository-reported development states, **not** independently tested hardware behavior or confirmation of production availability.

## Miniapp update checks and user consent

[MentraOS PR #4654](https://github.com/Mentra-Community/MentraOS/pull/4654) was reported merged into the development branch on October 11 (UTC). The change introduces automatic miniapp update checks, signature verification, and user consent before interrupting a running miniapp. GlassesResearch has not independently confirmed production rollout or hardware behavior. The important research question is whether the owner can inspect, decline, or defer an update without losing normal use.

## Secure pairing and transfer of control

[MentraOS PR #4567](https://github.com/Mentra-Community/MentraOS/pull/4567) remained open when reviewed. It proposes a three-press pairing gesture, explicit notification when another phone takes ownership, and safeguards around reconnection. The proposal says ownership transfer does **not** erase stored media. This makes residual-data handling a priority for owner-control and privacy evaluation; a proposed safeguard should not be confused with a shipped implementation.

## GlassesResearch disposition

**Across the Wire:** Attribute both upstream reports, preserving the distinction between a development-branch merge and an open proposal. **Not Verified:** No independent device-level reproduction, production release confirmation, or residual-media test is presented here.

**Follow-up:** Verify the actual pairing/ownership transfer experience, whether previously stored media remain accessible, and whether miniapp updates can be declined or deferred on physical hardware.

**Primary sources:** [PR #4654](https://github.com/Mentra-Community/MentraOS/pull/4654) · [PR #4567](https://github.com/Mentra-Community/MentraOS/pull/4567).
