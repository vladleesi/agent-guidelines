#!/usr/bin/env python3
"""Compose release-pinned modules into AGENTS.md using only the standard library."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


SOURCE = Path(__file__).resolve().parents[1]
START = b"<!-- agent-guidelines:begin -->"
END = b"<!-- agent-guidelines:end -->"
MANIFEST = ".agent-guidelines.json"
RELEASE = re.compile(r"v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", re.ASCII)
MODULE = re.compile(r"[a-z][a-z0-9-]*", re.ASCII)


def git(*args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(SOURCE), *args], capture_output=True, check=False
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"Cannot read release from source checkout: {detail}")
    return result.stdout


def read_output(path: Path) -> bytes:
    if path.is_symlink():
        raise ValueError(f"Refusing to replace symlink: {path}")
    if path.exists() and not path.is_file():
        raise ValueError(f"Expected a regular file: {path}")
    return path.read_bytes() if path.exists() else b""


def replace_block(original: bytes, block: bytes) -> bytes:
    """Preserve every byte outside a single, correctly delimited managed block."""
    if START not in original and END not in original:
        separator = b"" if not original or original.endswith(b"\n\n") else (
            b"\n" if original.endswith(b"\n") else b"\n\n"
        )
        return original + separator + block + b"\n"
    if original.count(START) != 1 or original.count(END) != 1:
        raise ValueError("AGENTS.md must have one matching pair of managed markers")
    start = original.index(START)
    end = original.index(END) + len(END)
    if end < start or (start and original[start - 1:start] != b"\n"):
        raise ValueError("Managed markers must be ordered and on their own lines")
    if not original[start + len(START):].startswith((b"\n", b"\r\n")):
        raise ValueError("Begin marker must be on its own line")
    end_start = end - len(END)
    if end_start and original[end_start - 1:end_start] != b"\n":
        raise ValueError("End marker must be on its own line")
    if original[end:] and not original[end:].startswith((b"\n", b"\r\n")):
        raise ValueError("End marker must be on its own line")
    return original[:start] + block + original[end:]


def compose(ref: str, commit: str, modules: list[str]) -> bytes:
    parts = [
        START.decode(),
        "# Shared coding guidelines",
        f"Source: vladleesi/agent-guidelines {ref} ({commit}).",
        "Generated section: update with scripts/sync.py; keep local rules outside it.",
        "Apply these guidelines to relevant work in this directory and its descendants.",
        "Explicit project-specific rules outside this section and more specific",
        "directory instructions take precedence over these shared defaults.",
    ]
    for name in modules:
        if not isinstance(name, str) or not MODULE.fullmatch(name):
            raise ValueError(f"Invalid module name: {name!r}")
        content = git("show", f"{commit}:modules/{name}.md").decode("utf-8").strip()
        if not content.startswith("# ") or START.decode() in content or END.decode() in content:
            raise ValueError(f"Invalid module content: {name}")
        parts.extend(["", content])
    parts.extend(["", END.decode()])
    return "\n".join(parts).encode("utf-8")


def atomic_write(path: Path, content: bytes) -> None:
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
        temporary.chmod(mode)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def sync(
    target: Path,
    ref: str | None = None,
    modules: list[str] | None = None,
    check: bool = False,
) -> str:
    if not target.is_dir():
        raise ValueError(f"Target directory does not exist: {target}")
    agents_path = target / "AGENTS.md"
    manifest_path = target / MANIFEST
    original = read_output(agents_path)
    manifest_bytes = read_output(manifest_path)
    saved = json.loads(manifest_bytes) if manifest_bytes else {}
    if not isinstance(saved, dict):
        raise ValueError("Manifest must be a JSON object")
    if saved and (set(saved) != {"ref", "commit", "modules"}
                  or not isinstance(saved["ref"], str)
                  or not RELEASE.fullmatch(saved["ref"])
                  or not isinstance(saved["commit"], str)
                  or not re.fullmatch(r"[0-9a-f]{40}", saved["commit"])):
        raise ValueError("Invalid manifest; expected ref, full commit, and modules")
    ref = ref if ref is not None else saved.get("ref")
    modules = modules if modules is not None else saved.get("modules")
    if not isinstance(ref, str) or not RELEASE.fullmatch(ref):
        raise ValueError("Select a release tag with --ref vMAJOR.MINOR.PATCH")
    if not isinstance(modules, list) or not modules or any(not isinstance(n, str) for n in modules):
        raise ValueError("Select a nonempty module list with --modules")
    if len(set(modules)) != len(modules):
        raise ValueError("Select each module only once")
    commit = git("rev-parse", "--verify", f"refs/tags/{ref}^{{commit}}").decode().strip()
    if saved.get("ref") == ref and saved.get("commit") != commit:
        raise ValueError("Pinned release tag moved; refusing to replace the recorded commit")
    block = compose(ref, commit, modules)
    updated = replace_block(original, block)
    manifest = (json.dumps({"ref": ref, "commit": commit, "modules": modules}, indent=2) + "\n").encode()
    outputs = [(agents_path, original, updated), (manifest_path, manifest_bytes, manifest)]
    changed = [path.name for path, old, new in outputs if old != new]
    if check:
        if changed:
            raise ValueError("Out of sync: " + ", ".join(changed))
        return "Instructions match the pinned release"
    for path, old, new in outputs:
        if old != new:
            atomic_write(path, new)
    return "Updated " + ", ".join(changed) if changed else "Instructions already up to date"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True, help="Existing consumer directory")
    parser.add_argument("--ref", help="Release tag; defaults to the saved pin")
    parser.add_argument("--modules", nargs="+", help="Module names in composition order; defaults to saved selection")
    parser.add_argument("--check", action="store_true", help="Report drift without writing")
    args = parser.parse_args()
    try:
        print(sync(args.target.resolve(), args.ref, args.modules, args.check))
    except (ValueError, OSError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
