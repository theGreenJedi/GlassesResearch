# Evidence Acquisition Backlog

Last reviewed: 2026-08-13

This backlog converts the normalized `research/populated/` layer into explicit evidence-acquisition work. It is ordered by research value rather than by catalog ID.

## Priority 0 — unresolved catalog identity / incomplete report cards

These items block clean model-level conclusions and should be resolved before broad enrichment.

| Target | Status | Required next evidence / action |
|---|---|---|
| Mijia Smart Audio Glasses — GLS-0022 | **Partially resolved.** EV-0034 proves Xiaomi Smart Audio Glasses and the current Mijia Smart Audio Glasses are distinct generations/products; current Mijia specifications must not be copied into the 2022 row. | Recover 2022 mainland-China launch/store/manual/regulatory evidence and exact model number, then rename or split GLS-0022 if required. |
| Mijia Camera Glasses — GLS-0023 | **Identity confirmed; specification depth still unresolved.** Xiaomi still hosts the MIJIA Glasses Camera product/spec pages, but parsed engineering detail is insufficient for a full card. | Recover archived/manual/regulatory specifications, connectivity, battery, software and present-day service behavior. |
| Lucyd Lyte 2.1 — GLS-0032 | **Resolved as unsupported generation label.** EV-0035 finds no company/SEC evidence of a distinct Lyte 2.1 commercial hardware generation. | Catalog reconciliation: preserve stable-ID correction history; do not inherit Lyte 2.0 scores. |
| Lucyd Lyte 2.3 — GLS-0033 | **Resolved as unsupported generation label.** Company/SEC history instead establishes Lyte XL after Lyte 2.0. | Catalog reconciliation: replace unsupported generation naming with evidence-backed Lyte XL where appropriate; build XL card from exact evidence. |
| INMO Air 3 — GLS-0060 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_02.md`. | Move to ordinary enrichment queue. |
| INMO GO — GLS-0059 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_02.md`. | Move to ordinary enrichment queue. |
| Solos AirGo V2 — GLS-0029 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_01.md`. | Move to firmware/service-survival enrichment queue. |

## Priority 1 — cloud/service survival

This is the highest-value ownership research because it distinguishes a durable device from a service terminal.

### Closed/current AI glasses
- Meta / Ray-Ban / Oakley: separate local capture/audio/translation from Meta-AI-dependent functions; record first-run account/app/network requirements.
- Xiaomi AI Glasses: local-vs-cloud inference, companion/account requirements and regional feature differences.
- HTC VIVE Eagle: provider selection limits, local encrypted-storage behavior, offline capture/audio and AI failure modes.
- Rokid Glasses: translation/navigation/transcription/AI offline boundaries, companion requirements and SDK behavior without Rokid services.
- RayNeo X3 Pro: Creator Mode local execution versus Gemini/service dependence.
- Even G1/G2: display/plugin behavior without Even services, account requirements and phone-only custom-plugin survivability.

### Preservation controls
- Magic Leap 1: exact functionality lost after 2024-12-31 shutdown versus any surviving local behavior.
- Recon Jet / Jet Pro / Pro+: activation/login dependence after Recon Engage shutdown and what still works locally.
- Bose Frames: what survived Bose AR discontinuation; distinguish Bluetooth audio from abandoned AR software.
- RealWear HMT-1/HMT-1Z1: present-day local operation after end of support and firmware 12.6.
- HoloLens 1/2: post-support local application/install/account constraints.

Completion condition: function-by-function service-dependence matrix with dated evidence, not a single cloud yes/no field.

## Priority 2 — optical and prescription serviceability

For every ordinary-eyewear-form product, record direct corrective-lens support, exact correction limits, progressive support, replacement lens availability, and whether an ordinary independent optical shop can service it.

**Completed evidence in this mission:**
- Lucyd Lyte family: EV-0035 supports **ordinary optical service**; Innovative Eyewear says frames are designed for fitting by any optician and support prescription/sunglass/reading/blue-light formats.
- Xiaomi Smart Audio Glasses optical version: EV-0034 supports **ordinary optical service** via professional optical shops.
- Current Mijia Smart Audio Glasses: EV-0034 supports **ordinary optical service**; Xiaomi says ordinary-glasses lens thicknesses are supported and directs fitting to offline optical shops.

Next first wave: HeyCyan/W610, Meta/Ray-Ban/Oakley, Even G1/G2, Brilliant Frame/Halo, Solos, Huawei, Vuzix Z100/Blade 2, Rokid Glasses, RayNeo X3 Pro, Iristick G3, Ampere Dusk and Chamelo.

Do not treat `prescription compatible` as equivalent to independent serviceability.

## Priority 3 — normalized battery evidence

Use `research/battery-normalization.md`. Preserve manufacturer claims separately from measured results.

First measured candidates:
1. W610 — hands-on control device.
2. Even G2 — two-day claim / HUD workload.
3. Brilliant Frame or Halo — open-platform comparison.
4. Meta Ray-Ban Gen 2 — mainstream closed-AI comparison.
5. Solos AirGo V2 or Mentra Live — owner-programmable camera comparison.

Workloads: idle connected, audio, camera capture, repeated AI query, HUD/display and mixed use. Case capacity is separate from on-face runtime.

## Priority 4 — firmware/protocol/owner-access depth

Highest-value targets are products where application openness is already known but system-level ownership is unclear.

- W610: complete BLE/Wi-Fi transfer characterization, firmware update path, chipset mapping, debug/boot behavior.
- Solos AirGo 3/V/V2: firmware-update API boundaries, complete sensor exposure and whether owner endpoints remain functional without vendor services.
- Even G2: protocol behavior below Even Hub plugin layer.
- Rokid Glasses / RayNeo X3 Pro / INMO Air 3: developer-mode privilege boundaries, bootloader/firmware status and sensor exposure.
- Vuzix Android branches / RealWear / Epson / Lenovo / Iristick: APK/application access versus privileged/system access.

## Priority 5 — repairability, aging and parts

Record battery replacement, hinges, temples, charging contacts/cases, lens/display damage, connectors, replacement parts, teardown difficulty and software aging. One report is not a failure rate.

Open platforms (Brilliant/Mentra) should establish the repairability high-water mark; discontinued products should establish survivability failure modes.

## Priority 6 — value / ownership cost

Value is intentionally still ungraded on many current products. A value pass should use a dated price basis and compare capability, expected service life, required accessories/subscriptions, prescription cost and replacement risk. Historical launch MSRP and current secondary-market price are separate fields.

## Evidence record requirements

Every new finding should preserve:
- exact model/generation;
- field/function being tested;
- value/result;
- source class;
- confidence;
- evidence ID(s) or stable source;
- verification date;
- region/firmware/app version where relevant;
- qualification or conflicting evidence.

Unknown remains unknown. Negative findings require evidence; absence of documentation is not proof of absence.
