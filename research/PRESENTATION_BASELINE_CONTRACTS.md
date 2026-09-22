# Presentation Mission — WS0 Critical Contracts Baseline

Baseline commit: `50b6267ad6e2e43d68c4c240182816cd53fbe3b2`
Captured: 2026-09-20

This is the regression contract for the presentation mission. Presentation work may change how these systems are exposed, but may not silently remove or weaken them.

| Contract | Baseline source / enforcement |
|---|---|
| Canonical model identity and lifecycle | `models/THE_LIST.md` → `scripts/build_device_database.py`; validates declared count, stable GLS IDs, lifecycle/state, maker/model, evidence and public research paths. |
| Finder comparison data | `scripts/build_comparison_engine.py` plus comparison schema/data. |
| Finder capabilities | `scripts/build_finder_capabilities.py` and capability overrides; preserves explicit unknown semantics and provenance. |
| Report Card scoring | `scripts/build_report_card_scores.py`; Core dimensions plus legacy/extended scores, provenance and unknown semantics. |
| Aliases / lineage | canonical lineage/alias data consumed by generated surfaces and search. |
| Evidence / public dataset | evidence corpus plus public dataset generation and verification in the Pages build. |
| Generated model pages | staged device database → model-page generator; one canonical public page per GLS identity. |
| Internal model links / GLS resolver | generated during `scripts/prepare_site.py`. |
| RSS / follow surfaces | RSS builder plus follow-surface CI and live smoke test. |
| Newsroom / verified research | newsroom state, verified-change surfaces, verified research citations and their validators. |
| Community research/reviews | public community research plus generated review summaries/profiles and intake validation. |
| Internal links/fragments | `scripts/verify_built_site_links.py` after strict MkDocs build. |
| Public reachability | `scripts/verify_public_reachability.py` after build. |
| Search discoverability | `scripts/verify_discoverability.py`. |
| Built JS | Node syntax check over all built JavaScript. |
| Dynamic catalog/public data counts | Pages workflow derives expected counts from built `devices.json`, then reconciles model pages, public model records and citation files. |
| Deployment provenance | Pages workflow stamps `deployment.json` / `deployment.txt` and verifies the SHA. |
| Automation | repository workflows include catalog consistency/admission/discovery, newsroom intake/publication/cleanup, daily news collection/verification, search/wire, archive/Wayback, purchase-link health, daily whole-site links, feeds/follow, Lighthouse, community review, and Pages deployment. |

## Baseline presentation facts

At the baseline, the site used Material for MkDocs and exposed nine primary nav entries. Material features included navigation top/footer and search suggest/highlight. The presentation branch must preserve the contracts above while replacing documentation-oriented public chrome.

## Acceptance evidence still required for WS0

1. Saved baseline built-route inventory containing all generated/public URLs and status.
2. Saved current built-route inventory in the same format.
3. A diff mechanism that feeds the route ledger and can prove no important baseline route became stranded.
