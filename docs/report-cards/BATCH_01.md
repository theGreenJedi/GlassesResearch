# Report Card Research Batch 01

This batch follows the report-card-first pipeline: investigate, reconcile the canonical listing, preserve the evidence basis, grade only what can be defended, then use the results to audit or write editorial prose.

## GLS-0050 — Brilliant Labs Monocle

**Canonical check:** no correction required. The catalog correctly treats Monocle as a 2023 open/developer display device sold for retail/developer use.

**Evidence basis:** Brilliant Labs documents a 640×400 color OLED with roughly 20° FOV, 5 MP camera, microphone, Bluetooth 5.2, 70 mAh battery, touch controls, an nRF52832 MCU, FPGA acceleration, MicroPython, custom firmware support, OTA firmware, custom FPGA images, published schematics, mechanical files, and manual SWD/JTAG programming paths.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.0 | B+ | Remarkably capable for a clip-on module: display, camera, microphone, FPGA, BLE, RAM/flash and charging case; battery capacity and one-eye form limit endurance and polish. |
| Wearability | 6.0 | C | Very small, but it is visibly a clip-on module rather than ordinary eyewear and places hardware asymmetrically on one lens. |
| Visual AI | 8.0 | B+ | 5 MP camera, microphone, FPGA acceleration and documented camera access make it unusually suitable for owner-built CV/AI experiments. |
| Software | 9.0 | A | MicroPython, documented APIs, AR Studio, firmware update tooling and direct application development provide an unusually approachable stack. |
| Display / HUD | 7.5 | B | 640×400 color OLED and 20° FOV are useful for glanceable AR, though monocular and narrow compared with modern binocular AR systems. |
| Openness | 10.0 | A+ | Open-source software, schematics, mechanical files, custom firmware, FPGA development and documented low-level programming are exceptional. |
| Owner Control | 10.0 | A+ | Owners can replace firmware, program the FPGA, control sensors/display directly and avoid a single vendor application path. |
| Cloud Independence | 9.5 | A+ | Core device operation and custom applications can run without a vendor cloud; network services are optional application choices. |
| Hackability | 10.0 | A+ | SWD/JTAG, firmware source, schematics, MicroPython, FPGA access and published hardware details make Monocle a benchmark hacker device. |
| Value | Not yet graded | — | Current retail/secondary-market pricing needs a contemporaneous check before assigning a durable value score. |

**Primary sources:** Brilliant Labs Monocle Hardware Manual; Brilliant Labs Monocle Technical Documentation.

## GLS-0047 — Even Realities G1

**Canonical check:** no correction required. The listing correctly identifies G1 as a 2024 current retail discreet-display product.

**Evidence basis:** Even Realities documents binocular waveguides, dual green MicroLED displays, 640×200 resolution, 25° FOV, 20 Hz refresh, up to 1000-nit brightness, prescription support, lightweight conventional-eyewear construction, up to 1.5-day battery life, and companion-app functions including QuickNote, Translate, Navigate, Teleprompt, Even AI and notifications. No outward-facing camera is part of the product architecture.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 7.5 | B | Focused binocular HUD hardware, good optics and battery life, but intentionally limited sensing/compute compared with camera-first AI glasses. |
| Wearability | 9.5 | A+ | Ordinary-eyewear styling, light balanced construction and prescription support are central design strengths. |
| Visual AI | N/A | N/A | No outward-facing camera means visual understanding of the wearer’s scene is not part of the hardware design. |
| Software | 7.0 | B- | Useful first-party functions and companion software, but the public software surface is much narrower than open developer platforms. |
| Display / HUD | 8.0 | B+ | Binocular green MicroLED waveguides, 25° FOV and high brightness make it a strong glanceable HUD despite low refresh and monochrome output. |
| Openness | 5.0 | D+ | Public owner/developer access is limited compared with platforms exposing broad SDK, protocol or firmware control. |
| Owner Control | 5.0 | D+ | Owners control features and presentation but do not receive deep platform substitution or firmware control. |
| Cloud Independence | 5.5 | C- | Basic display functions are phone-linked, while AI/translation/navigation features materially depend on companion software and network services. |
| Hackability | 4.5 | D | The product is optimized as a finished consumer appliance rather than a documented experimentation platform. |
| Value | Not yet graded | — | Requires a current price and competitor check. |

**Primary sources:** Even Realities G1 product/specification page; Even Realities support documentation for G1 purchasing, fit and prescription options.

## GLS-0068 — Snap Spectacles (2024, 5th Gen)

**Canonical check:** no correction required. The listing correctly treats the fifth-generation Spectacles as a 2024 developer-access standalone AR platform.

**Evidence basis:** Snap documents standalone operation, see-through stereo waveguides, LCoS projectors, 46° FOV, 37 pixels/degree, 6DoF tracking, hand tracking, voice input, stereo audio, six microphones, dual Snapdragon compute, two color cameras, two infrared computer-vision cameras, IMUs, Wi-Fi 6, Bluetooth, GNSS, 226 g mass and roughly 45 minutes of continuous runtime. Lens Studio, Snap OS, developer kits and experimental camera/microphone/location/network permissions form the supported development stack.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 9.0 | A | Dense standalone AR hardware with stereo displays, multiple cameras, IR sensing, dual compute and strong tracking; battery/runtime and mass remain major constraints. |
| Wearability | 4.5 | D | At roughly 226 g and around 45 minutes continuous runtime, this is a developer wearable computer rather than ordinary all-day glasses. |
| Visual AI | 9.0 | A | Multiple outward-facing color/IR cameras, IMUs and supported experimental permissions make contextual vision a core capability. |
| Software | 9.0 | A | Snap OS, Lens Studio, developer kits, interaction frameworks and active tooling form a mature AR development environment. |
| Display / HUD | 9.0 | A | Stereo see-through waveguides, 46° FOV, 37 PPD and high-rate reprojection place the display system well above discreet notification HUDs. |
| Openness | 7.5 | B | Broad supported developer APIs and tools are available, but the underlying OS/firmware remains vendor-controlled rather than open source. |
| Owner Control | 7.0 | B- | Developers can build rich experiences and request extended permissions, but cannot freely replace the platform or firmware stack. |
| Cloud Independence | 7.0 | B- | The glasses are standalone and can run local experiences, while Snap’s broader ecosystem and optional cloud services remain important to many workflows. |
| Hackability | 7.5 | B | Excellent supported experimentation surface through Lens Studio and experimental APIs, but little evidence of low-level firmware/hardware modification access. |
| Value | Not yet graded | — | Developer-program economics and access conditions are not comparable to normal retail pricing. |

**Primary sources:** Spectacles official hardware/technical-specification pages; Spectacles Build/Lens Studio documentation; Spectacles Support developer-settings documentation.

## GLS-0055 — Vuzix Blade 2

**Canonical check:** no correction required. The catalog correctly treats Blade 2 as an enterprise-oriented monocular display platform.

**Evidence basis:** Vuzix documents a right-eye 480×480 full-color waveguide display with 20° FOV, autofocus HD camera, stereo speakers, noise-cancelling microphones, Wi-Fi and Bluetooth, Android architecture, touch/voice interaction and developer tooling. The broader Blade developer documentation describes Android application development and standard wearable-computer capabilities.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.0 | B+ | Mature standalone wearable-computer hardware with camera, audio, display and wireless connectivity, though display resolution/FOV now look modest beside newer AR systems. |
| Wearability | 7.0 | B- | More glasses-like than industrial headsets and safety-certified, but still visibly technical and heavier than ordinary eyewear. |
| Visual AI | 7.0 | B- | Camera plus Android compute support owner/developer vision workflows, though modern multimodal AI is not the product’s defining native feature. |
| Software | 8.5 | A- | Android application development and Vuzix SDK/tooling create a strong supported software path. |
| Display / HUD | 7.0 | B- | Full-color 480×480 waveguide HUD is useful but monocular and narrow by current AR standards. |
| Openness | 8.0 | B+ | Standard Android development plus official SDKs and developer resources provide substantial application-level access. |
| Owner Control | 8.0 | B+ | Owners/developers can deploy purpose-built Android applications rather than being confined to a single companion-app workflow. |
| Cloud Independence | 8.5 | A- | Core Android applications and device functions can operate locally without inherent dependence on a vendor AI cloud. |
| Hackability | 8.0 | B+ | Supported Android/SDK access gives a strong experimentation surface, though firmware-level openness is below Brilliant Labs devices. |
| Value | Not yet graded | — | Current enterprise/retail pricing and use-case value need a contemporaneous comparison. |

**Primary sources:** Vuzix Blade 2 product page; Vuzix Blade developer overview and SDK documentation.

## Batch result

Four canonical models now have explicit evidence-backed Report Cards under the new pipeline. No canonical corrections were required in this batch. Each existing editorial paragraph for these models should be treated as provisionally validated against this evidence package; future edits should preserve the distinction between sourced facts and editorial interpretation.
