# High-Throughput Report Card Batch 06 — Epson, Sony, Lenovo, Iristick

**Research date:** 2026-08-12

This batch covers GLS-0106 through GLS-0119: seven Epson Moverio generations, Sony SmartEyeglass Developer Edition, two Lenovo ThinkReality A3 editions, and four Iristick enterprise models. The same catalog-wide 0–10 ruler defined in `research/REPORT_CARD_BENCHMARKS.md` is used here; scores are not normalized by era, product category, or enterprise intent.

## Report Cards

| ID | Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GLS-0106 | Epson Moverio BT-100 | 5.0 | 4.0 | N/A | 5.0 | 4.0 | 6.0 | 7.5 | 4.5 | 5.5 | 4.5 |
| GLS-0107 | Epson Moverio BT-200 | 6.0 | 5.5 | 4.0 | 6.0 | 6.0 | 7.0 | 8.0 | 6.5 | 6.0 | 5.5 |
| GLS-0108 | Epson Moverio BT-300 | 7.0 | 7.0 | 5.5 | 7.0 | 6.5 | 7.0 | 8.0 | 6.5 | 7.0 | 6.5 |
| GLS-0109 | Epson Moverio BT-30C | 6.5 | 7.5 | N/A | 6.5 | 6.5 | 8.0 | 9.5 | 6.5 | 7.0 | 7.0 |
| GLS-0110 | Epson Moverio BT-35E | 7.0 | 6.5 | 5.5 | 7.0 | 7.0 | 8.0 | 9.0 | 7.0 | 7.0 | 6.5 |
| GLS-0111 | Epson Moverio BT-40 / BT-40S | 7.5 | 7.0 | N/A | 7.5 | 7.0 | 8.0 | 9.0 | 7.0 | 8.0 | 7.0 |
| GLS-0112 | Epson Moverio BT-45C / BT-45CS | 8.5 | 6.5 | 7.0 | 8.0 | 7.5 | 8.5 | 9.0 | 7.5 | 8.5 | 7.5 |
| GLS-0113 | Sony SmartEyeglass Developer Edition SED-E1 | 6.0 | 5.0 | 4.5 | 6.0 | 6.5 | 7.0 | 8.0 | 6.5 | 5.5 | 5.0 |
| GLS-0114 | Lenovo ThinkReality A3 PC Edition | 8.5 | 6.5 | 6.5 | 8.0 | 7.0 | 8.0 | 9.0 | 7.0 | 8.5 | 7.0 |
| GLS-0115 | Lenovo ThinkReality A3 Industrial Edition | 8.5 | 6.5 | 7.5 | 8.5 | 7.5 | 8.0 | 8.5 | 7.5 | 8.5 | 7.0 |
| GLS-0116 | Iristick G2 | 7.5 | 8.0 | 7.0 | 7.5 | 6.0 | 8.0 | 8.5 | 6.0 | 6.5 | 6.5 |
| GLS-0117 | Iristick G2 PRO | 8.0 | 8.0 | 7.5 | 8.0 | 6.0 | 8.0 | 8.5 | 6.0 | 6.5 | 6.5 |
| GLS-0118 | Iristick H1 | 8.5 | 5.5 | 8.0 | 8.0 | 6.0 | 8.0 | 8.5 | 6.0 | 7.0 | 6.5 |
| GLS-0119 | Iristick G3 | 9.0 | 8.0 | 8.5 | 8.5 | 6.5 | 8.5 | 9.0 | 6.5 | 8.0 | 8.0 |

## Evidence notes

### Epson Moverio lineage

BT-100 established the lineage as a self-contained Android-powered binocular see-through display with a separate controller, Wi-Fi, removable storage and roughly six-hour battery life. Its historical importance is high, but on the current catalog-wide ruler its heavy two-piece architecture and limited software environment constrain wearability, display quality and owner freedom.

BT-200 materially improved the platform with a 960×540 binocular display, 23° field of view, camera, microphone, GPS, motion sensors, Bluetooth, Wi-Fi, Android, removable storage and a documented developer-oriented product path. The later BT-300 moved the family toward a much lighter Si-OLED AR form factor and a more credible application-development platform.

The tethered BT-30C changed the ownership model in a useful way: by acting primarily as a USB-C DisplayPort wearable display, it lets the owner choose the host computer and avoids mandatory manufacturer-cloud dependence. BT-35E adds camera and sensor access for enterprise workflows. BT-40/40S continue the modern tethered architecture with Epson's maintained Basic Function SDK.

BT-45C/45CS is the strongest Moverio entry in this batch. Epson documents a binocular Full-HD Si-OLED display, 34° field of view, centered 8MP autofocus camera, motion/environment sensors, integrated audio on BT-45C, USB-C host support, IP52 protection, industrial mounting options, and Android/Windows development through the Moverio Basic Function SDK. Epson documents display, sensor, camera and audio control APIs. That is substantial developer access, but it remains well short of the Monocle/Frame 10/10 openness benchmark because firmware, schematics and low-level hardware control are not broadly open.

### Sony SmartEyeglass SED-E1

Sony sold SED-E1 specifically as a Developer Edition and accompanied it with an SDK. The hardware combined a binocular transparent waveguide, 419×138 green monochrome display, 20° diagonal field of view, accelerometer, gyroscope, compass, light sensor, microphones, 3MP camera, Bluetooth and Wi-Fi. At approximately 77 g for the eyewear plus a cabled controller, and with roughly 150 minutes of non-camera battery life, it was more developer platform than everyday eyewear. Its public SDK earns meaningful openness and hackability credit, but the platform never approached open-firmware or open-hardware territory.

### Lenovo ThinkReality A3

Both A3 editions share unusually capable enterprise hardware: Qualcomm XR1, binocular 1080p displays, 8MP RGB camera, dual fisheye tracking cameras, 6DoF tracking, microphones, speakers, USB-C/DisplayPort connectivity and a roughly 130 g glasses assembly. The PC Edition emphasizes host-driven virtual monitors and therefore scores especially well for cloud independence and host choice. The Industrial Edition layers Lenovo's ThinkReality platform, managed deployment, remote assistance, guided workflows and 3D visualization over the same hardware, giving it stronger contextual/visual-AI utility. Lenovo's ThinkReality ecosystem includes SDK and enterprise deployment tooling, but the hardware/firmware stack remains proprietary.

### Iristick lineage

Iristick's design philosophy is notably owner-host-friendly: the glasses rely on a connected smartphone for compute, networking and application installation rather than forcing a dedicated vendor compute ecosystem. That architecture improves cloud independence and practical owner control even though the glasses themselves are not open hardware.

G2/G2 PRO pair a lightweight safety-glasses form factor with a central camera, optical zoom camera, adjustable monocular LCD HUD, microphones, speaker, touch/voice input and a pocket unit. G2 PRO is documented at 78 g, with a 16MP central camera, 5MP 6× optical-zoom module, 1080p video, hot-swappable battery and ANSI/EN safety certification.

H1 prioritizes rugged industrial deployment over eyewear-like wearability: 168 g, IP67, dual 16MP main cameras, zoom camera, OLED HUD, quad microphones, swappable power and PPE integration.

G3 is the strongest Iristick design in the batch. It uses a 95 g safety-glasses form factor, 640×400 OLED HUD up to 2000 nits, 16MP wide camera plus 16MP 3× optical-zoom camera, 1080p streaming, beamforming microphones, touch/voice control, prescription insert option, ANSI/EN safety certification and IP54. It connects directly to Android or iOS hosts over USB-C, drawing power and compute from the user's phone. This architecture gives it excellent practical control and cloud independence, while the proprietary device layer keeps openness/hackability well below the open-platform benchmark.

## Primary sources

- Epson BT-100 product/support: https://epson.com/Certified-ReNew/Wearables/Moverio-BT-100-Wearable-Display/p/V11H423020
- Epson BT-200 product/support: https://epson.com/Certified-ReNew/Wearables/Moverio-BT-200-Smart-Glasses-%28Developer-Version-Only%29/p/V11H560020
- Epson BT-300 Developer Edition release: https://news.epson.com/news/epson-announces-availability-of-developer-and-drone-editions-of-moverio-bt-300-ar-smart-glasses
- Epson BT-30C release: https://news.epson.com/news/moverio-bt-30c-smart-glasses
- Epson Moverio technical portal / SDK: https://tech.moverio.epson.com/en/
- Epson Moverio technical FAQ: https://tech.moverio.epson.com/en/technical_faq/
- Epson BT-45C product page: https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-BT-45C-AR-Smart-Glasses/p/V11H970020
- Sony SmartEyeglass SED-E1 release/specifications: https://www.sony.com/en/SonyInfo/News/Press/201502/15-016E/
- Lenovo ThinkReality A3 support specifications: https://support.lenovo.com/us/en/solutions/PD500497
- Lenovo ThinkReality A3 release: https://news.lenovo.com/pressroom/press-releases/thinkreality-a3-most-versatile-smart-glasses-ever-designed-for-the-enterprise/
- Iristick specifications: https://docs.iristick.com/smart-glasses/specifications/
- Iristick G2 PRO: https://iristick.com/tools/Iristick.G2-PRO/
- Iristick G3: https://iristick.com/tools/Iristick.G3/

## Batch result

Fourteen more canonical models now have explicit evidence-backed report cards using the fixed catalog-wide ruler. This completes the currently enumerated enterprise/industrial section of `THE_LIST.md` through GLS-0119; remaining work can now shift to the catalog's known-gap queue and any newly admitted models.