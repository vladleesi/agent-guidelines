# agent-guidelines

[![Checks](https://img.shields.io/github/actions/workflow/status/vladleesi/agent-guidelines/check.yml?branch=main&style=flat-square&label=checks)](https://github.com/vladleesi/agent-guidelines/actions/workflows/check.yml?query=branch%3Amain) [![Release](https://img.shields.io/github/v/release/vladleesi/agent-guidelines?style=flat-square&color=7c3aed)](https://github.com/vladleesi/agent-guidelines/releases/latest) [![MIT](https://img.shields.io/github/license/vladleesi/agent-guidelines?style=flat-square&color=0ea5e9)](LICENSE)

Pick a few Markdown modules, pin a release, and compose them into your project's
`AGENTS.md`. Shared defaults for coding agents, with **your project rules in charge**.

## 🚀 Quick start

Ask the agent working in your project:

```text
Integrate https://github.com/vladleesi/agent-guidelines at v1.0.2
using that release's README.

Inspect existing instructions and select relevant modules at appropriate directory
scopes. Consolidate duplicates only when the remaining rules preserve their meaning,
scope, strength, and exceptions for every affected agent. Keep project-specific
constraints and overrides outside generated sections.

Use the supplied synchronizer and configure documented discovery for the agents
this repository uses. Verify with --check and git diff --check, then summarize
changes and any limitations. Change only instruction-related files and integration
metadata.
```

<details>
<summary>Prefer commands? Git + Python 3.11+ are all you need.</summary>

From your project's root:

```sh
git clone --branch v1.0.2 --depth 1 https://github.com/vladleesi/agent-guidelines.git /tmp/agent-guidelines-v1.0.2
python3 /tmp/agent-guidelines-v1.0.2/scripts/sync.py \
  --target . --ref v1.0.2 --modules general agent-workflow frontend security testing
```

</details>

> [!TIP]
> Keep your existing `AGENTS.md`. Local rules **outside the generated markers**
> take precedence; updates replace only the shared section. Never edit that section by hand.

Commit `AGENTS.md` and `.agent-guidelines.json` in your project. Agents read the
instructions locally, with no network or source checkout needed.

## 🧩 Pick your modules

Modules have no implicit dependencies. Select only what the project needs.

| Module | Covers |
| --- | --- |
| [general](modules/general.md) | Code, boundaries, maintainability, documentation |
| [agent-workflow](modules/agent-workflow.md) | Exploration, context, tools, completion |
| [testing](modules/testing.md) | Focused checks and behavioral tests |
| [security](modules/security.md) | Trust boundaries, secrets, dependencies |
| [delivery](modules/delivery.md) | Git, CI, GitHub Actions, releases |
| [kotlin](modules/kotlin.md) | Kotlin, coroutines, Android, Multiplatform |
| [compose](modules/compose.md) | State, effects, lifecycle, adaptive UI |
| [backend](modules/backend.md) | APIs, persistence, concurrency, operations |
| [python](modules/python.md) | Types, resources, async, tooling |
| [frontend](modules/frontend.md) | Browser UI, accessibility, production assets |

**Kotlin UI:** `general agent-workflow kotlin compose testing security delivery`

**Python service:** `general agent-workflow python backend testing security delivery`

For mixed repositories, sync specialized modules into the relevant subdirectory.
Avoid repeating modules already selected in a parent scope.

Codex and Cursor discover `AGENTS.md`. For Claude Code configurations that need
an adapter, add `@AGENTS.md` to the existing `CLAUDE.md`. Copilot support varies
by interface: see [compatibility](docs/compatibility.md).

## 🔄 Update on your terms

Clone the desired release and run its synchronizer with
`--target /path/to/project --ref vX.Y.Z`. It reuses the saved module selection;
`--modules ...` replaces it. Review and commit the generated diff.

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
