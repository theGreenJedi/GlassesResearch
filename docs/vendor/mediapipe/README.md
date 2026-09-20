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
