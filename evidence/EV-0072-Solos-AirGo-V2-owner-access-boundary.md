# EV-0072 — Solos AirGo V2 SDK and owner-access boundary

Last verified: 2026-08-15  
Applies to: Solos AirGo V2 (GLS-0029), with V1 and AirGo 3/A5 compatibility context  
Evidence class: vendor-primary

## Established application-level access

Solos' current developer page describes a shared iOS/Android SDK with BLE control and Wi-Fi data transport for AirGo V2. It explicitly advertises:

- video streaming and recording on V2;
- configurable video resolution, H.264/H.265 codec, bitrate and electronic image stabilization;
- direct Wi-Fi connection using owner-supplied SSID and password;
- media enumeration, download and deletion for JPEG, MP4 and AVI files;
- low-power and voice-command APIs;
- webhooks and RTMP endpoints;
- compatibility with V1 APIs;
- a named Firmware Update API.

The linked public V2 API specification provides method-level detail for video streaming, video recording, Wi-Fi connection and media file access. This is strong evidence of owner-directed capture, transport and application integration.

Sources:

- [Solos SDK developer page](https://solosglasses.com/pages/developers)
- [Solos V2 API specification](https://cdn.shopify.com/s/files/1/0436/1912/3360/files/V2_API_specs.pdf?v=1767336276)

## Firmware boundary

The developer page names a Firmware Update API, but the linked four-page public V2 specification does not document firmware-update methods, image format, manifest source, signature verification, rollback, recovery or owner-supplied firmware.

Therefore the current evidence establishes **vendor-mediated firmware-update API availability**, not:

- downloadable firmware images;
- owner-selected firmware;
- source-available firmware;
- bootloader unlock;
- signature-key control;
- offline update continuity;
- rollback or recovery images;
- update service survival after vendor shutdown.

## Access and availability boundary

The page advertises a US$1,999 SDK kit with two devices, documentation, sample code and one year of support, but the kit is currently marked unavailable. Public method summaries and the linked PDF remain useful evidence; they do not prove that a new independent developer can currently obtain SDK binaries, activation or support.

## Classification

**Strong documented application/media access; firmware ownership and present SDK acquisition unresolved.**

This supports high application-level Owner Control and Hackability for AirGo V2. It must not be promoted to open firmware or unrestricted system access.

## Closure tests

1. Obtain the current SDK and record license, activation and account/network requirements.
2. Reproduce BLE control and Wi-Fi media enumeration/download with vendor cloud endpoints blocked.
3. Test custom RTMP/local endpoints and preserve traffic captures.
4. Inspect the Firmware Update API surface, manifest location, package format and signature behavior.
5. Verify whether update packages can be cached and replayed offline.
6. Test failure recovery, rollback and reset without risking the only production unit.
7. Publish exact exposed sensors and distinguish raw data from vendor-processed events.
