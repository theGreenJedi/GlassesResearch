# MYVU / StarV lineage investigation — 2026-09-02

## Executive finding

MYVU / StarV is not merely a retail curiosity. It is one of the clearest commercially shipped examples of the thin-display smart-glasses architecture GlassesResearch should track closely: a phone-companion design, binocular near-eye display, tiny MicroLED light engines, diffractive waveguides, open-ear audio, microphones, and low mass.

The original MYVU / StarV Air family is especially important because it combines **43 g mass**, **dual 1280×480 display**, **30° FOV**, **single-layer resin diffractive waveguides**, **0.3 cc MicroLED light engines**, and **up to 2000 nit eye brightness**. More importantly, a community implementation now demonstrates that the glasses can be controlled without the official application using a reverse-engineered Bluetooth protocol.

This moves the family from merely "interesting hardware" to a serious interoperability and teardown target.

## Confirmed lineage

### MYVU / StarV Air (XGA010C)

Manufacturer: Hubei Xingji Meizu Group Co., Ltd. / DreamSmart ecosystem.

Regulatory identity: XGA010C. FCC ID **2BHGZ-XGA010C**. FCC filings identify the applicant and manufacturer as Hubei Xingji Meizu Group Co., Ltd. and show Flyme AR firmware on the certified hardware.

Confirmed official specifications:

- 43 g
- 168.4 × 158 × 53 mm
- 183 mAh battery
- 30 MB memory / 20 MB storage
- binocular MicroLED display
- dual 1280×480 resolution
- 30° FOV
- 0.3 cc pure-color light engine
- single-layer resin diffractive waveguide lenses
- 1500 nit rated eye illuminance, 2000 nit maximum
- dual microphones
- dual speakers
- wear detection
- Bluetooth and USB-C
- Flyme AR

Meizu introduced MYVU in its 2023 ecosystem launch. That launch distinguished the 43 g MYVU from the heavier 71 g Explorer Edition, making clear that lightweight daily eyewear was a deliberate product branch rather than an accidental form factor.

### StarV Air2

Air2 is the clear successor in the same lightweight HUD lineage rather than a shift to entertainment glasses.

Confirmed official specifications / claims:

- 44 g
- 30° diagonal FOV
- 640×480 display
- single-green MicroLED light engine
- 0.15 cc light engine
- 4 µm pixel pitch
- up to 2000 nit eye brightness
- high-index tempered-glass waveguide system
- approximately 1.03 mm optical stack / waveguide thickness claim
- 204 mAh battery
- BT 5.2
- Flyme XR 2.0
- new physical scroll-wheel interaction
- prescription-lens support
- claimed ~40% average battery-life improvement versus MYVU

Air2 therefore appears to trade the original's 1280×480 binocular specification for a lower-resolution, highly optimized monochrome HUD architecture while reducing the light-engine volume by roughly half.

### StarV View — related brand, different optical branch

StarV View belongs to the same company / software ecosystem but **not the same optical lineage**. It uses Sony OLED, 1920×1080 per eye, 43.5° FOV and a 74 g cinema-display form factor. DreamSmart explicitly describes View as a BirdBath product, while Air2 is the waveguide product. GlassesResearch should not collapse these into one hardware lineage merely because they share the StarV brand.

## Interoperability breakthrough

A public 2026 community project, `Panny777/Meizu-Myvu-SDK`, has reverse-engineered the MYVU / Star Air XGA010C protocol and reports hardware-verified control without the official Meizu app.

The implementation supports:

- pairing and connection
- teleprompter
- notifications
- brightness and volume
- time synchronization
- settings
- trackpad actions
- weather
- navigation
- microphone audio ingestion
- custom speech-to-text and custom language-model backends
- rendering LLM responses using the glasses' existing on-lens UI

This is unusually important for owner control. The project documents a dual-link architecture: BLE establishes the session and announces a per-session RFCOMM relay; classic Bluetooth carries most app traffic. The reverse-engineered protocol documents GATT characteristics, heartbeat behavior, ECDH pairing, relay framing and application messages.

The SDK is unofficial and firmware-sensitive, but it demonstrates that MYVU's useful display surfaces are not cryptographically inseparable from Meizu cloud services. For GlassesResearch scoring, this is strong evidence toward **hackability and practical owner control**, while official openness remains weak because the protocol was discovered by reverse engineering rather than documented by the manufacturer.

## External-visibility / privacy concern

Community reports mention visible green waveguide artifacts and light leakage from outside the glasses. This is anecdotal rather than verified GlassesResearch testing, but it is sufficient to create a specific bench test when hardware is obtained:

1. Render high-contrast text at brightness levels 1/10, 5/10 and 10/10.
2. Photograph the wearer from 0°, ±15°, ±30° and ±45°.
3. Test indoor dim, office, shaded outdoor and direct-sun conditions.
4. Score whether a bystander can detect illumination, distinguish glyph shapes, or actually read content.
5. Repeat with both clear and tinted / prescription optical configurations where possible.

This should become a reusable GlassesResearch **external display visibility / privacy leakage** protocol for all waveguide glasses.

## Alibaba sourcing: genuine MYVU / StarV listings

Alibaba already contains multiple listings that appear to be resale / distribution of genuine Meizu-family hardware rather than generic lookalikes.

### MYVU / StarV Air generation

Observed current Alibaba offers include:

- **MYVU AR Smart Glasses AI Assistant Navigation Cycling Support IOS Android With 2000 Nit Peak Brightness Visible in Daylight** — Shenzhen Qianlang Era Technology Co., Ltd.; approximately **US$218.80–298**, MOQ 1.
- **MYVU StarV AR Smart Glasses 4K Video AI Assistant 3D Simultaneous 13 Languages Real-Time Translation Cycling Support English** — Fangshuo Industrial Limited; approximately **US$219.90–299**, MOQ 1.
- **Meizu STARV MYVU AR Smart Glasses Touch Control Type-C Charging Speech Teleprompter Real-time Simultaneous Subtitle Translation** — Shenzhen Xinmiao Future Technology Co., Ltd.; approximately **US$399–459**, MOQ 1.
- A separate Alibaba category listing advertises **MYVU AR Smart Glasses Real-time Translation Glasses Subtitles Travel Navigation Teleprompter** at **US$122**, but MOQ is 50. This is interesting as a wholesale floor, not presently a sample-buy route.

The ~US$219–299 MOQ-1 listings are the current priority because they are dramatically below the US$400+ specialty-retail route while mapping closely to official MYVU specifications.

### StarV Air2 generation

Observed Alibaba offers include:

- **StarV Air2 AR Smart Glasses 4K AI Assistant ... 13 Languages Real-Time Translation Cycling Support** — Guangzhou Dingfeng Electronic Trading Co., Ltd.; approximately **US$205.60–205.80**, MOQ 1.
- Other StarV Air2 listings around **US$379–429** and **US$459–559** from separate trading companies.

The ~US$206 MOQ-1 Air2 listing is therefore a high-priority verification target. Its title contains inaccurate / inflated terms such as "4K," so identity must be established from photos, packaging, model number and supplier confirmation rather than trusting listing text.

## Alibaba sourcing: close optical relatives, not proven MYVU lineage

Alibaba also contains products that converge strongly on the same architecture but should **not** be labeled MYVU relatives without hardware evidence.

Current examples:

- **2026 AR+AI Smart Glasses Full Color Binocular Waveguide Lens...** — about US$273.99, MOQ 1.
- **AI Smart Glasses, Real-time Translation AR Glasses, Binocular Color Screen Light Waveguide HUD Navigation Teleprompter** — about US$290–298, MOQ 1.
- **AR Smart Glasses with AI Assistant, Real-Time Translation, AR Navigation, Teleprompter, Touch Control** — about US$187–199, MOQ 2.
- Shanghai Top Display **0.32-inch / 624×405 / 1200 nit / 20° FOV** display glasses — broad category pricing starts around US$70, MOQ 1.
- Multiple optical-engine modules are also available independently, including MicroLED / Micro-OLED waveguide engines below complete-glasses pricing.

These are valuable as comparative architecture candidates, but visual similarity, "waveguide" wording or matching use cases are insufficient to establish common OEM lineage.

## What would prove common lineage

For each Alibaba candidate, collect and compare:

- exact model number from packaging and regulatory label
- Bluetooth advertised name and GATT service UUIDs
- whether service `0x0BD1` / StarryNet characteristics appear
- companion app package / QR code
- firmware naming and version strings
- FCC / CE / SRRC identifiers
- frame geometry and temple mold details
- charging connector placement
- control layout
- waveguide in-coupler / out-coupler geometry
- display resolution and FOV
- battery model and capacity
- internal PCB markings after teardown

A candidate that exposes the MYVU StarryNet Bluetooth service family or identifies itself as XGA010C would be strong evidence of direct lineage. Matching only the optics is evidence of architectural similarity, not lineage.

## Purchase priority

### Priority A — sample if identity is confirmed

1. **Alibaba MYVU / StarV Air at ~US$219–299, MOQ 1**. Best combination of known 43 g binocular waveguide hardware, FCC identity, established protocol reverse engineering and current availability.
2. **Alibaba StarV Air2 at ~US$206, MOQ 1**. Potentially exceptional value if it is authentic Air2. Verify actual model, packaging, serial / regulatory labels and whether it uses the same or evolved protocol before purchase.

### Priority B — comparative sample

3. **US$187–199 translation/navigation/teleprompter AR waveguide listing** if exact optical construction and weight can be verified. It could expose a lower-cost ODM architecture competing directly with MYVU.
4. **US$273.99 full-color binocular waveguide listing** as a binocular comparison if supplier can provide real optical and electrical specifications.

### Pass for now

- US$399–559 MYVU / Air2 reseller listings unless they provide a materially safer return path or authenticated global hardware.
- Any listing using "4K", "AR", "HUD" or "AI" without photographs or specifications proving an actual near-eye display.

## GlassesResearch implications

MYVU should be elevated from ordinary product coverage into a tracked lineage / interoperability case study.

The important story is not simply that a 43 g binocular waveguide product exists. It is that:

1. mass-produced binocular diffractive-waveguide glasses reached ordinary-eyewear mass years ago;
2. the architecture is deliberately phone-companion rather than a miniature standalone computer;
3. the hardware exposes enough protocol surface that an independent community client can now drive teleprompter, navigation, notifications and AI output;
4. genuine hardware appears in Chinese wholesale channels for roughly US$200–300, with community reports suggesting occasional consumer-channel prices near US$100–150;
5. the successor Air2 continues the lightweight waveguide branch rather than abandoning it.

For HawkFrame-like design research, this makes MYVU / StarV one of the strongest existing reference architectures for "glasses that happen to have a HUD" rather than "an AR headset disguised as glasses."

## Open questions

- Is Air2 protocol-compatible with XGA010C / the community SDK?
- What is Air2's exact regulatory model number?
- Who fabricates the waveguide lens and MicroLED light engine for each generation?
- Is the original MYVU display monochrome despite the dual 1280×480 specification, and what exact color / spectral characteristics are used?
- What is the actual eyebox and eye-relief tolerance?
- What privacy leakage exists at realistic brightness levels?
- Can either generation be driven at a lower layer than Meizu's launcher scenes, or are applications restricted to predefined UI surfaces?
- Can the light engines / waveguides be acquired as modules from the upstream optical supplier?
- Are the ~US$206 Air2 and ~US$219 MYVU Alibaba listings authentic retail hardware, gray-market stock, refurbs, or clones?

## Sources

- Meizu MYVU / StarV Air official specifications: https://www.meizu.com/global/product/starv-air/specs
- Meizu MYVU launch / 2023 ecosystem announcement: https://m.meizu.com/global/news/1739
- Meizu StarV Air2 official product page: https://m.meizu.com/global/product/starv-air2
- Meizu StarV Air2 official specifications: https://www.meizu.com/pl/product/starv-air2/specs
- DreamSmart product-family description: https://www.dreamsmart.com/en/business
- Meizu StarV View official specifications: https://www.meizu.com/ro/product/starv-view/specs
- FCC listing for XGA010C: https://fcc.report/FCC-ID/2BHGZ-XGA010C
- XGA010C regulatory test report mirror: https://device.report/m/598cbbf6feceaa5954c5ada53d4fceaa5544213c277d63faae5a99646d97d22c
- MYVU XGA010C manual mirror: https://manuals.plus/m/153cfb33637c670d0b66ca2161385eb55d2342402b6776f923efaa3d64534070
- Community MYVU SDK: https://github.com/Panny777/Meizu-Myvu-SDK
- Reverse-engineered protocol: https://github.com/Panny777/Meizu-Myvu-SDK/blob/main/PROTOCOL.md
- Community MYVU client: https://github.com/Panny777/Meizu-Myvu-Client
- Alibaba MYVU / StarV search surfaces and current offers: https://www.alibaba.com/countrysearch/CN/virtual-assistant.html
- Alibaba AR smart-glasses search surface: https://www.alibaba.com/premium/ar_smart_glasses.html
- Alibaba teleprompter-glasses search surface: https://www.alibaba.com/insights/teleprompter-glasses.html

## Evidence state

Official Meizu / DreamSmart specifications and FCC identity: **verified from first-party / regulatory sources**.

Protocol openness: **verified as a working third-party reverse-engineering project, not official SDK support**.

Alibaba prices / suppliers: **discovery-state marketplace observations; require exact-listing and seller verification before purchase**.

Common lineage for non-MYVU Alibaba waveguide glasses: **not established**.