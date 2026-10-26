# Maintaining agent-guidelines

- Keep reusable instructions in `modules/`. This file governs this repository only;
  never include it in generated consumer instructions.
- Give each rule one owning module. Keep modules independently usable, without
  implicit imports or required companion modules. Split only for practical reuse.
- Write direct, observable instructions. Remove rules that repeat agent defaults
  without addressing a demonstrated failure or useful engineering constraint.
- Keep project commands, infrastructure, personal details, and vendor adapters out
  of reusable modules. Verify technical claims against current primary sources.
- Keep synchronization dependency-free and deterministic. Preserve consumer bytes
  outside the managed block; reject malformed markers and unsafe output paths.
- Update tests and documentation when changing selection, output, or compatibility.
  For synchronization or module changes, run `python3 -m unittest discover -s tests -v`.
  For documentation-only changes, review affected links and examples. Run
  `git diff --check` before delivery.
- Treat module names, CLI options, manifest fields, and managed markers as public
  interfaces. Document migrations for incompatible changes.
- Version the collection together using immutable `vMAJOR.MINOR.PATCH` tags,
  starting at `v1.0.0`. Use MAJOR for incompatible changes, MINOR for compatible
  additions, and PATCH for compatible fixes. Record material changes in `CHANGELOG.md`.
- Separate reusable rule changes from repository maintenance in changelog entries
  using `### Reusable agent guidelines` and `### Repository updates`; omit empty
  sections.
- Use the first dated entry in `CHANGELOG.md` as the release version and notes.
  CI creates its tag and GitHub Release only after all checks pass on that commit
  on `main`. Never move published tags or replace release notes; use a new version.
- Keep one version variable in README shell examples and derive versioned checkout
  paths, clone refs, and sync refs from it. Update it and the prompt's release pin
  together. Use the version being released when preparing a release; use the latest
  published stable release when correcting stale examples. Do not increment the
  collection version for README-only corrections.
- Keep the README a short working entry point. Put discovery caveats and source
  rationale in the existing documents rather than expanding the quick start.
