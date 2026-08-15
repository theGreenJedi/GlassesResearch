# EV-0073 — Even G2 official-platform and direct-BLE owner-access boundary

Last verified: 2026-08-15  
Applies to: Even Realities G2 (GLS-0048)  
Evidence classes: vendor-primary; community-primary/reproduced project claims

## Official Even Hub path

Even Realities documents Even Hub as an open application platform inside the Even Realities mobile app. The official flow requires:

- an updated Even Realities app;
- an Even Hub developer account and platform registration;
- uploading `.ehp` packages to the vendor platform;
- QR-code testing through the app's Developer Center;
- vendor publication review before public discoverability;
- cloud synchronization of the glasses menu.

Installed plugin data is described as cached locally on the phone, but discovery, upload, testing enrollment, publication, updates and menu synchronization remain platform-mediated. “Open app platform” therefore does not mean account-free sideloading or a vendor-independent package channel.

Sources:

- [Even Hub support documentation](https://support.evenrealities.com/hc/en-us/articles/15688149217167-Even-Hub)
- [Even Hub Developer Platform Terms](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service)

## Direct BLE community path

Independent projects provide evidence of a second, lower-level route:

- `even-g2-protocol` documents direct BLE connection, a seven-packet authentication handshake, teleprompter display and calendar functions;
- `g2-kit-unofficial` documents dual-arm BLE transport, packet framing, protobuf messages, audio, events, text/image rendering and direct operation without Even Hub SDK or vendor blobs;
- `men-g2-ble-gateway` reports local HTTP/WebSocket/MCP control on official firmware without cloud or internet, with its BLE layer derived from MentraOS work.

These are community projects and their exact firmware/device coverage must remain version-scoped. Together they materially demonstrate that useful display/input pathways are not confined to the official portal.

Sources:

- [even-g2-protocol](https://github.com/i-soxi/even-g2-protocol)
- [g2-kit unofficial](https://github.com/Commute773/g2-kit-unofficial)
- [G2 BLE Gateway](https://github.com/gpsnmeajp/men-g2-ble-gateway)

## Classification

**Vendor-mediated official plugin ecosystem plus community-demonstrated direct BLE control.**

This establishes strong application-level owner-access potential. It does not establish:

- an officially documented raw G2 protocol;
- stable compatibility across future firmware;
- bootloader unlock or firmware signing-key control;
- a vendor-independent firmware update/recovery path;
- unrestricted sensor/display privilege;
- account-free access to official Even Hub tooling;
- long-term survival of cloud-synced official plugin menus.

## Closure tests

1. Reproduce direct BLE connection on a clean host with official app stopped and vendor endpoints blocked.
2. Record firmware, characteristic map, authentication exchange and dual-arm behavior.
3. Test text, image, touch/ring events, microphone and settings separately.
4. Compare official `.ehp` capabilities with direct BLE capabilities.
5. Determine whether locally cached official plugins launch after sign-out and endpoint blocking.
6. Preserve compatible community tools/releases and document breakage across firmware updates.
7. Keep custom-firmware claims separate until installation, signing, rollback and recovery are independently verified.
