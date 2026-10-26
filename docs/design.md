# Design notes

## Integration workflows

The default is a one-time import: selected rules become local instructions with
source attribution and the MIT notice. Agents need neither a manifest nor an
upstream checkout to read them. Record the source repository, release, commit,
and selected modules alongside the imported rules so their origin remains clear.
Include a local instruction to consult or update this collection only on explicit
request; attribution links do not authorize fetching upstream.

Prepare each module selection with the pinned release's synchronizer in an empty
temporary target directory, then run `--check` against that target with the same
source checkout. This verifies the staged generated section and manifest. Copy the
selected module headings and rules into the consumer's instruction files, leaving
the staging manifest, managed markers, and generated synchronization notice out.
Retain source attribution and state directory scope and project-specific
precedence outside the imported text. Preserve unrelated files and customizations.

Deduplication removes whole redundant rules or copies, never rewrites their
wording. Prefer an imported rule over an equivalent existing general rule only
when meaning, scope, strength, exceptions, and coverage for the affected agents
match. A newer source alone does not establish equivalence. Retain partial
overlaps unchanged, preserve project-specific constraints as explicit overrides,
and report contradictions that precedence does not resolve. Use nested files
where they preserve useful scope; a path heading in a root file is a textual
instruction, not a discovery mechanism. See [instruction discovery](compatibility.md).

After placement and deduplication, compare every retained imported rule with its
pinned source, verify scope and agent discovery, and review `git diff --check`.
The staging `--check` does not validate the final consolidated files. A one-time
import has no ongoing synchronization contract; do not run sync against those
files unless a maintained integration is explicitly requested.

### Maintained synchronization

The optional maintained workflow retains a generated section and manifest for
deliberate updates. It does not configure automatic upstream checks or updates.
The offline composer reads selected `modules/*.md` blobs from a release commit,
writes one marked section, and records the tag, commit, and ordered selection.
Committed instructions work without the composer or a network connection.

Local rules remain outside the section, byte for byte on subsequent syncs. A new
section may add separating newlines after existing content. Malformed markers,
unknown modules, symlinked output files, and moved saved tags fail before writing.
Each output file is replaced atomically; the pair is not a filesystem transaction.
After interrupted I/O, rerun sync and review both files before committing.
`--check` verifies shared content and metadata while allowing local rules to change.
The initial pin trusts the selected release; later syncs reject a different commit
for the same saved tag.

## Curation decisions

- Retain a rule when it prevents a concrete failure or guides a recurring decision.
  Keep shared principles in general modules and platform mechanisms in specialized
  modules. Avoid arbitrary limits, speculative abstractions, and mandated architectures.
- Match validation to risk and authorization. No blanket build prohibition or
  mandatory test run for every documentation edit. Project-required checks still
  apply; push-only tasks end after reporting the result, while requested CI fixing
  includes relevant investigation and verification within the granted authorization.
- Consumer versioning and release conventions remain optional and project-owned.
  [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) supplies the compatibility,
  deprecation, pre-release, and metadata rules only where adopted. This collection's
  own stable `vMAJOR.MINOR.PATCH` tags and release workflow are maintenance policy,
  not a template imposed on consumer projects; the synchronizer accepts stable tags
  only, independently of consumers' versioning schemes.
- Disclosure review and incident handling follow
  [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  and [GitHub's sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
  Revocation or rotation addresses exposed credentials; history cleanup needs
  separate authorization and does not erase copies elsewhere. Legitimate public
  attribution and contact information remain useful project content.
- Respect consumers' action and workflow pinning policies. Full commit SHAs identify
  immutable revisions; version tags can move. This repository's CI retains its
  existing explicit version tags. Publisher review and CI privilege separation follow
  [GitHub's secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use).
- Preserve cancellation in [Kotlin](https://kotlinlang.org/docs/cancellation-and-timeouts.html)
  and [Python](https://docs.python.org/3/library/asyncio-exceptions.html), and use
  [Compose lifecycle/key guidance](https://developer.android.com/develop/ui/compose/side-effects).
- Apply [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
  to protected resources without requiring authentication for public content.
- Use task-relevant retrieval and compact checkpoints following
  [Anthropic's context guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  This is a qualitative design rationale, not measured proof of agent performance.
  Discovery behavior comes from [official sources](compatibility.md).
