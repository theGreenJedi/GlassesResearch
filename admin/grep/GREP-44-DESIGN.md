# GREP-44 — Comprehensive Owned-Device Investigation

Status: design specification
Purpose: GlassesResearch's highest-depth repeatable evaluation for specimens it owns and can revisit. GREP-44 is intended to support the strongest available Report Card evidence without requiring destructive teardown.

## Relationship to GREP-42 and GREP-46

GREP-44 does not invent alternate versions of shared tests. It incorporates the GREP-42 controlled-inspection core and, when sufficient use time exists, the GREP-46 real-world modules. Shared field IDs retain their meanings and prior valid observations may be carried forward with their original date/evidence ID.

A practical GREP-44 packet therefore consists of:
1. GREP-42 identity, metrology, power, interfaces and basic-function core;
2. GREP-44 deep technical modules below;
3. GREP-46 longitudinal/use-case evidence where applicable;
4. completion/coverage matrix and Report Card handoff.

## Section 44-A — Configuration freeze

Before deep testing record specimen ID; hardware markings; firmware; companion app/version; paired host/OS; account state; network environment; correction/lens configuration; enabled settings; and any modifications. Significant firmware/app changes create a new configuration checkpoint so results from different states are not silently mixed.

## Section 44-B — Repeatable power characterization (`PW`)

Beyond GREP-42 observations:
- controlled charge time from defined starting state;
- idle endurance under defined radios/settings;
- representative mixed-use endurance;
- capability stress session where meaningful (camera/display/audio);
- charging input behavior with identified meter/source;
- thermal observations at defined checkpoints;
- standby/self-discharge observation where practical;
- low-battery behavior and feature degradation;
- power-off behavior and whether radios/functions actually cease.

Each runtime result records firmware, settings, starting/ending state, workload and environment.

## Section 44-C — Interface/protocol investigation (`IF/OP/OC/HK`)

Where lawful and non-destructive:
- complete USB descriptors/classes and mode changes;
- BLE advertising/GATT service/characteristic inventory;
- pairing/authentication behavior;
- Wi-Fi activation trigger and role (client/AP/direct) where observable;
- local media-transfer path;
- command/control path and observable protocol structure;
- button/touch/wear-sensor events visible to host;
- documented or discoverable SDK/API availability;
- third-party client feasibility demonstrated vs merely claimed;
- firmware/update package availability and format where obtainable through normal owner paths;
- bootloader/debug/service interfaces observed without bypassing access controls.

Record captures/artifacts, tool versions, and steps sufficient for another investigator to repeat the observation.

## Section 44-D — Software and dependency map (`SW/OC/CI/PR`)

Build a function-by-function dependency matrix:

Function | works glasses-only | requires phone | requires vendor app | requires account | requires internet | requires vendor cloud | third-party/local path tested | evidence

Functions include every major capability claimed or observed.

Also record app permissions requested vs granted; behavior when optional permissions are denied; network destinations observed during defined actions where testing is performed; offline behavior; logout/account-loss behavior; export/delete controls; subscription/paywall dependencies; and update behavior.

Network observation proves observed traffic, not absence of all possible traffic.

## Section 44-E — Owner-control challenge tests (`OC/CI/HK`)

Defined challenges should include where applicable:
- use core hardware after blocking internet;
- use after vendor app is force-stopped;
- retrieve owner-created media without vendor cloud;
- retrieve media without vendor app through a demonstrated alternative path;
- pair/re-pair after app removal where safe;
- deny nonessential permissions and retest;
- export data in ordinary files/formats;
- use documented/community alternative companion software when evidence and safety justify it;
- recover from reset using owner-accessible procedures.

Each challenge records PASS/FAIL/BLOCKED and exactly what that result establishes. Failure of one method does not prove impossibility of all methods.

## Section 44-F — Camera and visual-AI characterization (`VA`)

When applicable, preserve original files and metadata.

Controlled camera set: resolution/mode inventory; close printed text at defined distance; indoor static scene; outdoor daylight; high-contrast scene; moving subject; low-light scene; capture latency; repeat capture reliability; stabilization comparison if claimed; microphone with video; file metadata/codec/container; transfer time for defined file.

Visual-AI tests preserve the actual input, prompt, output, latency and expected/known answer where accuracy is evaluated. Separate on-device, phone-mediated and cloud-mediated processing only when evidence establishes the boundary.

## Section 44-G — Display/optics characterization (`DP`)

When applicable record optical architecture claimed/established; monocular/binocular; correction configuration; known evaluator PD/IPD if voluntarily measured for reproducibility; fit position; content source; resolution/FOV/brightness as MEASURED versus CLAIMED.

Tests should cover:
- text readability using standardized test content;
- usable display area and clipping;
- eyebox/fit tolerance;
- brightness/readability under recorded ambient conditions;
- color/uniformity/artifacts;
- binocular alignment where applicable;
- transparency interference with phone, monitor, window, point light and representative real-world scene;
- frontal/bystander light leakage under defined conditions;
- display latency where measurable;
- prolonged visual comfort through GREP-46 sessions.

Instrument values require instrument/method identification. Until a controlled optical rig exists, observations remain observations rather than pseudo-precision.

## Section 44-H — Audio characterization (`AU`)

Where equipment permits: repeatable playback content; defined wearer listening positions/levels; call receive/transmit samples; leakage observations/measurements at defined distances; quiet/background/wind trials; latency where relevant; simultaneous/multipoint behavior; interaction with other Bluetooth audio devices. Preserve samples where privacy permits.

## Section 44-I — Privacy/security observations (`PR`)

This is evidence collection, not a penetration test by default. Record camera/microphone indicators versus actual activation; unexpected activation; permission behavior; local storage accessibility; encryption/authentication claims only when established; network behavior under defined actions; reset/data-removal behavior; pairing exposure; and security/update documentation.

Potential vulnerabilities become separate responsible research; GREP-44 must not encourage bypassing access controls or destructive exploitation merely to complete a checkbox.

## Section 44-J — Serviceability and physical architecture (`SV/HW`)

Without destructive teardown: lens/removable insert paths; charging accessory replaceability; consumables; screws/fasteners; replaceable nose pads/temples where documented; manufacturer repair route; battery service claim; reset/recovery; firmware support; parts availability.

Optional teardown is a separately authorized annex. A GREP-44 can be complete without teardown. If teardown occurs, record pre-teardown baseline, disassembly sequence, component markings, board/battery/camera/display identification, damage, reassembly and post-test state.

## Section 44-K — Longitudinal evaluation (`WR/UC/VL`)

Attach/carry forward GREP-46 sessions. For owned devices, target enough time to expose novelty decay and reliability patterns rather than a predetermined flattering duration. Record cumulative wear hours, days, charging cycles where known, firmware changes, failures, and use cases abandoned or adopted.

## Section 44-L — Claim reconciliation

For each material manufacturer/vendor claim encountered during evaluation, classify:
- independently verified hands-on;
- consistent with observation but not verified;
- primary-source claim only;
- commercial/seller claim only;
- contradicted/disproven by defined test;
- not tested;
- not testable with current equipment.

Do not create a requirement to test every marketing sentence. Prioritize claims that materially affect purchase decisions or Report Card categories.

## Section 44-M — Completion and Report Card handoff

Produce a coverage matrix for Hardware, Wearability, Visual AI, Software, Openness, Owner Control, Cloud Independence, Hackability and Value. For each category record evidence IDs, evidence lanes, applicable tests completed, unresolved questions, and whether evidence is sufficient for a score or requires UNKNOWN/insufficient-evidence treatment.

Record total test sessions, evaluation span, wear hours, artifacts, configuration checkpoints, blocked tests, N/A tests, and whether teardown occurred.

The examiner does not write scores onto GREP-44. The Report Card process consumes this evidence after the examination is closed or at an explicitly labeled interim checkpoint.