# Git, CI, and releases

- Commit and push only within the user's authorization, reusing authorization
  already granted. Inspect the working tree, complete intended diff, and full staged
  content before committing; exclude accidental edits, unrelated files, and unintended
  generated output. Keep commits coherent and follow the project's commit convention.
- After a successful authorized push, report the locally known commit hash and push
  result. For a push-only task, stop: do not fetch remote refs or monitor CI,
  deployments, releases, or promotions unless requested or required by an agreed
  workflow. Treat a rejected push as a failure; never force-push, rewrite published
  history, or bypass branch protection without explicit permission.
- When asked to verify CI, inspect the relevant checks and report their status.
  When asked to fix CI or make checks pass, investigate relevant failures, implement
  fixes, and validate locally. Push fixes and monitor those checks within the granted
  authorization; continue until they pass or a meaningful blocker prevents progress.
- Distinguish failures caused by the changes from pre-existing or infrastructure
  failures. Avoid redundant polling, repeated unchanged checks, unbounded retries,
  and unrelated fixes. A CI task does not authorize extra deployments or releases.
- Run relevant checks on pull requests and the revision being released. Build once
  and promote the checked artifact where practical; do not substitute an unchecked
  branch tip or rely on stale status from another commit.
- Give CI jobs minimal permissions and secrets. Separate untrusted contribution
  checks from privileged publication. Never execute untrusted checkout or artifacts
  with privileged `pull_request_target` or `workflow_run` credentials.
- Pass untrusted event values through data arguments or environment variables,
  not interpolated shell code. Disable persisted checkout credentials when unneeded.
- Preserve the project's GitHub Action and reusable-workflow pinning policy.
  Full-length commit SHAs identify immutable revisions; version tags can move.
  Review the source repository, publisher, and changes before adoption or updates.
- Pin supported toolchains and restore dependencies reproducibly. Key caches by
  relevant inputs; ensure cache misses still work. Bound jobs with timeouts and
  cancel obsolete checks without interrupting releases that require serialization.
- Inspect existing versioning, tag, release, changelog, and publication conventions
  before proposing changes. Do not replace another versioning scheme. Introduce or
  change versioning, tagging, releases, or release automation only with user approval;
  if absent, suggest them only for a relevant benefit and explain it briefly.
- Increment versions only under an existing policy or explicit authorization.
  Where SemVer 2.0.0 is adopted, classify changes against the declared public API:
  from `1.0.0`, use MAJOR for incompatible changes, MINOR for compatible additions
  or deprecations, and PATCH for compatible fixes. Reset lower components when
  incrementing MAJOR or MINOR; `0.y.z` has no stable API guarantee. Document
  user-visible changes and required migrations.
- Follow SemVer pre-release syntax and ordering when used: `-alpha.1` precedes the
  associated normal release, and numeric identifiers have no leading zeroes.
  `+build` metadata does not affect precedence. Do not invent pre-release conventions
  where the project has none.
- Publish releases only within granted authorization. Preserve published tags,
  release notes, and assets; use a new release for corrections unless the user
  explicitly authorizes changing published history.
- Before infrastructure or deployment changes, inspect the existing setup and use
  existing resources and the smallest safe change. Preserve hosting, domains, and
  deployment configuration unless the task requires changes. Assess security,
  availability, compatibility, data preservation, rollback, and financial impact;
  avoid speculative scaling and use protected environments where supported.
- Deploy, including to production, publish websites, or provision infrastructure
  only with existing authorization or explicit approval. Explain meaningful cost
  and operational consequences before seeking approval. Require explicit approval
  before enabling paid services or increasing recurring costs, including compute
  and minimum instances, storage, databases, networking, paid APIs, service tiers,
  build minutes, and managed services.
