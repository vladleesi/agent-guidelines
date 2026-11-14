# Changelog

## 1.10.0 — 2026-11-14

### Reusable agent guidelines

- Require runtime verification of changed interactive features in an appropriate
  browser, emulator, simulator, or physical device, including affected states and
  platforms, runtime errors, and explicit reporting of verification gaps.
- Add diff-scoped, evidence-backed review findings to `agent-workflow`, including
  indirect breakage, deduplication, and an explicit no-findings outcome.
- Extend long-task checkpoints with objectives, constraints, failed approaches,
  and evidence references while reusing existing task state.
- Tighten exploration and documentation guidance without removing constraints.
  Clarify that read-only reviews also protect new project files while permitting
  ordinary check artifacts, and keep required checks explicit in standalone testing
  guidance. Project policy can require repeated checks.

### Repository updates

- Document runtime verification, review, and checkpoint rationale, make review
  routing explicit, and refresh context measurements and README pins.
  Module selections, sync interfaces, and managed markers remain compatible.

## 1.9.0 — 2026-11-12

### Reusable agent guidelines

- Condense all recommended modules, merging related workflow, documentation,
  and exception-handling rules while preserving scope, approval gates, security,
  and validation requirements. Keep the legacy `delivery` snapshot unchanged.
- Extend `agent-workflow` with targeted reads/searches, bounded output, reuse of
  findings, batched independent operations, concise communication, and stopping
  criteria scaled to task complexity and risk.
- Keep backend/Python security and language, packaging, distributable, migration,
  and public-page verification safeguards in Core. Defer CI tuning and SemVer
  mechanics through existing task routes; preserve independent module use.
- Make Compose derived-state guidance account for supported versions, including
  `computedStateOf` for inexpensive derivations.

### Repository updates

- Update Core placement and standalone routing coverage, context measurements,
  source rationale, and README pins. Module names, selections, CLI options,
  manifest fields, markers, and synchronization behavior remain compatible.

## 1.8.0 — 2026-11-09

### Reusable agent guidelines

- Add Compose rendering and scrolling guidance: single background ownership,
  lazy keys, content types, and cache windows, composition work, deferred state
  reads, image sizing, modifier nodes, offscreen effects, and overdraw/frame
  investigation. Rules use each project's existing tokens, helpers, and loaders.
- Require explicit approval before rewrites, cleanups, or performance
  investigations such as profiling, tracing, or benchmarks beyond the requested
  change; agents suggest them with reasons and scope when evidence shows a need.
- Scope Compose rules to changed code and move platform checks to Core. Base
  Android rendering-performance claims on optimized physical-device before/after
  comparisons, state unmeasured effects, and remind users about Baseline Profile
  coverage.

### Repository updates

- Extend the Compose task route to performance work and Baseline Profiles; add
  Compose Core placement tests, source rationale, recomputed context
  measurements, and README release pins.

## 1.7.0 — 2026-10-31

### Reusable agent guidelines

- Require current Git author settings in `git` Core. Overriding author identity
  or adding co-author trailers, AI/tool attribution, or other optional commit
  metadata requires explicit user approval.

### Repository updates

- Update README release pins, context measurements, and Core placement coverage
  for the commit attribution safeguard.

## 1.6.0 — 2026-10-31

### Reusable agent guidelines

- Specify content-based parameter and property names in `general`; document
  parameters when their source or format is not clear from their names.
- Add a readability-based `runCatching` preference in `kotlin` for suitable
  non-suspending fallbacks. Retain `try`/`catch` for specific exceptions, cleanup,
  and rethrowing, with cancellation propagation preserved in either form.

### Repository updates

- Update README release pins, naming and exception-handling rationale, and
  context measurements. Existing general and Kotlin task routes cover the rules.

## 1.5.0 — 2026-10-30

### Reusable agent guidelines

- Add optimization safeguards to `general` Core: preserve the existing design,
  prefer the smallest local diff, and require explicit approval for new
  architecture, configuration schemes, dependencies, files, or surrounding
  component changes. Reuse existing approval; explain correctness limitations
  and propose the smallest alternative before editing beyond the original scope.
- When reverting an optimization, restore and validate the prior design and
  behavior, remove additions used only by that optimization, and preserve
  unrelated changes.

### Repository updates

- Update README release pins, optimization rationale, context measurements, and
  Core placement coverage for the new safeguards.

## 1.4.0 — 2026-10-29

### Reusable agent guidelines

- Add Core safeguards for read-only reviews and unavailable deployment guidance
  or settings. Clarify that optimization and deployment requests do not authorize
  higher recurring costs; resolve uncertain billing impact before applying changes.
- Extend `security` to cover provenance, notices, and use/redistribution permissions
  for copied code, fonts, icons, assets, and data without imposing a license or tool.
- Consolidate deployment preflight guidance and extend the existing `frontend`
  cache rule for fingerprinted static assets and revalidatable HTML entry points.

### Repository updates

- Update README release pins, source rationale, context measurements, and Core
  placement coverage for the new safeguards.

## 1.3.0 — 2026-10-28

### Reusable agent guidelines

- Extend `general` documentation rules for new and existing docs and published-site
  copy: write for intended readers, replace stale explanations, remove repetition,
  and exclude task history and unnecessary detail. Preserve essential contracts,
  safeguards, notices, release history, generated specifications, and agent
  instructions; verify affected links, anchors, and examples after restructuring.

### Repository updates

- Update README release pins, documentation curation rationale, context
  measurements, and Core placement coverage for documentation safeguards.

## 1.2.0 — 2026-10-26

### Reusable agent guidelines

- Add independently selectable `git`, `ci`, `release`, and `deployment` modules.
  Deprecate `delivery` but retain its published wording for compatibility.
  Retain action-specific authorization,
  validation, history protection, and cost approval without required companions.
- Restore qualifiers lost during compaction: applicable project checks, sequencing
  edits, repeated unchanged CI checks, and navigation state needed after reload.
  Clarify Compose interaction targets, README purpose, and authorized changes to
  existing release conventions.
- Mark Core and Task guidance within the 13 recommended modules for selective placement;
  preserve every rule verbatim and keep security and authorization gates in Core.

### Repository updates

- Document optional replacement of `delivery` and update README examples/pins.
  Existing selections remain valid; no automatic aliases, updates, or selection
  changes are introduced. Synchronizer interfaces and behavior are unchanged.
- Cover independent operational selections, legacy pins, compatible upgrades,
  and explicit selection changes with synchronization regression tests.
- Default new one-time imports to a local core plus explicitly routed task guidance
  when the agent can read local files. Document eager and directory-scoped fallbacks,
  discovery differences, context measurements, and import coverage checks. Keep the
  maintained synchronizer's full inline output and public interfaces unchanged.

## 1.1.1 — 2026-10-25

### Reusable agent guidelines

- Compact all ten modules while preserving requirements, authorization boundaries,
  security, cancellation, validation, and release safeguards. Keep modules
  independently usable and retain their names and scopes.

### Repository updates

- Shorten repository instructions, the import prompt, and integration documentation;
  retain verbatim pinned imports, project precedence, licensing, and both workflows.
- Clarify Codex's configurable 32 KiB project-instruction budget and refresh source
  references. Synchronization, manifests, markers, CI, and published releases remain
  unchanged.

## 1.1.0 — 2026-10-25

### Reusable agent guidelines

- Strengthen disclosure review, secret handling, privacy, and incident guidance while
  preserving legitimate public attribution and project metadata.
- Respect recorded user decisions, optional tooling, and existing version, tag,
  release, and action-pinning conventions; clarify adopted SemVer 2.0.0 rules.
- Require available project checks before readiness or commits, stop after push-only
  tasks, and support authorized CI investigation, fixing, and verification.
- Cover existing published websites and require authorization for deployments,
  infrastructure provisioning, paid services, and recurring cost increases.

### Repository updates

- Refresh module descriptions and source rationale without changing synchronization,
  discovery, module names, manifests, or managed markers.
- Read current `main` check-suite status in the README badge so queued or running
  checks are represented instead of reusing the previous workflow result.
- Set the README shell example's release in one variable, derive its versioned
  temporary checkout path, and record the convention in repository instructions.

## 1.0.3 — 2026-10-25

- Make the README prompt copyable and default to a self-contained, one-time import
  that preserves rule wording, removes equivalent duplicates, and retains
  project-specific constraints and overrides.
- Document temporary synchronization checks, final text and discovery verification,
  source attribution and licensing, and upstream access only on explicit request.
  Keep maintained synchronization as an optional workflow.
- Align README examples with `v1.0.3` and record repository guidance to update all
  release pins together without version bumps for README-only corrections.
- Keep the checks badge in the shared flat-square style and include all workflow
  events on `main`, with a matching branch-filtered workflow link.

## 1.0.2 — 2026-10-25

- Remove unrelated project references and research history from public design notes.

## 1.0.1 — 2026-10-25

- Create version tags and GitHub Releases from the changelog after both CI test
  jobs pass on the exact `main` commit; preserve existing releases on reruns.
- Refresh the README with flat-square badges, a clearer quick start, and concise
  guidance for module selection, local rules, and intentional updates.

## 1.0.0 — 2026-10-25

- Add ten independently selectable engineering and agent-workflow modules.
- Compose release-pinned instructions into a managed `AGENTS.md` section while
  preserving project rules and recording the source commit and selection.
- Add offline drift checks, Claude Code import adapter, compatibility guidance,
  synchronization regression tests, and MIT licensing.
