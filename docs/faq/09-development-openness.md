# Development, openness, protocols, and repairability

Openness is a stack: hardware documentation, boot access, firmware, protocols, SDKs, app licensing, cloud dependence, and repair parts can each be open or closed.

**Information reviewed:** 2026-08-05. Product availability, software, prices, and advertised battery life can change. Unless explicitly marked hands-on, statements below are sourced from manufacturers, project documentation, or attributed community material.

## 81. Which smart-glasses platforms are open source?

MentraOS is published under an MIT license and supports several hardware platforms. Brilliant Labs publishes repositories and documentation for its devices, and Halo is presented as open hardware and software. Team Open Smart Glasses publishes mechanical, electrical, and software files. Sources: [MentraOS](https://github.com/Mentra-Community/MentraOS), [Brilliant Labs GitHub](https://github.com/brilliantlabsAR), [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses).

## 82. What is MentraOS?

MentraOS is an open-source smart-glasses software platform with an SDK and miniapp store. It supports Mentra Live, Even G1/G2, and Vuzix Z100, with other hardware planned. Its architecture uses the phone as the app runtime so lightweight glasses can share one connection and run multiple miniapps. Sources: [MentraOS overview](https://mentraglass.com/os), [MentraOS roadmap](https://mentraglass.com/blogs/blog/mentra-roadmap-update-moving-to-miniapps-on-the-phone).

## 83. Can developers build apps for Ray-Ban Meta glasses?

Consumers can use Meta’s supported features and integrations, but Ray-Ban Meta is not the default recommendation for unrestricted hardware/protocol development. Access is controlled relative to Mentra, Brilliant Labs, Vuzix, or Rokid developer ecosystems. Before choosing it for a project, verify the current official SDK/API scope rather than assuming camera, sensors, or BLE characteristics are available.

## 84. Can developers build apps for Even G2 or Vuzix Z100?

Yes, through supported routes. Vuzix provides its Ultralite SDK for text, images, simple animations, taps, screen state, and battery state. MentraOS lists Even G1/G2 and Vuzix Z100 as supported hardware for its miniapps. Sources: [Vuzix Z100 SDK overview](https://support.vuzix.com/docs/overview-28), [MentraOS compatibility](https://mentraglass.com/os).

## 85. What makes smart glasses hackable?

Useful indicators include accessible firmware/update files, documented USB or BLE protocols, an SDK without restrictive gates, unlockable boot paths, serial/debug pads, reproducible builds, available recovery images, standard components, community captures, and replaceable hardware. Marketing phrases such as `open AI` do not prove any of these.

## 86. What is the difference between an SDK and an open protocol?

An SDK is vendor-supplied code and documentation for approved functions. An open protocol documents the messages on the wire so independent implementations can interoperate. An SDK may be proprietary, cloud-bound, revocable, or limited; an open protocol may enable clients on unsupported platforms. Serious research records both.

## 87. Why capture BLE services and packets from smart glasses?

Captures reveal advertised identities, services, characteristics, notifications, commands, and state transitions. They can preserve knowledge even if the app disappears. Capture only devices and traffic you are authorized to inspect, record firmware/app versions, redact personal data, and store raw evidence plus decoded notes.

## 88. Can smart-glasses firmware be replaced?

Sometimes, but usually not safely without signed images, bootloader access, hardware documentation, and a recovery method. A firmware dump is not the same as a flashable replacement. Begin by preserving official updates, hashes, partitions, logs, and recovery procedures; do not experiment on the only working specimen without a rollback path.

## 89. Are smart-glasses batteries and parts repairable?

Fashion-oriented models often use glued or sealed batteries and proprietary charging; Ray-Ban explicitly says its embedded batteries are not replaceable. Enterprise modules and open hardware projects offer better prospects. Repairability should include parts availability, disassembly damage, calibration, waterproofing, firmware pairing, and lens service—not just whether screws exist. Source: [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses).

## 90. What artifacts should a smart-glasses research repository preserve?

Preserve lawful copies or metadata for manuals, APKs, SDKs, firmware and update URLs, hashes, BLE captures, protocol schemas, logs, model files, PCB photographs, regulatory filings, lens templates, flashing/recovery instructions, tools, repositories, and community posts. Record provenance, retrieval date, license, redistribution status, model/revision, and authenticity caveats.
