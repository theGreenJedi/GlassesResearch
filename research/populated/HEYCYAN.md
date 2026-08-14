# HeyCyan / W610 — populated research record

Canonical lineage source: [`lineages/HEYCYAN.md`](../../lineages/HEYCYAN.md). Earlier detailed population work remains in [`lineages/HEYCYAN_POPULATION.md`](../../lineages/HEYCYAN_POPULATION.md). This normalized record makes the lineage discoverable alongside the other populated research families.

## Lineage identity
Confirmed commonality is the HeyCyan software ecosystem. Confirmed catalog members include W610 (GLS-0039) and Anko Camera Glasses (GLS-0120). Shared software does **not** prove common PCB, chipset, firmware image, charging system, mechanical design or ODM.

## Evidence base
Core evidence includes:

- EV-0001 — HeyCyanSmartGlassesSDK
- EV-0002 — CyanBridge / Alternative HeyCyan App and SDK
- EV-0003 — CyanBridge release history
- EV-0006 — W610 FCC record
- EV-0007 — SANVNET W610-linked regulatory manual
- EV-0008 — Goodway W610 specification/customization page
- [`evidence/EV-0033-CyanBridge-v2.1.1.md`](../../evidence/EV-0033-CyanBridge-v2.1.1.md) — current CyanBridge 2.1.1 evidence
- [`evidence/EV-0044-W610-community-protocol-and-owner-access.md`](../../evidence/EV-0044-W610-community-protocol-and-owner-access.md) — bounded protocol and owner-access assessment

## W610 connectivity / software
GlassesResearch directly observed Bluetooth identity `HeyCyan Glasses`. Public community projects demonstrate Bluetooth/BLE interaction and independent Android companion software. Community work also documents Bluetooth-to-Wi-Fi media-transfer behavior on compatible devices.

Confidence is strongest for W610/identified HeyCyan-compatible hardware; protocol equivalence must not be assumed for every marketplace rebrand.

## Owner control and openness
W610 has unusually strong owner-control evidence for low-cost consumer glasses:

- public community SDK;
- independent companion application;
- BLE interaction outside the vendor application;
- third-party assistant/model pathways;
- vendor-app-independent hands-on startup/discovery work.

CyanBridge v2.1.1 strengthens this materially by documenting remote OpenAI-compatible model endpoints, including Ollama/other servers reachable through owner-controlled networking, while also improving HeyCyan media-sync reliability and diagnostics.

This supports strong application/companion-level Openness, Owner Control and Hackability. It does **not** establish open firmware, an unlocked boot chain or unrestricted low-level sensor access.

## AI architecture
The ecosystem supports owner-selected downstream assistant/model workflows through companion software. Current evidence does not establish that general AI inference runs on the glasses themselves; the glasses primarily serve as capture/audio/control hardware with phone and/or external model processing.

## Cloud independence
Basic startup and Bluetooth discovery have been observed without the vendor application. Independent companion software reduces dependence on the original vendor stack. EV-0044 documents a concrete community media path: BLE requests transfer mode and reports the glasses address, while Wi-Fi Direct and a local HTTP manifest carry media. That makes media continuity plausible without the official user interface. It is still community-source evidence, retains vendor-library dependencies, and must be reproduced on the owned W610 with the official app stopped. AI, configuration, authentication and firmware functions still need function-by-function offline testing.

## Anko Camera Glasses
Anko/Kmart Australia is a confirmed HeyCyan software-ecosystem member. Photo/video and connected assistant/audio functions are documented, but direct W610 protocol, hardware, firmware and community-tool compatibility remain provisional until tested on the retail unit.

## OEM / silicon boundary
FCC, SANVNET and Goodway evidence provide concrete W610 supply-chain clues, but applicant, supplier, software platform, retailer and ODM roles remain separate claims. Shared HeyCyan software is not evidence of shared silicon across Anko or other suspected rebrands.

## Ownership gaps
Prescription/optical serviceability, normalized battery workloads, repairability, aging/failure patterns, exact offline boundaries, firmware access, complete sensor exposure and confirmed cross-rebrand compatibility remain active evidence targets.

## Next tests
1. Convert hands-on W610 observations into dated GlassesResearch-verified EV records.
2. Run normalized offline/service-dependence and battery tests on the physical W610.
3. Extract EV-0008 chipset details into the silicon map.
4. Establish W610 independent optical-serviceability evidence.
5. Test CyanBridge/SDK compatibility on Anko when hardware is available.
6. Continue OEM/regulatory correlation without equating software lineage with manufacture.