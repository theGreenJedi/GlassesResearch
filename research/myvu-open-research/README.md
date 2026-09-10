# MYVU Open Research

An evidence-led integration layer for public technical knowledge about the Meizu MYVU / Star Air family, centered on the XGA010C lineage.

> One reverse-engineering project often leads to another—and sometimes to an entire technical ecosystem. We follow those connections because that’s where discoveries ordinary product searches miss tend to surface.

## Purpose

This is **not** a replacement for, or unattributed copy of, upstream community projects. It is a provenance-preserving map of what is known, what has been reproduced, what appears model-specific, what conflicts, and what still needs bench verification.

## Evidence states

- **UPSTREAM-DOCUMENTED** — stated or implemented by an identified public technical source.
- **COMMUNITY-REPORTED** — owner/developer observation not independently reproduced by GlassesResearch.
- **GR-VERIFIED** — reproduced by GlassesResearch on identified hardware/firmware using a documented procedure.
- **INFERRED** — technically supported inference, explicitly distinguished from observation.
- **UNKNOWN / CONFLICTING** — insufficient or contradictory evidence.

## Current upstreams

1. **Panny777 / Meizu-Myvu-Client** — hardware-verified client and original reverse-engineering reference; Android + Python implementations. MIT-licensed original code, but this repository references rather than copies it by default.
2. **Panny777 / Meizu-Myvu-SDK** — structured Android SDK and detailed XGA010C wire-protocol documentation. MIT-licensed original code; protocol behavior may vary with firmware.
3. **FerSaiyan / Alternative-HeyCyan-App-and-SDK (CyanBridge)** — downstream integration that explicitly uses Panny777's MYVU BLE/ECDH/RFCOMM/heartbeat/display work while independently researching other glasses families.

See `SOURCES.md` for direct links and attribution.

## What we currently know

### Hardware identity / lineage

The strongest upstream documentation identifies the tested Meizu MYVU / Star Air as **XGA010C**. Compatibility with similarly branded MYVU/Imiki/Air/Air2 hardware must not be assumed solely from branding.

### Transport architecture — UPSTREAM-DOCUMENTED

Panny777 documents a mandatory two-link design:

1. BLE wakes/negotiates the glasses, performs ECDH-based bonding, maintains heartbeat, and announces the session RFCOMM endpoint.
2. Classic Bluetooth RFCOMM carries the primary app relay after the BLE setup.

For the documented Air-family path, BLE service `0x0BD1` uses Air characteristics `0x2020/0x2021/0x2022/0x2023`; Panny777 separately documents V2 units using `0x2010/0x2011/0x2012`. This is an immediate warning against assuming protocol identity across visually or commercially related variants.

### Pairing / session behavior — UPSTREAM-DOCUMENTED

Panny777 documents P-256 ECDH, an encrypted DeviceInfo exchange, an ability-authentication stage, a captured/replayed initialization burst, a 3-second BLE heartbeat, and a per-session random RFCOMM UUID synchronized over BLE. The SDK notes that the glasses accept one central at a time during testing.

### Features demonstrated upstream

Panny777's client/SDK documents teleprompter, notifications, settings, time sync, trackpad, status queries, weather, navigation, and microphone-backed AI workflows. CyanBridge explicitly credits Panny777's hardware-verified MYVU protocol work for its native MYVU integration.

## Community observations requiring verification

| Observation | State | Why it matters | GR disposition |
|---|---|---|---|
| Imiki-branded MYVU not discovered by Panny777 client v0.3 | COMMUNITY-REPORTED | Possible protocol/identifier/lineage boundary | Capture advertising data, GATT services/characteristics and model identifiers; test MAC-directed pairing |
| Imiki owner reports shutdown after ~10 seconds or less during teleprompter/AI use | COMMUNITY-REPORTED | Possible sleep/watchdog/firmware/app interaction | Reproduce with timed bench procedure on identified hardware/firmware |
| Owner reports ~10-hour mixed-use workday battery | COMMUNITY-REPORTED | Useful field-use datum | Preserve as owner report; do not convert to measured battery life |
| Owner reports ~3.5 hours under constant music use | COMMUNITY-REPORTED | Useful stress-use datum | Reproduce with controlled audio/battery procedure if matching hardware obtained |
| Pronounced rainbow artifacts under overhead lighting | COMMUNITY-REPORTED | Waveguide usability/social-environment issue | Add overhead-light artifact check to optical bench procedure |
| Regional/iOS reports include Chinese-number/account friction and failed/nonpersistent pairing | COMMUNITY-REPORTED | Suggests app/region/OS compatibility fragmentation | Build OS × app-region × hardware × firmware compatibility matrix |

## Best-practice baseline

Until testing disproves it:

- Record **exact model number and firmware** before interpreting compatibility.
- Record companion app build/region and host OS/version.
- Do not pre-assume that MYVU, Air, Air2, Imiki-branded, or visually identical units expose identical BLE characteristics or application behavior.
- During protocol testing, isolate other paired/connected hosts because the documented XGA010C accepts one central at a time.
- Preserve packet captures and raw identifiers before normalizing them into a protocol description.
- Never promote an owner report to a hardware fact without reproduction.
- Prefer reversible/non-destructive tests; factory-reset/recovery operations remain outside routine testing unless specifically justified.

## Planned artifacts

- `COMPATIBILITY.md` — hardware × firmware × host OS × app/client matrix.
- `PROTOCOL-CROSSWALK.md` — normalized comparison of upstream protocol findings without redistributing proprietary vendor code.
- `FAILURE-MODES.md` — provenance-linked reports and reproduction status.
- `TEST-PLAN.md` — common conformance/bench procedures.
- `SOURCES.md` — upstream projects, discussions and attribution.

## Publication status

**Research branch / not yet placed on glassesresearch.org.** Site placement will be decided after the knowledge base is mature enough to publish.