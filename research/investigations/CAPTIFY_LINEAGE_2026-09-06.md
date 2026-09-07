# Captify lineage investigation — 2026-09-06

## Scope

This investigation follows a user-supplied comparison/roundup lead into primary Captify, DreamSmart/MYVU, support, and regulatory evidence. Comparison rankings are discovery surfaces only and do not verify specifications.

## Company and product identity

Captify Glass, Inc. presents itself as a San Francisco accessibility company focused on captioning glasses for deaf and hard-of-hearing users. Captify says co-founder Tom Pritsky has bilateral hearing loss and co-founded the company with Jason Gui, whose earlier wearable work includes Vue Glasses.

Current first-party catalog surfaces expose two products:

- **Captify Myvu** — current retail captioning glasses at https://captify.glass/products/captify-myvu
- **Captify Pro** — current retail captioning glasses at https://captify.glass/products/captify-pro

## Captify Myvu relationship to DreamSmart / MYVU

Captify explicitly states that its standard/Myvu edition is built in collaboration with **DreamSmart MYVU**. Published Captify Myvu specifications closely align with the existing MYVU Air / StarV Air platform tracked as `GLS-0167`: 43 g, binocular diffractive waveguide display, 640×480 resolution, 30° FOV, 1,500-nit claim, 180 mAh battery, Bluetooth 5.3, dual microphones, and stereo directional speakers.

**Disposition:** treat Captify Myvu as a software/service/accessibility edition built on the existing MYVU / StarV Air hardware lineage rather than silently minting a second hardware-generation identity. Captify branding, software, support, prescription program, and commercial package remain separately material and should be tracked as a Captify product/service layer associated with `GLS-0167`.

## Captify Pro — distinct hardware generation

Captify Pro is materially distinct from Captify Myvu. Captify publishes a 37 g chassis, 145 mm frame width, 128 mm temples, 49×41 mm lens dimensions, 20 h standby / 4 h continuous-use claims, magnetic charging, and a different controls/UI surface.

Regulatory evidence independently identifies **Captify Pro model CAP001, FCC ID 2BQMS-CAP001**, with Captify Inc. listed as applicant/manufacturer in a July 2025 RF exposure evaluation. This provides a stable model identity independent of marketing copy.

**Admission decision:** Captify Pro crosses The List purchaser-history threshold as a current named product with direct retail access, primary support documentation, and stable regulatory identity. Reserve `GLS-0218` for Captify Pro / CAP001 unless a concurrent catalog merge has consumed that identifier before reconciliation.

## Architecture and service-survival boundary

Captify says a phone is required for captioning because speech-to-text processing is performed on the paired iOS/Android phone. Captify Pro's standard plan includes offline captions, offline translations, environmental sound detection, and automated note-taking. The optional $15/month Premium plan adds higher-accuracy processing, speaker differentiation, summaries, custom vocabulary, cloud backup/sync, and Ask AI over prior conversations.

The current public privacy policy is broad and service-level. It identifies account/order/prescription information, device/usage data, analytics, and sharing with service providers, but does **not** clearly enumerate treatment of conversation audio, transcripts, locally retained notes, cloud-synced conversations, or the retention/export/deletion semantics of Premium conversation history.

**Research consequence:** offline operation is a meaningful owner-control strength, but owner-control and privacy scores must remain ungraded until the app is inspected or Captify publishes transcript/audio-specific data-flow documentation.

## Software / support surface

Captify maintains a public support center for setup, captions, translation, battery/charging, pairing, troubleshooting, and factory reset. Setup documentation identifies the companion application as **Captify Glass**, requires Bluetooth and microphone permissions, and documents app-mediated pairing. Caption sessions are saved to the app's session list.

No public developer SDK, open protocol, source repository, bootloader path, sideloading route, or documented third-party app interface was established in this pass. Openness therefore remains **unknown/closed-by-default pending evidence**, not zero and not inferred from absence.

## Specification discrepancy

Captify's current first-party pages conflict on prescription range for Captify Pro. The main product page/FAQ advertises sphere support down to -20.00, while the dedicated specification page states -10.00 to +6.00 and cylinder -6.00 to +6.00. Do not silently normalize this discrepancy. Treat the conservative dedicated specification range as the reproducible baseline until Captify resolves the conflict.

## Sources

Primary:
- https://captify.glass/products/captify-pro
- https://captify.glass/pages/pro-specifications
- https://captify.glass/products/captify-myvu
- https://captify.glass/pages/captify-myvu
- https://captify.glass/pages/faqs
- https://captify.glass/pages/subscription
- https://captify.glass/pages/about-us
- https://captify.glass/pages/privacy-policy
- https://help.captify.glass/hc/en-us/categories/43034252521235-Captify-Pro
- https://help.captify.glass/hc/en-us/articles/43602292076947-Setting-Up-Your-Captify-Pro-for-the-First-Time
- FCC test record for CAP001 / FCC ID 2BQMS-CAP001

Secondary context:
- HearingTracker comparison of live-captioning glasses — useful independent category context; not specification authority.

## Open questions

1. Is Captify Pro hardware designed/manufactured entirely by Captify or by an undisclosed ODM despite Captify being the FCC applicant/manufacturer of record?
2. What is the exact chipset, display engine/waveguide supplier, microphone topology, and Bluetooth service/protocol surface?
3. Are transcript/audio data ever uploaded when Standard offline mode is used?
4. Can saved transcripts/notes be exported in an open format and deleted completely?
5. What firmware-update path exists for CAP001 and what remains functional if Captify's service disappears?
6. Can CAP001 operate as a generic display/audio peripheral outside the Captify Glass app?
7. What is the authoritative prescription range for Captify Pro?
