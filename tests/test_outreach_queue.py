"""Tests for review-only community outreach candidate preparation."""
import unittest
from scripts.build_outreach_queue import build_candidates, render_markdown


class QueueTests(unittest.TestCase):
    def test_groups_discussions_and_ignores_unpublished(self):
        src = "https://www.reddit.com/r/SmartGlasses/comments/abc/question/"
        registry = {"questions": [
            {"id": "Q-1", "status": "answered", "evidence_state": "published",
             "canonical_question": "A?", "last_observed": "2026-11-01", "answer_url": "/docs/faq/a/#a",
             "observations": [{"source": "reddit_rss", "source_url": src}]},
            {"id": "Q-2", "status": "answered", "evidence_state": "published",
             "canonical_question": "B?", "last_observed": "2026-11-02", "answer_url": "/docs/faq/b/#b",
             "observations": [{"source": "reddit_rss", "source_url": src}]},
            {"id": "Q-3", "status": "observed", "evidence_state": "unresearched",
             "answer_url": None, "observations": [{"source": "reddit_rss", "source_url": "https://reddit.com/r/SmartGlasses/comments/xyz"}]},
        ]}
        result = build_candidates(registry)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]["questions"]), 2)
        self.assertIn("DRAFT CANDIDATES ONLY", render_markdown(result, 15))
        self.assertEqual(build_candidates(registry, {"entries": [{"source_url": src, "status": "posted"}]}), [])

    def test_only_allowed_external_hosts_and_local_answers(self):
        registry = {"questions": [
            {"id": "Q-1", "status": "answered", "evidence_state": "published",
             "answer_url": "//untrusted.example", "observations": [{"source": "reddit_rss", "source_url": "https://reddit.com/r/a/comments/b"}]},
            {"id": "Q-2", "status": "answered", "evidence_state": "published",
             "answer_url": "/docs/faq/a", "observations": [{"source": "reddit_rss", "source_url": "https://reddit.com.evil.test/a"}]},
        ]}
        self.assertEqual(build_candidates(registry), [])


if __name__ == "__main__":
    unittest.main()
