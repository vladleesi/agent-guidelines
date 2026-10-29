# Design notes

## Integration workflows

Use the [README import prompt](../README.md) for a one-time, self-contained import
by default. Choose Inline or Core + Task placement below; use maintained sync only
when explicitly requested. Reading imported guidance needs no network, manifest,
script, or upstream checkout.

1. Stage each selection with the pinned synchronizer in an empty temporary target;
   run `--check` using the same checkout. This checks staging, not final placement.
2. Group imports with existing instructions by topic; preserve directory, language,
   platform, and agent scope. Imported bullets and continuations stay verbatim:
   never rephrase, split, or merge them; headings/order may change. Remove only
   wholly redundant imported copies. For partial overlaps, keep imported bullets
   intact and retain additional local requirements.
3. Rewrite only locally maintained instructions, preserving every requirement,
   scope, strength, exception, and affected agent. Preserve unrelated files,
   customizations, and working-tree changes. Leave global, organization-managed,
   generated, and unrelated instructions unchanged unless explicitly authorized.
   Keep stronger/conflicting project rules as concise overrides outside imports;
   retain uncertain requirements and report conflicts precedence cannot resolve.
   A newer source alone does not establish equivalence.
4. Remove staging manifests, markers, and sync notices. Outside imported text,
   retain source repository, release, full commit, selected modules, scope, project
   precedence, and the MIT notice. Record that fetching, comparing with, or updating
   upstream requires explicit request; attribution links grant no such permission.
5. Compare final imported bullets with the pin and check for lost local requirements.
   Verify [discovery and scope](compatibility.md#limits-and-verification), add only
   necessary adapters/config, and run `git diff --check`. Report checks/limitations
   without adding standard discovery explanations to consumer instructions.

### Task-based loading

**Inline:** keep full selected modules in applicable automatically discovered
instruction files. Use this for small selections or when dependable root discovery
and local file reads cannot be established. Modules without placement sections,
including legacy `delivery`, stay inline.

**Core + Task:** default for new one-time imports with verified discovery and local
file reads. Core/Task headings guide placement; they neither load files nor change
rule scope. Only selected modules apply; Core is not a separate required module.

1. Keep selected **Core** rules and existing project architecture, commands, critical
   conventions, decisions, restrictions, and overrides in applicable automatically
   discovered files. Never defer Core rules or broaden scope to reduce size.
2. Put each selected **Task guidance** section, with its module title, in ordinary
   local Markdown, normally `docs/agent-guidance/<module>.md`. Reuse suitable existing
   documentation locations; keep each retained bullet once and create no empty files.
   Keep the MIT notice alongside guidance and release, full commit, and selection
   in root instructions.
3. Add this routing text to the applicable `AGENTS.md`. Keep only installed task-file
   rows, adjust paths, and add project paths where useful. Preserve directory,
   language, platform, and agent scope in both routes and destinations.

```markdown
## Local task guidance

Before relevant analysis, edits, or commands, read all matching files below.
Paths are relative to this AGENTS.md, not the shell's working directory.
Recheck routes when the task expands, crosses scopes, or context is compacted;
read guidance again if it is no longer in context. If required guidance is missing
or unreadable, report it and stop the affected work. These files supplement the
core rules; project-specific instructions and recorded decisions take precedence.
Consider indirect effects of commands, including CI, publication, and deployment,
before acting; reading a guide grants no additional authorization.

| Work | Read first |
| --- | --- |
| Code, configuration, dependency, or documentation changes/review | `docs/agent-guidance/general.md` |
| Investigation, planning, or tool use | `docs/agent-guidance/agent-workflow.md` |
| Changes needing validation, test work, CI fixes, or release preparation | `docs/agent-guidance/testing.md` |
| Kotlin, Gradle, Android, or Multiplatform | `docs/agent-guidance/kotlin.md` |
| Compose UI or its platform integration | `docs/agent-guidance/compose.md` |
| Python code, packaging, or interpreter/dependency changes | `docs/agent-guidance/python.md` |
| Services, APIs, persistence, or backend concurrency | `docs/agent-guidance/backend.md` |
| Browser UI, navigation, assets, or public web content | `docs/agent-guidance/frontend.md` |
| CI status/failures, workflows, actions, or workflow-triggering operations | `docs/agent-guidance/ci.md` |
| Versions, changelogs, tags, release artifacts, or publication | `docs/agent-guidance/release.md` |
```

Verify every selected task section has a route, every route resolves to its local
file, and representative tasks read guidance from both root and nested working
directories. Apply the one-time import checks above; staging `--check` cannot verify
routing or the final import. Do not use eager `@` imports for task files.

Git, security, and deployment currently contain only Core rules. Keep CI/release
bullets intact even when they mix details with approval gates; do not shorten or
split them for a size target. Core retains required verification and security,
Git, CI, release, deployment, and cost safeguards for the selected modules.

Use nested `AGENTS.md` instead of a task-file copy only where all supported workflows
discover the directory scope; retain root routes for agents started elsewhere.
Root path headings alone do not control discovery, and directory scope alone cannot
route operation-based tasks. Existing layouts change only on authorized updates;
conversion from maintained sync to a one-time import requires an explicit request.
Placement changes alone require no wording migration.

### Maintained synchronization

Follow the [README sync commands](../README.md). The offline composer reads selected
release-commit blobs into one managed `AGENTS.md` section and records tag, commit,
and ordered module selection. It includes **Core and Task guidance inline**;
headings do not defer loading. Upstream checks and updates are never automatic.

- Preserve local bytes outside the block; initial insertion may add separating
  newlines. `--check` detects shared-content/metadata drift offline without writing
  and permits local edits outside the block.
- Malformed markers, unknown modules, symlinked outputs, and moved saved tags fail
  before writes. Initial pinning trusts the release; later syncs reject a changed
  commit for that saved tag.
- Each file is replaced atomically; the pair is not a transaction. After interrupted
  I/O, rerun sync and review both files before committing.
- For directory scope, use `--target` on an existing subdirectory, select only its
  modules, keep shared modules at the parent, and verify actual working-directory
  discovery. Each target has its own pin and `--check`. Use the one-time recipe for
  operation-based routing.

### Replacing the legacy delivery module

Since v1.2, `git ci release deployment` are independently selectable. Deprecated
`delivery` retains its v1.1.1 wording; old pins and existing selections remain valid.
CLI options, markers, and manifest fields are unchanged. New integrations should
use the focused modules; never combine them with overlapping `delivery`.

For an authorized maintained migration, inspect the saved selection and replace
`delivery` with the desired modules, retaining other names and their order. Pass the
**entire selection**: `--modules` replaces it. Choose fewer delivery topics only if
they are outside the intended scope. From the v1.2 checkout, replacing
`general delivery testing` with all four:

```sh
python3 scripts/sync.py --target /path/to/project --ref v1.2.0 \
  --modules general git ci release deployment testing
python3 scripts/sync.py --target /path/to/project --check
```

Review both generated files before committing. Without `--modules`, upgrades
preserve the saved selection, including `delivery`. Never hand-edit the manifest or
managed block to migrate. Refresh one-time imports only on explicit request using
the staging and reconciliation workflow above; do not run maintained sync on
consolidated imports.

## Module boundaries

Select modules by relevant operations and platforms; see [README examples](../README.md).
Modules have no implicit dependencies. Each retains approval/validation gates for
its actions, including when companion modules are absent. Shared principles and
specialized mechanisms have one owner; limited overlap supports independent use.
The frozen `delivery` snapshot provides compatibility without aliases or a second
owner for new rules; removing it requires a future major release.

## Context measurements

The 13 recommended modules total **23,130 bytes**; with legacy `delivery`, the source
collection totals **27,197 bytes**.
These fixture measurements compare full Inline and Core + Task root instructions
with identical selections: README Kotlin/Python examples and all 13 for mixed.

| Configuration | Inline root bytes | Core + Task root bytes | Reduction |
| --- | ---: | ---: | ---: |
| Kotlin/Compose library | 17,657 | 10,255 | 41.9% |
| Python/backend service | 18,484 | 11,594 | 37.3% |
| Mixed platform | 23,422 | 11,873 | 49.3% |

UTF-8 sizes include routing, titles, and attribution with a 40-character commit;
exclude project/global rules, MIT notice contents, history, and tool framing.
Small selections for Git, CI, or releases stay inline. These are instruction sizes,
not measured token, latency, billing, or adherence improvements.

Task reads add context: typical Kotlin and Python code work reaches 18,390 and
19,246 bytes, about 4% above Inline. Reading every task file also exceeds Inline;
content accumulates without automatic eviction. Recheck routes as scope expands:
dependency, CI, or infrastructure work may also need language/backend guidance.
Keep safeguards intact regardless of root size. See [loading evidence and limits](compatibility.md#limits-and-verification).

## Curation decisions

- Keep rules addressing concrete failures or recurring engineering decisions;
  avoid arbitrary limits, speculative abstractions, and mandated architectures.
  Repeat cleanup, cancellation, or
  validation mechanisms only where independent module use needs them.
- Keep documentation guidance in `general`: reader needs and scoped replacement
  of stale or repetitive content control growth without size quotas. Preservation
  and required verification stay in Core; writing guidance uses the existing
  documentation route. Routine user-documentation cleanup does not authorize
  shortening agent instructions.
- Match verification to risk and authorization; required project checks apply.
  No blanket build ban or test mandate for every docs edit. Push-only work stops
  after reporting; CI fixing includes authorized investigation and verification.
- Consumer versioning/releases remain optional and project-owned. Apply
  [SemVer](https://semver.org/spec/v2.0.0.html) only where adopted; collection release
  conventions do not bind consumers. The synchronizer accepts stable tags only.
- [Secret handling](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  and [incident cleanup](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository):
  revoke/rotate exposures; history cleanup needs separate authorization and cannot
  erase other copies. Preserve legitimate public attribution and contacts.
- [CI security](https://docs.github.com/en/actions/reference/security/secure-use):
  respect consumer action/workflow pins, review publishers, and separate privileges.
  Full SHAs identify immutable revisions; tags can move. This repository uses version tags.
- Preserve [Kotlin](https://kotlinlang.org/docs/coroutines-cancellation.html) and
  [Python](https://docs.python.org/3/library/asyncio-exceptions.html) cancellation,
  and [Compose lifecycle/effect keys](https://developer.android.com/develop/ui/compose/side-effects).
- Apply [authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
  to protected resources without requiring authentication for public content.
- Keep read-only reviews free of tracked-file changes. Deployment changes require
  applicable operational guidance and current settings; unresolved billing impact
  cannot be treated as permission to increase costs. These safeguards stay in Core.
- Extend provenance and permission checks to copied code and non-code material in
  `security`, reusing the project's notice mechanism without imposing a license or
  tool. [REUSE](https://reuse.software/spec-3.3/) describes file-level licensing
  information, including material that cannot carry inline notices.
- Keep static asset cache details in the existing `frontend` task route:
  [fingerprinted resources and revalidatable HTML](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching#common_caching_patterns)
  have different freshness needs. This extends the existing cache policy rule.
- [Task-relevant retrieval and checkpoints](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  inform the design; they are not evidence of measured agent performance.
