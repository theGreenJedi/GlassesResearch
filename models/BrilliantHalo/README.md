---
description: "Brilliant Labs Halo smart-glasses research: open-source hardware and software, display and audio architecture, developer SDKs, prescription support, AI features, and evidence-backed unknowns."
---

# Brilliant Labs Halo smart glasses — GLS-0052

**Brilliant Labs Halo** is an open-source AI smart-glasses platform aimed at both everyday use and developer experimentation. Brilliant currently lists Halo for sale at **$399** and describes the product as open-source hardware and software rather than a closed accessory tied only to one companion experience.

## What Halo is

Halo combines a heads-up color display with audio, microphones, low-power sensing, and a small on-device AI-capable processor. Brilliant's current product material describes:

- a frame weighing just over 40 g;
- a color display;
- a low-power optical sensor intended for AI inference;
- dual microphones with audio-activity detection;
- dual bone-conduction speakers;
- a low-power AI processor;
- an IPD design range of roughly 58–72 mm;
- an adjustable display optic spanning approximately +2 to -6 diopters;
- prescription and sunglass lens options through a partner optical service.

The earlier published hardware stack identifies the compute platform as an **Alif Balletto B1** with Cortex-M55 CPU/NPU resources, with software built around **ZephyrOS** and a Lua-oriented application layer.

## Open source and developer access

Halo's clearest differentiator is development access. Brilliant says the device's design files and code are open source and provides a **Brilliant SDK** plus a **Flutter SDK** for iOS and Android development.

That makes Halo relevant to several GlassesResearch criteria at once:

- **Openness:** public code/design access is materially stronger than a vendor-only app surface.
- **Owner control:** developers can build custom experiences instead of being limited to one fixed assistant interface.
- **Hackability:** the product is explicitly presented as a prototyping and experimentation platform.
- **Cloud independence:** open hardware/software creates a path toward owner-controlled operation, but the actual offline boundary still has to be verified function by function.

Open source does **not** automatically mean every firmware path is replaceable, every sensor is exposed, or every AI feature can run without Brilliant-operated services.

## AI and software experience

Brilliant markets Halo with **Noa**, its conversational AI agent, and with **Miniapps** that can be created and shared through its software ecosystem. The product is therefore both a consumer AI-glasses experience and a developer platform.

GlassesResearch treats those as separate layers. The existence of Noa does not determine what the hardware itself can do offline, and the existence of an SDK does not prove unrestricted access to every device function.

## Wearability and optics

Brilliant positions Halo as ordinary-looking eyewear rather than a headset. The current product page says the frame is just over 40 g and supports prescription lenses. The display optic itself can be adjusted across a stated diopter range, while prescription lens fulfillment is handled separately.

Independent measurements of comfort, optical clarity, display visibility, battery life, heat, and long-duration wear are still needed before those claims can be treated as verified performance.

## What remains unknown

Important open questions include:

- independently measured battery life under standardized workloads;
- exact offline behavior for Noa, Miniapps, speech, and other AI functions;
- repairability and parts availability;
- firmware replacement and boot-chain access;
- low-level sensor/API completeness;
- long-term app and cloud-service dependence;
- real-world prescription serviceability outside the designated partner path.

Unknowns remain unknown rather than being inferred from the product's open-source positioning.

## Primary sources

- [Brilliant Labs Halo product page](https://brilliant.xyz/products/halo)
- [Brilliant Labs developer documentation](https://docs.brilliant.xyz/)
- [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR)

## Related GlassesResearch resources

- [Comparison engine](../../docs/COMPARISON_ENGINE.md)
- [Community & development](../../resources/COMMUNITY_AND_DEVELOPMENT.md)
- [Open-source and hacking research](../../hacking/README.md)
- [Report Card methodology](../../docs/REPORT_CARD.md)
