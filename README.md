# agent-guidelines

[![Checks](https://img.shields.io/github/check-suites/vladleesi/agent-guidelines/main?style=flat-square&label=checks)](https://github.com/vladleesi/agent-guidelines/actions?query=branch%3Amain) [![Release](https://img.shields.io/github/v/release/vladleesi/agent-guidelines?style=flat-square&color=7c3aed)](https://github.com/vladleesi/agent-guidelines/releases/latest) [![MIT](https://img.shields.io/github/license/vladleesi/agent-guidelines?style=flat-square&color=0ea5e9)](LICENSE)

Import selected Markdown rules from a pinned release. Keep core rules in
`AGENTS.md` and read local task guidance when needed. **Project rules override
shared defaults.**

## 🚀 Quick start

Ask the agent working in your project:

```text
Import relevant rules from https://github.com/vladleesi/agent-guidelines
at v1.3.0 as a one-time, self-contained addition to this repository.

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

3. Follow docs/design.md's "Task-based loading" recipe from that release. Keep each
   selected module's Core section in the applicable AGENTS.md; put Task guidance
   in local docs/agent-guidance/<module>.md files with explicit read-before-work
   routes. Preserve project architecture, commands, restrictions, and scope.
   Use full inline instructions if file reads/discovery are unavailable. Keep
   imported bullets verbatim, including continuations; never split or merge them.

4. Remove only wholly redundant imported copies. Rewrite/deduplicate local rules
   only if every requirement, scope, strength, exception, and affected agent remains
   covered. For partial overlaps, retain imported bullets and additional local
   requirements. Keep stronger/conflicting project requirements as concise overrides
   outside imported text; retain uncertain requirements.

5. Verify root discovery and task-file reads for agents used here, including work
   started in subdirectories. Check routing for cross-cutting tasks and indirect
   release/deployment effects. Add adapters only as needed; no eager task imports.

6. Compare retained imports with pinned source; check for lost local requirements,
   missing routes/files, and duplicate rules. Run git diff --check. Report core and
   task sizes, overrides, removed duplicates, conflicts, discovery checks/limits.
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
| [git](modules/git.md) | Commits, pushes, authorization, history safety |
| [ci](modules/ci.md) | Checks, failure investigation, workflow security and costs |
| [release](modules/release.md) | Versioning, changelogs, tags, publication safeguards |
| [deployment](modules/deployment.md) | Hosting, infrastructure, rollback, cloud costs |
| [kotlin](modules/kotlin.md) | Kotlin, coroutines, Android, Multiplatform |
| [compose](modules/compose.md) | State, effects, lifecycle, adaptive UI |
| [backend](modules/backend.md) | APIs, persistence, concurrency, operations |
| [python](modules/python.md) | Types, resources, async, tooling |
| [frontend](modules/frontend.md) | Browser UI, accessibility, production assets |

**Kotlin/Compose library:** `general agent-workflow kotlin compose testing security git ci release`

**Python service:** `general agent-workflow python backend testing security git ci release deployment`

For a website, use `git ci deployment` for delivery tasks; a Git-only task can use
just `git`. The deprecated [delivery](modules/delivery.md) module remains available
for existing selections. Do not combine it with the four replacements; see
[optional migration](docs/design.md#replacing-the-legacy-delivery-module).

Selection chooses coverage; placement determines context. The one-time workflow
uses [task-based loading](docs/design.md#task-based-loading). Nested `AGENTS.md`
files are an alternative for stable directory scopes, not operation-based routing.
Keep small selections such as `git` inline; avoid repeating parent rules.

See [compatibility](docs/compatibility.md) for agent discovery, Claude adapters,
and Copilot interface limitations.

## 🔄 Optional maintained synchronization

Choose this workflow to retain a generated section for deliberate future updates.
Git and Python 3.11+ are required only when synchronizing.
It includes **all selected rules inline**; section headings do not defer loading.

From your project's root, set the release once:

```sh
guidelines_ref=v1.3.0
guidelines_dir="/tmp/agent-guidelines-$guidelines_ref"

git clone --branch "$guidelines_ref" --depth 1 \
  https://github.com/vladleesi/agent-guidelines.git "$guidelines_dir"
python3 "$guidelines_dir/scripts/sync.py" \
  --target . --ref "$guidelines_ref" \
  --modules general agent-workflow frontend testing security git ci deployment
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
