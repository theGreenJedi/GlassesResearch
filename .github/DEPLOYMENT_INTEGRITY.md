# Deployment integrity contract

The public site is considered successfully deployed only when production proves that it is serving the exact Git commit that triggered the Pages deployment.

The Pages workflow writes two provenance artifacts into every built site:

- `/deployment.json` — machine-readable repository, ref, workflow run, event, and commit SHA
- `/deployment.txt` — the deployed commit SHA alone

After GitHub Pages deploys, the workflow fetches `https://glassesresearch.org/deployment.json` with cache-busting and no-cache request headers and requires its `sha` to equal `GITHUB_SHA` for that deployment run.

The same post-deploy gate also smoke-tests high-value visitor-facing surfaces that previously exposed stale-deployment ambiguity, including Finder capability wording, the Reference Desk, citation exports, and embeddable model-card assets.

A successful build is not sufficient. A successful deployment requires the live-domain SHA match and feature smoke tests to pass.

## Public route contract

Reader-facing URLs are an external compatibility surface, not merely a byproduct of current navigation.

`data/public-route-contract.json` records canonical public routes and any compatibility aliases that GlassesResearch promises to preserve. `scripts/public_route_contract.py` validates that registry, installs aliases only after the normal MkDocs discoverability audit, verifies the resulting Pages artifact, and probes the same promises on the live domain.

Canonical routes must remain present in the sitemap. Compatibility aliases must resolve to the same public content while remaining out of the sitemap so search discovery continues to point at the canonical route.

The route contract is checked during Pages builds, after production deployment, by the recurring public-surface smoke test, and by the daily whole-site link review. This separates two different integrity questions: internal-link checks prove that the current site is coherent; the public-route contract proves that previously promised outside-world URLs still work.
