# GlassesResearch Report Cards

Smart glasses are full of tradeoffs that disappear when everything is collapsed into one overall score. GlassesResearch grades **ten independent dimensions** so a buyer, developer, researcher, or owner can see where a device is strong — and where control has been traded away.

## Published report cards

Scores are deliberately conservative and are assigned only where the available evidence is strong enough to support a judgment. **Not yet graded** means exactly that; it is not a zero. **N/A** is reserved for dimensions that genuinely do not apply.

### Vuzix Z100

A lightweight, display-first design with an unusually strong official developer story. Vuzix documents a 640×480 monochrome microLED waveguide, 30° field of view, BLE connectivity, two-plus-day runtime, prescription support, and Android/iOS SDKs with sample code. The SDK can send text, images, and animations and monitor taps, screen state, battery, and connection state.

**What it means:** Z100 is one of the clearest examples of smart glasses that do less on the face in exchange for giving developers more control. It is not trying to be a self-contained AI computer; it is a lightweight HUD endpoint with a well-documented phone-side development path. That trade produces unusually good owner control, cloud independence, and hackability for something that still looks and wears like glasses.

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

**What it means:** Glass EE2 is dated as a consumer product but still remarkably modern as an ownership model. It behaves much more like a small Android computer you happen to wear than a sealed accessory tied to one companion app. That is why its camera and display no longer look impressive beside current hardware while its Openness, Owner Control, Cloud Independence, and Hackability remain benchmark-level strengths.

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

### Brilliant Labs Frame

Frame is one of the strongest owner-control examples in the current catalog. Brilliant Labs publishes not only product specifications but also schematics, block diagrams, BLE documentation, SDKs, public firmware source, direct-Bluetooth development paths, and a documented SWD debug interface.

**What it means:** Frame is less polished than some closed consumer products, but that is not the interesting part. The interesting part is that Brilliant Labs gives the owner the map to the machine: firmware source, BLE protocol, schematics, SDKs, and even low-level debug access. For developers and researchers, that makes Frame one of the rare glasses where curiosity does not immediately run into a locked door.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | 7.5 | B | Color OLED, 720p camera, microphone, sensors, FPGA/MCU architecture and documented internals make it capable and unusually inspectable, though battery capacity is modest. |
| Wearability | 7.5 | B | Built as glasses rather than an industrial headset and supports prescription clips, but the electronics remain more conspicuous than ordinary eyewear. |
| Visual AI | 7.0 | B- | Camera access and an open software stack make visual-AI workflows practical, though the glasses are better treated as an open interface than as a self-contained high-end inference platform. |
| Software | 8.5 | A- | Python, Flutter, Lua and direct-BLE development provide several supported ways to build useful applications. |
| Display / HUD | 7.5 | B | A 640×400 color OLED at roughly 20° FOV is useful and developer-accessible, but not a wide-field XR display. |
| Openness | 10.0 | A+ | Schematics, BLE protocol documentation, multiple SDKs, public firmware source and hardware documentation set an exceptional openness benchmark. |
| Owner Control | 9.5 | A+ | Owners can choose software stacks, communicate directly over BLE and modify firmware rather than remaining confined to one vendor application. |
| Cloud Independence | 9.0 | A | Core hardware control, display, camera and firmware development do not inherently depend on a vendor cloud service. |
| Hackability | 10.0 | A+ | Public firmware source, BLE specifications, schematics and documented SWD access provide both supported and low-level experimentation paths. |
| Value | Not yet graded | — | Value should be scored against current purchase price and competing hardware at the time of evaluation. |

Sources: [Frame hardware manual](https://docs.brilliant.xyz/frame/hardware/), [Frame SDK](https://docs.brilliant.xyz/frame/frame-sdk/), [Frame Bluetooth specification](https://docs.brilliant.xyz/frame/frame-sdk-bluetooth-specs), [Frame firmware source](https://github.com/brilliantlabsAR/frame-codebase).

### Even Realities G2

G2 takes almost the opposite approach from camera-first AI glasses: discreet binocular information display, no outward-facing camera, no speakers, and a strong emphasis on looking like ordinary eyewear.

**What it means:** G2 may be one of the best answers to the question “can smart glasses just be glasses?” Its strengths are discretion, comfort, prescription support, and a useful binocular HUD rather than cameras or spectacle-sized computing. The cost of that elegance is control: much of the intelligence lives in the companion software and cloud, so the wearer gets a refined product but not nearly the same freedom to replace the stack underneath it.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | 8.0 | B+ | Binocular MicroLED waveguides, four microphones, IP65 protection and a 36 g frame create a focused and well-integrated information-display package. |
| Wearability | 9.5 | A+ | At 36 g with conventional-eyewear styling and prescription options, discretion and everyday wearability are central strengths. |
| Visual AI | N/A | N/A | G2 has no outward-facing camera, so visual understanding of what the wearer sees is not part of the hardware design. |
| Software | 7.5 | B | The companion app provides useful AI, translation and information functions, but the product remains materially dependent on that software layer. |
| Display / HUD | 8.5 | A- | Binocular 640×350 MicroLED waveguides, 27.5° FOV and 60 Hz prioritize glanceable information while retaining normal-eyewear form. |
| Openness | 5.5 | C- | BLE is documented as a transport, but the public development surface is narrower than platforms built around broad SDK and firmware access. |
| Owner Control | 5.0 | D+ | The wearer controls use and presentation but does not receive the same degree of firmware, endpoint or platform substitution available on open developer glasses. |
| Cloud Independence | 4.5 | D | Even documents Bluetooth plus internet requirements for current functions and cloud-assisted AI/translation services. |
| Hackability | 5.0 | D+ | BLE provides an interface surface, but low-level access and supported modification paths are limited compared with open developer platforms. |
| Value | Not yet graded | — | A durable value score requires contemporaneous pricing and comparison with competing prescription-ready HUD glasses. |

Sources: [Even G2 specifications](https://support.evenrealities.com/hc/en-us/articles/13499229138959-Specs), [Even G2 Q&A](https://support.evenrealities.com/hc/en-us/articles/14601104557839-G2-General-Q-A), [Even translation glasses](https://www.evenrealities.com/en-CA/translation-glasses).

### XREAL One

XREAL One is fundamentally a tethered spatial display rather than a standalone AI computer. That narrow architecture produces a very different report card: high display capability and strong cloud independence, but little reason to score camera-based visual AI at all.

**What it means:** XREAL One is easiest to understand as a private spatial monitor that happens to be worn on your face. That focus gives it a much better display than most everyday smart glasses and avoids much of the vendor-cloud problem because the connected host remains the real computer. The tradeoff is obvious: it is less autonomous and less socially invisible than ordinary eyewear, but for display-first use it is operating in a different league.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | 8.5 | A- | Dual 1080p Micro-OLED displays, up to 120 Hz, X1 spatial compute, electrochromic dimming and open-ear audio form a strong display-focused hardware package. |
| Wearability | 7.5 | B | Much lighter and more glasses-like than a headset, though wired host dependence limits everyday freedom compared with untethered eyewear. |
| Visual AI | N/A | N/A | XREAL One is a display/interaction device without an outward-facing visual-AI camera architecture. |
| Software | 7.5 | B | XREAL provides SDK documentation and spatial modes, but useful operation still depends heavily on the connected host ecosystem. |
| Display / HUD | 9.0 | A | 1920×1080 per eye, up to 120 Hz and roughly 50° FOV make display quality the defining strength. |
| Openness | 7.5 | B | Official Unity/XR development support and documentation provide meaningful developer access without opening the entire firmware stack. |
| Owner Control | 8.0 | B+ | Standard USB-C DisplayPort hosts give owners broad freedom over the source device and displayed content. |
| Cloud Independence | 9.5 | A+ | Core display and spatial operation are driven by a local wired host and do not inherently require cloud services. |
| Hackability | 7.0 | B- | Standard host interfaces and SDKs offer useful experimentation, while deeper firmware and hardware control remain more limited. |
| Value | Not yet graded | — | Value is highly sensitive to current retail price and whether the buyer specifically needs a private large-screen spatial display. |

Sources: [XREAL SDK](https://docs.xreal.com/), [XREAL One specifications](https://tutorials.xreal.com/docs/glasses/one-series/spec/), [XREAL One connection guide](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/), [XREAL One firmware FAQ](https://tutorials.xreal.com/docs/glasses/one-series/faq/).

### Solos AirGo family

Solos is notable because its public developer program exposes a surprisingly broad set of useful interfaces across both audio and camera-equipped AirGo models: BLE control, sensors, microphones, audio I/O, touch, camera access on supported models, video streaming, webhooks and RTMP endpoints.

**What it means:** Solos is interesting less because of any single AirGo model than because the company exposes enough of the plumbing to let developers route the glasses into their own systems. BLE, microphones, sensors, camera access on supported models, webhooks, and RTMP make the family unusually adaptable. It is not open firmware in the Brilliant Labs sense, but it gives builders far more useful handles than the typical companion-app-only consumer product.

Because the family spans materially different hardware, dimensions that depend on the exact camera/display configuration are withheld rather than pretending one grade fits every AirGo generation.

| Dimension | Score | Grade | Why |
|---|---:|:---:|---|
| Hardware | Not yet graded | — | AirGo 3/A5 audio models and AirGo V camera models differ enough that a single family hardware grade would be misleading. |
| Wearability | Not yet graded | — | Form, weight and camera hardware vary by model generation. |
| Visual AI | Not yet graded | — | Camera-equipped AirGo V models support visual workflows, while audio-only models do not. |
| Software | 8.0 | B+ | The SDK exposes audio, microphones, sensors, touch, camera/video on supported models, webhooks, RTMP and application wrappers. |
| Display / HUD | N/A | N/A | The currently documented AirGo family is audio/camera oriented rather than a visual HUD platform. |
| Openness | 8.5 | A- | A commercial SDK with documented BLE, Wi-Fi, sensor, audio and camera interfaces creates a substantial supported development surface. |
| Owner Control | 8.0 | B+ | Custom mobile applications, endpoints, webhooks and RTMP workflows let developers redirect much of the intelligence and data path. |
| Cloud Independence | 7.5 | B | BLE/local application control is available, while some assistant and streaming workflows naturally use network services. |
| Hackability | 7.5 | B | Supported SDK access substantially reduces the need for reverse engineering, though firmware-level control is not documented as open. |
| Value | Not yet graded | — | Family-wide pricing and capability differences make a single value score inappropriate. |

Sources: [Solos SDK / Developer Program](https://solosglasses.com/pages/developers), [Solos product site](https://solosglasses.com/).

### W610 / HeyCyan family — hands-on card in progress

The W610 is the first GlassesResearch hands-on platform. We have directly observed the `HeyCyan Glasses` Bluetooth identity, electronics concentrated primarily in the right temple, two right-temple controls, a hinge-area status LED, and basic startup behavior. Initial testing intentionally avoided the vendor application so that owner-controlled interfaces could be investigated first.

**What it means:** W610 is where source research becomes laboratory work. Unlike the cards above, we can eventually grade this family using our own repeated observations of BLE behavior, firmware, battery, controls, and owner-controlled software paths. For now the absence of scores is intentional: this is the card where we can afford to wait for direct evidence instead of borrowing confidence from a spec sheet.

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
