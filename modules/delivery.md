# Git, CI, and releases

- Keep commits coherent and review the final diff and staged filenames for accidental
  edits, secrets, and generated output. Follow the project's commit convention.
  Perform commits, pushes, releases, deployments, and history rewrites only within
  the user's authorization, reusing authorization already granted.
- Run relevant checks on pull requests and the revision being released. Build once
  and promote the checked artifact where practical; do not substitute an unchecked
  branch tip or rely on stale status from another commit.
- Give CI jobs minimal permissions and secrets. Separate untrusted contribution
  checks from privileged publication. Never execute untrusted checkout or artifacts
  with privileged `pull_request_target` or `workflow_run` credentials.
- Pass untrusted event values through data arguments or environment variables,
  not interpolated shell code. Disable persisted checkout credentials when unneeded.
- Reference GitHub Actions and reusable workflows with explicit release version
  tags, not commit SHAs or branch names. Review the publisher and changes before
  updating; tags can move and do not provide an immutability guarantee.
- Pin supported toolchains and restore dependencies reproducibly. Key caches by
  relevant inputs; ensure cache misses still work. Bound jobs with timeouts and
  cancel obsolete checks without interrupting releases that require serialization.
- Follow the project's versioning contract. For SemVer APIs, distinguish incompatible
  changes, compatible additions, and fixes; document migration steps and user-visible
  changes. Preserve published history, tags, and assets; issue a new release for corrections.
- Before deployment or infrastructure changes, check cost, data, rollback, and
  compatibility implications. Use protected environments and short-lived credentials
  where supported.
