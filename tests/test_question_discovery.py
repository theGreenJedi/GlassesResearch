"""Regression tests for the published Practical Answers registry seed."""
import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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


    def test_existing_registry_does_not_autocredit_new_unverified_faq(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            faq = root / "faq"
            faq.mkdir()
            (faq / "09-development-openness.md").write_text(
                "## Can an observed new glasses question be answered?\n\n"
                "An evidence-qualified draft awaiting production proof.\n\n"
                "## Can a separate new question be answered?\n\n"
                "Another unpublished draft.\n"
            )
            registry_path = root / "registry.json"
            original = {
                "next_id": 2,
                "questions": [{
                    "id": "Q-000001",
                    "normalized": discovery.norm(
                        "Can an observed new glasses question be answered?"
                    ),
                    "canonical_question": "Can an observed new glasses question be answered?",
                    "status": "observed",
                    "answer_url": None,
                    "evidence_state": "unresearched",
                }],
            }
            registry_path.write_text(json.dumps(original), encoding="utf-8")
            with patch.object(discovery, "REGISTRY", registry_path), \
                 patch.object(discovery, "FAQ_ROOT", faq):
                loaded = discovery.load_registry()
            self.assertEqual(loaded, original)
            self.assertEqual(loaded["questions"][0]["status"], "observed")
            self.assertIsNone(loaded["questions"][0]["answer_url"])
            self.assertEqual(loaded["next_id"], 2)

    def test_nested_practical_answers_are_seeded_once(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "09-development-openness.md").write_text(
                "## Veyra practical answers\n\n"
                "### 1. What is Veyra?\n\nA clear answer.\n\n"
                "### 2. Is Veyra open source?\n\nA second answer.\n"
            )
            with patch.object(discovery, "FAQ_ROOT", root):
                result = discovery.seed_published_answers({"next_id": 1, "questions": []})
                self.assertEqual(len(result["questions"]), 2)
                self.assertEqual(
                    result["questions"][0]["answer_url"],
                    "/docs/faq/09-development-openness/#1-what-is-veyra",
                )
                self.assertEqual(len(discovery.seed_published_answers(result)["questions"]), 2)

    def test_nested_faq_search_metadata_covers_each_answer(self):
        import seo_hook
        markup = (
            "## Veyra practical answers\n\n"
            "### 1. What is Veyra?\n\nFirst answer.\n\n"
            "### 2. Is it open source?\n\nSecond answer.\n\n"
            "## Another topic\n\nUnrelated text.\n"
        )
        schema = json.loads(seo_hook._faq_schema(markup, "https://example.org/faq/"))
        self.assertEqual([entity["name"] for entity in schema["mainEntity"]],
                         ["What is Veyra?", "Is it open source?"])
        self.assertEqual([entity["acceptedAnswer"]["text"] for entity in schema["mainEntity"]],
                         ["First answer.", "Second answer."])

    def test_question_scoped_vs_site_traffic(self):
        self.assertTrue(discovery.looks_like_question("Can I use this pair offline?", scoped=True))
        self.assertFalse(discovery.looks_like_question("Can I use this pair offline?"))
        self.assertTrue(discovery.looks_like_question("Can smart glasses work without internet?"))
        self.assertFalse(discovery.looks_like_question("Best summer vacation deals?"))

    def test_independent_observations_dont_multiply_on_recrawl(self):
        reg = {"next_id": 1, "questions": []}
        observed = {
            "question": "Can smart glasses work offline?", "source": "github_issues",
            "source_url": "https://github.com/elsewhere/project/issues/12",
            "observed_at": "2026-10-21",
        }
        self.assertEqual(len(discovery.reconcile(reg, [observed, observed])), 1)
        self.assertEqual(len(reg["questions"]), 1)
        self.assertEqual(len(reg["questions"][0]["observations"]), 1)
        reobserved = {**observed, "observed_at": "2026-10-22"}
        self.assertEqual(len(discovery.reconcile(reg, [reobserved])), 0)
        self.assertEqual(len(reg["questions"][0]["observations"]), 1)
        independent = {**observed, "source": "stackexchange", "source_url": "https://stackoverflow.com/q/15"}
        discovery.reconcile(reg, [independent])
        self.assertEqual(len(reg["questions"]), 1)
        self.assertEqual(len(reg["questions"][0]["observations"]), 2)

    def test_github_external_question_has_original_url(self):
        class Reply:
            def raise_for_status(self):
                pass
            def json(self):
                return {"items": [{
                    "title": "Can smart glasses run without internet?",
                    "body": "I need to know before buying.",
                    "html_url": "https://github.com/other/glasses/issues/8",
                    "comments": 5,
                }]}
        with patch.object(discovery.requests, "get", return_value=Reply()) as get:
            rows = discovery.github_questions(['"smart glasses"'])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_url"], "https://github.com/other/glasses/issues/8")
        self.assertIn("-repo:theGreenJedi/GlassesResearch", get.call_args.kwargs["params"]["q"])

    def test_stackexchange_questions_do_not_need_a_trailing_question_mark(self):
        class Reply:
            def raise_for_status(self):
                pass
            def json(self):
                return {"items": [{
                    "title": "How to interface a microcontroller with smart glasses",
                    "link": "https://electronics.stackexchange.com/q/12",
                    "score": 3,
                }]}
        with patch.object(discovery.requests, "get", return_value=Reply()):
            rows = discovery.stackexchange_questions([{"site": "electronics", "q": "smart glasses"}])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["metrics"]["score"], 3)

    def test_discovery_continues_without_search_console(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            (folder / "faq").mkdir()
            (folder / "faq" / "01-basics.md").write_text("## What are smart glasses?\n\nSmart glasses are worn on the face.\n")
            (folder / "sources.json").write_text(json.dumps({
                "github_queries": ["smart glasses"], "stackexchange": [],
                "reddit_rss": [],
            }))
            question = {
                "question": "Can smart glasses be used offline?", "source": "github_issues",
                "source_url": "https://github.com/other/device/issues/1",
                "observed_at": "2026-10-21",
            }
            with patch.object(discovery, "REGISTRY", folder / "registry.json"), \
                 patch.object(discovery, "FAQ_ROOT", folder / "faq"), \
                 patch.object(discovery, "SOURCES", folder / "sources.json"), \
                 patch.object(discovery, "REPORT_JSON", folder / "report.json"), \
                 patch.object(discovery, "REPORT_MD", folder / "report.md"), \
                 patch.object(discovery, "github_questions", return_value=[question]), \
                 patch.object(discovery, "stackexchange_questions", return_value=[]), \
                 patch.object(discovery, "reddit_rss_questions", side_effect=RuntimeError("RSS unavailable")), \
                 patch.object(discovery, "gsc_questions", side_effect=RuntimeError("GSC unavailable")), \
                 patch.object(discovery, "external_questions", return_value=[]):
                self.assertEqual(discovery.main(), 0)
            report = json.loads((folder / "report.json").read_text())
            self.assertEqual(report["new_questions"], 1)
            self.assertEqual(report["published_answers"], 1)
            self.assertEqual(report["minimum_published_answers"], 1000)
            self.assertEqual(report["remaining_to_minimum"], 999)
            self.assertEqual(report["sources"]["google_search_console"]["status"], "unavailable")
            self.assertEqual(report["research_queue"][0]["source_urls"], [question["source_url"]])
            self.assertEqual(sum(q["status"] == "answered" for q in json.loads((folder / "registry.json").read_text())["questions"]), 1)

    def test_no_external_sources_fails_visible(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            (folder / "faq").mkdir()
            (folder / "sources.json").write_text(json.dumps({
                "github_queries": [], "stackexchange": [], "reddit_rss": [],
            }))
            with patch.object(discovery, "REGISTRY", folder / "registry.json"), \
                 patch.object(discovery, "FAQ_ROOT", folder / "faq"), \
                 patch.object(discovery, "SOURCES", folder / "sources.json"), \
                 patch.object(discovery, "REPORT_JSON", folder / "report.json"), \
                 patch.object(discovery, "REPORT_MD", folder / "report.md"), \
                 patch.object(discovery, "github_questions", side_effect=RuntimeError("off")), \
                 patch.object(discovery, "stackexchange_questions", side_effect=RuntimeError("off")), \
                 patch.object(discovery, "reddit_rss_questions", side_effect=RuntimeError("off")), \
                 patch.object(discovery, "gsc_questions", return_value=[]), \
                 patch.object(discovery, "external_questions", return_value=[]):
                with self.assertRaisesRegex(RuntimeError, "No independent internet question sources"):
                    discovery.main()
            self.assertFalse((folder / "report.json").exists())



    def test_discard_unrelated_questions_from_fulltext_issue_hit(self):
        class Reply:
            def raise_for_status(self):
                pass
            def json(self):
                return {"items": [{
                    "title": "Ask HN: How do I build a search website?",
                    "body": "One of my bookmarks mentions smart glasses. How is the weather today?",
                    "html_url": "https://github.com/other/not-glasses/issues/3",
                }]}
        with patch.object(discovery.requests, "get", return_value=Reply()):
            self.assertEqual(discovery.github_questions(['"smart glasses"']), [])

    def test_keep_scoped_product_repository_questions(self):
        class Reply:
            def raise_for_status(self):
                pass
            def json(self):
                return {"items": [{
                    "title": "Can developers add display support?",
                    "body": "What makes MentraOS glasses drop the stream?",
                    "html_url": "https://github.com/Mentra-Community/MentraOS/issues/42",
                }]}
        with patch.object(discovery.requests, "get", return_value=Reply()):
            rows = discovery.github_questions(["MentraOS"])
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(r["source_url"].endswith("/issues/42") for r in rows))

    def test_stackexchange_fulltext_query_cannot_launder_offtopic_title(self):
        class Reply:
            def raise_for_status(self):
                pass
            def json(self):
                return {"items": [{
                    "title": "Why does my Python array raise IndexError?",
                    "link": "https://stackoverflow.com/q/22", "tags": ["python"],
                }]}
        with patch.object(discovery.requests, "get", return_value=Reply()):
            rows = discovery.stackexchange_questions([{"site": "stackoverflow", "q": "smart glasses"}])
        self.assertEqual(rows, [])

    def test_reddit_only_extracts_actual_post_title_question(self):
        rss = """<feed xmlns="http://www.w3.org/2005/Atom"><entry>
        <title>Are smart glasses comfortable all day?</title>
        <link href="https://www.reddit.com/r/SmartGlasses/comments/abc/topic"/>
        <content type="html">&lt;a href="https://images.example.com/photos?width=640"&gt;
        unrelated link title="How can I repair my washing machine?"&lt;/a&gt;</content>
        </entry></feed>"""
        class Reply:
            text = rss
            def raise_for_status(self):
                pass
        with patch.object(discovery.requests, "get", return_value=Reply()):
            rows = discovery.reddit_rss_questions(["https://www.reddit.com/r/SmartGlasses/new/.rss"])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["question"], "Are smart glasses comfortable all day?")


if __name__ == "__main__":
    unittest.main()
