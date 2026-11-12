# Git operations

## Core

- Commit and push only within user authorization; reuse existing permission.
  Before committing, run available applicable project-required checks and inspect
  the working tree, full intended diff, and all staged content. Exclude unrelated/
  accidental edits and unintended generated output; keep commits coherent and
  follow commit conventions.
- Use current Git author settings. Overriding identity or adding co-author
  trailers, AI/tool attribution, or optional metadata requires explicit user approval.
- After an authorized push, report the locally known commit hash and result.
  Treat rejected pushes as failures. Stop push-only tasks; fetch remote refs or
  monitor CI, deployments, releases, or promotions only on request or under an
  agreed workflow.
- Force-pushes, published-history rewrites, and branch-protection bypasses require
  explicit permission.
