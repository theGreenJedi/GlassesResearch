---
title: "Smart-Glasses Host Compatibility"
description: "Evidence-backed compatibility between smart glasses and phones, laptops, handhelds, consoles, adapters, video transports, power paths, apps and spatial modes."
---

# Smart-glasses host compatibility

A USB-C plug does not answer the question **“will these glasses work with my device?”**

Compatibility can depend on video transport, power, operating-system support, adapters, vendor software and the exact glasses generation. GlassesResearch therefore records compatibility as evidence rather than assuming that matching connectors are enough.

The machine-readable seed dataset is [`data/host-compatibility.json`](../data/host-compatibility.json). It will grow as manufacturer documentation, reproducible testing and attributable community observations establish specific combinations.

## What “compatible” must tell you

A useful compatibility record distinguishes:

| Question | Why it matters |
|---|---|
| Physical connector | USB-C, HDMI, Bluetooth or another connector/transport does not by itself establish capability. |
| Video/data protocol | For display glasses, USB-C often needs **DisplayPort Alt Mode**; ordinary USB-C data/charging is not enough. |
| Power source | Some glasses are powered by the host; adapters or docks may need their own power path. |
| Direct or adapted connection | An adapter can make a host usable while changing audio, charging, refresh-rate or spatial behavior. |
| Operating mode | Basic mirrored video, 3DoF/spatial display, camera/data access and vendor-app integration are different claims. |
| Software dependency | A vendor app, driver, account, SDK or companion device may be required for features beyond basic display output. |
| Evidence state | Manufacturer documentation, GlassesResearch testing and community reports have different evidentiary weight. |

## Initial verified transport rule: XREAL One family

XREAL's current One-series documentation establishes that compatible hosts provide video over **USB-C DisplayPort Alt Mode** and supply power to the glasses. The initial structured records therefore cover `GLS-0074` XREAL One, `GLS-0075` XREAL One Pro and `GLS-0156` XREAL 1S at that transport level.

This does **not** mean every USB-C phone, laptop, handheld or console works. A named device combination remains unknown until evidence establishes its actual video path, required adapter and supported operating mode.

Primary source: [XREAL — connect a One-series device](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/)

## Evidence rules

1. **Connector ≠ protocol.** USB-C presence never proves DisplayPort Alt Mode.
2. **Family support ≠ universal host support.** A transport supported by a glasses family does not establish every phone or console combination.
3. **“Works” must name the function.** Mirrored video is different from spatial tracking, audio, camera/data access or companion-app integration.
4. **Unknown stays unknown.** Missing evidence is not converted into “incompatible.”
5. **Community experience remains attributed.** A reproducible owner report can be useful evidence without becoming a universal manufacturer specification.
6. **Search demand can reveal a useful question, not dictate the answer.** Compatibility pages are built from verified records rather than keyword-driven claims.

## Research backlog

The next high-value coverage is current XREAL, VITURE, RayNeo and Rokid display eyewear, followed by:

- Apple and Android phone video-output differences;
- Steam Deck and other handheld-computer paths;
- console paths requiring docks or HDMI conversion;
- power-injection requirements;
- basic display versus spatial/3DoF features;
- software or firmware updates that break previously working combinations;
- generic, owner-controlled display paths that survive after vendor applications disappear.

The internal research method and field definitions are preserved in [`research/host-compatibility.md`](../research/host-compatibility.md).
