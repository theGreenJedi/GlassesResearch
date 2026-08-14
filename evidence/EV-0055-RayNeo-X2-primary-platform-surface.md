# EV-0055 — RayNeo X2 primary platform surface

Verified: 2026-08-14
Source class: vendor primary
Confidence: high for the documented retail configuration and supported development path
Scope: RayNeo X2 (`GLS-0065`)

## Sources

- RayNeo X2 product page: https://www.rayneo.com/products/tcl-rayneo-x2
- RayNeo X2 FAQ and assisted-development guide: https://www.rayneo.com/pages/faq-x2
- RayNeo developer portal: https://open.rayneo.com/

## Verified hardware and product role

RayNeo's surviving product page documents X2 as an untethered standalone AR system rather than a display accessory. The retail configuration combines Snapdragon XR2 compute, 6 GB RAM, 128 GB storage, a 590 mAh battery, Wi-Fi 5, Bluetooth 5.2, GPS, USB 2.0, a 16 MP camera with 1080p capture, three microphones, onboard sensors and binocular full-color MicroLED waveguide displays. The same page documents a $499 US retail route, now marked out of stock, and prescription-lens fitting through a local optician or RayNeo's optical partner.

RayNeo gives two different maximum-brightness figures on the same page—1,000 nits in the summary and 1,500 nits in the detailed presentation. The conflict is preserved rather than silently resolved. No brightness value is promoted into the structured comparison record.

## Verified software and owner-access surface

The product page documents translation, navigation/SLAM, camera capture, notifications, voice control, temple controls and optional ring input. Some first-party experiences are cloud-backed: RayNeo specifically identifies Microsoft Azure for face-tracking translation and GPT-4 with Vision for its AI companion.

The support FAQ independently establishes a meaningful local owner-development path. X2 accepts third-party Android APKs over ADB; firmware 1.2.66 and later requires owners to enable `mercury_install_allowed` before installation. RayNeo also documents screen mirroring with `scrcpy`, microphone-routing parameters for third-party applications and thermal/current guidance for developers. This is stronger than a companion-app-only appliance, although it is not evidence of open firmware, unlocked bootloaders or open hardware.

## Catalog implication

X2 now has enough generation-specific primary evidence for a conservative Report Card and structured comparison record. Its strongest ownership trait is local Android application deployment. Its cloud score remains lower than its owner-control score because several headline assistant and translation experiences use vendor-selected network services.

