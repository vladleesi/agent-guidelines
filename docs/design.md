# Design notes

## Integration workflows

The default one-time import makes selected rules self-contained local instructions.
Record the source repository, release, commit, selected modules, and MIT notice
alongside them. Reading requires no manifest or upstream checkout. Record that
fetching, comparing with, or updating this collection requires explicit request;
attribution links grant no upstream access.

Stage each selection with the pinned synchronizer in an empty temporary target;
run `--check` there with the same source checkout. This verifies only the staged
section/manifest. Group selected rules with existing instructions by topic; omit
the staging manifest, markers, and sync notice. Outside imported text, retain
attribution, directory scope, and project-specific precedence. Preserve unrelated
files and customizations.

Preserve directory, language, platform, and agent scope. Headings/order may change;
retained imported bullets, including continuations, stay verbatim. Never rephrase,
split, or merge them. Remove only wholly redundant imported copies; retain partial
overlaps unchanged.

Rewrite only locally maintained target instructions; preserve global,
organization-managed, generated, and unrelated instructions unless explicitly
authorized. Local rules may be split, shortened, rewritten, or removed only if
every distinct requirement, scope, strength, exception, and affected agent remains
covered. For partial overlaps, keep imported bullets intact and only additional
local requirements. A newer source alone proves no equivalence. Keep stronger or
conflicting project requirements as concise overrides outside imported text.
Retain uncertain requirements; report conflicts precedence cannot resolve. Use
nested files for useful scope; root-file path headings do not control discovery. See
[instruction discovery](compatibility.md).

After placement/deduplication, compare retained bullets with pinned source, check
for lost local requirements, verify scope/discovery, and run `git diff --check`.
Add adapters/config only as needed; report discovery checks/limitations without
adding standard discovery explanations to consumer instructions. Staging `--check`
does not validate final consolidated files. Do not sync a one-time import unless
maintained integration is explicitly requested.

### Maintained synchronization

Optional maintained synchronization keeps a generated section and manifest for
deliberate updates, never automatic upstream checks/updates. The offline composer
reads selected `modules/*.md` blobs from a release commit, writes one marked section,
and records tag, commit, and ordered selection. Committed instructions need neither
composer nor network.

Subsequent syncs preserve local bytes outside the section; initial insertion may add
separating newlines. Malformed markers, unknown modules, symlinked outputs, and moved
saved tags fail before writes. Each output is replaced atomically, but the pair is
not a transaction. After interrupted I/O, rerun sync and review both files before
committing. `--check` verifies shared content/metadata, allowing local edits. Initial
pinning trusts the selected release; later syncs reject a different commit for that
saved tag.

## Curation decisions

- Keep rules that prevent concrete failures or guide recurring decisions. General
  modules own shared principles; specialized modules own platform mechanisms.
  Resource cleanup, cancellation, and validation recur where independent use needs
  specific mechanisms. Avoid arbitrary limits, speculative abstractions, and mandated
  architectures.
- Match validation to risk/authorization; no blanket build ban or test requirement
  for every docs edit. Required project checks still apply. Push-only tasks stop
  after reporting; CI fixing includes authorized investigation/verification.
- Consumer versioning/releases remain optional and project-owned.
  [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) governs compatibility,
  deprecation, pre-releases, and metadata only where adopted. This collection's
  `vMAJOR.MINOR.PATCH` releases are repository policy, not consumer requirements.
  The synchronizer accepts stable tags only, independently of consumer schemes.
- Disclosure review/incidents follow
  [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  and [GitHub's sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
  Revoke/rotate exposed credentials; history cleanup needs separate authorization
  and cannot erase other copies. Preserve legitimate public attribution/contacts.
- Respect consumer action/workflow pins: full commit SHAs identify immutable
  revisions; tags can move. This CI retains explicit version tags. Publisher review
  and privilege separation follow
  [GitHub's secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use).
- Preserve cancellation in [Kotlin](https://kotlinlang.org/docs/coroutines-cancellation.html)
  and [Python](https://docs.python.org/3/library/asyncio-exceptions.html), and use
  [Compose lifecycle/key guidance](https://developer.android.com/develop/ui/compose/side-effects).
- Apply [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
  to protected resources without requiring authentication for public content.
- Task-relevant retrieval/checkpoints follow
  [Anthropic's context guidance](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).
  This is design rationale, not measured agent performance. Discovery behavior
  comes from [official sources](compatibility.md).
