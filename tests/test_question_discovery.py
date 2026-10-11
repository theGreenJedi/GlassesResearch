"""Regression tests for the published Practical Answers registry seed."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import question_discovery as discovery


class QuestionDiscoveryTests(unittest.TestCase):
    def test_seed_real_published_answers(self):
        registry = {"next_id": 1, "questions": []}
        result = discovery.seed_published_answers(registry)
        self.assertGreaterEqual(len(result["questions"]), 100)
        self.assertTrue(all(q["answer_url"] and q["status"] == "answered" for q in result["questions"]))
        self.assertEqual(len(result["questions"]), len(discovery.seed_published_answers(result)["questions"]))

    def test_existing_question_link_and_numbered_heading(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "01-basics.md").write_text(
                "## 1. What are smart glasses?\n\nAn answer.\n\n"
                "## 2. Can smart glasses work offline?\n\nAnother answer.\n"
            )
            original = discovery.FAQ_ROOT
            discovery.FAQ_ROOT = root
            try:
                existing = {
                    "next_id": 2,
                    "questions": [{
                        "id": "Q-000001", "normalized": discovery.norm("What are smart glasses?"),
                        "canonical_question": "What are smart glasses?",
                        "status": "observed", "evidence_state": "unresearched",
                        "answer_url": None,
                    }]
                }
                result = discovery.seed_published_answers(existing)
                self.assertEqual(len(result["questions"]), 2)
                first, second = result["questions"]
                self.assertEqual(first["answer_url"], "/docs/faq/01-basics/#1-what-are-smart-glasses")
                self.assertEqual(first["status"], "answered")
                self.assertEqual(first["evidence_state"], "published")
                self.assertEqual(second["answer_url"], "/docs/faq/01-basics/#2-can-smart-glasses-work-offline")
            finally:
                discovery.FAQ_ROOT = original


if __name__ == "__main__":
    unittest.main()
