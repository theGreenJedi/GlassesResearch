# Iristick — populated research record

Source basis: `docs/report-cards/HIGH_THROUGHPUT_BATCH_06.md`, Iristick specification/docs and product pages cited there.

## Architecture
Iristick is unusually owner-host-friendly for enterprise smart glasses: the glasses rely on a connected smartphone for compute, networking and app installation rather than forcing a dedicated vendor compute ecosystem. That improves practical Owner Control and Cloud Independence without making the glasses open hardware.

## G2 — GLS-0116
Lightweight safety-glasses form with central camera, optical zoom camera, adjustable monocular LCD HUD, microphones, speaker, touch/voice input and pocket unit.

Anchor: H7.5 W8.0 VAI7.0 S7.5 O6.0 OC8.0 CI8.5 Hack6.0 HUD6.5 V6.5.

## G2 PRO — GLS-0117
Documented around 78 g with 16 MP central camera, 5 MP 6× optical-zoom module, 1080p video, hot-swappable battery and ANSI/EN safety certification.

Anchor: H8.0 W8.0 VAI7.5 S8.0 O6.0 OC8.0 CI8.5 Hack6.0 HUD6.5 V6.5.

## H1 — GLS-0118
Rugged industrial/PPE branch: ~168 g, IP67, dual 16 MP main cameras, zoom camera, OLED HUD, quad microphones, swappable power and PPE integration.

Anchor: H8.5 W5.5 VAI8.0 S8.0 O6.0 OC8.0 CI8.5 Hack6.0 HUD7.0 V6.5.

## G3 — GLS-0119
Strongest eyewear-oriented design in the packet: ~95 g safety-glasses form, 640×400 OLED HUD up to 2000 nits, 16 MP wide camera + 16 MP 3× optical-zoom camera, 1080p streaming, beamforming microphones, touch/voice control, prescription insert option, ANSI/EN safety certification and IP54. Connects directly to Android/iOS hosts by USB-C and draws power/compute from the user's phone.

Anchor: H9.0 W8.0 VAI8.5 S8.5 O6.5 OC8.5 CI9.0 Hack6.5 HUD8.0 V8.0.

### Optical serviceability
Current Iristick documentation explicitly provides an optional magnetic prescription insert: the wearer takes it to an optician for lens fitting and then attaches it to the G3. This supports **ordinary-optician service through an owner-removable insert**, not direct service of the certified safety lens, HUD optics or electronics. Exact correction/progressive limits, materials, price, stock, certification effects and cross-model insert compatibility remain unknown. See [EV-0069](../../evidence/EV-0069-Iristick-prescription-insert-serviceability.md).

## Ownership interpretation
Host-phone architecture keeps apps/networking under substantial owner/enterprise control and makes core operation less vendor-cloud-bound than sealed standalone appliances. Proprietary device electronics/firmware keep openness below open-hardware benchmarks.

## Evidence gaps
Exact SDK/API licensing and sensor access, phone compatibility by model, firmware/update behavior, G3 correction limits and insert supply, non-optical repairability, battery/parts availability, current pricing and post-vendor/service survival.