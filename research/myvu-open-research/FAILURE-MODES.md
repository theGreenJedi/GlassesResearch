# MYVU Failure-Mode Register

No entry is a product-level fact unless its evidence state supports that conclusion.

**Register review date:** 2026-09-10

## FM-001 — Imiki discovery/pairing failure

**State:** COMMUNITY-REPORTED  
**Hardware:** Imiki-branded MYVU; exact printed model pending  
**Software:** Panny777 client v0.3 reported  
**Public contributor:** `General-Pen-3779`  
**Source thread:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/update_i_opensourced_my_meuizu_myvu_ar_glasses/  
**Direct comment:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/comment/oz7aa4k/  
**Retrieved:** 2026-09-10  
**Observation:** contributor reported that v0.3 did not detect the Imiki MYVU glasses for pairing. Panny777/OP suggested pairing by MAC address; successful resolution has not been established in the captured evidence.  
**Hypotheses to test:** different advertising identity, GATT-generation difference, app/firmware lineage, central already occupied, permissions/host behavior.  
**Disposition:** obtain exact model/firmware and capture BLE advertisements + full service/characteristic inventory before debugging application features.

## FM-002 — rapid shutdown during teleprompter/AI

**State:** COMMUNITY-REPORTED  
**Hardware:** Imiki-branded MYVU; exact model/firmware pending  
**Public contributor:** `AttentionDiligent735`  
**Source thread:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/update_i_opensourced_my_meuizu_myvu_ar_glasses/  
**Direct comment:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/comment/p3l34o6/  
**Source date:** Reddit surfaced the comment as 2026-09-04 during the 2026-09-10 review. Preserve that date as the retrieval-observed date unless a canonical timestamp is later captured.  
**Retrieved:** 2026-09-10  
**Observation:** owner reported the Imiki glasses shutting down at roughly 10 seconds or less while teleprompting or using AI and requested a sleep-time option.  
**Disposition:** timed reproduction; separately record screen-off, standby, wear-detection, heartbeat and connection state to distinguish UI sleep from link/watchdog/device shutdown.

## FM-003 — iOS/regional pairing friction

**State:** COMMUNITY-REPORTED  
**Hardware:** MYVU regional variant(s), exact identity pending  
**Source thread:** https://www.reddit.com/r/SmartGlasses/comments/1it0ptk/myvu_smart_glasses/  
**Published:** 2025-02-19; relevant follow-up comments span 2025-04-27 through 2026-09-04.  
**Retrieved:** 2026-09-10  
**Observation:** reports in the thread describe China-sold Air2 hardware requiring the Chinese MYVU app and Chinese-number/account activation; a 2026-06-30 U.S. report says the global Android app worked while iOS pairing immediately dropped; a 2026-09-04 UK iPhone owner reported successful login using a Chinese number but failure at the final Bluetooth pair step.  
**Caution:** these are multiple owner reports across different markets, devices and app builds, not one controlled compatibility test.  
**Disposition:** build an OS × app-region × hardware × firmware matrix; preserve exact official-app build/region and hardware identity. Do not generalize to all MYVU hardware or iOS versions.

## FM-004 — overhead-light rainbow artifacts

**State:** COMMUNITY-REPORTED  
**Public contributor:** `Candid_Twist5196`  
**Source thread:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/update_i_opensourced_my_meuizu_myvu_ar_glasses/  
**Direct comment:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/comment/p0cnkbq/  
**Retrieved:** 2026-09-10  
**Observation:** owner reported pronounced rainbow effects from the waveguides under overhead lighting.  
**Disposition:** include repeatable indoor-lighting observations in optical/wearability bench work; record source type, angle, brightness/environment and which eye/display path is affected.

## FO-001 — field-use battery observations

**State:** COMMUNITY-REPORTED  
**Public contributor:** `Candid_Twist5196`  
**Source:** https://www.reddit.com/r/augmentedreality/comments/1v1zcph/comment/p0cnkbq/  
**Retrieved:** 2026-09-10  
**Observation:** owner described the glasses lasting through a roughly 10-hour mixed-use workday and about 3.5 hours with constant music use.  
**Caution:** workload, starting state-of-charge, volume, radios, firmware, host and exact hardware identity were not controlled in the report. These are useful field observations, not GlassesResearch battery measurements.  
**Disposition:** retain as owner-use evidence; reproduce only on an identified matching specimen using a documented battery procedure.

## Evidence promotion rule

A `COMMUNITY-REPORTED` entry may move to `GR-VERIFIED` only after GlassesResearch reproduces the relevant behavior on identified hardware/firmware using `TEST-PLAN.md` and preserves the resulting evidence record. Failed reproduction does not erase the community report; it creates a new, separately attributed result.