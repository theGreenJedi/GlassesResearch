---
title: "Smart-Glasses Host Compatibility"
description: "Evidence-backed compatibility between smart glasses and phones, laptops, handhelds, consoles, adapters, video transports, power paths, apps and spatial modes."
---

# Smart-glasses host compatibility

A USB-C plug does not answer the question **“will these glasses work with my device?”**

Compatibility can depend on video transport, power, operating-system support, adapters, vendor software and the exact glasses generation. GlassesResearch therefore records compatibility as evidence rather than assuming that matching connectors are enough.

The machine-readable dataset is [`data/host-compatibility.json`](../data/host-compatibility.json). It grows only when manufacturer documentation, reproducible testing or explicitly attributed community observations establish a specific combination.

## Quick answers — verified manufacturer paths

These are **connection-path findings**, not blanket claims that every application, spatial mode, refresh rate or accessory feature works identically.

| Glasses | Host | Result | Required path | Evidence |
|---|---|---|---|---|
| XREAL One / One Pro / 1S | Steam Deck / Steam Deck OLED | **Yes — direct** | USB-C with DP video; host powers glasses | [XREAL](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/) |
| XREAL One / One Pro / 1S | Switch / Switch OLED / Switch 2 | **Yes — adapted** | XREAL Hub | [XREAL](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/) |
| XREAL One / One Pro / 1S | PlayStation / Xbox | **Yes — adapted** | HDMI-C adapter | [XREAL](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/) |
| RayNeo Air 3s Pro | Steam Deck / ROG Ally | **Yes — direct** | USB-C display path | [RayNeo](https://www.rayneo.com/pages/gaming-consoles) |
| RayNeo Air 3s Pro | Nintendo Switch | **Yes — adapted** | charged RayNeo JoyDock | [RayNeo](https://www.rayneo.com/pages/gaming-consoles) |
| RayNeo Air 3s Pro | PS4/PS5 / Xbox Series/One | **Yes — adapted** | HDMI-to-USB-C adapter | [RayNeo](https://www.rayneo.com/pages/gaming-consoles) |
| VITURE Pro 2 | Steam Deck / Steam Deck OLED | **Yes — direct** | DP Alt Mode display path | [VITURE](https://www.viture.com/compatibility) |
| VITURE Pro 2 | Switch / Switch OLED / Switch 2 | **Yes — adapted** | VITURE Mobile Dock | [VITURE](https://www.viture.com/compatibility) |
| VITURE Pro 2 | PS4/PS5 / Xbox Series/One | **Yes — adapted** | VITURE Mobile Dock via HDMI | [VITURE](https://www.viture.com/compatibility) |
| Rokid Max 2 | Steam Deck | **Yes — direct** | USB-C display output | [Rokid](https://global.rokid.com/blogs/max-2/how-can-i-connect-rokid-max-2-to-different-devices) |
| Rokid Max 2 | iPhone 15-series and later USB-C iPhones | **Yes — direct** | USB-C display output | [Rokid](https://global.rokid.com/blogs/phones) |

**Unknown means unknown.** A combination not in this table is not automatically incompatible. It simply has not yet crossed the evidence threshold for this quick-answer layer.

## Important mode boundaries

A connection can work while a feature does not. XREAL, for example, documents One-series connection to Switch, PlayStation and Xbox but its current feature matrix does **not** list UltraWide Mode for those console columns. VITURE notes that some DP-capable phones, including Pixel 8/9 series in its current compatibility guidance, do not provide the 4K output it requires for its Immersive 3D mode. These are exactly the differences GlassesResearch intends to preserve instead of flattening everything into a single yes/no compatibility badge.

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

## Transport rule: direct USB-C display glasses

Current XREAL One-series, VITURE, RayNeo Air-series and Rokid display-glasses documentation all reinforce the same important rule: a USB-C-shaped port is not enough. Direct video generally requires an actual DisplayPort-capable USB-C output (vendor terminology varies between **DP Alt Mode**, **DisplayPort over USB-C**, or USB-C display output) plus an adequate power path.

The structured dataset preserves model-specific evidence rather than extrapolating that rule to every generation.

## Evidence rules

1. **Connector ≠ protocol.** USB-C presence never proves DisplayPort Alt Mode.
2. **Family support ≠ universal host support.** A transport supported by a glasses family does not establish every phone or console combination.
3. **“Works” must name the function.** Mirrored video is different from spatial tracking, audio, camera/data access or companion-app integration.
4. **Unknown stays unknown.** Missing evidence is not converted into “incompatible.”
5. **Community experience remains attributed.** A reproducible owner report can be useful evidence without becoming a universal manufacturer specification.
6. **Search demand can reveal a useful question, not dictate the answer.** Compatibility pages are built from verified records rather than keyword-driven claims.

## Research backlog

The first named-host population now covers representative current XREAL, RayNeo, VITURE and Rokid display glasses. Next highest-value work is:

- broaden current model coverage without inheriting compatibility across generations;
- Apple and Android phone model-level video-output differences;
- Steam Deck and other handheld-computer paths;
- console paths requiring docks or HDMI conversion;
- power-injection requirements;
- basic display versus spatial/3DoF features;
- software or firmware updates that break previously working combinations;
- generic, owner-controlled display paths that survive after vendor applications disappear.

The internal research method and field definitions are preserved in [`research/host-compatibility.md`](../research/host-compatibility.md).
