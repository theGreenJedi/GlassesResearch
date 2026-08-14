# Report Card Research Batch 06

This batch applies the shared 0–10 benchmark ruler and the report-card-first research pipeline. Scores are catalog-relative, not category-relative. N/A is used only when a dimension genuinely does not apply.

## GLS-0018 — Razer Anzu

**Canonical check:** no correction required. The catalog correctly identifies Anzu as a 2021 legacy audio-glasses product.

**Evidence basis:** Razer documents open-ear audio, dual 16 mm drivers, two omnidirectional microphones, touch controls, Bluetooth 5.2, SBC/AAC, approximately five hours of battery life, 43–48 g weight, blue-light-filtering lenses, polarized sunglass replacement lenses, and a low-latency gaming mode through the Razer Audio app. There is no camera or display.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 6.5 | C+ | Competent audio hardware, microphones, touch controls and interchangeable lenses, but intentionally limited sensing and compute. |
| Wearability | 8.0 | B+ | 43–48 g and conventional frame styling make Anzu reasonably wearable, though still heavier than ordinary glasses. |
| Visual AI | N/A | N/A | No outward-facing camera is present. |
| Software | 5.5 | C- | Razer Audio app support, EQ/control and low-latency mode are useful, but the software surface is narrow. |
| Display / HUD | N/A | N/A | No display is present. |
| Openness | 3.0 | F+ | No meaningful public SDK, firmware source or hardware-development pathway is documented. |
| Owner Control | 4.0 | D- | Owners can pair broadly over Bluetooth and use standard audio functions, but cannot substantially repurpose the device platform. |
| Cloud Independence | 8.5 | A- | Core Bluetooth audio, microphone and control functions do not inherently require a vendor cloud. |
| Hackability | 3.5 | F+ | Standard Bluetooth audio is accessible, but there is little documented path to deeper device modification. |
| Value | Not yet graded | — | Requires a current secondary-market comparison. |

**Primary source:** https://mysupport.razer.com/app/answers/detail/a_id/4143/

## GLS-0021 — Huawei Eyewear 2

**Canonical check:** no correction required. The listing correctly treats Eyewear 2 as a 2023 region-limited current audio-glasses product.

**Evidence basis:** Huawei documents multiple optical/sunglass frame styles, roughly 36.6–43 g depending on frame/lenses, dual open-ear drivers, call noise reduction, touch controls, wear detection, Bluetooth 5.3, dual-device connection, IP54 resistance, accelerometer/gyroscope/capacitive sensing, 110 mAh per temple, up to 11 hours music playback, nine hours calling, and 50-minute full charging. There is no camera or display.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 7.0 | B- | Strong audio, sensors, battery, Bluetooth 5.3 and IP54 integration for a camera-free product. |
| Wearability | 9.0 | A | Multiple conventional optical styles, low-40 g mass and prescription-friendly design make wearability a core strength. |
| Visual AI | N/A | N/A | No outward-facing camera is present. |
| Software | 6.5 | C+ | Useful gesture customization, wear detection and dual-device behavior, but the software stack remains a finished consumer experience rather than a platform. |
| Display / HUD | N/A | N/A | No display is present. |
| Openness | 3.5 | F+ | Public developer or firmware-level access is minimal. |
| Owner Control | 4.5 | D | Cross-platform Bluetooth and dual-device use provide practical flexibility, but platform substitution is limited. |
| Cloud Independence | 9.0 | A | Core audio, calls, controls and Bluetooth operation are local and do not inherently depend on Huawei cloud services. |
| Hackability | 3.5 | F+ | No meaningful public low-level development path is documented. |
| Value | Not yet graded | — | Requires a current regional price/competitor comparison. |

**Primary sources:** https://consumer.huawei.com/en/audio/huawei-eyewear-2/ ; https://consumer.huawei.com/en/audio/huawei-eyewear-2/specs/

## GLS-0038 — Mentra Live

**Canonical check:** no correction required. The catalog correctly identifies Mentra Live as a current camera/audio product sold to retail and developer users.

**Evidence basis:** Mentra documents a 43 g frame, 119° camera, 3264×2448 stills, 1080p video, stereo speakers, three microphones, touch/buttons, Wi-Fi, Bluetooth, 260 mAh glasses battery, 2200 mAh charging case, 12+ hours mixed use, and MentraOS. Mentra states that developers can build Android/iOS apps that directly control camera, speakers, microphone, touchpad and buttons, including offline operation without Mentra-hosted cloud infrastructure. MentraOS is MIT-licensed and publicly developed. The public SDK further documents a glasses-side command path and version-linked durable OTA manifests; it also documents default usage telemetry, including a manufacturing serial, that owner-built apps can disable. [EV-0060](../../evidence/EV-0060-Mentra-Bluetooth-SDK-OTA-owner-control.md) preserves the architecture, release policy, privacy control and claim limits.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.0 | B+ | Strong camera/audio/connectivity package in a notably light frame; absence of a display narrows use cases but improves weight and endurance. |
| Wearability | 9.0 | A | At 43 g with a conventional frame and 12+ hour mixed-use claim, Mentra Live is unusually wearable for developer-oriented camera glasses. |
| Visual AI | 8.5 | A- | Wide-angle camera, microphones and open hardware access make it highly suitable for custom visual-AI workflows. |
| Software | 9.0 | A | MentraOS, app ecosystem, SDKs and direct hardware APIs create a broad development surface. |
| Display / HUD | N/A | N/A | Mentra Live intentionally has no display. |
| Openness | 9.5 | A+ | MIT-licensed MentraOS, public SDKs and direct control over exposed I/O put it very close to the catalog benchmark. |
| Owner Control | 9.5 | A+ | Owners can build their own host apps, control sensors and audio directly, work offline and avoid Mentra-hosted cloud infrastructure. |
| Cloud Independence | 9.5 | A+ | Core custom apps can run without Mentra cloud; cloud AI is optional to the owner’s chosen workflow. |
| Hackability | 9.0 | A | Open source OS/SDK and direct hardware-control paths make it highly hackable, though the hardware itself is not documented at Monocle/Frame schematic/firmware depth. |
| Value | Not yet graded | — | Current retail price is documented, but a full catalog-relative value comparison is still required. |

**Primary sources:** https://mentraglass.com/live ; https://github.com/Mentra-Community/MentraOS ; https://github.com/Mentra-Community/MentraOS/blob/dev/mobile/modules/bluetooth-sdk/README.md ; https://github.com/Mentra-Community/MentraOS/blob/dev/mobile/modules/bluetooth-sdk/RELEASING_CI.md

## GLS-0051 — Brilliant Labs Frame

**Canonical check:** no correction required. The catalog correctly identifies Frame as a 2024 open/developer display product.

**Evidence basis:** Brilliant documents a 640×400 color OLED, 20° FOV, 720p camera, microphone, FPGA, Bluetooth 5.3, 210 mAh battery, motion sensors, Lua-based OS, prescription support, full BLE development, Python/Flutter SDKs, Lua REPL, OTA firmware, open-source firmware, FPGA source, schematics, mechanical files and SWD access to the MCU.

| Dimension | Score | Grade | Evidence-based judgment |
|---|---:|:---:|---|
| Hardware | 8.5 | A- | Compact color display, camera, microphone, FPGA and sensors make Frame unusually capable for lightweight experimental eyewear. |
| Wearability | 7.5 | B | More conventional than Monocle and prescription-capable, but still visibly electronic and constrained by small-device battery/optics. |
| Visual AI | 8.5 | A- | 720p camera, microphone, FPGA and direct developer access make Frame a strong owner-controlled CV/AI platform. |
| Software | 9.5 | A+ | Lua on-device execution, BLE APIs, Python/Flutter SDKs, VS Code tooling and open firmware provide an exceptional software surface. |
| Display / HUD | 7.5 | B | 640×400 color OLED and 20° FOV are useful and programmable, though monocular/narrow relative to leading binocular AR displays. |
| Openness | 10.0 | A+ | Firmware source, FPGA source, schematics, mechanical files, BLE protocol documentation and custom firmware access meet the current catalog benchmark. |
| Owner Control | 10.0 | A+ | Owners can replace host software, execute their own code, alter firmware and FPGA logic, and avoid a single vendor application path. |
| Cloud Independence | 9.5 | A+ | Core hardware and owner-written applications can operate without a vendor cloud; cloud AI is optional. |
| Hackability | 10.0 | A+ | Open firmware, SWD access, FPGA source, schematics, Lua, direct BLE and documented hardware internals meet the catalog benchmark. |
| Value | Not yet graded | — | Requires a current price/performance comparison against the broader catalog. |

**Primary sources:** https://docs.brilliant.xyz/frame/hardware/ ; https://docs.brilliant.xyz/frame/frame-sdk/

## Batch result

Four more canonical models now have explicit evidence-backed Report Cards using the same catalog-wide ruler. This batch also strengthens the benchmark picture: Frame joins Monocle at 10/10 for Openness and Hackability, while Mentra Live establishes a near-benchmark example of open camera/audio glasses with unusually strong wearability and cloud independence.
