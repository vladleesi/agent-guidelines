# Git operations

## Core

- Commit and push only within user authorization; reuse existing permission.
  Before committing, run applicable project-required checks available in the
  environment and inspect the working tree, full intended diff, and all staged
  content. Exclude accidental or unrelated edits and unintended generated output.
  Keep commits coherent and follow project commit conventions.
- After a successful authorized push, report the locally known commit hash and
  push result. Stop push-only tasks: fetch remote refs or monitor CI, deployments,
  releases, or promotions only on request or as required by an agreed workflow.
- Treat rejected pushes as failures. Force-pushes, published-history rewrites,
  and branch-protection bypasses require explicit permission.
