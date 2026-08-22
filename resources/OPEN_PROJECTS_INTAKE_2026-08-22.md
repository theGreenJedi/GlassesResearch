# Open-project intake — 2026-08-22

This intake extends the main [Open Projects, Protocols, and Developer Resources](OPEN_PROJECTS_AND_PROTOCOLS.md) ledger with newly supplied projects that need lineage-aware preservation or verification before promotion into the long-lived table.

## Wearable Intelligence System → SmartGlassesManager

### Wearable Intelligence System (WIS)

- Source: https://github.com/emexlabs/WearableIntelligenceSystem
- Evidence lane: **Historical / archived project-primary**
- License: MIT
- Scope documented by the project: Android smartphone + Android smart-glasses framework; the README specifically names Vuzix Blade support.
- Substantive content: voice-command application launcher, live captions, translation, visual search, memory tools, phone↔glasses connectivity, HUD applications and developer documentation.

The WIS README explicitly labels the project **ARCHIVED** and says it was reorganized/upgraded into SmartGlassesManager. Preserve WIS because it contains glasses-specific implementation history and design assumptions that can disappear from a successor.

### SmartGlassesManager

- Current repository: https://github.com/Mentra-Community/SmartGlassesManager
- Historical redirect/source name: https://github.com/TeamOpenSmartGlasses/SmartGlassesManager/
- Evidence lane: **Project-primary / lineage successor**

GitHub resolves the earlier TeamOpenSmartGlasses repository lineage to the current Mentra-Community project. Treat SmartGlassesManager as the successor to WIS, not an independent confirmation of WIS behavior.

Research value:
- documents the software lineage that precedes later MentraOS work;
- useful for tracing device adapters, phone/glasses architecture and application abstractions across generations;
- helps distinguish renamed/reorganized code from truly independent implementations.

Preservation target:
- tags/releases/commit dates;
- supported-device lists by era;
- Android permissions and connection architecture;
- API/device adapter boundaries;
- licenses and successor notices.

## Nimbo X1 — emerging project-primary developer surface

- Project: https://nimbopearl.com/
- Evidence packet: [EV-0080](../evidence/EV-0080-Nimbo-X1-open-platform-claims.md)
- Evidence lane: **Project-primary + team claims; verification pending**

Nimbo currently claims an AOSP-based platform, open SDK, system-level signing, low-level interfaces, raw sensor access, custom camera/IMU applications, an independent App Center and user-configurable OpenAI-compatible AI endpoints.

This is potentially one of the more owner-accessible commercial full-color AR platforms in the current market, but the project is **not promoted to verified-open status merely because the claims are unusually strong**.

Preserve/verify as soon as available:
1. SDK packages and versions;
2. developer documentation;
3. sample applications and source licenses;
4. signing process and who receives signing authority;
5. camera/IMU/raw-sensor APIs and restrictions;
6. firmware/update/recovery paths;
7. app installation outside the Nimbo App Center;
8. AI endpoint configuration and service-blocked behavior.

## NIMO Holo-Optical Glasses + MentraOS

- Reservation: https://shop.nimoar.com/products/nimo
- MentraOS: https://github.com/Mentra-Community/MentraOS
- Community compatibility lead: https://www.reddit.com/r/augmentedreality/comments/1vlml5f/mentraos_running_on_nimo_smart_glasses_making/
- Evidence lane: **project-primary reservation + community/runtime compatibility**

NIMO's current $20 transaction is explicitly a refundable deposit reservation, not a product purchase. MentraOS compatibility is interesting because it may provide a third-party application surface, but compatibility with an open runtime does not establish that NIMO firmware/hardware itself is open.

Preserve as a pre-release development lead and verify the exact interface MentraOS uses when public documentation/code identifies it.

## Intake rule reinforced

A project belongs in the open-development research graph when it exposes usable code, protocols, developer interfaces, hardware files or preservation-worthy implementation history. Marketing statements such as “open,” “developer friendly,” or “privacy first” are discovery signals until inspectable artifacts establish what owners can actually do.
