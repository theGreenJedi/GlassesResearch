# Community watch execution receipts and recovery

This protocol distinguishes ChatGPT message-stream failure from GitHub/research failure. It does not expose or repair OpenAI scheduler internals.

## Required workflow
1. Assign a UTC run ID. Inspect relevant source evidence, target file, and recent commits.
2. Record material findings with canonical public URL, provenance (upstream code / community report / independent verification), and disposition. No material finding means no speculative write.
3. Fetch the target file and blob SHA; search for a stable evidence key (source URL or upstream commit SHA) before writing.
4. Commit authorized changes; capture commit SHA; **fetch again** and verify evidence key present.
5. After an ambiguous tool or message-stream failure, **read the repository before retrying**. If the key is present, treat the operation as completed; never duplicate. If absent, refresh SHA and retry once. Record exact available error, not a guessed root cause.
6. Check repository commit, deployment and live publication separately.
7. Record unresolved material failures using the schema below in a subsequent verified write; do not claim failed writes persisted.

## Receipt schema
```text
run_id: UTC time/task
step: discovery | evaluate | fetch | write | readback | deploy | live | notify
source_key: canonical public URL or upstream SHA
status: complete | no-change | failed | unknown | recovered
attempted_action: exact operation
error: verbatim available message or unavailable
commit_sha: actual SHA or none
readback: verified | absent | not-attempted
retry: none | succeeded | failed | not-safe
impact: completed and outstanding work
human_authority_required: yes | no
```

## Observed boundary, October 22, 2026
- User screenshots show ChatGPT Android **Error in message stream** while public-web/GitHub work was underway. These establish a response-stream symptom, not the root cause.
- A CyanBridge network-map finding was committed at [8d6c1b6](https://github.com/theGreenJedi/GlassesResearch/commit/8d6c1b6cc9134d0c3f9f73f478af06df099aeee7) and successfully fetched back. Underlying GitHub work therefore completed despite the visible stream error.
- The scheduler's internal error trace is unavailable. Unattended reliability is not yet demonstrated.

## Acceptance test
Perform an actual read/commit/readback cycle, then independently check that the same evidence key causes a no-op on a repeat run. Compare with subsequent scheduled runs; a task's last-run timestamp alone is not evidence of successful work.
