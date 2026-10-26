# Instruction discovery

Verified against official docs on 2026-10-25; live sessions were not tested in
every product.

| Agent/interface | Use of the local instructions |
| --- | --- |
| [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Reads the root-to-working-directory `AGENTS.md` chain; `AGENTS.override.md` wins at the same level. Start in the relevant directory; inspect deeper instructions before editing there. Combined project discovery defaults to 32 KiB (`project_doc_max_bytes`). |
| [Claude Code](https://code.claude.com/docs/en/memory#agentsmd) | Current defaults load `AGENTS.md` unless project `CLAUDE.md`/`CLAUDE.local.md` takes priority. For older versions, disabled native support, or existing Claude instructions, import with `@AGENTS.md` in a sibling `CLAUDE.md`. A Markdown link is not an import. |
| [Cursor Agent](https://cursor.com/docs/rules#agentsmd) | Supports root and nested `AGENTS.md`; directory-specific instructions combine with parent instructions. No `.cursor/rules` copy is needed. |
| [Copilot](https://docs.github.com/en/copilot/reference/custom-instructions-support) | CLI, cloud agent, and supported IDE features read `AGENTS.md`. GitHub.com Chat and some IDE/review surfaces use `.github/copilot-instructions.md` without native agent-file support. Check the support matrix for your interface. |

Without native Copilot support, attach `AGENTS.md` if file context is supported,
or switch to an interface with native discovery. A `.github/copilot-instructions.md`
pointer is **not** a portable import; it cannot guarantee loading without file-reading
tools. No adapter or second rule copy is provided for these interfaces.

The optional [Claude adapter](../adapters/CLAUDE.md) contains only `@AGENTS.md`.
Copy to a new sibling `CLAUDE.md` or append to an existing file without overwriting
customizations. Add nested sibling adapters where required by version/configuration.
Modern Claude deduplicates imported agent files.

Select modules during integration. One-time imports keep rule wording and remove
redundant copies; maintained sync includes full selected modules. Both workflows
use local discovery without fetching upstream or following module links. In mixed
repositories, scope specialized rules to relevant directories and broad guidance
to the root. Loading varies by tool: start in the applicable scope and inspect
loaded instructions/context where supported.

Restart/refresh after updates as required. Global settings, overrides, organization
policies, context limits, and disabled loading affect discovery. Codex's configurable
32 KiB project budget is not a universal agent limit; leave room for local rules
and other loaded project instructions. Instructions are not a security boundary.
