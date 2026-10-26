# Changelog

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
