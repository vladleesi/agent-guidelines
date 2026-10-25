"""Publish the first dated changelog entry after CI checks the same commit."""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import subprocess


HEADER = re.compile(r"## ((?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)) — (\d{4}-\d{2}-\d{2})", re.ASCII)


def release_notes(changelog: str) -> tuple[str, str]:
    lines = changelog.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("## ")), None)
    match = HEADER.fullmatch(lines[start]) if start is not None else None
    if match is None:
        raise ValueError("First changelog entry must be '## MAJOR.MINOR.PATCH — YYYY-MM-DD'")
    date.fromisoformat(match[2])
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    notes = "\n".join(lines[start + 1:end]).strip()
    if not notes:
        raise ValueError("Release notes must not be empty")
    return f"v{match[1]}", notes + "\n"


def publish(tag: str, notes: str, repo: str, commit: str) -> str:
    result = subprocess.run(
        ["gh", "api", "--paginate", "--slurp", f"repos/{repo}/releases"],
        capture_output=True, text=True, check=True,
    )
    for page in json.loads(result.stdout):
        for release in page:
            if release["tag_name"] == tag:
                if release["draft"]:
                    raise ValueError(f"An unfinished draft exists for {tag}; review it before retrying")
                return f"{tag} is already published; leaving it unchanged"
    existing = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}^{{commit}}"],
        capture_output=True, text=True, check=False,
    )
    if existing.returncode not in (0, 1):
        raise ValueError("Cannot inspect the existing release tag")
    if existing.returncode == 0 and existing.stdout.strip() != commit:
        raise ValueError(f"{tag} points to another commit; choose a new version")
    notes_path = Path(".research/release-notes.md")
    notes_path.parent.mkdir(exist_ok=True)
    notes_path.write_text(notes, encoding="utf-8")
    result = subprocess.run(
        ["gh", "release", "create", tag, "--repo", repo, "--target", commit,
         "--title", tag, "--notes-file", str(notes_path)],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate notes without publishing")
    args = parser.parse_args()
    try:
        tag, notes = release_notes(Path("CHANGELOG.md").read_text(encoding="utf-8"))
        if args.check:
            print(f"{tag} release notes validated")
        else:
            print(publish(tag, notes, os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_SHA"]))
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        detail = error.stderr if isinstance(error, subprocess.CalledProcessError) else str(error)
        parser.exit(1, f"error: {detail}\n")


if __name__ == "__main__":
    main()
