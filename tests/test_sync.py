"""Exercise preservation, failure safety, and real Git release composition offline."""

import importlib.util
import json
from collections import Counter
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
OPERATIONAL_MODULES = ("git", "ci", "release", "deployment")
spec = importlib.util.spec_from_file_location("guideline_sync", ROOT / "scripts/sync.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def one_time_files(contents, commit, ref="v1.2.0"):
    """Exercise the documented manual placement recipe; not an installer API."""
    files = {}
    core = []
    for name, content in contents.items():
        title = content.splitlines()[0]
        sections = dict(re.findall(r"^## (Core|Task guidance)\n\n(.*?)(?=^## |\Z)",
                                   content, flags=re.M | re.S))
        if not sections:
            core.append(content.rstrip())
        if "Core" in sections:
            core.append(title + "\n\n" + sections["Core"].rstrip())
        if "Task guidance" in sections:
            files[f"docs/agent-guidance/{name}.md"] = (
                title + "\n\n" + sections["Task guidance"].rstrip() + "\n").encode()
    recipe = (ROOT / "docs/design.md").read_text(encoding="utf-8")
    router = recipe.split("```markdown\n", 1)[1].split("\n```", 1)[0]
    rows = []
    for line in router.splitlines():
        path = re.search(r"`(docs/agent-guidance/[^`]+\.md)`", line)
        if path is None or path[1] in files:
            rows.append(line)
    header = (
        "# Shared coding guidelines\n\n"
        f"Source: vladleesi/agent-guidelines {ref} ({commit}).\n"
        f"Modules: {', '.join(contents)}.\n"
        "MIT notice: `docs/agent-guidance/LICENSE`.\n"
        "One-time import: fetch, compare with, or update upstream only on explicit request.\n"
        "Apply within this directory and descendants; preserve narrower rule scopes.\n"
        "Project-specific instructions and recorded decisions override shared defaults."
    )
    parts = [header]
    if files:
        parts.append("\n".join(rows))
    parts.extend(core)
    files["AGENTS.md"] = ("\n\n".join(parts) + "\n").encode()
    files["docs/agent-guidance/LICENSE"] = (ROOT / "LICENSE").read_bytes()
    return files


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

    def delivery_releases(self):
        """Create legacy and split-module release fixtures without upstream access."""
        folder = self.source / "modules"
        split = {name: (folder / f"{name}.md").read_bytes() for name in OPERATIONAL_MODULES}
        for name in split:
            (folder / f"{name}.md").unlink()
        legacy = (folder / "delivery.md").read_bytes()
        (folder / "delivery.md").write_bytes(legacy)
        self.git("add", "--all", "modules")
        self.commit("Legacy delivery fixture")
        self.git("tag", "v1.1.1")
        for name, content in split.items():
            (folder / f"{name}.md").write_bytes(content)
        self.git("add", "--all", "modules")
        self.commit("Split delivery fixture")
        self.git("tag", "v1.2.0")
        return legacy

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
                                  "frontend", "testing", "security", "git", "ci", "deployment"],
                       capture_output=True, check=True)
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
            headings = [line for line in body.splitlines() if line.startswith(b"# ")]
            self.assertEqual([b"# Shared coding guidelines", module.read_bytes().splitlines()[0]],
                             headings)
            self.run_sync(check=True)

    def test_one_time_placement_preserves_every_pinned_rule_and_routes_all_task_files(self):
        names = sorted(p.stem for p in (self.source / "modules").glob("*.md")
                       if p.stem != "delivery")
        selections = [names, ["delivery"], ["git"], ["ci"], ["release"], ["deployment"],
                      ["general", "agent-workflow", "kotlin", "compose", "testing",
                       "security", "git", "ci", "release"],
                      ["general", "agent-workflow", "python", "backend", "testing",
                       "security", "git", "ci", "release", "deployment"]]
        for selection in selections:
            with self.subTest(selection=selection):
                self.run_sync(ref="v1.0.0", modules=selection)
                self.run_sync(check=True)
                commit = json.loads((self.target / sync.MANIFEST).read_bytes())["commit"]
                # Fixture v1.0.0 carries the pending source. Read pinned blobs,
                # just as the staged import does, rather than working-tree copies.
                contents = {name: sync.git("show", f"{commit}:modules/{name}.md").decode()
                            for name in selection}
                files = one_time_files(contents, commit, ref="v1.0.0")
                root = files["AGENTS.md"].decode()
                imported = "\n".join(value.decode() for path, value in files.items()
                                     if path.endswith(".md"))
                def bullets(text):
                    return Counter(b.rstrip() for b in re.findall(
                        r"^- .*?(?=\n- |\n#+ |\Z)", text, flags=re.M | re.S))
                expected = Counter()
                for content in contents.values():
                    expected.update(bullets(content))
                self.assertEqual(expected, bullets(imported))
                paths = re.findall(r"`(docs/agent-guidance/[^`]+\.md)`", root)
                self.assertCountEqual(paths, [p for p in files if p.endswith(".md")
                                             and p != "AGENTS.md"])
                self.assertEqual(len(paths), len(set(paths)))
                self.assertNotIn("@docs/", root)
                self.assertNotIn(sync.START.decode(), imported)
                self.assertNotIn(sync.END.decode(), imported)
                self.assertNotIn(sync.MANIFEST, files)
                self.assertNotIn("Generated section:", imported)
                self.assertEqual((ROOT / "LICENSE").read_bytes(),
                                 files["docs/agent-guidance/LICENSE"])
                # Materialize the import and resolve from its owning file, even
                # when a task begins in a different working directory.
                with tempfile.TemporaryDirectory(dir=self.base) as temporary:
                    project = Path(temporary)
                    for path, value in files.items():
                        output = project / path
                        output.parent.mkdir(parents=True, exist_ok=True)
                        output.write_bytes(value)
                    nested = project / "src/backend"
                    nested.mkdir(parents=True)
                    for path in paths:
                        self.assertEqual(files[path], (nested.parents[1] / path).read_bytes())

    def test_critical_rules_stay_in_core_without_companion_modules(self):
        for name in ("security", "git", "deployment"):
            content = (ROOT / "modules" / f"{name}.md").read_text(encoding="utf-8")
            self.assertNotIn("## Task guidance", content)
        phrases = {
            "general": ["Preserve unrelated", "recorded user decisions", "get approval",
                        "concision must not hide actual behavior", "security limitations",
                        "data-loss warnings", "recovery steps", "license/copyright notices",
                        "Do not shorten agent instructions", "check affected links, anchors, and examples"],
            "agent-workflow": ["never authority", "authorization", "required validation",
                               "never skip required", "Claim publication"],
            "git": ["Commit and push only", "Treat rejected pushes", "explicit permission"],
            "security": ["Never commit credentials", "Before committing or sharing",
                         "History cleanup", "Deny unless explicitly", "Never invent protocols"],
            "ci": ["require explicit permission", "no extra deployment or release authority",
                   "unchecked branch tip", "Minimize CI permissions", "privileged publication",
                   "never interpolated shell code", "explicit approval", "recurring CI cost increases"],
            "release": ["only with user approval", "Increment versions only", "Before publishing",
                        "Publish only within granted authorization", "Preserve published tags",
                        "require explicit approval"],
            "deployment": ["rollback", "require existing authorization",
                           "explicit approval before enabling paid services"],
        }
        for name, required in phrases.items():
            content = (ROOT / "modules" / f"{name}.md").read_text(encoding="utf-8")
            core = content.split("## Core\n", 1)[1].split("## Task guidance", 1)[0]
            for phrase in required:
                with self.subTest(module=name, safeguard=phrase):
                    self.assertIn(phrase, " ".join(core.split()))

    def test_operational_selections_include_only_requested_modules_in_order(self):
        selections = [["git"], ["git", "ci", "release"], ["git", "ci", "deployment"],
                      list(OPERATIONAL_MODULES)]
        for selection in selections:
            with self.subTest(selection=selection):
                self.run_sync(ref="v1.0.0", modules=selection)
                body = (self.target / "AGENTS.md").read_bytes()
                contents = [(ROOT / "modules" / f"{name}.md").read_bytes() for name in selection]
                headings = [line for line in body.splitlines() if line.startswith(b"# ")]
                self.assertEqual([b"# Shared coding guidelines"] +
                                 [content.splitlines()[0] for content in contents], headings)
                for content in contents:
                    self.assertEqual(1, body.count(content.strip()))
                manifest = json.loads((self.target / sync.MANIFEST).read_bytes())
                self.assertEqual(selection, manifest["modules"])
                self.run_sync(check=True)

    def test_delivery_pin_and_selection_survive_minor_upgrade(self):
        legacy = self.delivery_releases()
        agents = self.target / "AGENTS.md"
        prefix, suffix = b"# Local\r\nKeep before.\r\n", b"\r\n# Local suffix\r\nKeep after.\r\n"
        agents.write_bytes(prefix)
        self.run_sync(ref="v1.1.1", modules=["general", "delivery", "testing"])
        agents.write_bytes(agents.read_bytes() + suffix)
        before = self.snapshot()
        self.assertIn(legacy.strip(), before["AGENTS.md"])
        self.assertEqual(legacy, (self.source / "modules/delivery.md").read_bytes())
        self.run_sync()
        self.run_sync(check=True)
        self.assertEqual(before, self.snapshot())

        with self.assertRaisesRegex(ValueError, "Out of sync"):
            self.run_sync(ref="v1.2.0", check=True)
        self.assertEqual(before, self.snapshot())
        self.run_sync(ref="v1.2.0")
        self.assertIn(legacy.strip(), agents.read_bytes())
        self.assertTrue(agents.read_bytes().startswith(prefix))
        self.assertTrue(agents.read_bytes().endswith(suffix))
        manifest = json.loads((self.target / sync.MANIFEST).read_bytes())
        self.assertEqual(["general", "delivery", "testing"], manifest["modules"])
        self.assertEqual("v1.2.0", manifest["ref"])
        self.run_sync(check=True)

        selection = ["general", *OPERATIONAL_MODULES, "testing"]
        self.run_sync(ref="v1.2.0", modules=selection)
        updated = agents.read_bytes()
        self.assertTrue(updated.startswith(prefix))
        self.assertTrue(updated.endswith(suffix))
        self.assertNotIn(legacy.strip(), updated)
        for name in OPERATIONAL_MODULES:
            self.assertIn((ROOT / "modules" / f"{name}.md").read_bytes().strip(), updated)
        manifest = json.loads((self.target / sync.MANIFEST).read_bytes())
        self.assertEqual({"ref": "v1.2.0", "commit": self.git("rev-parse", "v1.2.0"),
                          "modules": selection}, manifest)
        after = self.snapshot()
        self.run_sync()
        self.run_sync(check=True)
        self.assertEqual(after, self.snapshot())
        agents.write_bytes(updated.replace(b"# Git operations", b"# Edited Git operations"))
        drifted = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Out of sync"):
            self.run_sync(check=True)
        self.assertEqual(drifted, self.snapshot())

    def test_minor_upgrade_without_delivery_preserves_saved_selection(self):
        self.delivery_releases()
        self.run_sync(ref="v1.1.1", modules=["general", "testing"])
        self.run_sync(ref="v1.2.0")
        manifest = json.loads((self.target / sync.MANIFEST).read_bytes())
        self.assertEqual(["general", "testing"], manifest["modules"])
        body = (self.target / "AGENTS.md").read_bytes()
        for name in OPERATIONAL_MODULES:
            heading = (ROOT / "modules" / f"{name}.md").read_bytes().splitlines()[0]
            self.assertNotIn(heading, body)
        self.run_sync(check=True)


if __name__ == "__main__":
    unittest.main()
