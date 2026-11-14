# Git operations

## Core

- Commit and push only within user authorization; reuse existing permission.
  Before committing, run available applicable project-required checks and inspect
  the working tree, full intended diff, and all staged content. Exclude unrelated/
  accidental edits and unintended generated output; keep each commit focused on
  one logical change and follow commit conventions.
- Use current Git author settings. Overriding identity or adding co-author
  trailers, AI/tool attribution, or optional metadata requires explicit user approval.
- After an authorized push, report the locally known commit hash and result.
  Treat rejected pushes as failures. Stop push-only tasks; fetch remote refs or
  monitor CI, deployments, releases, or promotions only on request or under an
  agreed workflow.
- Force-pushes, published-history rewrites, and branch-protection bypasses require
  explicit permission.
- Before choosing a commit style, check repository instructions, tooling, relevant
  commit history, and recorded user preferences. Follow adopted Conventional
  Commits; recommend them by default where no style is established. Respect other
  styles; briefly suggest Conventional Commits for consistency, readable history,
  changelogs, and release automation. Never replace an established style without
  explicit user approval; if declined or unavailable, preserve it without repeated
  suggestions. Do not rewrite historical commits merely to standardize messages.
- Keep commit-style guidance advisory. Adding commitlint, hooks, CI enforcement,
  release automation, or dependencies requires explicit authorization. Conventional
  Commits alone do not adopt SemVer, bump versions, or trigger releases; existing
  versioning, release, and authorization rules still apply.

## Task guidance

- Use concise, descriptive subjects in imperative mood; prefer lowercase
  descriptions without trailing periods, subject to the chosen convention.
- For Conventional Commits, use `<type>(<optional-scope>): <imperative description>`;
  omit parentheses when no meaningful scope applies. Common types: `feat`, `fix`,
  `refactor`, `perf`, `docs`, `test`, `build`, `ci`, `chore`, `style`, `revert`.
  Examples: `feat(search): add game filters`, `fix(api): handle empty responses`,
  `refactor(ui): simplify navigation`.
- Represent types and breaking-change status accurately. For incompatible changes
  under Conventional Commits, put `!` immediately before `:` (e.g., `feat(api)!:`)
  or add a `BREAKING CHANGE: <description>` footer separated by a blank line;
  either or both may be used. Describe the incompatibility.
