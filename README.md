# agent-guidelines

[![Checks](https://img.shields.io/github/check-suites/vladleesi/agent-guidelines/main?style=flat-square&label=checks)](https://github.com/vladleesi/agent-guidelines/actions?query=branch%3Amain) [![Release](https://img.shields.io/github/v/release/vladleesi/agent-guidelines?style=flat-square&color=7c3aed)](https://github.com/vladleesi/agent-guidelines/releases/latest) [![MIT](https://img.shields.io/github/license/vladleesi/agent-guidelines?style=flat-square&color=0ea5e9)](LICENSE)

Import selected Markdown rules from a pinned release into your project's
`AGENTS.md`. **Project rules override shared defaults.**

## 🚀 Quick start

Ask the agent working in your project:

```text
Import relevant rules from https://github.com/vladleesi/agent-guidelines
at v1.1.1 as a one-time, self-contained addition to this repository.

1. Inspect instructions and agent discovery configuration; select relevant modules.
   Change only instruction-related files and attribution/license notices. Rewrite
   only locally maintained instructions; preserve global, organization-managed,
   generated, and unrelated instructions unless explicitly authorized. Preserve
   unrelated working-tree changes.

2. Stage with the pinned synchronizer and --check in a temporary directory. Retain
   source release, commit, selected modules, and MIT notice in final instructions
   or accompanying notices. Leave no import-created manifests, managed markers, or
   sync instructions. Record that fetching, comparing with, or updating this
   collection requires explicit request.

3. Group by topic; headings/order may change. Preserve directory, language,
   platform, and agent scope; use nested files where needed. Keep retained imported
   bullets verbatim, including continuation text: never rephrase, shorten, split,
   or merge them.

4. Remove only wholly redundant imported copies. Rewrite/deduplicate local rules
   only if every requirement, scope, strength, exception, and affected agent remains
   covered. For partial overlaps, retain imported bullets and additional local
   requirements. Keep stronger/conflicting project requirements as concise overrides
   outside imported text; retain uncertain requirements.

5. Verify documented discovery for agents used here. Add adapters/config only as
   needed; omit standard discovery explanations from repository instructions.

6. Compare retained imports with pinned source; check for lost local requirements.
   Run git diff --check. Report removed duplicates, grouped sections, retained
   overrides, unresolved conflicts, discovery checks, and limitations.
```

Commit the instructions, required discovery files, and attribution/license notices.
Agents need no manifest, network, or source checkout. See
[integration details](docs/design.md#integration-workflows) and the optional
maintained workflow below.

## 🧩 Pick your modules

Modules have no implicit dependencies. Select only what the project needs.

| Module | Covers |
| --- | --- |
| [general](modules/general.md) | Conventions, decisions, code, docs, published sites |
| [agent-workflow](modules/agent-workflow.md) | Exploration, tools, required validation, completion |
| [testing](modules/testing.md) | Focused checks and behavioral tests |
| [security](modules/security.md) | Trust boundaries, secrets, privacy, dependencies |
| [delivery](modules/delivery.md) | Git, CI, versioning, releases, deployment costs |
| [kotlin](modules/kotlin.md) | Kotlin, coroutines, Android, Multiplatform |
| [compose](modules/compose.md) | State, effects, lifecycle, adaptive UI |
| [backend](modules/backend.md) | APIs, persistence, concurrency, operations |
| [python](modules/python.md) | Types, resources, async, tooling |
| [frontend](modules/frontend.md) | Browser UI, accessibility, production assets |

**Kotlin UI:** `general agent-workflow kotlin compose testing security delivery`

**Python service:** `general agent-workflow python backend testing security delivery`

For mixed repositories, place specialized rules in the relevant subdirectory.
Avoid repeating modules already selected in a parent scope.

See [compatibility](docs/compatibility.md) for agent discovery, Claude adapters,
and Copilot interface limitations.

## 🔄 Optional maintained synchronization

Choose this workflow to retain a generated section for deliberate future updates.
Git and Python 3.11+ are required only when synchronizing.

From your project's root, set the release once:

```sh
guidelines_ref=v1.1.1
guidelines_dir="/tmp/agent-guidelines-$guidelines_ref"

git clone --branch "$guidelines_ref" --depth 1 \
  https://github.com/vladleesi/agent-guidelines.git "$guidelines_dir"
python3 "$guidelines_dir/scripts/sync.py" \
  --target . --ref "$guidelines_ref" \
  --modules general agent-workflow frontend security testing
```

Keep project-specific rules outside the generated markers; they take precedence.
Never edit the generated section by hand. Commit `AGENTS.md` and
`.agent-guidelines.json` in your project.

To update a maintained integration, clone the desired release and run its
synchronizer with `--target /path/to/project --ref vX.Y.Z`. It reuses the saved
module selection; `--modules ...` replaces it. Review and commit the generated diff.

Add `--check` to the sync command to detect drift offline without writing.
The saved tag/commit pin rejects moved tags. Projects never update automatically.

## Maintain & release

Run `python3 -m unittest discover -s tests -v` and `git diff --check`.
Add a dated version entry at the top of [CHANGELOG.md](CHANGELOG.md), then push to
`main`: CI creates its `vX.Y.Z` tag and GitHub Release **after both test jobs pass**
on that commit. Reruns preserve published releases; rerun the workflow on `main`
to retry a failed publication. Use SemVer and never move published tags.

Repository-only instructions live in [AGENTS.md](AGENTS.md); [design notes](docs/design.md)
explain the sources and tradeoffs. Include the [MIT notice](LICENSE) when
redistributing these guidelines, separately from your own project's license.
