# Design and sources

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

## Project evidence

Source, dependencies, tests, workflows, local instructions, and relevant branches
were inspected. GitHub branch inventories were checked against local commits.

| Project snapshot | Practices retained |
| --- | --- |
| [sideword-chat-server, `49604b7`](https://github.com/vladleesi/sideword-chat-server/tree/49604b71f30018a330ddd239befb83dbc37725ea), `develop` and `main` | Explicit HTTP/WebSocket boundaries, isolated test data, delivery/concurrency regression tests, redacted errors, concise authoritative docs. |
| [vladleesi.github.io, `15b21ea`](https://github.com/vladleesi/vladleesi.github.io/tree/15b21ea5eafe11f41c71067faec941433314ff0a), `main`; compared `take-control` | Semantic static HTML, progressive enhancement, local assets, production-output checks, measured performance. The design branch changes presentation, not universal visual rules. |
| [braindance, `22f2a8d`](https://github.com/vladleesi/braindance/tree/22f2a8de2025d37c34eb42c2caf94efdb353cf67), `develop` and `master`; compared `design-kit` and inspected `web-app` | Common/platform boundaries, read-only state, constructor dependencies, shared Compose UI, API tests, multi-target validation. `design-kit` is older; `web-app` contains deployment output rather than development source. |
| [links, `8fc21c6`](https://github.com/vladleesi/links/tree/8fc21c6acffb4fab31ac4c88b722d90eb8a64f08), `main` | Schema-validated configuration, safe URLs, configuration/presentation separation, local asset provenance, checked release artifacts. |

The inspected trees had no nested `AGENTS.md`. Braindance and Links also supplied
local instruction files outside their public snapshots. No analyzed checkout was modified.

## Curation decisions

- Retain a rule when it prevents a concrete failure or guides a recurring decision.
  Keep shared principles in general modules and platform mechanisms in specialized
  modules. Avoid arbitrary limits, speculative abstractions, and mandated architectures.
- Match validation to risk and authorization. No blanket build prohibition or
  mandatory test run for every documentation edit.
- Use GitHub Action version tags as explicitly requested, acknowledging that tags
  can move. Publisher review and CI privilege separation follow
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
