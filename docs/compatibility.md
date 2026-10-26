# Instruction discovery

Checked against official documentation on 2026-10-25. Discovery is different from
compliance: an instruction file is not a security boundary.

| Agent/interface | Automatic discovery and scope | Referenced task guidance |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Builds the Git-root-to-working-directory chain at session start; without a project root, checks only the working directory. At each level, `AGENTS.override.md` precedes `AGENTS.md`, then configured fallbacks. | Ordinary Markdown links do not extend that chain. Explicitly read relevant task files and deeper instructions before work there, even when starting at root. |
| [Claude Code](https://code.claude.com/docs/en/memory#agentsmd) | Since v2.1.277, defaults to ancestor/current `AGENTS.md` when no project `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` takes priority. Nested AGENTS load on a Read-tool access where local Claude files do not supersede them. Settings/version can disable this. | `@path` imports expand eagerly, including within AGENTS; they do not save context. Use explicit reads for deferred guidance. |
| [Cursor Agent](https://cursor.com/docs/rules#agentsmd) | Root AGENTS plus nested AGENTS when working with files in that directory or descendants; more specific instructions take precedence. | File mentions are read with tools when needed, not inlined. Explicit routing is still needed. Rules do not apply to Cursor Tab. |
| [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) | Discovers AGENTS at root, working directory, intermediate directories, and directories along affected file paths. Combines applicable files without a general precedence order. Inspect with `/instructions`. | Use explicit local reads, not an assumed portable Markdown import. Resolve contradictory project rules during integration. |
| [Copilot in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions) | Behavior depends on the selected harness. Local harness settings `chat.useAgentsMdFile` and `chat.useNestedAgentsMdFiles` enable nested discovery; relevant files can then be loaded by the agent. | Check instruction diagnostics and actual reads for that harness, not just the existence of files. |

For other Copilot surfaces, check the [support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support).
GitHub.com Chat and some IDE/review interfaces use `.github/copilot-instructions.md`
without native AGENTS support. Attach the complete applicable instructions if the
interface supports file context, or use a supported agent. A pointer file cannot
guarantee loading without file-reading tools; no duplicate rule collection is supplied.

The optional [Claude adapter](../adapters/CLAUDE.md) contains only `@AGENTS.md`.
Copy to a new sibling `CLAUDE.md` or append without overwriting customizations when
native AGENTS loading is unavailable or existing Claude instructions supersede it.
Add nested sibling adapters only where required. Current Claude deduplicates imported
AGENTS. Keep task paths as ordinary paths, not eager imports. No Cursor adapter is needed.

## Limits and verification

Codex defaults to **32 KiB of discovered project instructions** via
`project_doc_max_bytes`; nested files in the discovered chain share that budget.
Files explicitly read later still consume model context, although they are not part
of that discovery budget. Leave room for project rules and other instruction sources.

Claude's recommendation to keep CLAUDE files under 200 lines is not a universal
hard limit. Its current documentation specifies a 4 MiB skip threshold and separate
character limits for on-demand files; these are different from auto-memory limits.
Cursor and Copilot's linked guidance establishes no shared 32 KiB project budget.
Use the actual interface's limits and diagnostics, not an agent-independent size cap.

For the [one-time layout](design.md#task-based-loading), confirm root discovery and
observe explicit reads before a representative code, CI, release, and infrastructure
task. Repeat from a nested working directory and after context reset. Verify every
route resolves relative to its owning AGENTS, every task section has a route, and
critical rules are already in root context. Existing project decisions/overrides
must remain discoverable too. If that cannot be established, keep the applicable
guidance inline. A plain link, model assertion, or successful sync check alone is
not evidence of a file read.

Actual local check: Codex CLI 0.164.0 `debug prompt-input` in temporary repositories
included root instructions from root, root plus nested instructions from the nested
working directory, and no contents from an ordinary referenced task Markdown file.
This tested prompt construction without a model call, not autonomous routing or
rule adherence. Claude, Cursor, and Copilot were checked against docs, not live runs.
Regression fixtures also verify exact rule coverage and route/file correspondence.

Global settings, overrides, organization policies, disabled instructions, and
context truncation can change these results. Restart/refresh sessions as required.
Read deferred guidance again after it leaves context; no agent guarantees compliance.
