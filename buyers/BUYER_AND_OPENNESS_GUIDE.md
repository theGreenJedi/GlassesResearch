# Smart-Glasses Buyer, Openness, and Survival Guide

**Research snapshot:** 2026-08-05

This guide is not a ranked shopping list. It helps readers distinguish product categories, developer access, vendor dependence, prescription options, and the likelihood that a device remains useful if its original service disappears.

Claims below use manufacturer or project-primary sources unless explicitly labeled otherwise. Availability, prices, subscriptions, and software support can change; verify them before purchase.

## Decision table

| Device / family | Primary role | Display | Camera | Developer path | Prescription path | Dependency and survival assessment |
|---|---|---|---|---|---|---|
| [Brilliant Labs Frame](https://docs.brilliant.xyz/frame/hardware/) | Open development and computer-vision experimentation | 640×400 color OLED, 20° FOV | 720p | Published hardware manual, Lua OS/API material, schematics and project repositories | Optional personalized prescription solution | **Strong preservation posture.** Published technical detail and source material reduce dependence on one hosted service, although cloud AI features remain a separate dependency. |
| [Brilliant Labs Halo](https://brilliant.xyz/products/halo) | Open-source AI glasses with display, audio and sensing | Color display | Low-power optical sensor | Brilliant SDK, Flutter SDK, published code and design files claimed by manufacturer | Partner prescription lenses; display adjustment stated as +2 to -6 diopters | **Promising but verify shipment and source completeness.** Manufacturer lists Q1 2026 shipping and calls hardware/software open source. Treat availability and delivered capabilities as purchase-time checks. |
| [Vuzix Z100](https://www.vuzix.com/products/z100-smart-glasses) | Lightweight phone-connected heads-up display | 640×480 monochrome green microLED waveguide, right-eye | No camera listed | Official Android and iOS SDKs, samples and documentation; phone sends text, images and animations | Prescription inserts available | **Good developer continuity.** Public SDKs and a narrowly defined BLE peripheral architecture are favorable. Android use currently requires the Vuzix Connect app, so app availability remains relevant. |
| [Solos AirGo family](https://solosglasses.com/pages/developers) | Audio or camera smart glasses with mobile integrations | Model-dependent; AirGo 3/A5 are audio focused | AirGo V models include camera functions | Official iOS/Android SDK across AirGo V 1/2 and AirGo 3/A5; BLE control and Wi-Fi data on V2 | Frame/lens options vary by model; confirm with manufacturer or optician | **Moderate-to-good developer posture.** An official cross-model SDK exists, but functions and transports differ materially by generation. Do not assume one AirGo model's capabilities apply to another. |
| [MentraOS](https://github.com/Mentra-Community/MentraOS) compatible devices | Cross-device application platform | Depends on glasses | Depends on glasses | Open-source platform intended to support applications across compatible smart glasses | Depends on glasses | **Potential portability layer.** Value comes from reducing application lock-in across supported devices. Compatibility must be verified per exact hardware and platform release. |
| [Mentra Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) | Independent hardware experimentation | Project-defined | Project-defined | Published project files and software repository | DIY/project dependent | **High research value, lower consumer certainty.** Appropriate for builders and preservation research rather than buyers seeking a finished supported appliance. |
| [XREAL One](https://www.xreal.com/one/) family | Tethered display and spatial-computing glasses | Full-color display; specifications vary by exact model | Usually host/accessory dependent; verify exact model | Developer and accessory ecosystem exists, but openness differs from fully published hardware projects | Prescription insert routes vary | **Host-dependent rather than cloud-first.** Core display usefulness may outlive a companion cloud, but firmware, accessories and spatial features remain vendor dependent. |
| [Ray-Ban Meta](https://www.meta.com/ai-glasses/) / Meta AI glasses | Mainstream camera/audio assistant | No heads-up display in current camera/audio category | Yes | Consumer platform; not an open general-purpose hardware SDK comparable to Frame or Z100 | Prescription configurations are sold through supported optical channels | **High service dependence.** Strong mainstream support and retail ecosystem, but AI, account and companion-app functions depend heavily on Meta services. |
| [Even Realities G1/G2](https://www.evenrealities.com/) | Discreet display-first everyday glasses | Heads-up display; verify generation | Product-generation dependent | Public consumer integrations exist; verify current third-party developer access before purchase | Prescription ordering is a central product path | **Fit and display strengths, uncertain independent survival.** Do not infer an open SDK merely from integrations or automation demonstrations. |
| W610 / HeyCyan retail variants | Low-cost camera/audio experimentation | No confirmed heads-up display on the hands-on W610 variant | Yes, advertised; exact implementation under investigation | No verified independent SDK or protocol control yet | Replacement-lens feasibility not yet verified | **Research device, not an openness recommendation.** Low acquisition cost and shared-platform clues are useful, but app, firmware, BLE control and long-term service independence remain unresolved. |

## Product categories that should not be compared as equivalents

### Camera/audio assistant glasses

These capture audio and images and generally depend on a phone application or cloud service. They may look conventional, but they do not provide a visual heads-up display. Ray-Ban Meta and many low-cost W6xx variants belong primarily in this category.

### Display peripherals

These present information generated by a phone or host. The Vuzix Z100 is a clear example: its official documentation describes a Bluetooth peripheral controlled from Android or iOS applications. This category can offer strong battery life because processing remains on the host.

### Tethered display glasses

XREAL and similar products behave more like wearable monitors or spatial displays. Their long-term value often depends more on standard video compatibility and replaceable host devices than on cloud AI.

### Standalone or open development platforms

Frame, Halo, and open-hardware projects expose more of the hardware/software stack. They are better research platforms, but openness does not guarantee mature support, easy fit, or consumer-level reliability.

## Openness ladder

1. **Published hardware and software source** — design files, firmware/application source, build instructions and licenses are available.
2. **Documented public SDK/API** — third parties can build supported applications, but underlying firmware or hardware remains closed.
3. **Documented interoperability** — standard display, audio or Bluetooth behavior preserves some utility without a proprietary cloud.
4. **Community reverse engineering** — useful capabilities exist but may break across firmware revisions.
5. **Vendor application only** — core functions depend on an account, app and service controlled by one company.
6. **Cloud-essential appliance** — loss of service or account support substantially removes the product's purpose.

A product can occupy more than one rung. For example, a device may expose a public SDK while still requiring a vendor connection application.

## Rebrand and shared-platform warning signs

Treat products as possible relatives—not confirmed identical devices—when they share several of these:

- identical frame molds, button placement, LED location and charging method;
- the same companion application or package name;
- matching Bluetooth advertising names or service UUIDs;
- identical manuals, diagrams, QR codes or translated text errors;
- the same chipset and camera claims;
- seller photographs that appear to originate from one factory image set;
- firmware or application support tables naming multiple retail brands.

A matching appearance alone does not prove firmware compatibility. Never flash firmware based only on seller photos or a reused model number.

## Minimum purchase questions

Before buying, determine:

1. Does the product have a display, or only camera/audio capture?
2. What remains usable without an account, internet connection or subscription?
3. Is there an official SDK, and can it perform the function you actually need?
4. Are the SDK, application and firmware downloads publicly retrievable?
5. Is prescription support integrated, insert-based or merely claimed by a seller?
6. Does the frame fit your head and interpupillary range?
7. Is the device still receiving application and firmware updates?
8. Is there a recovery path if an update fails?
9. Are replacement cables, docks, lenses and batteries obtainable?
10. Can research evidence distinguish this exact hardware revision from similar rebrands?

## Research conclusion

For **open investigation**, Frame and documented open-hardware projects currently provide the strongest published research surface. For a **supported phone-driven display**, Z100 offers an unusually clear official SDK path. For **mainstream consumer capture and assistant features**, Meta offers scale but significant service dependence. W610-class devices remain valuable as inexpensive research subjects, but should not be described as open until independent control is demonstrated.