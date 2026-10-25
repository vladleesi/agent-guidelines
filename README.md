# agent-guidelines

Modular coding-agent instructions, composed into a project's `AGENTS.md` and
pinned to an immutable Git release. No runtime service or package dependencies.

## Modules

Choose only what the project needs; modules have no implicit dependencies.

| Module | Responsibility |
| --- | --- |
| [general](modules/general.md) | Code, boundaries, maintainability, documentation |
| [agent-workflow](modules/agent-workflow.md) | Exploration, context, tools, completion |
| [testing](modules/testing.md) | Risk-based checks and behavioral tests |
| [security](modules/security.md) | Trust boundaries, secrets, dependencies |
| [delivery](modules/delivery.md) | Git, CI, GitHub Actions, releases |
| [kotlin](modules/kotlin.md) | Kotlin, coroutines, Android, Multiplatform |
| [compose](modules/compose.md) | State, effects, lifecycle, adaptive UI |
| [backend](modules/backend.md) | APIs, persistence, concurrency, operations |
| [python](modules/python.md) | Python types, resources, async, tooling |
| [frontend](modules/frontend.md) | Browser UI, accessibility, production assets |

## Use in a project

Ask the coding agent working in your project:

> Integrate https://github.com/vladleesi/agent-guidelines at v1.0.0 using its README.
> Select only modules relevant to this project, preserve existing project instructions,
> and configure discovery for the agents this repository uses. Change only instruction-related files.

For manual setup, use Git and Python 3.11+ from the consuming project's root:

```sh
git clone --branch v1.0.0 --depth 1 https://github.com/vladleesi/agent-guidelines.git /tmp/agent-guidelines-v1.0.0
python3 /tmp/agent-guidelines-v1.0.0/scripts/sync.py \
  --target . --ref v1.0.0 --modules general agent-workflow frontend security testing
```

Leave your existing `AGENTS.md` in place. The synchronizer appends a managed
section and replaces only that section on updates. Keep project architecture,
commands, workflows, and exceptions **outside** its markers; these local rules
take precedence over shared defaults. For example, local build-approval rules
still apply. Review duplicated local rules before removing them, and never edit
the generated section by hand.

Commit `AGENTS.md` and `.agent-guidelines.json` in your project. Agents read both
local and shared instructions from `AGENTS.md`; they need no network access or
source checkout.

For Kotlin UI, select `general agent-workflow kotlin compose testing security delivery`.
For a Python service, select `general agent-workflow python backend testing security delivery`.
Run against a subdirectory to create a separately pinned, directory-scoped
`AGENTS.md`; avoid selecting the same modules at both root and child scope.

Codex and Cursor discover `AGENTS.md`. Current Claude Code also supports it, with
conditions; for older versions or an existing `CLAUDE.md`, add `@AGENTS.md` to that
file (the [adapter](adapters/CLAUDE.md) contains just this import). Copilot support
depends on the interface. See [compatibility and discovery](docs/compatibility.md).

Include this repository's [MIT notice](LICENSE) with redistributed guidelines;
keep it separate from your project's own license, for example in third-party notices.

## Update intentionally

Clone the desired release into a new source directory, then run its synchronizer
with `--target /path/to/project --ref vX.Y.Z`. The saved module selection is reused;
pass `--modules ...` to replace it. Review the generated diff and commit the update.
Never consume a moving branch automatically.

To verify offline against the recorded release, rerun the same source checkout
with `--target /path/to/project --check`. This detects drift without writing.
The manifest records both tag and commit; a moved tag is rejected for that pin.
Generation reads committed module blobs, so local source edits cannot affect output.
Keep the source checkout if you need offline regeneration.

## Maintain this collection

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Release the entire collection together using SemVer and immutable `vX.Y.Z` tags,
starting at `v1.0.0`: MAJOR for incompatible changes, MINOR for compatible additions,
PATCH for compatible fixes. Record changes and migrations in [CHANGELOG.md](CHANGELOG.md),
validate the finished commit, then create and push an annotated tag manually.
Do not move released tags. Repository maintenance rules live in [AGENTS.md](AGENTS.md)
and are never composed into consumer instructions. [Design notes](docs/design.md)
record the source evidence and the small set of deliberate tradeoffs.
