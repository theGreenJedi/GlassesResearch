# Report Card Research Batch 02

This batch applies the catalog-wide benchmark rubric and the report-card-first pipeline. Scores are relative to the same 0–10 ruler used across the entire catalog.

## GLS-0064 — Rokid Glasses

**Canonical check:** no correction required. The catalog correctly identifies Rokid Glasses as display-equipped AI/AR glasses rather than the separate display-free Rokid AI Glasses Style.

**Evidence basis:** Rokid documents a 49 g frame, Snapdragon AR1 Gen 1 plus NXP RT600, 2 GB RAM, 32 GB storage, dual-eye monochrome MicroLED waveguide display at 480×640, 30° FOV and up to 1,500 nits, 12 MP Sony IMX681 camera, four microphones, dual open-ear speakers, Wi-Fi 6, Bluetooth 5.3, 210 mAh battery, prescription support, translation, navigation, transcription and multimodal AI features.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.5 | A- | Strong integration of AR1 compute, camera, display, audio and wireless hardware in a 49 g frame, though battery capacity is still constrained by eyewear form factor. |
| Wearability | 8.5 | A- | 49 g, conventional-eyewear styling and prescription support are strong; still heavier and more electronic than the most discreet HUD glasses. |
| Visual AI | 8.5 | A- | A 12 MP first-person camera plus multimodal AI and image-recognition workflows make visual understanding a first-class function. |
| Software | 8.0 | B+ | Hi Rokid plus translation, navigation, transcription and AI features create a broad consumer software layer; developer openness is not as fully documented as the most open platforms. |
| Display / HUD | 8.5 | A- | Dual-eye MicroLED waveguides, 30° FOV and 1,500-nit brightness make it a strong glanceable HUD, though monochrome and modest-resolution compared with full-color AR leaders. |
| Openness | 7.0 | B- | Rokid publicly promotes an SDK/developer ecosystem, but current public evidence does not approach Monocle/Frame-level firmware, protocol and hardware openness. |
| Owner Control | 6.5 | C+ | Owners gain significant feature control but remain materially tied to Rokid's software stack and companion app for core functions. |
| Cloud Independence | 5.5 | C- | Some translation and AI functions can operate offline, but many headline AI services depend on networked models and the companion ecosystem. |
| Hackability | 6.5 | C+ | Developer resources and a large SDK community help, but low-level firmware/hardware modification paths are not documented at benchmark levels. |
| Value | Not yet graded | — | Requires a current market-price and competitor comparison. |

**Primary sources:** https://global.rokid.com/products/rokid-glasses ; https://global.rokid.com/pages/rokid-glasses ; https://global.rokid.com/pages/academy

## GLS-0066 — RayNeo X3 Pro

**Canonical check:** no correction required. The listing correctly treats X3 Pro as a current binocular full-color AI+AR platform.

**Evidence basis:** RayNeo documents binocular full-color MicroLED diffractive waveguides, 640×480 resolution, 30° FOV, 3,500-nit average and 6,000-nit peak brightness, Snapdragon AR1 Gen 1, 4 GB RAM, 32 GB storage, a 245 mAh battery, RGB plus spatial cameras, 12 MP Sony IMX681 imaging, RayNeo AIOS, Gemini Live, prescription support and a developer-facing Creator Mode.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 9.0 | A | Excellent current-generation integration of full-color displays, AR1 compute, dual-camera sensing, audio, memory and storage in a wearable frame. |
| Wearability | 7.5 | B | At about 76 g it is substantially more wearable than a headset, but still noticeably heavier than ordinary glasses and lightweight HUD competitors. |
| Visual AI | 9.0 | A | 12 MP RGB imaging, spatial camera hardware, Gemini integration and a spatial UI make contextual vision a core capability. |
| Software | 8.5 | A- | RayNeo AIOS, navigation, translation, Gemini and an AR app ecosystem provide a broad feature surface. |
| Display / HUD | 9.0 | A | Full-color binocular MicroLED, 640×480, 30° FOV and extreme brightness put the X3 Pro near the top of everyday-form-factor AR displays. |
| Openness | 7.5 | B | Creator Mode and developer positioning provide meaningful access, but the underlying firmware/OS stack is not documented as open. |
| Owner Control | 7.0 | B- | Developers can build within the supported ecosystem, while platform replacement and low-level control remain vendor-bounded. |
| Cloud Independence | 5.5 | C- | Core hardware can operate locally, but Gemini and several flagship services materially depend on cloud-connected AI. |
| Hackability | 7.0 | B- | Creator Mode provides a supported experimentation surface, though there is no evidence of firmware-source, schematics or debug access comparable to the 10/10 benchmark. |
| Value | Not yet graded | — | Requires a contemporaneous price/performance comparison. |

**Primary sources:** https://www.rayneo.com/collections/ai-smart-glasses/products/x3-pro-ai-display-glasses ; https://eu.rayneo.com/products/x3-pro-ai-display-glasses

## GLS-0098 — Vuzix M400

**Canonical check:** no correction required. The catalog correctly classifies M400 as an enterprise standalone Android wearable computer.

**Evidence basis:** Vuzix documents a modified Android 11 platform and explicitly states that standard Android development methods and APIs can be used for camera, sensors, Bluetooth/BLE, SQLite and other functions, with Vuzix-specific SDKs for speech, barcode and device-specific features.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.0 | B+ | Rugged enterprise wearable-computer architecture with camera, sensors, connectivity and modular mounting, but much less discreet than consumer eyewear. |
| Wearability | 5.5 | C- | Purpose-built for work rather than social invisibility; practical for shifts and task use, not ordinary all-day glasses wear. |
| Visual AI | 7.5 | B | Camera and local Android compute make machine-vision applications practical, though modern multimodal AI is not the native product identity. |
| Software | 9.0 | A | Standard Android development plus Vuzix SDKs and conventional APIs provide a mature application platform. |
| Display / HUD | 7.5 | B | Functional monocular enterprise HUD optimized for task information rather than immersive AR. |
| Openness | 8.5 | A- | Standard Android APIs, BLE, documented SDKs and normal app-development methods provide substantial access, though firmware and hardware design are not open. |
| Owner Control | 9.0 | A | Organizations and developers can deploy their own Android applications and control workflows without being confined to one consumer companion app. |
| Cloud Independence | 9.0 | A | Local Android applications can perform core device functions without inherent dependence on Vuzix cloud services. |
| Hackability | 8.5 | A- | Standard Android tooling, BLE and documented SDKs create a strong experimentation surface, but not a firmware/schematic-level one. |
| Value | Not yet graded | — | Enterprise pricing and use-case economics require a current comparison. |

**Primary source:** https://support.vuzix.com/docs/m400-m4000-technical-details

## GLS-0099 — Vuzix M4000

**Canonical check:** no correction required. The catalog correctly separates M4000 from M400 while keeping them in the same Android/software lineage.

**Evidence basis:** Vuzix documents the M4000 on the same modified Android 11 application platform as M400, with standard Android APIs for camera, sensors, Bluetooth/BLE, databases and Vuzix SDKs for device-specific functions. The important distinction is hardware/optical configuration rather than software openness.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.5 | A- | Strong enterprise hardware and optics with the same capable wearable-compute foundation as M400, aimed at hands-free field work. |
| Wearability | 5.5 | C- | Like M400, it is a task wearable rather than ordinary eyewear; comfort is secondary to ruggedness and enterprise utility. |
| Visual AI | 7.5 | B | Camera plus local Android compute support strong machine-vision and inspection workflows. |
| Software | 9.0 | A | Standard Android development and Vuzix SDKs provide a mature, familiar developer environment. |
| Display / HUD | 8.0 | B+ | The M4000's display-focused enterprise configuration is a stronger HUD proposition than M400, while remaining monocular and task-centric. |
| Openness | 8.5 | A- | Standard Android APIs, BLE and official SDK access are excellent by enterprise standards, but below firmware/hardware-open benchmarks. |
| Owner Control | 9.0 | A | Custom applications and enterprise workflows can be deployed without dependence on a single vendor consumer app. |
| Cloud Independence | 9.0 | A | Core local operation and custom Android apps do not inherently require cloud services. |
| Hackability | 8.5 | A- | Strong supported development access, though not low-level open hardware/firmware. |
| Value | Not yet graded | — | Requires contemporaneous enterprise pricing and deployment-value analysis. |

**Primary source:** https://support.vuzix.com/docs/m400-m4000-technical-details

## Batch result

Four additional canonical models now have explicit evidence-backed Report Cards using the shared benchmark ruler. No canonical corrections were required. The resulting cards can now serve as the source foundation for auditing or writing their human-readable editorial summaries.
