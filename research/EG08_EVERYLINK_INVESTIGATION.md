# EG08 / everyLink Original-Research Investigation

**Status:** Active investigation — not publication-ready  
**Opened:** 2026-08-22  
**Publication target:** GlassesResearch in-depth original research  
**Evidence standard:** [`docs/EVIDENCE_STANDARD.md`](../docs/EVIDENCE_STANDARD.md)

## Working article

**Working title:** *What Does everyLink Actually Collect? A GlassesResearch Investigation into the EG08 Smart-Glasses Ecosystem, Conflicting Privacy Disclosures, Cloud Dependence, and Owner Control*

This dossier is the working evidence record behind that article. It deliberately separates seller claims, developer declarations, technical capability, direct observation, and reproducible experiment results.

The investigation is not premised on wrongdoing. The initial finding is narrower and testable: the Android and iOS storefronts currently present materially different developer-supplied privacy disclosures for `everyLink`. GlassesResearch will document the discrepancy and determine, as far as reproducible testing allows, how the EG08/everyLink system actually behaves.

## Core rule

> **ACCESS ≠ TRANSMISSION ≠ COLLECTION ≠ SHARING.**

A permission proves capability, not use. A network connection proves transmission, not necessarily retention. A cloud request does not by itself prove data is retained or shared. Claims in the eventual article must preserve these distinctions.

## Research questions

1. Is `EG08` a stable OEM/ODM model designation or only one reseller's SKU?
2. Which commercial listings are the same EG08 hardware, close variants, or unrelated look-alikes?
3. Who is upstream of the EG08 hardware design and who is merely reselling/rebranding it?
4. What roles do Bluetooth, BLE, Wi-Fi, local storage, and the phone app play?
5. What does `everyLink` do locally and what functions require Internet/cloud services?
6. What user data, media, telemetry, identifiers, or metadata are transmitted during controlled actions?
7. Which destinations receive those transmissions and what organizations/services operate them?
8. Can EG08 operate usefully without `everyLink`?
9. Can an owner-written Android application access camera/media/audio/buttons/battery/storage directly?
10. Does any publicly usable SDK, API, protocol specification, sample project, or firmware development path exist?
11. What does the Alibaba phrase `SDK / Open API` correspond to technically, if anything?
12. Why does Google Play say the Android app may collect several classes of data while Apple's App Store says `Data Not Collected`?
13. Are Android and iOS implementations materially different, are declarations stale/inconsistent, or is another explanation supported by evidence?
14. How does EG08 compare with the owned W610 as a wearable, owner-controlled smart-glasses peripheral?

## Current evidence ledger

| ID | Claim / observation | Status | Confidence | Current basis |
|---|---|---|---|---|
| EG08-001 | A commercial smart-glasses platform is explicitly sold under model number `EG08`. | **Not Verified Yet** | Moderate | Repeated supplier listings explicitly naming EG08; no owned unit yet. |
| EG08-002 | The repeatedly published EG08 fingerprint is BES 2710Y, 12 MP camera, four microphones, 32 GB storage, 300 mAh battery, 38 g, 152.5 × 52 × 151.5 mm, with companion app `Every Link`. | **Not Verified Yet** | Moderate | Repeated commercial specification from Shenzhen Yushengchang; awaits physical verification. |
| EG08-003 | At least one supplier offers one explicitly identified EG08 sample for US$56 before shipping. | **Verified** as current listing state | High | Made-in-China listing explicitly says 1 piece / US$56. Price is time-sensitive. |
| EG08-004 | Alibaba seller Shenzhen Mingyang Smart Home advertises a `Developer Ready Smart Glasses SDK Open API` product with a hardware fingerprint strongly overlapping the published EG08 fingerprint. | **Not Verified Yet** | Moderate | Alibaba listing: BES 2710Y/Y6 family, 12 MP, four microphones, 32 GB eMMC, 300 mAh, 38 g. Listing does not establish that the unit is EG08. |
| EG08-005 | Mingyang's `SDK / Open API` language proves a usable owner-facing SDK/API. | **Unknown** | Low | No public SDK documentation, protocol specification, sample project, or developer repository has yet been located. Seller title is not proof. |
| EG08-006 | The Mingyang listing says live streaming requires the seller's dedicated app and describes a reserved live-streaming interface. | **Not Verified Yet** | Moderate | Seller FAQ/specification; requires runtime verification. |
| EL-001 | Google Play identifies `everyLink`, package `com.aivox.everylink`, as an app from Lita Digital Co., Ltd. | **Verified** | High | Current Google Play listing. |
| EL-002 | Google Play currently says `everyLink` may collect Personal info, Photos and videos, and five other data categories; says no data is shared with third parties; says data is encrypted in transit and deletion can be requested. | **Verified** as current developer declaration | High | Current Google Play Data Safety disclosure. This verifies the disclosure, not the app's actual runtime behavior. |
| EL-003 | Apple's App Store currently says `Data Not Collected` and `The developer does not collect any data from this app` for `everyLink` by Lita Digital Co Ltd. | **Verified** as current developer declaration | High | Current Apple App Store privacy disclosure. This verifies the disclosure, not the app's actual runtime behavior. |
| EL-004 | The Google Play and Apple App Store privacy disclosures are materially different. | **Verified** | High | Direct comparison of current official storefront disclosures. |
| EL-005 | Apple notes that `everyLink` may use location even when the app is not open. | **Verified** as storefront statement | High | Current App Store information panel. This is not proof that location data is collected by the developer. |
| EL-006 | Apple's version history says v1.0.2 added voice-to-text note-taking and simultaneous interpretation for the glasses. | **Verified** as release-note statement | High | Current App Store version history. |
| EL-007 | Publicly indexed Android metadata reports camera, microphone, location, media/storage and other permissions for `everyLink`. | **Not Verified Yet** | Moderate | Secondary app-metadata source. APK/manifest has not yet been independently archived and parsed by GlassesResearch. |
| EL-008 | No public EG08/everyLink SDK or sample repository has been found in the searches conducted so far. | **Unknown** | Moderate | Negative search result only. Absence from search is not proof of nonexistence. |
| W610-CTRL-001 | The owned W610 is a different identified model/platform from EG08; `EG08` is not a component expected to be "on" the W610. | **Verified** at model-identity level | High | Existing W610 chapter and direct owned-device observations identify the unit as W610/HeyCyan ecosystem. The W610 main SoC remains unknown in the current component database. |

## Initial OEM / lineage fingerprint

Until a physical EG08 unit is received, use the following as the **purchase and identity fingerprint**, not as verified hardware fact:

- model designation: `EG08`
- chipset: `BES 2710Y` or a clearly documented close suffix/revision
- camera: 12 MP
- microphones: four
- local storage: 32 GB
- battery: 300 mAh polymer
- weight: approximately 38 g
- dimensions: approximately 152.5 × 52 × 151.5 mm
- companion application: `Every Link` / `everyLink`
- Wi-Fi media transfer claimed
- no display

A listing that merely looks similar or says `12 MP AI glasses` is **not** enough to classify it as EG08.

## Current sourcing benchmark

### Explicit EG08 reference

Shenzhen Yushengchang Technology Co., Ltd. currently lists an explicitly identified `EG08` sample at **US$56 for one piece** before shipping. It publishes the complete fingerprint above and names the companion app `Every Link`.

This is the current price/identity benchmark. It is not Alibaba, but it is stronger identity evidence than a cheaper generic 12 MP listing.

### Alibaba candidate under investigation

Shenzhen Mingyang Smart Home Co., Ltd. currently advertises **Developer Ready Smart Glasses SDK Open API for Software & Hardware Integration**, one-piece ordering, with a hardware fingerprint strongly overlapping EG08. Current indexed pricing is approximately **US$71–85.20** depending on listing/quantity/locale.

**Classification:** likely EG08-family/rebrand candidate; **not yet proven to be EG08**.

The purchase decision must optimize for **identity certainty first** because the purpose of the sample is a reproducible EG08/everyLink experiment. A generic cheaper 12 MP pair is not a substitute if its lineage is uncertain.

## Privacy-disclosure discrepancy

### Google Play — Android

Current listing for `com.aivox.everylink` states:

- developer: Lita Digital Co., Ltd.
- may collect: `Personal info`, `Photos and videos`, plus five additional categories
- no data shared with third parties
- data encrypted in transit
- deletion request available

Google also states on the listing that the developer provided the Data Safety information and may update it over time.

### Apple App Store — iOS

Current listing for `everyLink` by Lita Digital Co Ltd states:

- `Data Not Collected`
- `The developer does not collect any data from this app.`
- the privacy information has not been verified by Apple
- the app may use location even when it is not open
- in-app purchases for blocks of service time are offered
- version 1.0.2 added voice-to-text note taking and simultaneous interpretation for the glasses

### What is established now

The **discrepancy itself is verified**. Its cause is not.

Plausible explanations to test include:

- Android and iOS implementations differ materially.
- Optional features differ by platform, region, account state, or app version.
- One declaration is stale.
- The developer interpreted Google and Apple disclosure definitions differently.
- Some processing may fall within one platform's transient/ephemeral exception but not another disclosure choice.
- Embedded third-party services differ by platform.
- A declaration may be incomplete or incorrect.

No one explanation should be promoted without evidence.

## Investigation phases

### Phase A — source preservation and identity graph

- [x] Record explicit EG08 commercial fingerprint.
- [x] Record explicit `Every Link` companion-app association.
- [x] Record current Google Play disclosure.
- [x] Record current Apple App Store disclosure.
- [x] Record Mingyang `SDK / Open API` claim as an unverified claim.
- [ ] Archive screenshots/PDF/text snapshots with dates where licensing and repository policy permit.
- [ ] Enumerate Alibaba, Made-in-China, retail, and OEM listings that share the exact fingerprint.
- [ ] Build alias/rebrand graph without transferring specs merely because frames look alike.
- [ ] Identify regulatory filings, Bluetooth SIG records, manuals, package labels, FCC IDs, CE documents, or manufacturer marks if available.
- [ ] Determine whether `EG08` is upstream ODM nomenclature or a downstream sales SKU.

### Phase B — app static analysis

Once a legally obtainable Android package or installed app is available:

- [ ] Record exact app version, package hash, acquisition date and source.
- [ ] Parse Android manifest permissions directly.
- [ ] Inventory embedded SDKs/libraries.
- [ ] Inventory hard-coded domains, URLs, IPs, certificate pins, API paths and cloud-provider identifiers.
- [ ] Identify Bluetooth/BLE, Wi-Fi, HTTP/WebSocket, media-transfer and update libraries.
- [ ] Identify analytics, crash-reporting, advertising, authentication and payment SDKs.
- [ ] Separate dormant capability from code paths exercised at runtime.
- [ ] Preserve enough reproducible metadata for later comparison after app updates.

### Phase C — hands-on EG08 hardware baseline

Before installing `everyLink`:

- [ ] Photograph packaging, labels, regulatory marks, frame, camera, controls, charging connector and identifiers.
- [ ] Record weight and physical dimensions.
- [ ] Record Bluetooth advertising name(s), addresses where appropriate, service UUIDs, classic Bluetooth profiles and BLE GATT services.
- [ ] Record behavior with no vendor app installed.
- [ ] Test standard calling/music profiles independently.
- [ ] Inspect USB behavior if any.
- [ ] Record any Wi-Fi network/AP behavior triggered by buttons or media operations.
- [ ] Establish whether photographs/video/audio can be retrieved without `everyLink`.

### Phase D — controlled runtime/network experiment

Use a controlled Android device and a reproducible network observation setup. Run one action at a time and record timestamps.

| Test | Action | Record |
|---|---|---|
| D0 | Install, do not launch | install-time contacts/network activity where observable |
| D1 | First launch | destinations, identifiers, config fetches, consent screens |
| D2 | Idle unpaired | background traffic and periodicity |
| D3 | Account creation/login if required | transmitted account fields and destinations |
| D4 | Pair EG08 | Bluetooth/Wi-Fi transitions, cloud dependency |
| D5 | Idle paired | background traffic with hardware attached |
| D6 | Take one controlled photograph | local storage path, transfer path, any network transmission |
| D7 | Import/view photograph | local vs remote behavior |
| D8 | Record controlled audio | local storage and network behavior |
| D9 | Voice-to-text | audio/text destinations and whether Internet is required |
| D10 | Translation | audio/text destinations and whether Internet is required |
| D11 | AI assistant, text-only | provider/endpoints and request flow |
| D12 | AI analysis of controlled image | whether image or derived representation leaves device |
| D13 | Record video | local transfer and any automatic cloud behavior |
| D14 | Delete media | local deletion, cloud requests, residual references |
| D15 | Logout/account deletion | deletion workflow and residual traffic |
| D16 | Repeat selected actions with Internet blocked | identify local-only vs cloud-required capabilities |
| D17 | Repeat selected actions with DNS/endpoint classes selectively blocked where safe | map dependencies without claiming content visibility that capture cannot prove |

Use deliberately non-sensitive test media created for the experiment. Do not expose unrelated personal photos, contacts, conversations, credentials, or bystanders.

### Phase E — owner-control / replacement-app experiment

- [ ] Determine whether standard Bluetooth profiles alone provide useful audio control.
- [ ] Map BLE GATT characteristics and commands where legally and technically appropriate.
- [ ] Identify media-transfer protocol over Wi-Fi/Bluetooth/USB.
- [ ] Test whether owner-written code can read battery state and button events.
- [ ] Test whether owner-written code can trigger capture or retrieve captured media.
- [ ] Determine whether camera preview/live frames are available outside vendor app.
- [ ] Determine whether `everyLink` can be replaced while retaining useful hardware functions.
- [ ] Search again for SDK/API materials using any vendor IDs, UUIDs, filenames, endpoints or library names learned from the device/app.

## Publication decision matrix

The article should separately report:

1. **Declared behavior** — what Google, Apple, Lita Digital and sellers say.
2. **Technical capability** — permissions, libraries, interfaces and architecture.
3. **Observed behavior** — what the controlled device/app actually did.
4. **Unknowns and limitations** — encryption, pinning, inaccessible payloads, regional differences, version drift, and any experiment we could not reproduce.

Do not phrase a permission as collection, a connection as retention, or a seller claim as a verified interface.

## EG08 vs owned W610: control value

The existing W610 is useful as a comparison/control device, but it is **not EG08**. The W610 chapter identifies an owned W610/HeyCyan-family unit and records `HeyCyan Glasses` as an observed Bluetooth name. Its component database still lists the main processor/SoC as unknown.

That means the project should not say that W610 uses or does not use a particular processor unless separately verified. The safe conclusion is model-level: **W610 and EG08 are different identified platforms/ecosystems.**

Potential comparative experiments:

- Bluetooth profile/service inventory
- vendor-app dependency
- camera/media transfer path
- offline functionality
- cloud dependence
- owner-written client feasibility
- wearability/weight

## Sources — current first-pass set

### EG08 identity / hardware

- Made-in-China, Shenzhen Yushengchang, explicit EG08 product:  
  https://4p-touch.en.made-in-china.com/product/nYpRKoUJRcWf/China-New-design-12MP-camera-smart-AI-bluetooth-glasses-with-AI-assistant-realtime-translation-meeting-recording-EG08.html
- Made-in-China video/product page, explicit EG08, one-piece US$56 reference:  
  https://www.made-in-china.com/video-channel/4p-touch_nYpRKoUJRcWf_New-design-12MP-camera-smart-AI-bluetooth-glasses-with-AI-assistant-realtime-translation-meeting-recording-EG08.html
- Alternate explicit EG08 listing with same fingerprint:  
  https://4p-touch.en.made-in-china.com/product/zYprOyRPXckM/China-High-quality-smart-bluetooth-AI-glasses-with-12MP-camera-music-AI-translation-video-recording-sounds-recording-EG08.html

### Alibaba candidate / SDK claim

- Alibaba indexed developer-ready / Open API product family:  
  https://electronics.alibaba.com/product/api-integration-for-ai
- Mingyang detailed listing observed during investigation:  
  https://germany.alibaba.com/product-detail/Developer-Ready-Smart-Glasses-SDK-Open_1601614184313.html

### everyLink

- Google Play:  
  https://play.google.com/store/apps/details?id=com.aivox.everylink
- Apple App Store:  
  https://apps.apple.com/am/app/everylink/id6751477978
- Developer-linked privacy policy destination surfaced by Apple:  
  https://www.smalink.co/privacy
- Secondary Android metadata lead, to be replaced/corroborated with direct APK analysis:  
  https://chrome-stats.com/d/com.aivox.everylink

### Internal comparison

- [`models/W610/README.md`](../models/W610/README.md)
- [`models/W610/hardware/COMPONENTS.md`](../models/W610/hardware/COMPONENTS.md)

## Publication boundary

This file is a **research dossier**, not the final article.

The final article should not state what everyLink `actually collects` until the observed-behavior phase provides evidence. If encryption or platform restrictions prevent content-level determination, the article should say exactly what could and could not be established.

The storefront discrepancy is the lead. **The experiment determines the story.**
