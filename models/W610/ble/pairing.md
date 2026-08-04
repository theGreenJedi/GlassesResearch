# W610 Bluetooth Pairing

## Evidence type

Firsthand observations from the project-owned W610 during initial setup in August 2026.

## Observed device name

`HeyCyan Glasses`

## Initial behavior

- The first pairing attempt did not complete successfully.
- After power cycling and repeating discovery, the glasses became visible again.
- At one point two related Bluetooth entries were visible, suggesting the platform may expose more than one Bluetooth role or cached identity.
- The exact identity and purpose of the second entry remain unresolved.

## Current conclusion

Basic Bluetooth discovery works without first installing the HeyCyan app. This is important because it permits a clean baseline before vendor software changes device state, grants permissions, associates an account, or initiates an update.

## Reproduction checklist

1. Record phone model, operating-system version, and Bluetooth state.
2. Power the glasses off completely.
3. Begin a Bluetooth scan.
4. Hold the rear power button until the startup tone and LED response occur.
5. Record every new device name, address type, signal strength, icon, and pairing prompt.
6. Attempt pairing once and record the exact result.
7. Power cycle the glasses and repeat before installing any vendor application.

## Still needed

- Address type and whether the address rotates
- Classic Bluetooth versus BLE identities
- Advertising payloads and service UUIDs
- Pairing method and authentication requirements
- Behavior after forgetting the device
- Differences with and without the HeyCyan app
- Sanitized screenshots or scan exports
