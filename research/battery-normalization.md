# Battery Normalization Framework

Manufacturer battery claims often describe different workloads and cannot be compared directly. GlassesResearch should separate claimed endurance from measured endurance and label the workload.

Track battery capacity when documented, charging method, case contribution, charge time, claimed endurance, and measured endurance. Normalize tests into useful workload classes: idle connected, audio playback, voice interaction, camera capture, repeated AI queries, HUD/display use, and mixed normal use.

Every measured result should record device and firmware version when known, host device, connectivity state, display brightness where relevant, starting and ending charge, elapsed time, major workload details, and test date.

Do not average incompatible workloads into a single universal battery-life number. Battery aging should be recorded separately from new-device endurance. Case capacity should not be presented as continuous on-face runtime.

Battery findings feed Hardware, Wearability, Value, and long-term ownership research.

## Source-bound claim matrix

[EV-0071](../evidence/EV-0071-normalized-battery-claims-wave-one.md) records the first cross-model claim boundary for Even G2, Brilliant Halo, Ray-Ban Meta Gen 2 and Solos AirGo V2. It keeps manufacturer-specific “typical,” “normal,” “moderate,” audio, call, camera/AI and case-recharge claims separate. These claims are not a valid endurance ranking.
## Operational templates

- [W610 normalized battery benchmark log](../models/W610/diagnostics/battery-benchmark-log.md) — first control-device implementation of this framework, including charge baseline, workload variables, interval telemetry, low-battery cutoffs, safety stops and three-run median/spread reporting.
