# General engineering

- Preserve unrelated working-tree changes and behavior outside the task. Complete
  affected callers, configuration, and documentation without incidental rewrites
  or upgrades.
- Respect existing project conventions and recorded user decisions over optional
  recommendations. Get approval before changing project-wide conventions. Revisit
  accepted or rejected decisions only when requested or requirements materially
  change; check project context before asking questions already answered there.
- Record lasting decisions when useful in existing project instructions or relevant
  documentation. Do not add configuration or documents just to remember trivial
  preferences.
- Prefer explicit names and straightforward control flow over dense expressions.
  Explain non-obvious constraints, not syntax.
- Separate business decisions from presentation, transport, and persistence where
  they change independently. Pass dependencies explicitly; add interfaces or layers
  only for a required boundary or substitution.
- Reuse suitable existing code, standard-library capabilities, and platform APIs.
  Suggest or add tools, dependencies, abstractions, services, or processes only for
  a present requirement or concrete risk, with a meaningful benefit. Avoid repeated
  suggestions unrelated to the task; prefer the simplest solution that meets it.
- Model meaningful states and failures explicitly. Distinguish absent, empty,
  invalid, and failed results when callers need different behavior. Do not silently
  replace failures with successful defaults or discard error context.
- Give resources an owner and cleanup path across success, failure, and cancellation.
  Define ordering for shared mutable state and overlapping work.
- Optimize measured bottlenecks using representative workloads. Give caches an
  explicit lifetime, key, and invalidation policy; avoid speculative complexity.
- Keep one authoritative explanation per topic and update affected setup, usage,
  contracts, and limitations. Keep the README a concise entry point; put necessary
  advanced details in existing documentation before creating another file.
- Keep public documentation focused on the project and its users. Exclude unrelated
  promotion, personal infrastructure, and private development context without user
  value. Preserve copyright, licensing, provenance, legitimate contributor and
  support information, and external links that provide useful functionality or context.
- Check whether affected content is published on an existing website or documentation
  site. Update its source descriptions, examples, versions, and compatibility details
  with the repository changes. Reuse its architecture, styling, generator, and
  existing validation; do not add a site for an unrelated task.
