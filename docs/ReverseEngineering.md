# Reverse Engineering

## Purpose

Provide a disciplined, reproducible workflow for investigating W610/W6xx hardware and software while preserving evidence and minimizing device risk.

## Working method

1. **State the question.** Define the specific behavior or interface being investigated.
2. **Preserve the baseline.** Record the untouched device state, software versions, and observable behavior.
3. **Change one variable.** Avoid experiments that combine multiple unknowns.
4. **Capture evidence.** Save logs, packet captures, photographs, hashes, and exact commands.
5. **Repeat.** Confirm the observation across multiple trials where practical.
6. **Classify the conclusion.** Mark it as confirmed, probable, possible, or disproven.
7. **Document recovery.** Record how to reverse the change or restore the device.

## Experiment template

### Question

What are we trying to learn?

### Environment

- Device and revision:
- Firmware:
- Host hardware:
- Host software:
- Tools and versions:

### Baseline

Describe the initial state and known behavior.

### Procedure

Number each action precisely.

### Evidence

Link logs, images, captures, hashes, and source material.

### Result

Describe what happened without interpretation.

### Interpretation

Explain the likely meaning and plausible alternatives.

### Confidence

Confirmed / Probable / Possible / Disproven

### Reproduction

Record whether another run or researcher reproduced the result.

## Priority investigations

- BLE advertisement and GATT mapping
- Button and LED state machine
- Audio and capture paths
- Vendor-app traffic and offline behavior
- Firmware acquisition and recovery options
- Hardware-family identification
- Prescription-lens geometry and repeatability
