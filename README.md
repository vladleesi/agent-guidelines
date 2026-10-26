# agent-guidelines

[![Checks](https://img.shields.io/github/check-suites/vladleesi/agent-guidelines/main?style=flat-square&label=checks)](https://github.com/vladleesi/agent-guidelines/actions?query=branch%3Amain) [![Release](https://img.shields.io/github/v/release/vladleesi/agent-guidelines?style=flat-square&color=7c3aed)](https://github.com/vladleesi/agent-guidelines/releases/latest) [![MIT](https://img.shields.io/github/license/vladleesi/agent-guidelines?style=flat-square&color=0ea5e9)](LICENSE)

Import selected Markdown rules into your project's `AGENTS.md` from a pinned
release. Shared defaults for coding agents, with **your project rules in charge**.

## 🚀 Quick start

Ask the agent working in your project:

```text
Import relevant rules from https://github.com/vladleesi/agent-guidelines
at v1.1.0 as a one-time, self-contained addition to this repository.

1. Inspect existing instructions and agent discovery configuration; select only
   relevant modules. Rewrite only this repository's locally maintained instructions;
   preserve global, organization-managed, generated, and unrelated instructions
   unless explicitly authorized to change them. Change only instruction-related
   files and attribution/license notices; preserve unrelated working-tree changes.

2. Use the pinned release's synchronizer and --check in a temporary directory.
   Retain source release, commit, and MIT notice in final instructions or
   accompanying notices. Leave no import-created manifests, managed markers, or
   synchronization instructions in this repository.
   Record in local instructions that this guideline collection must not be fetched,
   compared with upstream, or updated unless explicitly requested.

3. Combine related sections by topic. Headings and rule order may change; preserve
   directory, language, platform, and agent scope. Use nested files where needed.
   Keep retained imported rules verbatim, including continuation text. Move whole
   rules under local headings; do not shorten, rephrase, split, or merge them.

4. Deduplicate by meaning. Existing local instructions may be split, shortened,
   rewritten, or removed only if every distinct requirement, scope, strength,
   exception, and agent coverage survives. For partial overlaps, keep the imported
   rule intact and retain only additional local requirements. Keep stronger or
   conflicting project-specific requirements as concise overrides outside imported
   text. Retain uncertain requirements.

5. Use and verify documented discovery mechanisms for the agents used here. Add
   adapters or configuration only when needed. Keep explanations of standard
   discovery behavior out of repository instructions.

6. Compare retained imported rules with the pinned source and check for lost local
   requirements. Run git diff --check. In the final summary, report removed
   duplicates, consolidated sections, retained overrides, unresolved conflicts,
   discovery checks, and limitations.
```

Commit the resulting local instructions, required discovery files, and attribution
and license notices. Agents need no manifest, network, or source checkout.
See [integration details](docs/design.md#integration-workflows) for verification
and the optional maintained workflow below for deliberate synchronization.

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

Codex and Cursor discover `AGENTS.md`. For Claude Code configurations that need
an adapter, add `@AGENTS.md` to the existing `CLAUDE.md`. Copilot support varies
by interface: see [compatibility](docs/compatibility.md).

## 🔄 Optional maintained synchronization

Choose this workflow to retain a generated section for deliberate future updates.
Git and Python 3.11+ are required only when synchronizing.

From your project's root, set the release once:

```sh
guidelines_ref=v1.1.0
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

Use `--check` with the matching source checkout to detect drift offline.
The saved pin records both tag and commit, and same-version tag changes are rejected.
Projects never update automatically.

## Maintain & release

Run `python3 -m unittest discover -s tests -v` and `git diff --check`.
Add a dated version entry at the top of [CHANGELOG.md](CHANGELOG.md), then push to
`main`: CI creates its `vX.Y.Z` tag and GitHub Release **after both test jobs pass**
on that commit. Reruns preserve published releases; rerun the workflow on `main`
to retry a failed publication. Use SemVer and never move published tags.

Repository-only instructions live in [AGENTS.md](AGENTS.md); [design notes](docs/design.md)
explain the sources and tradeoffs. Include the [MIT notice](LICENSE) when
redistributing these guidelines, separately from your own project's license.
