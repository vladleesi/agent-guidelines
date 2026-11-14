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
Paths are relative to this AGENTS.md. Recheck routes as scope changes or context
is compacted; reread guidance no longer in context. If required files are missing
or unreadable, report and stop affected work. These supplement Core; project-specific
instructions and recorded decisions take precedence. Consider indirect CI,
publication, and deployment effects before acting; reading grants no authorization.

| Work | Read first |
| --- | --- |
| Code, configuration, dependency, or documentation changes/review | `docs/agent-guidance/general.md` |
| Investigation, planning, change reviews, or tool use | `docs/agent-guidance/agent-workflow.md` |
| Changes needing validation, test work, CI fixes, or release preparation | `docs/agent-guidance/testing.md` |
| Kotlin, Gradle, Android, or Multiplatform | `docs/agent-guidance/kotlin.md` |
| Compose UI, scrolling/rendering performance, Baseline Profiles, or platform integration | `docs/agent-guidance/compose.md` |
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

Git, security, and deployment contain only Core rules. Core retains security,
authorization, cost, and required-verification safeguards for each selected module,
including when used alone. CI tuning and SemVer mechanics use existing task routes.
Keep imported bullets intact even when they mix details with safeguards; collection
maintainers may revise them, but consumers must preserve pinned wording.

Use nested `AGENTS.md` instead of a task-file copy only where all supported workflows
discover the directory scope; retain root routes for agents started elsewhere.
Root path headings alone do not control discovery, and directory scope alone cannot
route operation-based tasks. Existing layouts change only on authorized updates;
conversion from maintained sync to a one-time import requires an explicit request.
Placement changes alone require no wording migration.

v1.9 keeps module names and task routes compatible. When updating a one-time
import, reconcile full selected modules so relocated Core rules do not remain
deferred. Existing pinned copies remain valid; maintained sync needs no migration.

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

Source instruction sizes, including module titles and placement headings:

| Selection | v1.9.0 characters | v1.10.0 characters | Approx. tokens before → after | Increase |
| --- | ---: | ---: | ---: | ---: |
| 13 recommended modules | 25,166 | 25,926 | 6,292 → 6,482 | 3.0% |
| Including frozen `delivery` | 29,233 | 29,993 | 7,308 → 7,498 | 2.6% |

Module text is ASCII, so character and UTF-8 byte counts match. Token estimates
use characters / 4, rounded; actual tokenization varies by model. This is a size
comparison, not measured latency, billing, or adherence improvement.

These fixture measurements compare full Inline and Core + Task root instructions
at v1.10.0 with identical selections: README Kotlin/Python examples and all 13 for mixed.
Core + Task uses `one_time_files` in `tests/test_sync.py`; Inline uses the same
complete attribution header followed by full module texts, separated by blank
lines and ending with a newline.

| Configuration | Inline root bytes | Core + Task root bytes | Reduction |
| --- | ---: | ---: | ---: |
| Kotlin/Compose library | 21,074 | 12,143 | 42.4% |
| Python/backend service | 19,047 | 12,841 | 32.6% |
| Mixed platform | 26,462 | 14,482 | 45.3% |

UTF-8 sizes include routing, titles, and attribution with a 40-character commit;
exclude project/global rules, MIT notice contents, history, and tool framing.
Small selections for Git, CI, or releases stay inline. Compared with the v1.8.0
fixtures, Core + Task roots change from 12,459, 12,665, and 14,077 bytes respectively,
while retaining relocated safeguards and adding runtime verification.

Task reads add context: root plus general, workflow, testing, and the relevant
language/UI or language/backend guides reaches 21,122 bytes for Kotlin and 19,044
for Python, approximately Inline size. Reading every mixed-platform task file
reaches 27,921 bytes and exceeds Inline; context accumulates without automatic
eviction. Recheck routes as scope expands:
dependency, CI, or infrastructure work may also need language/backend guidance.
Keep safeguards intact regardless of root size. See [loading evidence and limits](compatibility.md#limits-and-verification).

## Curation decisions

- Keep interactive-feature runtime verification in `testing` Core so it applies
  before task guidance is loaded, including when testing is selected alone.
  Run the changed workflow in an appropriate browser, emulator, simulator, or
  physical device; report unavailable checks and their remaining gaps. This is a
  collection completion policy, informed by
  [user-visible browser testing](https://playwright.dev/docs/best-practices#test-user-visible-behavior)
  and [testing scope and runtime fidelity](https://developer.android.com/training/testing/fundamentals/strategies).
  Compilation and unit tests cannot establish all interactive behavior; physical
  devices are needed where simulated capabilities or performance are inadequate.
  Reuse the existing testing route; remove the superseded optional UI-check rule.
- Prefer concise decision rules over repeated instructions. Workflow guidance
  separates bounded retrieval, reuse, and checkpoints; project policy can require
  repeated checks. Read-only review protects new files as well as tracked content,
  with ordinary check artifacts allowed. Testing Core requires project checks even
  when selected alone; task guidance focuses additional checks. Keep specialized
  rules and limited safeguard overlap needed for independent module use.
- Keep change reviews focused on actionable issues caused by the diff, including
  indirect breakage. Evidence, deduplication, and a no-findings outcome reduce
  review noise. Long-task checkpoints retain objectives, constraints, failed
  approaches, and evidence locations to avoid repeated investigation; reuse
  existing task state. Both belong in `agent-workflow` Task guidance, whose route
  explicitly includes change reviews. Authorization and required checks stay in
  Core. Actual token savings and adherence across agents remain unmeasured.
- Keep rules addressing concrete failures or recurring engineering decisions;
  avoid arbitrary limits, speculative abstractions, and mandated architectures.
  Repeat cleanup, cancellation, or validation only for independent module use.
  In v1.9, merge related workflow, documentation, and Kotlin exception rules;
  remove duplicate wording, not unique constraints. Keep token-efficiency practices
  in `agent-workflow`, including targeted retrieval, bounded output, reuse, batching,
  concise communication, and stopping once evidence suffices. Required checks and
  scope/approval gates override efficiency shortcuts.
- Keep content-based parameter/property naming and source/format documentation in
  `general`; its existing code route covers all languages. Keep `runCatching`
  selection in `kotlin` under its existing task route. This is a readability
  preference for suitable fallbacks, not a blanket replacement for `try`/`catch`.
  [`runCatching`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/run-catching.html)
  catches any `Throwable`; preserve cancellation with either form and retain
  [`try`/`catch` and `finally`](https://kotlinlang.org/docs/exceptions.html#handle-exceptions-using-try-catch-blocks)
  for specific exception handling, cleanup, or rethrowing.
- Keep documentation guidance in `general`: reader needs and scoped replacement
  of stale or repetitive content control growth without size quotas. Preservation
  and required verification stay in Core; writing guidance uses the existing
  documentation route. Routine user-documentation cleanup does not authorize
  shortening agent instructions.
- Keep optimization scope and reversion safeguards in `general` Core. An
  optimization request does not authorize a redesign, new files or dependencies,
  or surrounding component changes; existing explicit approval still applies.
  Explain correctness limitations and propose the smallest alternative before
  expanding scope. Reverting restores and validates the prior design and behavior,
  including removal of additions used only by the optimization. Agents suggest
  rewrites, cleanups, and profiling, tracing, or benchmark investigations beyond
  the request with reasons and scope, then start them only on explicit approval;
  a request for that investigation is approval. Measurement and cache guidance
  stays in Task guidance under the existing general route.
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
- Keep Compose rendering and scrolling rules in `compose`; its existing task
  route also covers performance work and Baseline Profiles. Core keeps only
  scope and verification: rules apply to changed code, broader cleanups and
  rendering investigations need explicit approval (repeated from `general` so
  `compose` works alone), and performance claims need optimized physical-device
  comparisons. [Physical-device benchmarks](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
  represent production rendering; emulator timings do not. Rules name no project
  helpers, paths, or new dependencies.
- Task rules follow primary guidance: [lazy keys and content types](https://developer.android.com/develop/ui/compose/lists),
  [deferred reads and cached calculations](https://developer.android.com/develop/ui/compose/performance/bestpractices),
  [strong skipping](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)
  lambda memoization, [image sizing](https://developer.android.com/develop/ui/compose/graphics/images/optimization),
  [modifier nodes](https://developer.android.com/develop/ui/compose/custom-modifiers),
  and [compositing](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers).
  A viewport-sized [cache window](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/layout/package-summary)
  is a tuning start, not a reason to upgrade dependencies. [Remove redundant fills](https://developer.android.com/topic/performance/rendering/overdraw)
  rather than requiring single painting; clearing the [window background](https://developer.android.com/reference/android/view/Window#setBackgroundDrawable(android.graphics.drawable.Drawable))
  requires opaque replacement coverage. The [overdraw overlay](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering)
  counts extra draws, while the rule counts total draws. [Frame statistics](https://developer.android.com/tools/dumpsys#gfxinfo)
  and [HWUI frame data](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/libs/hwui/FrameInfo.h)
  separate UI-thread work from queue delay but do not measure GPU execution; use
  traces for compositor waits. Libraries and non-Android targets need no
  [Baseline Profile](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
  infrastructure.
- Rechecked affected technical claims against these primary sources on 2026-11-12.
  Current [Compose guidance](https://developer.android.com/develop/ui/compose/performance/bestpractices)
  distinguishes `computedStateOf` for cheap derivations on Runtime 1.13+ from
  `derivedStateOf` for older versions or expensive repeated calculations. Keep the
  module version-aware without requiring an upgrade or adding dependencies.
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
