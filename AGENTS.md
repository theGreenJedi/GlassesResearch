# AGENTS.md

## Mission

Every contribution must strengthen GlassesResearch as a comprehensive, model-agnostic knowledge base for the entire smart-glasses ecosystem.

The W610 is the current hands-on reference device, not the boundary of the repository. Preserve useful information about any relevant model whether or not a maintainer owns it.

## Standing engineering directives

1. **Ecosystem-wide scope.** Design indexes, schemas, navigation, and terminology to scale across manufacturers and potentially hundreds of models.
2. **Evidence lanes stay distinct.** Never present externally sourced or inferred information as hands-on verification. Label claims as direct observation, repeated experiment, primary-source statement, commercial claim, community report, inference, hypothesis, disproven, or unknown.
3. **Archive first, organize second.** When lawful and practical, preserve fragile resources before refining taxonomy: firmware, APKs, SDKs, packet captures, protocol notes, model files, manuals, flashing instructions, recovery procedures, tools, repositories, and community posts. Record provenance, retrieval date, hashes, licensing, and redistribution constraints.
4. **Substance before scaffolding.** Do not add empty directories or placeholder-only pages. A new model chapter begins only when it contains useful sourced information.
5. **No orphan knowledge.** Give recurring models, components, organizations, applications, repositories, communities, and standards canonical homes and cross-link them.
6. **Model coverage is cumulative.** Each merge should preserve existing model knowledge and, whenever practical, improve cross-model discovery or add substantive coverage beyond the current hands-on device.
7. **Claims remain revisable.** Preserve corrections and contradictory evidence. Do not silently convert copied marketing claims into confirmation.
8. **Repository-first memory.** Durable project decisions belong in Git, not only in chat history.

## Required pull-request check

Before opening a pull request, state:

- which real research question or preservation need the change addresses;
- which models or ecosystem layers it affects;
- whether each important claim is hands-on, primary-source, community-sourced, or inferred;
- which fragile resources were archived or why only links could be recorded;
- how the change improves future ecosystem-wide work;
- what validation was performed.

## Architecture rule

Use `models/<canonical-model-id>/` for model-specific knowledge and shared catalogs for cross-model discovery. Do not force every model into the W610 chapter shape before evidence warrants it. Add a model to the registry first; create its chapter when real material exists.

## Recurring news and research updates

Follow `docs/news/WORKFLOW.md` for periodic ecosystem sweeps. News is an intake layer, not a substitute for canonical knowledge: material developments must update the release tracker and affected model, glossary, resource, FAQ, or backlog pages in the same pull request when practical.

Never create empty weekly digests. Distinguish announcement, preorder, targeted shipping, confirmed shipping, independent verification, and project hands-on status. Preserve corrections rather than silently rewriting old digests.
