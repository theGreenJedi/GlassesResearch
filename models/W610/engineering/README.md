# W610 Diagrams and Schematics

This section turns observations into editable diagrams: physical layout, controller relationships, signal paths, power distribution, connector pinouts, PCB maps, and eventually traced schematics.

## Current preliminary architecture

The following is an **inference**, not a confirmed schematic:

```text
Right-temple controls / LED
          |
          v
Main controller lead: JL7018F
          |
          +---- Bluetooth / audio behavior
          |
          +---- Vision coprocessor lead: Allwinner V821L2
                         |
                         +---- Camera / image processing / Wi-Fi transfer
```

The electronics-heavy right temple, camera, microphones, speakers, magnetic charging contacts, and observed Bluetooth behavior support creating a first physical block diagram. The exact wiring and controller assignments remain unverified.

## Canonical component leads

- [CMP-0001 — JL7018F](../../../glossary/components/CMP-0001-jl7018f.md)
- [CMP-0002 — Allwinner V821L2](../../../glossary/components/CMP-0002-allwinner-v821l2.md)

## Next drawings

1. External physical-layout diagram with controls, LED, camera, charging contacts, microphones, and speakers.
2. Observed-versus-inferred system block diagram.
3. Lens and temple measurement drawing.
4. PCB map after lawful, non-destructive inspection.

Every drawing must state whether each element is observed, vendor-claimed, sourced, reconstructed, or inferred, and should include an editable source format.
