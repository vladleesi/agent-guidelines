# CI workflows

## Core

- For CI verification, inspect relevant checks and report status. For CI fixing,
  investigate failures, fix and validate locally, then push and monitor within
  authorization until checks pass or a meaningful blocker prevents progress.
  Force-pushes, published-history rewrites, and branch-protection bypasses still
  require explicit permission; CI work grants no extra deployment or release authority.
- Run relevant checks on pull requests and any revision a workflow publishes or
  deploys. Where practical, build once and promote the checked artifact; never
  substitute an unchecked branch tip or another commit's stale status.
- Minimize CI permissions and secrets; separate untrusted contribution checks from
  privileged publication. Never execute untrusted checkouts or artifacts with
  privileged `pull_request_target` or `workflow_run` credentials.
- Pass untrusted event values as data arguments or environment variables, never
  interpolated shell code. Disable unneeded persisted checkout credentials.
- Pin supported toolchains and restore dependencies reproducibly. Key caches by
  relevant inputs; support cache misses. Set job timeouts; cancel obsolete checks
  without interrupting releases requiring serialization. Get explicit approval for
  new paid CI services or recurring CI cost increases.

## Task guidance

- Distinguish failures introduced by changes from pre-existing or infrastructure
  failures. Avoid redundant polling, repeated unchanged checks, unbounded retries,
  and unrelated fixes.
- Preserve project GitHub Action and reusable-workflow pinning policy. Full commit
  SHAs identify immutable revisions; tags can move. Review source repositories,
  publishers, and changes before adoption or updates.
