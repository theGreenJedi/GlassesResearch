# Qwen Glasses S1 / G1

**Status:** current in China as of 2026-08-21  
**Maker:** Alibaba  
**Current brand:** Qwen Glasses  
**Former launch brand:** Quark AI Glasses  
**Canonical GLS IDs:** **GLS-0161 (S1)** · **GLS-0162 (G1)**

## Identity / also known as

Alibaba launched the products in December 2025 as **Quark AI Glasses S1** and **Quark AI Glasses G1**. At MWC Barcelona on 2026-03-04, Alibaba unified the eyewear under the **Qwen Glasses** brand while retaining the S1 and G1 series names.

GlassesResearch treats this as a brand/name transition, not a third hardware generation:

- **GLS-0161 — Qwen Glasses S1**  
  Also known as: **Quark AI Glasses S1**
- **GLS-0162 — Qwen Glasses G1**  
  Also known as: **Quark AI Glasses G1**

## S1 versus G1

The two products are materially distinct and therefore receive separate stable IDs.

| | Qwen Glasses S1 | Qwen Glasses G1 |
|---|---|---|
| Product position | flagship | everyday / lower-cost |
| Display | dual display | no display; camera-first |
| Camera / audio / AI | yes | yes |
| Qwen App integration | yes | yes |
| China retail availability | yes | yes |
| Former name | Quark AI Glasses S1 | Quark AI Glasses G1 |

Alibaba's December launch says the G1 shares the S1's core hardware **except for the display** and claims a 40 g weight for G1. That statement does not authorize GlassesResearch to copy every S1 specification or score onto G1.

## Primary-source snapshot

Alibaba's launch material supports:

- Qwen-powered voice and visual AI interactions;
- photo/video capture and audio functions;
- Qwen App integration;
- real-time translation, meeting transcription and visual recognition;
- a swappable dual-battery architecture, with a vendor claim of up to 24 hours;
- S1 dual displays;
- S1 imaging claims including 0.6-second photo capture, 3K video and AI-enhanced 4K output;
- G1's camera-first/no-display design and 40 g vendor weight claim;
- support for the Model Context Protocol (MCP) as part of Alibaba's stated developer ecosystem direction.

On 2026-03-04 Alibaba said Qwen Glasses preorders were live in China and official sales would begin 2026-03-08. It said an international version was planned for later in 2026. China retail therefore crosses the canonical acquisition threshold; international availability remains region-limited rather than assumed.

## Owner-control and cloud boundary

The MCP claim is interesting but narrow. Alibaba's product announcement says the glasses support the standard MCP protocol to enable third-party development. That does **not** by itself prove:

- a publicly downloadable device SDK;
- unrestricted local API access to camera, microphones, displays, storage or sensors;
- owner-selectable AI models;
- bootloader, firmware, recovery or root access;
- cloud-independent AI operation;
- continued smart functions after Alibaba/Qwen service loss.

Until reproducible technical documentation or hands-on evidence establishes those boundaries, they remain unknown.

## Evidence

- [EV-0078 — Qwen Glasses S1/G1 primary product evidence](../../evidence/EV-0078-Qwen-Glasses-S1-G1-primary-product.md)
- [Canonical reconciliation](../THE_LIST_RECONCILIATION_2026-08-21_QWEN.md)
- Alibaba, December 2025 Quark launch: https://www.alibabacloud.com/blog/602717
- Alibaba, March 2026 Qwen/MWC announcement: https://www.alibabacloud.com/blog/alibaba-unveils-qwen-glasses-at-mwc-barcelona-accelerating-ai-hardware-ambitions_602920

## Open questions

- What exact production hardware differs between S1 and G1 beyond the display?
- Is there a public device SDK/API beyond Alibaba's general MCP ecosystem claim?
- Which functions execute on-glasses, on-phone, or in Alibaba/Qwen cloud services?
- What account and companion-app dependencies exist after initial setup?
- What functions survive without network or vendor service availability?
- What are the production prescription-lens options and serviceability limits?
- When does international retail availability actually begin?
