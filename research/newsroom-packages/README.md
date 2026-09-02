# Authorized Newsroom Draft Packages

This directory is the repository-side handoff from the live `glasses-news` Editorial Desk into canonical GlassesResearch work.

A package appears here only after:

1. the Scout discovered a source;
2. a human editor chose `Investigate & draft`, authorizing bounded News Desk/research work on that discovery;
3. the News Desk produced structured claims/routes and ordinary non-escalated draftable routes entered the machine-prepared repository queue; and
4. the repository intake workflow authenticated to the newsroom with a short-lived GitHub Actions OIDC identity and pulled the authorized package.

There is no routine second human publication click in this path. The explicit Editorial approval starts the research/draft pipeline; the resulting GlassesResearch pull request is the normal human decision point for canonical publication. Exception/escalation paths may still require additional judgment, but ordinary evidence-backed work should not.

**A package in this directory is not, by itself, a published fact.** It is an authorized draft input. Canonical research changes still have to be mapped to the exact repository destinations, validated by the existing evidence/promotion checks, and merged through the normal repository process.

Historical package envelopes retain the machine state token `second_gate_approved`. That string is a compatibility contract for already-ingested packages and existing actuators, not a description of the current operator flow. Renaming it would create needless migration risk, so current prose and UI should describe the actual one-Editorial-approval model while the persisted token remains stable.

This boundary is intentional: `glasses-news` never receives a GitHub write credential, and unpublished authorized packages are not exposed through an anonymous public feed. GlassesResearch proves its repository/workflow identity with a short-lived GitHub OIDC token; no long-lived shared secret is stored for this handoff.
