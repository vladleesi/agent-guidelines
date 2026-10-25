"""Check release selection and publication failure paths without GitHub access."""

import importlib.util
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("guideline_release", ROOT / "scripts/release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)
COMMIT = "a" * 40


class ReleaseTests(unittest.TestCase):
    def test_notes_select_first_entry_and_preserve_format(self):
        text = "# Changelog\n\n## 1.0.1 — 2026-10-25\n\n- Update.\n  More detail.\n\n## 1.0.0 — 2026-10-24\n\n- Old.\n"
        self.assertEqual(("v1.0.1", "- Update.\n  More detail.\n"), release.release_notes(text))

    def test_invalid_or_empty_first_entry_cannot_fall_back_to_an_old_release(self):
        for first in ["", "## Unreleased\n- Pending.", "## 01.0.0 — 2026-10-25\n- Invalid.",
                      "## 1.0.1 — 2026-02-30\n- Invalid.", "## 1.0.1 — 2026-10-25\n"]:
            text = first + "\n## 1.0.0 — 2026-10-24\n- Old.\n" if first else "# Changelog\n"
            with self.subTest(first=first), self.assertRaises(ValueError):
                release.release_notes(text)

    @patch.object(release.subprocess, "run")
    def test_published_release_on_later_page_is_unchanged(self, run):
        run.return_value.stdout = json.dumps([[], [{"tag_name": "v1.0.1", "draft": False}]])
        message = release.publish("v1.0.1", "- Notes.\n", "owner/repo", COMMIT)
        self.assertIn("already published", message)
        self.assertEqual(1, run.call_count)

    @patch.object(release.subprocess, "run")
    def test_draft_requires_review(self, run):
        run.return_value.stdout = json.dumps([[{"tag_name": "v1.0.1", "draft": True}]])
        with self.assertRaisesRegex(ValueError, "unfinished draft"):
            release.publish("v1.0.1", "- Notes.\n", "owner/repo", COMMIT)
        self.assertEqual(1, run.call_count)

    @patch.object(release.subprocess, "run")
    def test_api_failure_does_not_attempt_publication(self, run):
        run.side_effect = subprocess.CalledProcessError(1, ["gh", "api"], stderr="API unavailable")
        with self.assertRaises(subprocess.CalledProcessError):
            release.publish("v1.0.1", "- Notes.\n", "owner/repo", COMMIT)
        self.assertEqual(1, run.call_count)

    @patch.object(release.subprocess, "run")
    def test_conflicting_unpublished_tag_is_not_reused(self, run):
        run.side_effect = [subprocess.CompletedProcess([], 0, "[[]]"),
                           subprocess.CompletedProcess([], 0, "b" * 40 + "\n")]
        with self.assertRaisesRegex(ValueError, "another commit"):
            release.publish("v1.0.1", "- Notes.\n", "owner/repo", COMMIT)
        self.assertEqual(2, run.call_count)

    @patch.object(release.subprocess, "run")
    def test_tag_inspection_errors_do_not_look_like_missing_tags(self, run):
        run.side_effect = [subprocess.CompletedProcess([], 0, "[[]]"),
                           subprocess.CompletedProcess([], 128, "")]
        with self.assertRaisesRegex(ValueError, "Cannot inspect"):
            release.publish("v1.0.1", "- Notes.\n", "owner/repo", COMMIT)
        self.assertEqual(2, run.call_count)

    @patch.object(release.subprocess, "run")
    def test_new_release_targets_checked_commit_with_exact_notes(self, run):
        notes = "- Keep literal $values and `code`.\n"
        for tag_status in [subprocess.CompletedProcess([], 1, ""),
                           subprocess.CompletedProcess([], 0, COMMIT + "\n")]:
            with self.subTest(existing_tag=tag_status.returncode):
                run.reset_mock()
                run.side_effect = [subprocess.CompletedProcess([], 0, "[[]]"), tag_status,
                                   subprocess.CompletedProcess([], 0, "https://example.com/release\n")]
                message = release.publish("v1.0.1", notes, "owner/repo", COMMIT)
                self.assertEqual("https://example.com/release", message)
                command = run.call_args.args[0]
                self.assertEqual(COMMIT, command[command.index("--target") + 1])
                self.assertEqual("v1.0.1", command[3])
                path = Path(command[command.index("--notes-file") + 1])
                self.assertEqual(notes, path.read_text(encoding="utf-8"))
                self.assertTrue(run.call_args.kwargs["check"])


if __name__ == "__main__":
    unittest.main()
