# Deployment integrity contract

The public site is considered successfully deployed only when production proves that it is serving the exact Git commit that triggered the Pages deployment.

The Pages workflow writes two provenance artifacts into every built site:

- `/deployment.json` — machine-readable repository, ref, workflow run, event, and commit SHA
- `/deployment.txt` — the deployed commit SHA alone

After GitHub Pages deploys, the workflow fetches `https://glassesresearch.org/deployment.json` with cache-busting and no-cache request headers and requires its `sha` to equal `GITHUB_SHA` for that deployment run.

The same post-deploy gate also smoke-tests high-value visitor-facing surfaces that previously exposed stale-deployment ambiguity, including Finder capability wording, the Reference Desk, citation exports, and embeddable model-card assets.

A successful build is not sufficient. A successful deployment requires the live-domain SHA match and feature smoke tests to pass.
