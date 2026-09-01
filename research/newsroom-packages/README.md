# Approved Newsroom Publication Packages

This directory is the repository-side handoff from the live `glasses-news` Editorial Desk into canonical GlassesResearch work.

A package appears here only after:

1. the Scout discovered a source;
2. a human editor approved the discovery for semantic News Desk processing;
3. the News Desk produced structured claims/routes;
4. a human editor approved the resulting promotion package at the second publication gate; and
5. the repository intake workflow authenticated to the newsroom with a short-lived GitHub Actions OIDC identity and pulled the approved package.

**A package in this directory is not, by itself, a published fact.** It is an authorized publication input. Canonical research changes still have to be mapped to the exact repository destinations, validated by the existing evidence/promotion checks, and merged through the normal repository process.

This boundary is intentional: `glasses-news` never receives a GitHub write credential, and unpublished approved packages are not exposed through an anonymous public feed. GlassesResearch proves its repository/workflow identity with a short-lived GitHub OIDC token; no long-lived shared secret is stored for this handoff.
