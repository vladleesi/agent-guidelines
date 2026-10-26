# General engineering

## Core

- Preserve unrelated working-tree changes and out-of-scope behavior. Update
  affected callers, configuration, and docs without incidental rewrites or
  upgrades.
- Follow project conventions and recorded user decisions over optional advice;
  get approval for project-wide convention changes. Revisit accepted or rejected
  decisions only on request or materially changed requirements. Consult project
  context before asking answered questions.

## Task guidance

- Record useful lasting decisions in existing instructions or relevant docs; do
  not create config or documents for trivial preferences.
- Prefer explicit names and clear control flow over dense expressions. Explain
  non-obvious constraints, not syntax.
- Separate business decisions from independently changing presentation,
  transport, and persistence. Pass dependencies explicitly; add interfaces or
  layers only for required boundaries or substitutions.
- Reuse suitable code, standard libraries, and platform APIs. Suggest or add
  tools, dependencies, abstractions, services, or processes only for current
  requirements or concrete risks with meaningful benefit. Avoid repeated
  unrelated suggestions; choose the simplest adequate solution.
- Model meaningful states and failures explicitly; distinguish absent, empty,
  invalid, and failed results where callers need it. Never silently turn
  failures into successful defaults or discard error context.
- Give resources an owner and cleanup across success, failure, and cancellation.
  Define ordering for shared mutable state and overlapping work.
- Optimize measured bottlenecks with representative workloads. Define cache
  lifetime, keys, and invalidation; avoid speculative complexity.
- Keep one authoritative explanation per topic; update affected setup, usage,
  contracts, and limitations. Keep README a concise entry point; put advanced
  details in existing docs first.
- Keep public docs relevant to project users. Exclude unrelated promotion,
  personal infrastructure, and private development context without user value.
  Preserve copyright, licensing, provenance, legitimate contributor and support
  info, and useful external links.
- Update affected website or documentation sources alongside repository changes:
  descriptions, examples, versions, compatibility. Check for published content;
  reuse site architecture, styling, generator, and validation. Add no unrelated
  site.
