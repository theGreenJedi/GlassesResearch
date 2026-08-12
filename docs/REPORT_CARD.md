# GlassesResearch Report Cards

Smart glasses are full of tradeoffs that disappear when everything is collapsed into one overall score. GlassesResearch grades **ten independent dimensions** so a buyer, developer, researcher, or owner can see where a device is strong — and where control has been traded away.

## Inaugural report cards

These are the first published cards. Scores are deliberately conservative and are assigned only where the available evidence is strong enough to support a judgment. **Not yet graded** means exactly that; it is not a zero.

### Vuzix Z100

A lightweight, display-first design with an unusually strong official developer story. Vuzix documents a 640×480 monochrome microLED waveguide, 30° field of view, BLE connectivity, two-plus-day runtime, prescription support, and Android/iOS SDKs with sample code. The SDK can send text, images, and animations and monitor taps, screen state, battery, and connection state.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | 7.5 | B | Purpose-built, very light display hardware and long runtime, but intentionally narrow capability. |
| Wearability | 8.5 | A- | Designed for all-day use and prescription-ready. |
| Visual AI | N/A | N/A | The glasses are primarily a display endpoint rather than an onboard visual-AI device. |
| Software | 8.0 | B+ | Documented Android/iOS integration, demo apps, sample code, and SDK documentation. |
| Display / HUD | 8.0 | B+ | See-through microLED waveguide; useful 30° monocular HUD, though monochrome and modest resolution. |
| Openness | 9.0 | A | Official SDKs, sample code, documented APIs, and explicit third-party application support. |
| Owner Control | 8.5 | A- | Developers control displayed content and can build ground-up phone applications around the glasses. |
| Cloud Independence | 8.5 | A- | Core display integration is BLE/phone based and is not presented as dependent on cloud AI. |
| Hackability | 8.0 | B+ | BLE plus supported SDK access creates a strong experimentation surface without requiring reverse engineering first. |
| Value | Not yet graded | — | Pricing and purchase channels vary enough that we are withholding a durable value score. |

Sources: [Vuzix Z100 product page](https://www.vuzix.com/products/z100-smart-glasses), [Vuzix Z100 SDK overview](https://support.vuzix.com/docs/overview-28), [Vuzix Android SDK](https://support.vuzix.com/docs/sdk-for-android).

### Google Glass Enterprise Edition 2

Glass EE2 remains an important owner-control benchmark because Google shipped it on Android Open Source Project rather than a sealed appliance stack. Google documents Android 8.1/AOSP, standard Android API development, ADB and fastboot access, USB debugging, screen mirroring, 32 GB storage, Bluetooth 5.0, Wi-Fi, an 8 MP camera, RGB display, microphones, sensors, and USB-C.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | 7.5 | B | Capable enterprise sensor/compute package for its generation, now dated by current hardware standards. |
| Wearability | 7.0 | B- | Lightweight for an enterprise wearable but visibly a computer rather than ordinary eyeglasses. |
| Visual AI | 4.5 | D | Camera and compute are available, but modern multimodal AI was not a native product strength. |
| Software | 7.5 | B | Standard Android APIs and mature Android tooling substantially reduce proprietary development friction. |
| Display / HUD | 7.0 | B- | Useful glanceable RGB display, but modest 640×360 resolution and older optical design. |
| Openness | 9.5 | A+ | AOSP, standard Android development, ADB/fastboot, USB debugging, and conventional developer tooling. |
| Owner Control | 9.5 | A+ | Applications can be developed and deployed using familiar Android mechanisms without a vendor-only app model. |
| Cloud Independence | 9.5 | A+ | AOSP applications and local device operation do not inherently require a Google cloud AI service. |
| Hackability | 9.5 | A+ | ADB, fastboot, AOSP, USB debugging, standard Android APIs, and accessible device information make it unusually owner-accessible. |
| Value | Not yet graded | — | It is discontinued enterprise hardware with a secondary-market value proposition that changes substantially over time. |

Sources: [Google Glass EE2 developer guide](https://developers.google.com/glass-enterprise/guides/get-started), [Google Glass EE2 specifications](https://support.google.com/glass-enterprise/customer/answer/9220200).

### W610 / HeyCyan family — hands-on card in progress

The W610 is the first GlassesResearch hands-on platform. We have directly observed the `HeyCyan Glasses` Bluetooth identity, electronics concentrated primarily in the right temple, two right-temple controls, a hinge-area status LED, and basic startup behavior. Initial testing intentionally avoided the vendor application so that owner-controlled interfaces could be investigated first.

We are **not converting curiosity into fake precision**. The W610 card remains unscored until the BLE, firmware, software, battery, and owner-control investigations produce enough repeatable evidence for dimension-level grades. Its eventual scores will therefore have a different evidentiary character from source-only cards: they can include direct GlassesResearch testing.

See the [W610 research chapter](../models/W610/README.md) and [HeyCyan technology lineage](../lineages/HEYCYAN.md).

## The ten dimensions

| Dimension | What we measure |
|---|---|
| **Hardware** | Camera/vision, audio, microphones, battery, weight, thermals, build quality, and core physical capability. Display performance is graded separately. |
| **Wearability** | Looks like glasses, comfort, size, discretion, fit, and everyday practicality. |
| **Visual AI** | Can the glasses actually understand **what am I looking at?** Useful visual perception and the ability to turn what the wearer sees into machine-understandable context. |
| **Software** | App quality, stability, features, updates, integrations, and day-to-day software experience. |
| **Display / HUD** | Presence and usefulness of visual output: readability, resolution, brightness, field of view, color, implementation, information density, and outdoor usability. |
| **Openness** | SDK/API access, sensor access, documentation, open-source components, and supported developer access. |
| **Owner Control** | Sideloading, replaceable AI, local processing, custom endpoints, and the owner's ability to choose the intelligence layer. |
| **Cloud Independence** | What continues working without the manufacturer's servers, account services, or cloud AI. |
| **Hackability** | BLE access, firmware access, reverse-engineering potential, sideloading paths, exposed interfaces, and community tooling. |
| **Value** | Useful capability relative to purchase price. |

## Grade scale

| Score | Grade |
|---:|:---|
| 9.5–10.0 | A+ |
| 9.0–9.4 | A |
| 8.5–8.9 | A- |
| 8.0–8.4 | B+ |
| 7.5–7.9 | B |
| 7.0–7.4 | B- |
| 6.5–6.9 | C+ |
| 6.0–6.4 | C |
| 5.5–5.9 | C- |
| 5.0–5.4 | D+ |
| 4.0–4.9 | D |
| 0.0–3.9 | F |

## N/A is not failure

A dimension that genuinely does not apply receives **N/A**, not zero and not an F. A device designed without a HUD receives Display / HUD: N/A. Missing evidence is different again and is shown as **Not yet graded**.

## No universal winner

There is intentionally no single overall grade. Excellent hardware should not conceal weak owner control; exceptional openness should not conceal poor wearability. The useful answer depends on what the owner values.

## Benchmarking and revision

A **10** represents the best demonstrated state of the category against the current GlassesResearch benchmark, not theoretical perfection. Cards are living research: scores can change when firmware changes, capabilities disappear, new evidence appears, or the category advances. A score change should be explainable from evidence rather than taste alone.
