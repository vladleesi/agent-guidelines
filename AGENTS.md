# Maintaining agent-guidelines

- Keep reusable rules in `modules/`. This file governs this repository only;
  never generate it into consumer instructions.
- Give each rule one owning module. Keep modules independently usable without
  implicit imports or required companions. Split only for practical reuse.
- Keep security, authorization, and required-verification safeguards in Core.
  Task guidance needs explicit read-before-work routes; headings alone do not
  control loading. Validate placement and coverage when changing either section.
- Write direct, observable rules. Remove agent defaults unless they address a
  demonstrated failure or useful engineering constraint.
- Exclude project commands, infrastructure, personal details, and vendor
  adapters from modules. Verify technical claims against current primary
  sources.
- Keep sync dependency-free and deterministic. Preserve consumer bytes outside
  managed blocks; reject malformed markers and unsafe output paths.
- Update tests/docs for selection, output, or compatibility changes. For
  sync/module changes, run `python3 -m unittest discover -s tests -v`; for
  docs-only changes, review affected links/examples. Run `git diff --check`
  before delivery.
- Treat module names, CLI options, manifest fields, and managed markers as
  public interfaces; document migrations for incompatible changes.
- Version the collection together with immutable `vMAJOR.MINOR.PATCH` tags from
  `v1.0.0`: MAJOR for incompatibility, MINOR for compatible additions, PATCH for
  compatible fixes. Record material changes in `CHANGELOG.md`.
- Separate changelog entries into `### Reusable agent guidelines` and
  `### Repository updates`; omit empty sections.
- The first dated changelog entry supplies the release version/notes. CI creates
  its tag and GitHub Release only after all checks pass on that `main` commit.
  Never move published tags or replace release notes; use a new version.
- Use one README shell version variable for checkout paths, clone refs, and sync
  refs; update it with the prompt pin. Use the release being prepared, or the
  latest published stable release for stale-example fixes. No version bump for
  README-only corrections.
- Keep README a short entry point; put discovery caveats and source rationale in
  existing docs.
