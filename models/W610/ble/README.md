# W610 BLE and Protocol Research

This section records Bluetooth advertisements, pairing behavior, GATT discovery, captures, commands, and interoperability tests.

## Current observations

- The received unit advertises as `HeyCyan Glasses`.
- Initial pairing did not succeed immediately; later scans showed two device entries, suggesting multiple radios, modes, or cached identities that require controlled retesting.
- The project intentionally began with vendor-app avoidance so native advertising and pairing behavior could be documented before the app altered device state.

## Known related entities

- [APP-0001 — HeyCyan](../../../glossary/applications/APP-0001-hecyan.md)
- [STD-0001 — Bluetooth SIG](../../../glossary/standards/STD-0001-bluetooth-sig.md)

## Next tests

1. Capture advertisements while powered off, booting, idle, pairing, and after button presses.
2. Record address type, service UUIDs, manufacturer data, RSSI, and device-name changes.
3. Enumerate GATT services without writing characteristics.
4. Compare Android and Linux scanner results.
5. Sanitize captures before publication.

No UUID or command should be labeled as W610-specific until reproduced on the received device.
