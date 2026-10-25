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
  mandatory test run for every documentation edit.
- Use readable GitHub Action version tags, acknowledging that tags can move.
  Publisher review and CI privilege separation follow
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
- [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md)
  was reviewed for reuse and minimal scope. No upstream text or implementation is
  copied; persona, intensity modes, mandatory self-checks, and shortest-diff rules
  are excluded. Correctness and maintainability take priority over token savings.
