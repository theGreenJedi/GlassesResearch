# Evidence Acquisition Backlog

Last reviewed: 2026-08-14

This backlog converts the normalized `research/populated/` layer into explicit evidence-acquisition work. It is ordered by research value rather than by catalog ID.

## Priority 0 — unresolved catalog identity / incomplete report cards

These items block clean model-level conclusions and should be resolved before broad enrichment.

| Target | Status | Required next evidence / action |
|---|---|---|
| Mijia Smart Audio Glasses (1st generation) — GLS-0022 | **Identity corrected.** Contemporaneous launch reporting places Xiaomi Youpin crowdfunding in April 2023; EV-0034 prevents later Mijia specifications from being copied backward. | Recover the first-generation Xiaomi Youpin page, manual, regulatory filing and exact model number; keep detailed scoring deferred. |
| Mijia Glasses Camera — GLS-0023 | **Identity and dedicated Xiaomi route confirmed.** The 2022 camera/display product is separate from the 2023 audio branch; period sources report model `MJSV01FC`. | Preserve `https://www.mi.com/mjglass`; recover manual/regulatory proof for the model number, connectivity, battery, software and service behavior. |
| Retired Lucyd Lyte 2.1 label — GLS-0032 | **Completed.** Removed from the canonical model count after EV-0035 found no company/SEC evidence of a distinct commercial generation; stable ID retained in the correction ledger. | No model scoring. Reopen only if primary acquisition evidence emerges. |
| Lucyd Lyte XL — GLS-0033 | **Identity corrected.** Company and SEC history establish the October 2023 Lyte XL successor; former `Lyte 2.3` naming is preserved only in the correction ledger. | Recover exact electronics/battery documentation and build an XL-specific card without inherited 2.0 scores. |
| INMO Air 3 — GLS-0060 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_02.md`. | Move to ordinary enrichment queue. |
| INMO GO — GLS-0059 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_02.md`. | Move to ordinary enrichment queue. |
| Solos AirGo V2 — GLS-0029 | **Completed.** Full common-ruler card imported from `HIGH_THROUGHPUT_BATCH_01.md`. | Move to firmware/service-survival enrichment queue. |

## Priority 1 — cloud/service survival

This is the highest-value ownership research because it distinguishes a durable device from a service terminal.

### Closed/current AI glasses
- Meta / Ray-Ban / Oakley: **source boundary completed in EV-0045** — passive optics, local storage, phone-audio residue and Gen 2 offline translation are separated from the mandatory first-run phone/account/app/network gate and service-backed AI. Remaining: empirical offline capture/import, sign-out, endpoint-blocking and previously downloaded translation-pack tests.
- Xiaomi AI Glasses: local-vs-cloud inference, companion/account requirements and regional feature differences.
- HTC VIVE Eagle: **offline boundary completed in EV-0041** — button capture, onboard storage and narrow commands survive offline; media management uses VIVE Connect; advanced VIVE AI requires app connection plus phone internet. Remaining: first-run/account, sign-out, standard file access, provider/region limits and backend-shutdown testing.
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
