"""Exercise preservation, failure safety, and real Git release composition offline."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("guideline_sync", ROOT / "scripts/sync.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SyncTests(unittest.TestCase):
    def setUp(self):
        scratch = ROOT / ".research"
        scratch.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.source = self.base / "source"
        self.target = self.base / "consumer with spaces"
        self.source.mkdir()
        self.target.mkdir()
        shutil.copytree(ROOT / "modules", self.source / "modules")
        shutil.copytree(ROOT / "scripts", self.source / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        (self.source / "AGENTS.md").write_text("PRIVATE_MAINTENANCE_SENTINEL\n", encoding="utf-8")
        self.git("init", "--quiet")
        self.git("add", ".")
        self.commit("Initial fixture")
        self.git("tag", "v1.0.0")
        source_patch = patch.object(sync, "SOURCE", self.source)
        source_patch.start()
        self.addCleanup(source_patch.stop)

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.source), *args], stderr=subprocess.PIPE).decode().strip()

    def commit(self, message):
        return self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                        "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", message)

    def run_sync(self, **kwargs):
        return sync.sync(self.target, **kwargs)

    def initial(self, modules=None):
        self.run_sync(ref="v1.0.0", modules=modules or ["general", "testing"])

    def snapshot(self):
        return {p.name: p.read_bytes() for p in self.target.iterdir() if p.is_file()}

    def test_selection_pin_and_idempotence(self):
        self.initial()
        before = self.snapshot()
        body = before["AGENTS.md"].decode()
        self.assertIn("# General engineering", body)
        self.assertIn("# Testing and validation", body)
        self.assertNotIn("# Compose UI", body)
        self.assertNotIn("PRIVATE_MAINTENANCE_SENTINEL", body)
        manifest = json.loads(before[sync.MANIFEST])
        self.assertEqual(manifest, {"ref": "v1.0.0", "commit": self.git("rev-parse", "HEAD"),
                                    "modules": ["general", "testing"]})
        self.run_sync()
        self.run_sync(check=True)
        self.assertEqual(before, self.snapshot())

    def test_existing_and_later_local_rules_preserved_byte_for_byte(self):
        local = b"# Project rules\r\n\r\nUse local conventions.\r\n"
        agents = self.target / "AGENTS.md"
        agents.write_bytes(local)
        self.initial()
        first = agents.read_bytes()
        self.assertTrue(first.startswith(local))
        suffix = b"\r\n# More local rules\r\nKeep this too.\r\n"
        agents.write_bytes(first + suffix)
        self.run_sync(modules=["frontend"])
        updated = agents.read_bytes()
        self.assertTrue(updated.startswith(local))
        self.assertTrue(updated.endswith(suffix))
        self.assertNotIn(b"# General engineering", updated)
        self.run_sync(check=True)

    def test_dirty_source_cannot_change_pinned_output(self):
        self.initial()
        before = self.snapshot()
        (self.source / "modules/general.md").write_text("# Changed\n", encoding="utf-8")
        self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_upgrade_reuses_selection_and_preserves_local_rules(self):
        self.initial()
        agents = self.target / "AGENTS.md"
        agents.write_bytes(b"# Local\n\n" + agents.read_bytes())
        module = self.source / "modules/general.md"
        module.write_bytes(module.read_bytes() + b"\n- A new fixture rule.\n")
        self.git("add", "modules/general.md")
        self.commit("Update fixture")
        self.git("tag", "v1.1.0")
        self.run_sync(ref="v1.1.0")
        self.assertTrue(agents.read_bytes().startswith(b"# Local\n\n"))
        self.assertIn(b"A new fixture rule", agents.read_bytes())
        manifest = json.loads((self.target / sync.MANIFEST).read_bytes())
        self.assertEqual(manifest["modules"], ["general", "testing"])
        self.assertEqual(manifest["ref"], "v1.1.0")

    def test_check_detects_drift_without_writing(self):
        self.initial()
        agents = self.target / "AGENTS.md"
        agents.write_bytes(agents.read_bytes().replace(b"# General engineering", b"# Edited content"))
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Out of sync"):
            self.run_sync(check=True)
        self.assertEqual(before, self.snapshot())

    def test_check_on_uninitialized_target_does_not_write(self):
        with self.assertRaisesRegex(ValueError, "Out of sync"):
            self.run_sync(ref="v1.0.0", modules=["general"], check=True)
        self.assertEqual({}, self.snapshot())

    def test_invalid_selection_and_ref_fail_before_writes(self):
        self.initial()
        before = self.snapshot()
        cases = [
            {"modules": ["general", "missing"]}, {"modules": ["../AGENTS"]},
            {"modules": ["general", "general"]}, {"modules": []},
            {"ref": "main"}, {"ref": "v01.0.0"}, {"ref": "v9.9.9"},
        ]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                self.run_sync(**case)
            self.assertEqual(before, self.snapshot())

    def test_malformed_markers_are_not_overwritten(self):
        agents = self.target / "AGENTS.md"
        cases = [sync.START, sync.END, sync.END + b"\n" + sync.START,
                 sync.START + b"\n" + sync.START + b"\n" + sync.END,
                 b"text " + sync.START + b"\n" + sync.END,
                 sync.START + b" extra\n" + sync.END,
                 sync.START + b"\r extra\n" + sync.END,
                 sync.START + b"\ntext" + sync.END,
                 sync.START + b"\n" + sync.END + b" extra",
                 sync.START + b"\n" + sync.END + b"\r extra"]
        for content in cases:
            agents.write_bytes(content)
            before = self.snapshot()
            with self.subTest(content=content), self.assertRaises(ValueError):
                self.run_sync(ref="v1.0.0", modules=["general"])
            self.assertEqual(before, self.snapshot())

    def test_crlf_markers_preserve_surrounding_bytes(self):
        agents = self.target / "AGENTS.md"
        prefix, suffix = b"# Local\r\n\r\n", b"\r\n# Local suffix\r\n"
        agents.write_bytes(prefix + sync.START + b"\r\nold\r\n" + sync.END + suffix)
        self.initial()
        self.assertTrue(agents.read_bytes().startswith(prefix))
        self.assertTrue(agents.read_bytes().endswith(suffix))
        self.run_sync(check=True)

    def test_moved_tag_is_rejected(self):
        self.initial()
        before = self.snapshot()
        (self.source / "new.txt").write_text("new commit", encoding="utf-8")
        self.git("add", "new.txt")
        self.commit("Next fixture")
        self.git("tag", "--force", "v1.0.0")
        with self.assertRaisesRegex(ValueError, "tag moved"):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_invalid_manifest_is_not_overwritten(self):
        manifest = self.target / sync.MANIFEST
        for content in [b"not json", b"[]", b'{"ref":"v1.0.0"}',
                        b'{"ref":"v1.0.0","commit":"bad","modules":["general"]}']:
            manifest.write_bytes(content)
            with self.subTest(content=content), self.assertRaises(ValueError):
                self.run_sync()
            self.assertEqual(content, manifest.read_bytes())
            self.assertFalse((self.target / "AGENTS.md").exists())

    def test_symlink_outputs_rejected_without_changing_referent(self):
        external = self.base / "external.md"
        external.write_bytes(b"Do not overwrite\n")
        for name in ["AGENTS.md", sync.MANIFEST]:
            link = self.target / name
            link.symlink_to(external)
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "symlink"):
                self.run_sync(ref="v1.0.0", modules=["general"])
            self.assertEqual(b"Do not overwrite\n", external.read_bytes())
            link.unlink()
        self.assertEqual({}, self.snapshot())

    def test_nested_scope_does_not_touch_parent(self):
        (self.target / "AGENTS.md").write_bytes(b"Parent rules\n")
        nested = self.target / "src"
        nested.mkdir()
        sync.sync(nested, ref="v1.0.0", modules=["kotlin"])
        self.assertEqual(b"Parent rules\n", (self.target / "AGENTS.md").read_bytes())
        self.assertIn(b"# Kotlin", (nested / "AGENTS.md").read_bytes())

    def test_readme_cli_works_from_a_shallow_release_clone(self):
        clone = self.base / "release clone"
        subprocess.run(["git", "clone", "--quiet", "--branch", "v1.0.0", "--depth", "1",
                        self.source.as_uri(), str(clone)], capture_output=True, check=True)
        command = [sys.executable, str(clone / "scripts/sync.py"), "--target", str(self.target)]
        subprocess.run(command + ["--ref", "v1.0.0", "--modules", "general", "agent-workflow",
                                  "frontend", "security", "testing"], capture_output=True, check=True)
        before = self.snapshot()
        subprocess.run(command + ["--check"], capture_output=True, check=True)
        self.assertEqual(before, self.snapshot())
        failed = subprocess.run(command + ["--ref", "main"], capture_output=True)
        self.assertEqual(1, failed.returncode)
        self.assertIn(b"error:", failed.stderr)

    def test_each_module_is_independently_composable(self):
        for module in sorted((ROOT / "modules").glob("*.md")):
            self.run_sync(ref="v1.0.0", modules=[module.stem])
            body = (self.target / "AGENTS.md").read_bytes()
            self.assertIn(module.read_bytes().strip(), body)
            self.assertEqual(1, body.count(sync.START))
            self.run_sync(check=True)


if __name__ == "__main__":
    unittest.main()
