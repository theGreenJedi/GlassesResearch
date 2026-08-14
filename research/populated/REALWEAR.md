# RealWear — populated research record

Source basis: `docs/report-cards/HIGH_THROUGHPUT_BATCH_05.md`, RealWear support/firmware sources, and `EV-0037`.

## Lineage
HMT-1 / HMT-1Z1 → Navigator 500 → Navigator 520 / Navigator Z1. The lineage is rugged, voice-first monocular enterprise wear rather than ordinary-eyeglass form.

## Report-card anchors
- **HMT-1 — GLS-0101:** H6.5 W4.0 VAI5.5 S6.5 O6.0 OC7.0 CI8.0 Hack6.0 HUD5.0; Value not yet graded.
- **HMT-1Z1 — GLS-0102:** H7.0 W3.5 VAI5.5 S6.5 O6.0 OC7.0 CI8.0 Hack6.0 HUD5.0; Value not yet graded.
- **Navigator 500 — GLS-0103:** H8.0 W4.5 VAI7.0 S7.5 O6.5 OC7.5 CI8.5 Hack6.5 HUD5.5; Value not yet graded.
- **Navigator 520 — GLS-0104:** H8.5 W4.5 VAI7.0 S8.0 O6.5 OC7.5 CI8.5 Hack6.5 HUD7.0; Value not yet graded.
- **Navigator Z1 — GLS-0105:** H8.5 W4.0 VAI7.0 S8.0 O6.5 OC7.5 CI8.5 Hack6.5 HUD7.0; Value not yet graded.

## Architecture and lifecycle
HMT-1/HMT-1Z1 established the rugged monocular Android model with 854×480 display and voice-first operation. Z1's intrinsically safe construction is a hardware advantage in hazardous environments but a wearability cost on the catalog-wide ruler.

RealWear now explicitly classifies HMT-1/HMT-1Z1 as End of Life / End of Support. Firmware 12.6 is the final firmware line and no further security updates are planned. Crucially, RealWear also states that an end-of-life device **will still work**, while warning that third-party applications may eventually fail and no new Android security patches will arrive.

Service-survival state: **discontinued-functional**, not nonfunctional. This is a useful Cloud Independence control case: vendor support ended without remotely disabling the core device.

## Function-level offline evidence
Release 12 documentation distinguishes local from cloud dictation. English, German and Mandarin Chinese support local dictation without internet connectivity; other supported dictation languages rely on cloud dictation. Core operation is therefore neither wholly offline nor wholly cloud-bound.

Navigator 500/520/Z1 remain supported through at least December 2030 according to RealWear's current firmware-support policy, with an Android-16-based OS planned for currently supported devices in 2026.

## Ownership interpretation
Android enterprise application deployment gives meaningful owner/application control and practical local operation. The platform remains proprietary, so public app deployment should not be confused with open firmware, schematics or unrestricted low-level access. HMT-1/HMT-1Z1 demonstrate that proprietary hardware can nevertheless retain useful local operation after vendor EOS.

## Evidence gaps
Current pricing/value, exact SDK/API exposure by generation, account/MDM dependence, repairability, battery/parts availability, prescription/PPE fit, firmware access and long-term third-party-app survival remain open.