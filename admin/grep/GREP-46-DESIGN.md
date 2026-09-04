# GREP-46 — Real-World Experience and Use Cases

Status: design specification
Purpose: produce reproducible longitudinal usability and use-case evidence capable of supporting a Report Card while separating experience from bench specifications.

## Form header

Record form revision; specimen ID/GLS ID; evaluator; evaluation start/end dates; firmware/app versions observed; paired phone/device and OS; prescription/correction configuration; approximate PD/IPD if known and relevant; total days used; estimated total wear hours; environments represented; and functions intentionally excluded.

## Section 46-A — Wear sessions (`WR`)

Use repeated session rows rather than one retrospective impression. Each row records date, environment/activity, duration, starting fit state, and observations.

Standard checkpoints where practical: initial, 30 min, 2 h, 4 h, end-of-day.

Fields include:
- `WR-01` Initial comfort.
- `WR-02` Nose pressure/marks.
- `WR-03` Temple/ear pressure.
- `WR-04` Slippage/reposition frequency.
- `WR-05` Heat at temples/face.
- `WR-06` Balance/front or side heaviness.
- `WR-07` Eye fatigue/headache/nausea where display applicable.
- `WR-08` Interaction with prescription correction.
- `WR-09` Hair/hat/hearing-protection/earbud interference where relevant.
- `WR-10` Social wearability: does the device materially alter normal interaction? Record observation, not a universal aesthetic judgment.

Report Card relevance: Wearability.

## Section 46-B — Daily reliability (`FN/SW`)

For each day/session record unexpected disconnects, failed controls, app crashes, reboot/re-pair events, lost captures, notification failures, stalled transfers, cloud/service failures, and recovery steps. Record denominator where possible (for example 2 failed transfers / 31 attempts) rather than only anecdotes.

- `FN-01` Successful power/start sessions / attempts.
- `FN-02` Pairing/reconnection reliability.
- `FN-03` Control reliability.
- `FN-04` Capture/function success rate by applicable capability.
- `SW-01` Companion stability.
- `SW-02` Recovery burden after failure.

Report Card relevance: Hardware, Software, Value.

## Section 46-C — Battery in lived use (`PW`)

Each battery session records start/end percentage or indicator, start/end time, major functions used, approximate capture/display/audio workload, paired-device state, ambient conditions if material, and charging interruptions.

Do not turn mixed-use observations into a laboratory battery-runtime claim. They support real-world endurance only.

## Section 46-D — Defined use-case trials (`UC`)

Each trial records: use case, goal, environment, prerequisites, number of attempts, result, failure mode, workaround, evidence ID, and evaluator note. Suggested modules are used only when the device claims/supports them.

### Everyday communication
Calls; voice messages; notifications; assistant queries; music/podcast; switching between glasses and other audio devices.

### Camera / memory capture
Hands-free still; hands-free video; spontaneous capture; close document/text; moving subject; indoor; outdoor; media retrieval and sharing burden.

### Visual AI
Ask about visible object; read text; identify scene; follow-up query; latency observation; wrong-answer event; offline behavior. Do not score factual accuracy without preserving prompt/input and expected result.

### Translation
Conversation; sign/menu/text; supported-language path; latency; usability in noise; offline/cloud behavior where observable.

### Display/HUD
Notifications; reading short text; reading longer text; navigation; bright outdoors; dim room; screen/phone viewing through optics; walking; display stability as glasses shift.

### Navigation
Route initiation; instruction timing; glanceability; recovery after missed turn; phone dependency; outdoor visibility. Safety-critical use must not require unsafe behavior.

### Work/task assistance
Checklist/instructions; reference information; hands-busy task; meeting/notes where appropriate; repeated task usefulness.

### Exercise/outdoor
Walking; light exercise; sweat/slippage; wind/noise; sunlight; temperature exposure within manufacturer limits. Do not perform destructive environmental testing under GREP-46.

## Section 46-E — Display experience (`DP`)

When applicable, use defined conditions rather than “looks good.” Record content used, ambient condition, correction configuration, and fit position.

- `DP-01` Text readability at normal fit.
- `DP-02` Bright-outdoor readability.
- `DP-03` Dim-room comfort.
- `DP-04` Eyebox/fit tolerance as glasses shift naturally.
- `DP-05` Real-world transparency interference: phone, monitor, window, bright point source, dark/light text where applicable.
- `DP-06` External display/light leakage observation from bystander positions under stated conditions.
- `DP-07` Binocular alignment/double-image/eye-strain observation.

Instrumented optical measurements belong in GREP-44; GREP-46 captures lived behavior.

## Section 46-F — Audio experience (`AU`)

Defined trials: quiet room, ordinary indoor background, outdoor/wind where safe, call transmit/receive, music/spoken word. Record intelligibility/usefulness, volume adequacy, obvious leakage at a stated distance, and interaction with environmental awareness. Subjective observations remain labeled as such.

## Section 46-G — Owner friction (`OC/CI/SW`)

Record real-world moments where the owner is forced toward or away from vendor infrastructure: mandatory app use, mandatory account, internet requirement, cloud outage effect, export friction, file ownership, subscription/paywall encounter, forced update, permission prompt, region restriction, or inability to use a feature with preferred phone/software.

These observations can strongly support Owner Control and Cloud Independence but must distinguish one observed workflow from universal impossibility.

## Section 46-H — Privacy/social observations (`PR`)

Record whether bystanders can recognize recording state under actual use; accidental capture events; privacy indicator behavior; microphone/camera activation surprises; permission/network events observed; and social reactions only as anecdotal observations. Do not infer legal compliance or universal social acceptability.

## Section 46-I — Usefulness ledger (`UC/VL`)

For each claimed major use case, finish with:
- Works reliably and reduces friction
- Works but does not reduce friction
- Works only with material caveats
- Failed in tested scenario
- Not tested
- Not applicable

Require a short evidence-backed reason. This is not the Report Card score; it is structured input to it.

## Section 46-J — Completion and handoff

Record days, wear hours, sessions, use-case trials, applicable/completed/blocked modules, evidence count, unresolved questions, and any material changes in opinion between first use and end of evaluation.

The Report Card must disclose GREP-46 duration and coverage. One afternoon of wear cannot be described as longitudinal testing merely because the same form was used.