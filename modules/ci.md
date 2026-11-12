# CI workflows

## Core

- For CI verification, inspect checks and report status. For CI fixing, investigate,
  fix, validate locally, then push and monitor within authorization until checks
  pass or a meaningful blocker prevents progress. Force-pushes, published-history
  rewrites, and branch-protection bypasses require explicit permission; CI grants
  no extra deployment or release authority.
- Check pull requests and each published/deployed revision. Where practical, build
  once and promote the checked artifact; never substitute an unchecked branch tip
  or another commit's status.
- Minimize CI permissions and secrets; separate untrusted contribution checks from
  privileged publication. Never execute untrusted checkouts or artifacts with
  privileged `pull_request_target` or `workflow_run` credentials.
- Pass untrusted event values as data arguments or environment variables, never
  interpolated shell code. Disable unneeded persisted checkout credentials.
- Get explicit approval for new paid CI services or recurring CI cost increases.

## Task guidance

- Distinguish introduced, pre-existing, and infrastructure failures. Avoid redundant
  polling, unchanged checks, unbounded retries, and unrelated fixes.
- Pin supported toolchains and restore dependencies reproducibly. Key caches by
  relevant inputs; support misses. Set timeouts; cancel obsolete checks without
  interrupting releases requiring serialization.
- Preserve project GitHub Action and reusable-workflow pinning policy. Full commit
  SHAs identify immutable revisions; tags can move. Review source repositories,
  publishers, and changes before adoption or updates.
