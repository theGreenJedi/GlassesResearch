# XR Display Lineage Profiles

These paragraphs are the human-readable output of High-Throughput Report Card Batch 03. They explain the architectural tradeoffs behind the scores rather than repeating the tables.

## GLS-0069 — Nreal Light

Nreal Light is historically important because it tried to make **real 6DoF AR look like glasses before the rest of the market had settled on simple wearable monitors**. XREAL's surviving official material records a 52-degree field of view, spatial positioning and a phone-connected architecture aimed at both consumers and developers. That gives Light a stronger Display/HUD and Software story than many early glasses, but its Visual AI score remains modest by modern standards: its sensing was primarily there to understand geometry and position digital content, not to run a multimodal assistant that understood the wearer's world. Light is best read as an early spatial-computing bridge—far more ambitious than a private screen, far more wearable than a headset, and still visibly constrained by the tethered hardware of its era.

## GLS-0070 — XREAL Air

XREAL Air marks the moment the lineage deliberately simplified. Instead of carrying full spatial sensing and compute on the face, Air became a **high-quality private display driven by whatever device the owner already had**. That architectural retreat is actually why its report card remains attractive: Visual AI is N/A, but Cloud Independence and Owner Control are strong because the glasses do not need XREAL's servers to show a laptop, phone or console. The wearer owns the compute source; the glasses provide the optics and audio. Air therefore helped establish the modern XR-glasses category as something different from autonomous AR—a wearable monitor whose usefulness survives even if the vendor's cloud ambitions change.

## GLS-0071 — XREAL Air 2

Air 2 refines that wearable-monitor idea rather than changing it. XREAL documents a 72 g frame, Sony 0.55-inch Micro-OLED panels, 1920×1080 resolution per eye, up to 120 Hz refresh and a 46-degree field of view. Those numbers translate into the report card exactly where they should: excellent Display/HUD, strong Hardware and unusually good Cloud Independence, but no Visual AI because there is no world-facing camera. The interesting ownership advantage is architectural rather than ideological. Air 2 is not open hardware, yet the owner can plug it into many different hosts and choose the software stack there. **A closed display peripheral can still provide meaningful user control when it refuses to own the computer behind the display.**

## GLS-0072 — XREAL Air 2 Pro

Air 2 Pro is Air 2 with one deceptively useful optical improvement: three-level electrochromic dimming. That does not make it a new computing platform, but it makes the private-screen concept work better in the messy lighting conditions of actual life. The same 1080p-per-eye, 120 Hz Micro-OLED architecture remains host-driven and cloud-independent, while adjustable transparency lets the wearer decide how much of the outside world competes with the virtual screen. Its report card therefore moves only slightly above Air 2 in Hardware and Display/HUD rather than pretending a tint control transformed the product. The significance is practical: **Pro improves immersion without sacrificing the simple, owner-selected-host architecture that makes the Air family unusually durable against ecosystem lock-in.**

## GLS-0073 — XREAL Air 2 Ultra

Air 2 Ultra is where XREAL swings the pendulum back toward true AR. The familiar Micro-OLED display is joined by dual environment sensors, 6DoF tracking, depth mesh, plane detection, spatial anchors, image tracking and hand/head tracking through XREAL's developer stack. That pushes Hardware, Software, Visual AI-adjacent sensing and Hackability materially upward compared with the ordinary Air models. Yet Ultra still does not become an open Brilliant-style platform: the sensors and APIs are documented for development, while firmware and low-level hardware remain proprietary. **Ultra's real achievement is giving developers spatial understanding without forcing a full headset onto the user's face.** At 83 g it is less forgettable than Air 2, but far more capable as an AR instrument.

## GLS-0075 — XREAL One Pro

One Pro pushes host-driven XR close to the current optical ceiling. XREAL's X Prism engine expands the field of view to 57 degrees, offers two IPD ranges covering a much broader population and pairs the display with dedicated on-glasses spatial processing. The result is one of the catalog's strongest Display/HUD scores without pretending that it is autonomous AI eyewear. Its core value remains local: a connected host supplies content and applications, while the glasses stabilize and present them without requiring a cloud service. That produces an unusual combination—**premium proprietary optics with strong practical owner control**. One Pro is expensive enough that Value no longer automatically follows display quality, but as a wearable spatial monitor it demonstrates how far the category can advance without turning the glasses into a sealed cloud computer.

## GLS-0076 — VITURE One

VITURE One approaches the same host-driven problem with a different emphasis: make the display adaptable to the wearer's eyes and surroundings. Its 1080p-per-eye Micro-OLED system, 43-degree field of view, -5.0D myopia adjustment, electrochromic lenses, spatial audio and magnetic host connection make the glasses less about sensing the world than about reliably replacing a screen. That is why Visual AI is N/A while Display/HUD, Owner Control and Cloud Independence score strongly. Like XREAL Air, VITURE One is proprietary but does not insist on owning the content source. **The connected phone, console or computer remains the user's computer**, which gives a simple display accessory more long-term autonomy than many nominally smarter AI glasses.

## GLS-0077 — VITURE One Lite

One Lite strips the One concept down to its most portable-display essentials. VITURE's own launch history says it was introduced for January 2024 shipping as the lower-cost model, using standard USB-C input and non-dimmable outer lenses while retaining 3D, beta 3DoF and up to -5.0D myopia adjustment. That simplification shows up honestly in the card: Hardware and Display/HUD dip slightly because the electrochromic layer is gone, while Owner Control remains strong and Cloud Independence stays near the top of the catalog. **Lite is a good example of subtraction improving architectural clarity.** It gives up one premium optical convenience, but keeps the part that matters most for longevity: a standards-based host connection and no mandatory service dependency.

## GLS-0078 — VITURE Pro

VITURE Pro is the generation where the company's private-screen thesis became genuinely premium. VITURE documents a 77 g frame, 120 Hz 1080p display, up to 1000 nits perceived brightness, improved electrochromic dimming, myopia adjustment and HARMAN-tuned audio, while SpaceWalker provides multi-screen and spatial software across several host platforms. That pushes Hardware, Software and Display/HUD close to the top tier, yet the ownership story stays pleasantly boring: the glasses still work as a local display attached to an owner-selected device. **Pro's intelligence lives largely in making the screen better rather than trying to become the user's assistant.** For GlassesResearch, that distinction matters because it yields excellent cloud independence without needing open firmware.

## GLS-0079 — VITURE Luma

Luma advances the display itself: 1200p Micro-OLED, a 50-degree field of view, very high contrast, wide color coverage and roughly 1000-nit perceived brightness, all in a 77 g host-powered frame. SpaceWalker adds 3DoF, multi-screen layouts and real-time 2D-to-3D conversion, but the glasses still avoid pretending they are a standalone spatial computer. That combination is why Luma earns one of the catalog's strongest Display/HUD scores alongside excellent Cloud Independence and practical Owner Control. **Luma is what happens when nearly all of the engineering budget is spent on being a better window into someone else's computer.** It cannot see the wearer's world, but it also does not need a vendor cloud to remain useful.

## GLS-0080 — VITURE Luma Pro

Luma Pro takes the same 1200p generation and improves the things that determine whether great optics actually fit a human: 52-degree field of view, two IPD-oriented frame sizes, electrochromic control, myopia adjustment and HARMAN audio. At 79–81 g it remains unmistakably XR eyewear rather than ordinary glasses, but its display quality now sits in the same top consumer tier as XREAL One Pro. The common ruler makes the comparison useful: both score near the ceiling for Display/HUD, while neither approaches Brilliant Labs in Openness because excellent interoperability is not the same as open firmware or hardware. **Luma Pro is a very capable, very local, very proprietary display—and those three facts can coexist without contradiction.**

## Audit note

GLS-0074 XREAL One already had a substantive evidence-derived paragraph in `PROFILES_AR_DISPLAY.md`; Batch 03 validated that profile and did not duplicate it here.
