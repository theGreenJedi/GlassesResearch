# EV-0068 — W610 optical-serviceability boundary

Last verified: 2026-08-15  
Applies to: W610 / GLS-0039 and the project-owned W610 specimen  
Evidence classes: vendor-primary claim; GlassesResearch firsthand observation

## Question

Does the W610 have merely a prescription-compatible product claim, or is there enough evidence to classify it as ordinarily serviceable by an independent optical shop?

## Evidence

### Goodway supplier record (EV-0008)

Goodway's current W610 page places the following under **OEM / ODM Customization**:

- removable lenses;
- customizable lenses, including prescription options.

This is useful exact-model evidence that a W610 supply configuration can be built with removable or corrective lenses. Its commercial context matters: the page is addressed to B2B customization customers. It does not say that any retail W610 can be brought to any ordinary optician, that replacement lenses or fronts are sold to owners, or that independent reglazing is approved.

Source: [Goodway W610 specification page](https://www.goodwaytechs.com/goodway-ai-smart-glasses-with-8mp-camera-real-time-translation-ip65-waterproof-42g-lightweight-w610.html) (EV-0008), verified 2026-08-15.

### Project-owned specimen

GlassesResearch directly observed that:

- the supplied lenses are tinted;
- their seating/fit and optical quality are unimpressive;
- electronics are concentrated in the right temple;
- the exact lens-retention method has not yet been documented;
- no lens dimensions, trace, base curve, bevel, material, or correction range has yet been measured.

These observations establish an owned-device test surface, not a successful prescription conversion.

Source: [W610 physical overview](../models/W610/hardware/physical-overview.md).

## What is not established

Current evidence does not establish:

- an exact sphere/cylinder correction range;
- progressive, prism, high-index, photochromic, or multifocal support;
- lens material, base curve, edge thickness, bevel, or minimum-center-thickness requirements;
- that the owned specimen matches the supplier's removable-lens configuration;
- ordinary independent optical-shop acceptance;
- an authorized optical network or retail prescription-ordering path;
- replacement fronts, blanks, donor lenses, or a downloadable lens template;
- electronics-safe heating, ultrasonic-cleaning, lens-removal, or reassembly instructions;
- whether optical work affects sealing, alignment, warranty, or temple electronics.

## Classification

**Prescription-compatible supplier claim; ordinary optical service unverified.**

Do not set a simple positive `prescription_support` field from this record. The supplier claim is meaningful, but the missing correction limits, exact retail-variant confirmation, service channel, and demonstrated reglazing path would make a boolean “yes” misleading.

## Hands-on closure protocol

Before promoting W610 to ordinary- or specialist-serviceable optics:

1. Record the specimen's seller, label, packaging, firmware, and physical revision.
2. Photograph lens seating from front, rear, top, and hinge-adjacent angles.
3. Identify the retention system without forcing or heating the frame.
4. Measure lens A, B, DBL, effective diameter, frame wrap/base curve, center and edge thickness, and groove/bevel geometry.
5. Trace or scan the supplied lens before any removal and preserve it as a donor/template.
6. Ask an independent optician whether the exact frame can be safely edged and fitted, recording rejected as well as accepted work.
7. Record material, prescription, fitting method, heating/cleaning restrictions, sealing effects, cost, and post-fit optical and electronic checks.
8. Avoid heat or ultrasonic cleaning near the electronics-bearing temples unless exact-model guidance is obtained.

A documented successful fitting on the owned unit would establish a specimen-level path. It should not automatically be generalized to every W610 marketplace or OEM variant.
