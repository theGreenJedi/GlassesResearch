---
title: "Deployment Provenance"
description: "Machine-verifiable proof of which GlassesResearch commit is currently live."
---

# Deployment provenance

GlassesResearch publishes machine-readable deployment provenance so repository state and live production state can be distinguished without inference.

- [`/deployment.json`](https://glassesresearch.org/deployment.json) reports the exact Git commit SHA and GitHub Actions run that produced the deployed artifact.
- [`/deployment.txt`](https://glassesresearch.org/deployment.txt) contains only the deployed commit SHA.

The production deployment workflow does not declare success merely because the site responds. It requires the live `deployment.json` SHA to equal the commit SHA that triggered the deployment, then verifies current visitor-facing feature surfaces.

This is an operational verification surface, not a substitute for source citations or research provenance.
