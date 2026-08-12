# Lineage Research — Envision Assistive Glasses

**Research date:** 2026-08-12

## Lineage finding

Envision now has two distinct assistive-eyewear branches: the original **Envision Glasses** built on Google Glass Enterprise Edition 2 hardware, and the newer **Ally Solos Glasses** built with Solos hardware. Read/Home/Professional are software/support editions of the same Envision Glasses hardware, not separate generations.

### Envision Glasses

Envision Glasses use Google Glass Enterprise Edition 2 hardware: Snapdragon XR1, 3 GB RAM, 32 GB storage, 640×360 monocular display, 8 MP camera, Wi-Fi/Bluetooth, AOSP 8.1 and roughly 46 g body weight. Envision layers its accessibility stack on top: instant/scan/batch text, scene description, object/person finding, cash/color/light recognition, calling and conversational assistance. Current edition prices are $1,899 Read, $2,499 Home and $3,499 Professional.

A notable ownership nuance is that many core functions can operate offline when offline mode is selected: text reading/scanning, cash recognition after currency download, light/color detection, QR scanning, object finding, people detection and Explore. Online operation improves text accuracy and enables service-backed features, so the system is neither cloud-free nor helpless without cloud access.

### Ally Solos Glasses

Ally Solos Glasses are a separate 2025–2026 branch developed with Solos. They connect to a smartphone through the Ally app, use voice-first AI to read text, describe surroundings, translate, identify objects, search the web and access schedule/weather information, and can also function as headphones. Envision documents up to 15 hours battery life with swappable battery stems. The current Envision store lists them at $699, though availability can vary and the store may show sold out.

## Report cards

| Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Envision Glasses | 7.0 | 7.0 | 8.0 | 9.0 | 4.0 | 6.5 | 7.0 | 4.5 | 5.5 | 5.0 |
| Ally Solos Glasses | 6.5 | 9.0 | 8.0 | 8.5 | 3.0 | 5.5 | 4.0 | 3.0 | N/A | 7.5 |

### Common-ruler rationale

- **Envision Glasses** inherit solid XR1-era hardware and a real monocular HUD; the accessibility software is the standout feature and is unusually deep.
- Their **Cloud Independence 7.0** reflects meaningful offline operation for a surprising number of core features, while online services remain important for higher-accuracy and service-backed functions.
- **Ally Solos** trade the display and standalone processing of Glass EE2 for much more ordinary-eyewear wearability and lower price, but their phone/app/AI-service architecture makes them more cloud- and host-dependent.
- Neither branch is an open developer platform; the underlying Android/Solos heritage provides some technical surface, but Envision's assistive stack is proprietary.
- Read/Home/Professional editions do not receive separate hardware scores because they are software/support tiers on the same Envision Glasses hardware.

## Primary sources

- Envision Glasses technical specifications: https://support.letsenvision.com/hc/en-us/articles/7604910350609-Technical-Specifications
- Offline capability: https://support.letsenvision.com/hc/en-us/articles/4437254114449-Which-features-work-without-an-Internet-connection
- Envision Glasses editions/pricing: https://support.letsenvision.com/hc/en-us/articles/7602816580369-What-are-Envision-Glasses
- Ally Solos overview: https://support.letsenvision.com/hc/en-us/articles/38089378498193-What-are-Ally-Solos-Glasses
- Ally Solos store/pricing: https://shop.letsenvision.com/

## Lineage rule

Do not count Envision Read/Home/Professional as separate models. Do count Ally Solos as separate hardware because it is a different physical platform and host architecture.