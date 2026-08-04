# HeyCyan Companion Application — W610 Baseline

## Relationship to the owned device

The owned specimen advertises as `HeyCyan Glasses`, and the included manual contains a QR code directing the user toward vendor software. The project intentionally did not begin by installing the app.

## Why installation was deferred

A clean pre-app baseline preserves evidence that might otherwise be changed by:

- account registration
- permissions grants
- Bluetooth bonding
- Wi-Fi provisioning
- cloud association
- time synchronization
- configuration writes
- firmware updates

## Current known role

Commercial material associates the W610 platform with the HeyCyan application. The app is therefore a high-value research target for:

- supported-device identifiers
- BLE services and commands
- Wi-Fi media-transfer behavior
- firmware-update endpoints
- cloud APIs and domains
- permissions and privacy behavior
- feature gating and account requirements

## Safe acquisition plan

1. Obtain the official store package or preserve the installer from a trusted source.
2. Record version, package name, signing certificate, cryptographic hashes, requested permissions, and publication metadata.
3. Perform static analysis before installation.
4. Use a non-primary Android device or isolated profile for dynamic testing.
5. Capture network traffic only where authorized and without exposing credentials or unrelated personal data.

## Current limitations

The exact package identifier and current supported-model list have not yet been verified from a preserved APK. Search results and reseller references are leads, not substitutes for the package itself.

## Related

- [APP-0001 — HeyCyan](../../../glossary/applications/APP-0001-hecyan.md)
- [W610 pairing observations](../ble/pairing.md)
- [Investigation 001 — W610 Identity](../investigations/001-identity.md)
