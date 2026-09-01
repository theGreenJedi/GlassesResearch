# Approved Newsroom Publication Packages

This directory is the repository-side handoff from the live `glasses-news` Editorial Desk into canonical GlassesResearch work.

A package appears here only after:

1. the Scout discovered a source;
2. a human editor approved the discovery for semantic News Desk processing;
3. the News Desk produced structured claims/routes;
4. a human editor approved the resulting promotion package at the second publication gate; and
5. the credentialless repository intake workflow pulled that approved package from the public read-only newsroom queue.

**A package in this directory is not, by itself, a published fact.** It is an authorized publication input. Canonical research changes still have to be mapped to the exact repository destinations, validated by the existing evidence/promotion checks, and merged through the normal repository process.

This boundary is intentional: `glasses-news` never receives a GitHub write credential. GlassesResearch pulls approved packages using its own GitHub Actions identity instead.
