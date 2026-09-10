# MYVU Failure-Mode Register

No entry is a product-level fact unless its evidence state supports that conclusion.

## FM-001 — Imiki discovery/pairing failure

**State:** COMMUNITY-REPORTED  
**Hardware:** Imiki-branded MYVU; exact printed model pending  
**Software:** Panny777 client v0.3 reported  
**Observation:** client did not discover glasses for pairing. MAC-address pairing was suggested; successful resolution has not been established in the evidence captured by GR.  
**Hypotheses to test:** different advertising identity, GATT-generation difference, app/firmware lineage, central already occupied, permissions/host behavior.  
**Disposition:** obtain exact model/firmware and capture BLE advertisements + full service/characteristic inventory before debugging application features.

## FM-002 — rapid shutdown during teleprompter/AI

**State:** COMMUNITY-REPORTED  
**Hardware:** Imiki-branded MYVU; exact model/firmware pending  
**Observation:** owner reported shutdown after roughly 10 seconds or less during teleprompter/AI use.  
**Disposition:** timed reproduction; separately record screen-off, standby, wear-detection, heartbeat and connection state to distinguish UI sleep from link/watchdog/device shutdown.

## FM-003 — iOS/regional pairing friction

**State:** COMMUNITY-REPORTED  
**Hardware:** MYVU regional variant(s), exact identity pending  
**Observation:** reports include Chinese-number/account requirements and failed or nonpersistent iOS pairing.  
**Disposition:** compatibility matrix; preserve exact official-app build/region and hardware identity. Do not generalize to all MYVU hardware or iOS versions.

## FM-004 — overhead-light rainbow artifacts

**State:** COMMUNITY-REPORTED  
**Observation:** pronounced rainbow artifacts reported under overhead lighting.  
**Disposition:** include repeatable indoor-lighting observations in optical/wearability bench work; record source type, angle, brightness/environment and which eye/display path is affected.

## Field-use observations

- ~10-hour mixed-use workday battery — COMMUNITY-REPORTED.
- ~3.5-hour constant-music battery — COMMUNITY-REPORTED.

These are useful owner observations, not GlassesResearch battery measurements.