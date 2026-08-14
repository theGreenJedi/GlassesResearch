# W610 Diagnostics

This section records normal-state baselines, reproducible fault tests, charging and connectivity behavior, audio/camera checks, and recovery attempts.

## Current baseline

- Power control is the rear button on the right temple in current testing.
- Power activation produces an audible tone and a brief LED flash near the right hinge.
- The Bluetooth name observed is `HeyCyan Glasses`.
- Initial pairing was inconsistent, and later scans showed two device entries. This requires a controlled retest before assigning a fault cause.
- The vendor app was intentionally avoided during the initial baseline.

## First diagnostic checklist

Use the [baseline checklist](baseline-checklist.md) for the repeatable procedure.

1. Record charge source, cable/adapter, LED response, and elapsed charging time.
2. Test cold boot, short press, long press, and power-cycle behavior.
3. Scan Bluetooth from two independent hosts and record advertisements.
4. Check microphones, speakers, camera trigger, and storage behavior without changing firmware.
5. Photograph every state and record exact timestamps.

## Reporting format

Every test must state prerequisites, steps, expected result, observed result, device state, risks, and date. A failed pairing attempt is an observation, not proof of defective hardware.
