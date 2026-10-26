# Design notes

## Integration workflows

The default one-time import makes selected rules self-contained local instructions.
Record the source repository, release, commit, selected modules, and MIT notice
alongside them. Reading requires no manifest or upstream checkout. Record that
fetching, comparing with, or updating this collection requires explicit request;
attribution links grant no upstream access.

Stage each selection with the pinned synchronizer in an empty temporary target;
run `--check` there with the same source checkout. This verifies only the staged
section/manifest. Group selected rules with existing instructions by topic; omit
the staging manifest, markers, and sync notice. Outside imported text, retain
attribution, directory scope, and project-specific precedence. Preserve unrelated
files and customizations.

Preserve directory, language, platform, and agent scope. Headings/order may change;
retained imported bullets, including continuations, stay verbatim. Never rephrase,
split, or merge them. Remove only wholly redundant imported copies; retain partial
overlaps unchanged.

Rewrite only locally maintained target instructions; preserve global,
organization-managed, generated, and unrelated instructions unless explicitly
authorized. Local rules may be split, shortened, rewritten, or removed only if
every distinct requirement, scope, strength, exception, and affected agent remains
covered. For partial overlaps, keep imported bullets intact and only additional
local requirements. A newer source alone proves no equivalence. Keep stronger or
conflicting project requirements as concise overrides outside imported text.
Retain uncertain requirements; report conflicts precedence cannot resolve. Use
nested files for useful scope; root-file path headings do not control discovery.
Use the placement recipe below and check [instruction discovery](compatibility.md).

After placement/deduplication, compare retained bullets with pinned source, check
for lost local requirements, verify scope/discovery, and run `git diff --check`.
Add adapters/config only as needed; report discovery checks/limitations without
adding standard discovery explanations to consumer instructions. Staging `--check`
does not validate final consolidated files. Do not sync a one-time import unless
maintained integration is explicitly requested.

### Task-based loading

For new one-time imports into agents with local file-reading tools, use the
module sections as placement hints. They do not change rule scope or activate
loading by themselves; every module still works alone and in full inline form.
Keep modules without placement sections, including legacy `delivery`, fully inline.

1. Keep existing project architecture, commands, critical conventions, decisions,
   restrictions, and overrides in their applicable automatically discovered files.
   Copy **Core** sections of selected modules there, verbatim. These retain Git
   safety, all security/privacy rules, required verification, project precedence,
   CI privilege/check/cost gates, release approval/validation, and deployment gates.
   A selection only covers its selected modules; this recipe adds no dependencies.
2. Copy each selected **Task guidance** section into an ordinary local Markdown
   file, normally `docs/agent-guidance/<module>.md`, with its module title. Keep
   each bullet once across core and task files. Reuse an existing appropriate
   documentation directory where available; create no empty files. Copy the MIT
   notice alongside the guidance and record release, full commit, and selection
   in the root instructions. No runtime manifests, scripts, or network are needed.
3. Add the following routing text to the applicable `AGENTS.md`, keeping only rows
   for task files actually installed. Adjust paths to the local layout and add
   concrete project paths when they clarify scope. Preserve applicable directory,
   platform, and agent restrictions in both the route and destination. Never defer
   Core rules or move scoped rules to a broader scope merely to save bytes.

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

4. Retain source attribution and the explicit-request-only upstream policy from
   the one-time workflow. Verify every imported bullet against the pinned source,
   every route against its local file, and every selected task section against a
   route. Test representative tasks from root and nested working directories.
   A successful staging `--check` is not a routing or final-import check.

Git, security, and deployment currently contain only Core rules: they need no task
file. Some CI and release details stay in Core because splitting their bullets
would weaken verbatim imports or move approval gates out of automatic context.
Do not shorten them to hit a size target. Core is a placement category, not a new
module or a requirement to import modules irrelevant to a repository.

Use the full inline layout for small selections or interfaces without dependable
root discovery and local file reads. Do not use eager `@` imports for task files.
Existing consumers retain their layout until an authorized integration update;
changing placement alone needs no wording migration. Do not dismantle a maintained
integration unless conversion to the one-time workflow is explicitly requested.

Native nested `AGENTS.md` files remain useful for genuinely directory-specific
rules. Use them instead of a task-file copy when all supported workflows discover
that scope, and retain explicit root routing for agents started elsewhere. A
release can affect the whole repository without touching a release directory, so
directory nesting alone cannot implement operation-based loading. Agent-specific
glob systems add configuration and divergent discovery without solving that case
portably. Further wording compression cannot remove irrelevant topics from context.
The hybrid therefore changes placement, not the synchronization architecture.

### Maintained synchronization

Optional maintained synchronization keeps a generated section and manifest for
deliberate updates, never automatic upstream checks/updates. The offline composer
reads selected `modules/*.md` blobs from a release commit, writes one marked section,
and records tag, commit, and ordered selection. Committed instructions need neither
composer nor network.

The composer deliberately includes Core and Task guidance together; it does not
interpret headings or generate a second layout. For directory-scoped maintenance,
run it with `--target` set to the existing subdirectory and select only that scope's
modules. Keep shared modules at the parent and verify discovery from the working
directories actually used. Each target has its own pin and `--check`; this is not
per-task loading. Prefer the one-time recipe for operation-based routing.

Subsequent syncs preserve local bytes outside the section; initial insertion may add
separating newlines. Malformed markers, unknown modules, symlinked outputs, and moved
saved tags fail before writes. Each output is replaced atomically, but the pair is
not a transaction. After interrupted I/O, rerun sync and review both files before
committing. `--check` verifies shared content/metadata, allowing local edits. Initial
pinning trusts the selected release; later syncs reject a different commit for that
saved tag.

### Replacing the legacy delivery module

Version 1.2 adds `git ci release deployment` while retaining deprecated `delivery`
with its v1.1.1 wording. Existing selections can upgrade without renaming modules;
old pins keep their original text. CLI options, markers, and manifest fields are
unchanged, and nothing updates automatically. Do not select `delivery` alongside
its replacements: their rules overlap.

To opt into the focused modules, inspect the saved selection and replace `delivery`
with the desired modules, preserving the other names and their order. Pass the
**entire selection**: `--modules` replaces the list rather than appending to it.
From the v1.2 source checkout, this example migrates `general delivery testing` while
retaining all four delivery topics:

```sh
python3 scripts/sync.py --target /path/to/project --ref v1.2.0 \
  --modules general git ci release deployment testing
python3 scripts/sync.py --target /path/to/project --check
```

Review both generated files before committing. Without an explicit `--modules`
replacement, an upgrade preserves `delivery` and the rest of the saved selection.
Choose fewer replacement modules only when those activities are outside the
intended scope. Do not hand-edit the manifest or managed block to migrate.

One-time imports need no migration until an update is explicitly requested. Use
the one-time staging and reconciliation workflow above for an authorized refresh;
do not run maintained sync against consolidated instructions.

## Module boundaries

Git operations, CI workflows, versioned publication, and deployment have different
consumers: libraries can select `git ci release`, websites `git ci deployment`,
services all four, and Git-only tasks just `git`.
Combining CI and releases would make websites load versioning policy; combining
releases and deployments would make libraries load hosting policy.

Each module retains the approval and validation gates for actions it can initiate.
For example, CI fixes still need permission for history rewrites, and paid runners
still need cost approval without selecting `git` or `deployment`. This limited
overlap makes the modules independent; detailed policies have one owner.

The split uses ordinary files and explicit selection. A frozen legacy `delivery`
module keeps this addition compatible with a minor release without alias expansion
or synchronizer changes. It is a compatibility snapshot, not a second owner for new
rules; removing it would require a future major release. New integrations should
select the focused modules. Selection removes irrelevant modules; Core/Task
placement defers selected details until needed without requiring companion modules.

## Context measurements

Measured for the 13 recommended modules against their layout before Core/Task
headings, not the older published 10-module release. UTF-8 bytes and whitespace-separated words;
not tokens, latency, or billed usage. All 95 existing bullets remain byte-for-byte
identical, once each. No rule wording was shortened in this loading change.

| Module | Before bytes / words | After bytes / words |
| --- | ---: | ---: |
| agent-workflow | 1,793 / 241 | 1,821 / 246 |
| backend | 1,537 / 196 | 1,555 / 199 |
| ci | 1,739 / 226 | 1,767 / 231 |
| compose | 1,632 / 220 | 1,650 / 223 |
| deployment | 913 / 109 | 922 / 111 |
| frontend | 1,464 / 193 | 1,482 / 196 |
| general | 2,432 / 310 | 2,460 / 315 |
| git | 779 / 106 | 788 / 108 |
| kotlin | 1,671 / 222 | 1,689 / 225 |
| python | 1,283 / 166 | 1,301 / 169 |
| release | 1,407 / 188 | 1,435 / 193 |
| security | 2,648 / 330 | 2,657 / 332 |
| testing | 1,382 / 184 | 1,400 / 187 |
| **Total** | **20,680 / 2,691** | **20,927 / 2,735** |

The 247-byte increase is section labels. Legacy `delivery` is excluded from these
recommended selections and their totals; it is retained only for compatibility.
It adds 4,067 bytes / 531 words, making the complete source collection
24,994 bytes / 3,266 words. This does not increase consumers' selected context.
The following compares a full inline one-time import with the routed recipe,
using the same attribution/precedence
wrapper and a 40-character commit. Includes route text and module titles;
excludes project-specific rules, MIT notice contents, global instructions,
conversation history, and tool framing. The regression fixture constructs
these layouts; a consumer with existing local rules will be larger.

| Configuration | Before automatic bytes / words | After automatic bytes / words | Reduction |
| --- | ---: | ---: | ---: |
| Kotlin/Compose library | 15,975 / 2,078 | 9,292 / 1,194 | 41.8% |
| Python/backend service | 16,418 / 2,108 | 10,247 / 1,305 | 37.6% |
| Git only | 1,189 / 149 | 1,189 / 149 | 0.0% |
| CI only | 2,148 / 269 | 2,148 / 269 | 0.0% |
| Release only | 1,821 / 231 | 1,821 / 231 | 0.0% |
| Mixed platform | 21,215 / 2,746 | 10,526 / 1,339 | 50.4% |

Kotlin/Compose and Python/backend use the README selections; mixed platform selects
all 13 recommended modules, excluding `delivery`. Git-only, CI-only, and release-only
imports stay inline: routing adds little value when nearly every task needs the same
guide. No modules were omitted from the
large selections to obtain these savings. All deployment rules and some detailed
CI/release clauses remain automatic to retain intact authorization safeguards.
The larger core files exceed the suggested 4–8 KB range deliberately.

For a fresh mixed-platform session, add these **explicit file reads** to its
10,526-byte core. Names below refer only to the Task guidance portions; core rules
of selected modules already apply to every row.

| Task | Additional task files | Added bytes | Core + task bytes |
| --- | --- | ---: | ---: |
| Edit a Compose screen | general, agent-workflow, testing, kotlin, compose | 7,420 | 17,946 |
| Fix a Python backend bug | general, agent-workflow, testing, python, backend | 6,937 | 17,463 |
| Update a Python packaging dependency | general, agent-workflow, testing, python | 5,400 | 15,926 |
| Fix CI workflow configuration | general, agent-workflow, testing, ci | 4,537 | 15,063 |
| Prepare a release and check CI | general, agent-workflow, testing, ci, release | 4,811 | 15,337 |
| Change cloud hosting configuration | general, agent-workflow, testing | 4,117 | 14,643 |

These are bounded scenarios before any additional push/publication or unrelated
code work. A dependency affecting service behavior also needs backend guidance;
a CI failure in application code needs that language/domain guidance. Infrastructure
that changes workflows or service contracts also needs CI/backend guidance. Recheck
routes as scope changes. Ordinary task files are not automatically discovered.
Full code tasks in the smaller Kotlin and Python selections reach 16,712 and
17,184 bytes respectively, about 5% above their inline baselines. Those tasks gain
startup headroom, not lower total context after reading the relevant guidance.

Reading every task file reaches 17,406 bytes for Kotlin, 17,878 for Python, and
22,924 for mixed platform, slightly more than inline because of routing/titles.
Deferred content accumulates during a session; this is not automatic context
eviction. Actual loading tests and agent-specific limits are described in
[compatibility](compatibility.md#limits-and-verification).

## Curation decisions

- Keep rules that prevent concrete failures or guide recurring decisions. General
  modules own shared principles; specialized modules own platform mechanisms.
  Resource cleanup, cancellation, and validation recur where independent use needs
  specific mechanisms. Avoid arbitrary limits, speculative abstractions, and mandated
  architectures.
- Match validation to risk/authorization; no blanket build ban or test requirement
  for every docs edit. Required project checks still apply. Push-only tasks stop
  after reporting; CI fixing includes authorized investigation/verification.
- Consumer versioning/releases remain optional and project-owned.
  [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) governs compatibility,
  deprecation, pre-releases, and metadata only where adopted. This collection's
  `vMAJOR.MINOR.PATCH` releases are repository policy, not consumer requirements.
  The synchronizer accepts stable tags only, independently of consumer schemes.
- Disclosure review/incidents follow
  [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  and [GitHub's sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
  Revoke/rotate exposed credentials; history cleanup needs separate authorization
  and cannot erase other copies. Preserve legitimate public attribution/contacts.
- Respect consumer action/workflow pins: full commit SHAs identify immutable
  revisions; tags can move. This CI retains explicit version tags. Publisher review
  and privilege separation follow
  [GitHub's secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use).
- Preserve cancellation in [Kotlin](https://kotlinlang.org/docs/coroutines-cancellation.html)
  and [Python](https://docs.python.org/3/library/asyncio-exceptions.html), and use
  [Compose lifecycle/key guidance](https://developer.android.com/develop/ui/compose/side-effects).
- Apply [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
  to protected resources without requiring authentication for public content.
- Task-relevant retrieval/checkpoints follow
  [Anthropic's context guidance](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).
  This is design rationale, not measured agent performance. Discovery behavior
  comes from [official sources](compatibility.md).
