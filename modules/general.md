# General engineering

## Core

- Preserve unrelated changes and out-of-scope behavior; update affected callers,
  configuration, and docs without incidental rewrites or upgrades.
- Follow project conventions and recorded user decisions; get approval for
  project-wide convention changes. Revisit decisions only on request or materially
  changed requirements. Consult existing context before asking answered questions.
- For optimization requests, preserve the existing design and prefer the smallest
  local diff. New architecture, configuration schemes, dependencies, files, or
  surrounding component changes require explicit approval; reuse approval already
  given for that scope. If correctness needs broader changes, explain why, propose
  the smallest alternative, and obtain approval before editing beyond scope.
  Suggest out-of-scope rewrites, cleanups, or performance investigations (profiling,
  tracing, benchmarks) only with evidence, reason, and scope; start them only with
  explicit approval.
- When asked to revert an optimization, restore the prior design and behavior,
  remove additions used solely by it, and validate the restored state.
- Keep docs accurate: preserve behavior, safeguards, API/protocol contracts,
  prerequisites, security limitations, data-loss warnings, and recovery steps;
  add no unsupported claims. Preserve license/copyright notices, attribution,
  published release history, generated specifications, and legitimate contributor
  and support information. Do not shorten agent instructions during routine user-doc
  cleanup. After restructuring, check affected links, anchors, and examples.

## Task guidance

- Record lasting decisions in existing instructions/docs; create no files for
  trivial preferences.
- Name parameters/properties by content (`snapshotJson`, `gameId`); document
  sources or formats the name does not convey. Use clear control flow; explain
  non-obvious constraints rather than syntax.
- Separate business decisions from independently changing presentation, transport,
  and persistence. Pass dependencies explicitly; add layers/interfaces only for
  required boundaries or substitutions.
- Reuse suitable code, standard libraries, and platform APIs. Add or suggest tools,
  dependencies, abstractions, services, or processes only when current needs or
  concrete risks justify them; choose the simplest adequate solution. Do not repeat
  unrelated suggestions.
- Model meaningful states and failures; distinguish absent, empty, invalid, and
  failed results where needed. Never silently replace failures with successful
  defaults or discard error context.
- Give resources an owner and cleanup on success, failure, and cancellation;
  define ordering for shared mutable state and overlapping work.
- Optimize measured bottlenecks with representative workloads. Define cache
  lifetime, keys, and invalidation; avoid speculative complexity.
- Write docs and published-site copy for usage, integration, operation, maintenance,
  and contribution. Explain each topic once and link to it; keep README to purpose,
  quick start, and references, with detail in existing docs. Preserve useful links,
  provenance, and rationale that prevents mistakes.
- Replace stale/repetitive explanations within scope. Use short paragraphs,
  descriptive headings, minimal working examples, and tables where clearer; avoid arbitrary
  size targets. Omit task histories, progress, abandoned approaches, repeated
  summaries, speculation, and promotion/private context without reader value.
- Update affected docs and published content with changes to setup, usage,
  contracts, limitations, descriptions, examples, versions, and compatibility.
  Reuse site architecture, styling, generator, and validation; add no unrelated site.
