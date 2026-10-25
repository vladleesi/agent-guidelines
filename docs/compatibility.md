# Instruction discovery

Verified against official documentation on 2026-10-25. These are documented
discovery mechanisms, not a claim that live sessions were tested in every product.

| Agent/interface | Use of the local instructions |
| --- | --- |
| [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Reads `AGENTS.md` along the repository-root-to-working-directory chain. `AGENTS.override.md` takes precedence at the same level. Start from the relevant directory; inspect deeper instructions before editing there. The combined discovery budget defaults to 32 KiB. |
| [Claude Code](https://code.claude.com/docs/en/memory#agentsmd) | Current versions load `AGENTS.md` when no project `CLAUDE.md` or `CLAUDE.local.md` takes priority. For older versions, disabled native support, or an existing Claude instruction file, put `@AGENTS.md` in a sibling `CLAUDE.md`. This is a documented import, not a Markdown link. |
| [Cursor Agent](https://cursor.com/docs/rules#agentsmd) | Supports root and nested `AGENTS.md`; directory-specific instructions combine with parent instructions. No `.cursor/rules` copy is needed. |
| [Copilot](https://docs.github.com/en/copilot/reference/custom-instructions-support) | The CLI, cloud agent, and supported IDE features read `AGENTS.md`. Support differs by interface: GitHub.com Chat and some IDE/review surfaces use `.github/copilot-instructions.md` without native agent-file support. Check the linked support matrix for your surface. |

For a Copilot interface without native support, explicitly attach the local
`AGENTS.md` when that interface supports file context, or use an interface with
native discovery. A pointer in `.github/copilot-instructions.md` is **not** a
portable import and cannot guarantee loading in review or chat features without
file-reading tools. This collection intentionally does not promise support there
through a misleading adapter or maintain a second copy of the rules.

The optional Claude adapter contains only `@AGENTS.md`. Copy it into a new sibling
`CLAUDE.md`, or add that line to the existing file without overwriting customizations.
For nested instructions, add a sibling adapter at that scope when required by your
Claude version/configuration. Modern Claude deduplicates imported agent files.

Selection happens during integration. One-time imports preserve selected rule
wording while removing redundant copies; maintained synchronization includes the
full text of selected modules. Discovery is the same for both workflows: agents
read local instructions without fetching this repository or following links to
module files. For mixed repositories, place specialized rules in the relevant
directory and retain only broadly applicable guidance at the root. Directory
loading differs by tool; start in the applicable scope and confirm loaded context
using that tool's instruction/context inspection feature where available.

Restart or refresh sessions after updates as required by the tool. Global settings,
overrides, organization policies, context limits, and disabled instruction loading
can affect discovery. Instructions guide behavior; they are not a security boundary.
