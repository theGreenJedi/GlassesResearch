# EV-0037 — RealWear service survival and optical-service evidence wave two

Verified: 2026-08-13
Source class: vendor primary
Confidence: confirmed for exact cited products/functions

## RealWear HMT-1 / HMT-1Z1 service survival

Primary sources:
- https://support.realwear.com/knowledge/realwear-hmt-security-update-end-of-support-notice
- https://support.realwear.com/knowledge/firmware-release-12.6-release-notes
- https://support.realwear.com/knowledge/realwear-firmware-update-and-support-policy
- https://support.realwear.com/knowledge/speech-keyboard-hmt-interaction

RealWear explicitly classifies HMT-1 and HMT-1Z1 as End of Life / End of Support and states that firmware 12.6 is the final firmware line. RealWear also explicitly says an end-of-life Android device will still work, although third-party applications may cease functioning properly and no further Android security updates will be supplied.

This is direct service-survival evidence: HMT-1/HMT-1Z1 are not equivalent to a destructive cloud shutdown. The correct preservation state is `discontinued-functional` with security/software-aging risk rather than `nonfunctional`.

RealWear's Release 12 documentation also distinguishes cloud and local dictation. English, German and Mandarin Chinese local dictation can operate without internet connectivity; other supported dictation languages rely on cloud dictation. This provides function-level Cloud Independence evidence rather than a single device-wide score.

RealWear states Navigator 500, Navigator 520, Navigator Z1 and Arc 3 are currently supported through at least December 2030 and that currently supported devices are planned to receive an Android-16-based OS during 2026.

## Even G2 optical service model

Primary sources:
- https://www.evenrealities.com/prescription-smart-glasses
- https://support.evenrealities.com/hc/en-us/articles/15404592516879-Purchasing-Even-Products
- https://www.evenrealities.com/en-LT/smart-glasses

Even G2 supports prescription lenses as an integrated digital-lens/display unit. Even documents a correction range of approximately -12.00 to +12.00 for supported single-vision prescriptions. Online ordering supports single vision, while progressive lenses and individualized UltraFit lenses are available through authorized/certified optician partners.

Even also documents lens replacement when a prescription changes: owners do not need to replace the frame, but the replacement process is coordinated through Even/support. This is stronger than vendor-only nonreplaceable optics but should not be labeled ordinary independent optical service. The best current state is `specialist/authorized optical service` because the display/digital-lens architecture is integrated and certified partners are part of the supported pathway.

## Solos optical service model

Primary sources:
- https://solosglasses.com/products/airgo3-argon-collection-argon-6s-front-frame
- https://solosglasses.com/products/argon-x-photochromic-smartglasses-solos-airgo3

Solos accepts externally issued prescriptions for its prescription products and documents custom lens production through its lab, including different lens indices/finishes. The modular front-frame architecture is separable from the smart temples. This is strong evidence that prescription eyewear is a first-class design requirement.

The current vendor pages do not, by themselves, establish that every Solos model can be serviced by any ordinary independent optical shop. Therefore the evidence state is `vendor/specialist optical service confirmed; ordinary independent service provisional` until an official service statement or repeatable independent fitting evidence is documented.

## Research implications

- RealWear HMT-1/HMT-1Z1: service state upgrades from generic end-of-support to explicitly `discontinued-functional`; local dictation gives function-level offline evidence.
- Even G2: prescription support becomes quantified and progressive support is confirmed through authorized opticians; serviceability should be scored as specialist/authorized rather than ordinary-independent.
- Solos: prescription architecture is confirmed as external-prescription friendly and modular, but independent ordinary-optician service remains unproven at vendor-primary level.
