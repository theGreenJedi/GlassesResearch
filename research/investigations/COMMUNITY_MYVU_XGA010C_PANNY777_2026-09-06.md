# Community research note — Panny777 / MYVU XGA010C

**Evidence lane:** Community-attributed technical research  
**Subject:** MYVU Air / StarV Air, model XGA010C  
**Contributor/source:** GitHub user `Panny777`  
**Status:** Public third-party reverse engineering; not yet independently reproduced by GlassesResearch

## Why this work matters

Public work by GitHub user **Panny777** substantially advances what can be known about the MYVU Air / StarV Air (XGA010C) beyond manufacturer specifications. The work includes an unofficial Android SDK, a working client, and a protocol document derived from packet captures of the glasses and official application.

GlassesResearch treats these findings as **community-attributed evidence**. They are useful and technically detailed, but they are not promoted to independently verified GlassesResearch findings until reproduced on a GlassesResearch-controlled specimen.

## Reported methodology

According to the project's public documentation, the protocol work was developed from packet captures and a working reverse-engineered client. The published SDK then models the protocol as reusable modules and includes byte-level protocol tests.

The public methodology therefore includes:

1. capture of device/application Bluetooth traffic;
2. reverse engineering of the transport and application protocol;
3. implementation of an independent client capable of driving the glasses;
4. validation against physical MYVU / Star Air hardware;
5. documentation of the wire protocol and connection sequence;
6. packaging of the result as an unofficial Android SDK and client;
7. publication under an MIT license.

This is a useful reproducibility pattern for future GlassesResearch software-interoperability investigations: observe traffic, identify protocol layers, reproduce bounded commands, validate on hardware, document uncertainty, and separate captured behavior from inference.

## Community-attributed findings

The following findings are reported by Panny777's public SDK and protocol documentation for **Meizu MYVU / Star Air, model XGA010C**:

### Device identity

The SDK explicitly targets **Meizu MYVU / Star Air AR glasses, model XGA010C**.

### Two-link Bluetooth architecture

The glasses reportedly require both **BLE** and **Classic Bluetooth / RFCOMM**. BLE must be established first; it handles pairing/session setup and announces a per-session RFCOMM relay. Classic Bluetooth then carries most application traffic.

### Pairing and session behavior

The protocol documentation describes:

- a StarryNet BLE service family;
- ECDH-based pairing using P-256;
- a recurring heartbeat requirement;
- a per-session RFCOMM UUID announced over BLE;
- application-level ability/authentication handshakes;
- sequencing requirements for application messages.

These details are particularly relevant to owner control because they indicate that the useful display/application surfaces can be accessed by an independent implementation rather than only through the official Meizu application.

### Independent control surfaces

The published SDK reports support for:

- teleprompter content;
- notifications;
- brightness and volume control;
- time synchronization;
- weather data;
- device settings;
- trackpad events/actions;
- turn-by-turn navigation;
- microphone audio ingestion;
- custom speech-to-text engines;
- custom language-model backends;
- rendering answers into the glasses' existing LLM-card scene.

The SDK itself ships no required proprietary cloud AI client for these higher-level features; speech recognition and language-model functions can be supplied by the integrator.

### Connection behavior and failure modes

The project reports several behaviors useful for future bench replication:

- the official Meizu app can occupy the single central connection and block another client;
- BLE must come up before BR/EDR pairing;
- the classic-Bluetooth application relay may drop and require reconnection;
- background execution on some Android OEM builds may require battery-optimization exemptions;
- some multi-turn AI behavior depends on state/signals normally supplied by the official cloud stack.

### Weather data uses metric units

The reverse-engineered weather payload is reported to use integer temperatures in **degrees Celsius**, with the official app hardcoding metric units and no unit-negotiation flag. This aligns with GlassesResearch's metric-first measurement policy.

## What this evidence does — and does not — establish

This work is strong evidence of **practical hackability and third-party interoperability** for XGA010C. It demonstrates a working independent implementation and publishes enough protocol detail for others to inspect and reproduce.

It does **not** establish official openness. Meizu did not publish this protocol as an official SDK or documented public interface. GlassesResearch should therefore distinguish:

- **official openness:** weak / not established;
- **community-discovered interoperability:** strong evidence;
- **GlassesResearch independent verification:** pending acquisition and bench replication.

## Replication targets for GlassesResearch

When GlassesResearch obtains an XGA010C specimen, the first software-interoperability replication set should be deliberately narrow and reproducible:

1. confirm advertised Bluetooth name and StarryNet service family;
2. confirm BLE-first connection requirement;
3. confirm per-session RFCOMM relay behavior;
4. reproduce one benign output command, such as a teleprompter message;
5. reproduce brightness control;
6. capture one inbound trackpad or status event;
7. record firmware/app versions and all observed deviations from the community documentation.

Any reproduced result should retain attribution to the original community work while being promoted separately into the GlassesResearch independently verified evidence lane.

## Attribution and source integrity

GlassesResearch is summarizing publicly documented technical findings and linking to the original work. No claim here should be read as a GlassesResearch lab result unless separately marked as independently reproduced.

Primary public sources:

- Panny777 — MYVU Android SDK (unofficial): https://github.com/Panny777/Meizu-Myvu-SDK
- Panny777 — reverse-engineered MYVU wire protocol: https://github.com/Panny777/Meizu-Myvu-SDK/blob/main/PROTOCOL.md
- Panny777 — MYVU client monorepo: https://github.com/Panny777/Meizu-Myvu-Client

## Disposition

**Include as community-attributed technical evidence for GLS-0167 (MYVU Air / StarV Air / XGA010C).**

This work should inform the model's Hackability, Owner Control, Cloud Independence, and Software evidence narratives, but should not be converted into GlassesResearch-owned findings until replicated.