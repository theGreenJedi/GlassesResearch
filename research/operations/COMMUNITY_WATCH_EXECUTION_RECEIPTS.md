# Community watch execution receipts and recovery

## Purpose
A ChatGPT message-stream error is **not** proof that research, a GitHub write, or a site deployment failed. This file defines a durable, inspectable checkpoint convention for community-watch runs. It does not instrument OpenAI's scheduler or expose its internal logs.

## Run procedure
1. Assign a run ID (UTC date/time plus task identifier) and inspect the latest relevant investigation/network file and recent commits before doing any write.
2. Record each material finding with its source URL, observed date, provenance class (upstream code, community claim, independent measurement), and target disposition. No finding means no speculative write.
3. Before an update, fetch the target file and its blob SHA. Check for a stable evidence key (canonical source URL or upstream commit SHA) to avoid duplicates.
4. Commit only authorized evidence-qualified changes. Capture the resulting commit SHA. **Fetch the file again** and verify the evidence key is present. A commit response alone is not a verified read-back.
5. If the tool returns an ambiguous error or the response stream stops, **read the repository before retrying**. If the evidence key exists, mark the operation recovered/already complete; do not commit it again. If absent, refresh the blob SHA and retry once. Escalate only after a confirmed unresolved failure.
6. Distinguish repository commit, site build/deployment, and live public visibility. None implies the others without a corresponding check.
7. For a material failure, append a compact receipt to this file in a subsequent successful write. Do not claim that a receipt survived a failed write without reading it back.

## Receipt schema

```text
run_id: <UTC timestamp/task>
step: discovery | evaluation | fetch | write | readback | deploy | live-check | notify
source_evidence_key: <canonical URL or upstream SHA; omit private data>
status: complete | no-change | failed | unknown | recovered
attempted_action: <exact operation>
error: <verbatim available message, or unavailable>
commit_sha: <actual SHA or none>
readback: verified | absent | not-attempted
retry: none | succeeded | failed | not-safe
impact: <what completed; what remains>
needs_human_authority: yes | no
```

## Known boundary evidence (October 22, 2026)
- ChatGPT Android displayed “Error in message stream” during a public-web/GitHub research sequence. Screenshot is user-provided evidence of **response delivery failure**, not a GitHub error trace.
- The community network map update documenting a CyanBridge public claim was committed as [8d6c1b6cc9134d0c3f9f73f478af06df099aeee7](https://github.com/theGreenJedi/GlassesResearch/commit/8d6c1b6cc9134d0c3f9f73f478af06df099aeee7) and fetched back successfully. This establishes that at least one underlying write completed despite a stream error.
- Root cause of the platform message-stream failure is **unknown**. No scheduler internals, hidden exception trace, or successful unattended end-to-end run are established by this document.

## Acceptance criteria
A direct run demonstrates a persisted evidence key and verified readback; a subsequent run detects that key and avoids a duplicate; an unattended scheduled run independently produces verifiable outcomes. Until then, scheduled reliability remains unproven.
