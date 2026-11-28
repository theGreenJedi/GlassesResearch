"""Gate tests for offline-only outreach; no external requests or posting."""
import unittest

from scripts.build_outreach_drafts import (
    validate_candidates, validate_drafts, validate_reply_reviews, render_packets,
    REQUIRED_CHECKS,
)


SRC = "https://www.reddit.com/r/SmartGlasses/comments/abc/question/"
ANSWER = "https://glassesresearch.org/docs/faq/04-battery/#battery-claims"
CANDIDATE = {
    "source_url": SRC, "platform": "Reddit", "last_observed": "2026-11-06",
    "questions": [{"id": "Q-42", "question": "How long does the battery last?",
                   "answer_url": ANSWER}],
}


def candidate_approval():
    record = {
        "source_url": SRC, "decision": "approved_for_drafting",
        "reviewer": "human reviewer", "reviewed_at": "2026-11-06",
        "notes": "Original question and rules manually checked.",
    }
    record.update({field: True for field in REQUIRED_CHECKS})
    return record


def proposed_reply():
    return {
        "source_url": SRC, "answer_url": ANSWER, "author": "research editor",
        "reply_body": "The test workload matters. A useful comparison specifies audio/camera mode and test conditions.",
    }


class DryRunGateTests(unittest.TestCase):
    def test_gate_closed_by_default(self):
        decisions = validate_candidates({"schema_version": 1, "entries": []}, [CANDIDATE])
        self.assertEqual(decisions, {})
        self.assertEqual(validate_drafts({"schema_version": 1, "entries": []}, {}, [CANDIDATE]), {})
        result = render_packets([CANDIDATE], {}, {}, {})
        self.assertIn("awaiting candidate review", result)
        self.assertIn("Platform replies sent: **0**", result)
        self.assertNotIn("test workload matters", result)

    def test_explicit_approval_required_and_validated(self):
        x = candidate_approval()
        x["community_rules_reviewed"] = False
        with self.assertRaisesRegex(ValueError, "six manual checks"):
            validate_candidates({"schema_version": 1, "entries": [x]}, [CANDIDATE])
        x = candidate_approval()
        decisions = validate_candidates({"schema_version": 1, "entries": [x]}, [CANDIDATE])
        self.assertEqual(decisions[SRC]["decision"], "approved_for_drafting")

    def test_held_candidate_cannot_be_drafted(self):
        decisions = validate_candidates(
            {"schema_version": 1, "entries": [{"source_url": SRC, "decision": "hold"}]},
            [CANDIDATE],
        )
        with self.assertRaisesRegex(ValueError, "approved"):
            validate_drafts({"schema_version": 1, "entries": [proposed_reply()]}, {}, [CANDIDATE])
        self.assertEqual(decisions[SRC]["decision"], "hold")

    def test_draft_requires_approved_match_and_nonempty_body(self):
        approved = {SRC: candidate_approval()}
        item = proposed_reply()
        item["answer_url"] = "https://glassesresearch.org/not-our-answer"
        with self.assertRaisesRegex(ValueError, "original approved answer"):
            validate_drafts({"schema_version": 1, "entries": [item]}, approved, [CANDIDATE])
        item = proposed_reply()
        item["reply_body"] = "   "
        with self.assertRaisesRegex(ValueError, "nonempty"):
            validate_drafts({"schema_version": 1, "entries": [item]}, approved, [CANDIDATE])
        drafts = validate_drafts({"schema_version": 1, "entries": [proposed_reply()]}, approved, [CANDIDATE])
        self.assertIn(SRC, drafts)
        packet = render_packets([CANDIDATE], approved, drafts, {})
        self.assertIn("The test workload matters", packet)
        self.assertIn("NOT FOR POSTING", packet)

    def test_stage_two_never_allows_posting(self):
        drafts = {SRC: proposed_reply()}
        with self.assertRaisesRegex(ValueError, "no posting"):
            validate_reply_reviews(
                {"schema_version": 1, "entries": [{"source_url": SRC, "decision": "posted"}]}, drafts
            )
        reviews = validate_reply_reviews(
            {"schema_version": 1, "entries": [{
                "source_url": SRC, "decision": "accepted_for_dry_run_only",
                "reviewer": "editor", "reviewed_at": "2026-11-06",
            }]}, drafts)
        self.assertEqual(reviews[SRC]["decision"], "accepted_for_dry_run_only")

    def test_duplicate_or_unrecognized_candidate_rejected(self):
        x = candidate_approval()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_candidates({"schema_version": 1, "entries": [x, x]}, [CANDIDATE])
        with self.assertRaisesRegex(ValueError, "unknown"):
            validate_candidates(
                {"schema_version": 1, "entries": [{**x, "source_url": "https://reddit.com/unknown"}]}, [CANDIDATE]
            )


if __name__ == "__main__":
    unittest.main()
