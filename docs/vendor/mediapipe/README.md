# Virtual try-on runtime

This directory is the publication boundary for the browser-local face-tracking runtime.

The public try-on must not fetch its tracking JavaScript, WASM, model weights, camera frames, landmarks, or derived geometry from third-party hosts. Before any model's `try_on_asset` is published, this directory must contain the pinned, reviewed runtime files referenced by `docs/javascripts/model-try-on.js`:

- `vision_bundle.mjs`
- `wasm/` runtime files
- `face_landmarker.task`

## Privacy contract

Camera permission is requested only after the visitor chooses **View these glasses on my face**. Audio is never requested. Camera frames and landmarks remain on the visitor's device. Closing the dialog stops all camera tracks.

## Product boundary

Try-on is a visual appearance preview. It must not claim optical, prescription, bridge, temple, pupillary-distance, or physical fit accuracy unless a later calibrated fitting method is independently validated.

## Dependency publication gate

Do not copy third-party runtime files into this repository until their exact version, upstream source, license, integrity hash, and redistribution basis have been recorded. Until then, model try-on assets remain unpublished and no visitor is offered a broken or privacy-weakened try-on button.


## Publication hold — telemetry and artifact provenance

**Do not publish this runtime yet.** Current upstream MediaPipe privacy documentation states that MediaPipe Tasks sends performance and utilization metrics to Google and places informed-consent responsibilities on the integrating application. That conflicts with GlassesResearch's no-tracking requirement for camera activation unless a specific Web build can be independently verified to make no third-party requests.

Self-hosting the JavaScript, WASM, and task model is therefore necessary but not sufficient.

Before this directory may contain an enabled production runtime, record and verify all of the following:

1. exact Web package/runtime version and immutable upstream source;
2. exact model artifact provenance and redistribution basis;
3. SHA-256 hashes for every shipped JS/WASM/model artifact;
4. a network test demonstrating zero third-party requests during initialization, camera use, tracking, and shutdown;
5. the license notices required for redistribution;
6. an explicit GlassesResearch approval record naming the tested artifacts and date.

If the stock Web runtime cannot meet the zero-third-party-request requirement, use a different locally executed landmark implementation or a reproducible telemetry-free build. Do not weaken the site's privacy promise to accommodate the library.
