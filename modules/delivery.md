# Git, CI, and releases

- Commit or push only as authorized; reuse existing permission. Inspect working
  tree, full intended diff, and all staged content before committing. Exclude
  accidental or unrelated edits and unintended generated output. Keep commits
  coherent and follow project commit conventions.
- After successful authorized pushes, report the locally known hash and push
  result. Stop push-only tasks: fetch remote refs or monitor CI, deployments,
  releases, or promotions only on request or under agreed workflows. Treat
  rejected pushes as failures. Force-push, rewrite published history, or bypass
  branch protection only with explicit permission.
- For CI verification, inspect relevant checks and report status. For CI fixing,
  investigate, fix, validate locally, then push and monitor within authorization
  until checks pass or a meaningful blocker prevents progress.
- Distinguish change-caused, pre-existing, and infrastructure failures. Avoid
  redundant polling, unchanged checks, unbounded retries, and unrelated fixes.
  CI tasks authorize no extra deployments or releases.
- Run relevant checks on pull requests and the release revision. Build once and
  promote the checked artifact where practical; never substitute unchecked
  branch tips or another commit's stale status.
- Minimize CI permissions and secrets; separate untrusted contribution checks
  from privileged publication. Never execute untrusted checkouts or artifacts
  with privileged `pull_request_target` or `workflow_run` credentials.
- Pass untrusted event values as data arguments or environment variables, never
  interpolated shell code. Disable unneeded persisted checkout credentials.
- Preserve GitHub Action and reusable-workflow pinning policy. Full commit SHAs
  identify immutable revisions; tags can move. Review source repositories,
  publishers, and changes before adoption or updates.
- Pin supported toolchains and restore dependencies reproducibly. Key caches by
  relevant inputs; support cache misses. Set job timeouts; cancel obsolete
  checks without interrupting releases requiring serialization.
- Inspect versioning, tag, release, changelog, and publication conventions
  first; do not replace another scheme. Introduce or change versioning, tags,
  releases, or release automation only with user approval. Suggest absent
  conventions only for a relevant, briefly explained benefit.
- Increment versions only under existing policy or explicit authorization. For
  adopted SemVer 2.0.0, classify the declared public API from `1.0.0`: MAJOR for
  incompatible changes, MINOR for compatible additions or deprecations, PATCH
  for compatible fixes. Reset lower components on MAJOR or MINOR increments;
  `0.y.z` offers no stable API guarantee. Document user-visible changes and
  migrations.
- Where used, follow SemVer pre-release syntax and ordering: `-alpha.1` precedes
  its normal release; numeric identifiers have no leading zeroes; `+build`
  metadata does not affect precedence. Do not invent pre-release conventions
  where the project has none.
- Publish only within granted authorization. Preserve published tags, notes, and
  assets; correct them in a new release unless explicitly authorized to change
  published history.
- Before infrastructure or deployment changes, inspect the setup, reuse
  resources, and choose the smallest safe change. Preserve hosting, domains, and
  deployment config unless the task requires otherwise. Assess security,
  availability, compatibility, data preservation, rollback, and financial
  impact. Avoid speculative scaling; use protected environments where supported.
- Deploy (including production), publish websites, or provision infrastructure
  only with existing authorization or explicit approval. Explain material cost
  and operational consequences before seeking approval. Require explicit
  approval to enable paid services or increase recurring costs: compute and
  minimum instances, storage, databases, networking, paid APIs, service tiers,
  build minutes, and managed services.
