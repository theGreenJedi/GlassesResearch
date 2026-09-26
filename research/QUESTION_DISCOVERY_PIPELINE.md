# Question Discovery and Answer Pipeline

GlassesResearch does not choose a quota for questions. The corpus is an observation-driven research product: if people ask ten materially distinct questions, there are ten; if they ask one hundred thousand, the registry can hold one hundred thousand.

## Daily loop

1. **Observe** — collect question-shaped search language from approved sensors. Search Console is the first-party baseline; approved external feeds can extend discovery.
2. **Normalize and deduplicate** — preserve human wording as variants while assigning one stable ID to the underlying question.
3. **Research** — determine what evidence is needed and gather manufacturer, documentary/regulatory, community, and independent evidence under normal GlassesResearch provenance rules.
4. **Answer or abstain** — publish only when the evidence supports an answer. "Unable to verify" is a valid outcome.
5. **Measure** — treat Practical Answers as an analytics cohort: impressions, clicks, CTR, position, answer pages receiving impressions, and the query language that reaches them.
6. **Feed back** — new query wording can become a variant of an existing question or surface a genuinely new question for the next research cycle.

## Canonical registry

`research/questions/registry.json` is the machine-readable source of truth. Each entry receives a stable `Q-######` identifier and records:

- canonical question and observed wording variants
- first/last observation dates and source observations
- research/evidence state
- lifecycle status
- canonical answer URL once published

Discovery never implies truth and never authorizes publication.

## Lifecycle

`observed → triaged → researching → answered`

Other valid states include `duplicate`, `unable_to_verify`, and `out_of_scope`. Duplicate wording should point to the canonical question rather than create SEO-shaped copies.

## Automation boundary

The daily job may automatically discover, normalize, deduplicate, register, and measure questions. It may prepare research work. It must not lower the evidence standard or publish unsupported answers simply because a query exists.

The purpose is not keyword production. The purpose is to notice what people need to know and do the research required to answer it.
