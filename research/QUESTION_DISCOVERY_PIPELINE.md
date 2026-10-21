# Question Discovery and Answer Pipeline

## Mission and floor

**Discover real questions about GlassesResearch subject matter anywhere on the public internet, research them, and keep publishing answers. At least 1,000 evidence-backed *published* answers is the minimum milestone. There is no upper limit.**

An internet user's question is eligible even if GlassesResearch has **zero Google impressions or clicks**. Relevance to smart/AI/AR glasses, wearable augmentation, accessibility, owner control, hardware, privacy, firmware, protocols, research and adjacent scoped subjects is the admission test—not our own search performance. Questions need not be popular to qualify. Do not manufacture questions merely to reach the target.

## Discovery: independent first, Search Console supplemental

Daily source configuration is retained in `research/question-sources.json`. The scheduled question-discovery job searches:

- Public GitHub issues across repositories other than GlassesResearch, preserving the issue URL and engagement signals.
- Stack Exchange communities for real user questions, preserving the post URL, score, and answer count.
- Relevant public Reddit RSS discussions, preserving the original thread URL.
- Additional editor-approved external JSON question feeds.
- Google Search Console as a *supplemental site performance sensor*, **not the discovery boundary**.

One inaccessible source must not be silently represented as success. Source-level health is reported in `analytics/question-discovery.md`. If no independent internet source works, discovery should fail visibly instead of recording a misleading clean run. Respect API policies, rate limits and source permissions. An extracted question is **not** evidence that its phrasing or implied claims are correct.

## Relevance before volume

Search hits are not necessarily questions about glasses. Reject generic full-text results, link dumps, markdown fragments, boilerplate issue templates and unrelated search matches. Use an explicit glasses/model match in GitHub issue titles or a relevant hardware project, and require additional issue-body questions to be topically self-contained. Stack Exchange title/tags must actually match the topic; Reddit question extraction uses the author's post title, not HTML image links or cross-posted article excerpts. Reject false positives before writing to the canonical registry. Candidate counts must not be inflated to approach 1,000.

## Normalization, deduplication and prioritization

`research/questions/registry.json` owns stable `Q-######` identifiers, source URLs, original language/variants, lifecycle state, first and last observations, and canonical published URLs.

- Merge repeated crawls of the same source URL; do not claim those are new demand.
- Avoid publishing SEO duplicates. Genuine different questions remain separate.
- Prioritize research using independent mentions, cross-source observations and relevant community signals; Search Console clicks are **not** a research eligibility test.
- Include low-frequency, high-value questions on offline use, accessibility, safety, openness and ownership.
- Report separately: **published answers**, **unanswered research candidates**, **new questions**, **the remaining count to 1,000**, and per-source health. The size of the registry must never be reported as the number of answered questions.

## Answer production

`observed → triaged → researching → answered`

Discovery must feed an ongoing evidence/research/publication loop rather than terminate at a candidate list. Before publishing:

1. Find direct source documentation, dated manufacturer claims, regulatory material, independent evidence and relevant firsthand results.
2. Verify the actual answer and preserve provenance. Contradictory evidence must be explained or marked disputed; unknowns stay unknown.
3. Publish the answer in the appropriate Practical Answers topic with the source links and limitations clearly visible.
4. Mark the registry entry `answered` **only after** a live answer URL exists and the content meets the editorial standard; preserve the record for correction/updates.
5. Measure the published Q&A cohort's impressions, clicks, CTR and rankings. This analytics feedback must not restrict discovery.

The automatic *discovery and research-queue* stages are implemented. Automatic fact research/answer authoring and evidence-gated publication **remain a separate implementation dependency**; the daily discovery job must never fabricate an answer or set `answered` merely to improve a number. A future automated publishing actuator must verify cited source/evidence state, apply editorial/verification gates, and route disputes or insufficient evidence for review. This distinction is part of the public accuracy contract, not a reason to abandon the publishing objective.

## Governance

Automation may collect, normalize, deduplicate, prioritize and prepare research without repeatedly asking for approval. Fully verified, policy-bounded routine content can eventually be published automatically under a separately tested evidence gate. Escalate only irreducible uncertainty, policy changes or disputes; never lower evidence standards to hit the 1,000 minimum. Keep working after 1,000.
