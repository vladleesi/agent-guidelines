# General engineering

- Preserve unrelated working-tree changes and behavior outside the task. Complete
  affected callers, configuration, and documentation without incidental rewrites
  or upgrades.
- Follow repository formatting and naming conventions unless they cause a concrete
  correctness or maintenance problem. Prefer explicit names and straightforward
  control flow over dense expressions. Explain non-obvious constraints, not syntax.
- Separate business decisions from presentation, transport, and persistence where
  they change independently. Pass dependencies explicitly; add interfaces or layers
  only for a required boundary or substitution.
- Reuse suitable existing code, standard-library capabilities, and platform APIs.
  Add dependencies, abstractions, or infrastructure only for a present need.
- Model meaningful states and failures explicitly. Distinguish absent, empty,
  invalid, and failed results when callers need different behavior. Do not silently
  replace failures with successful defaults or discard error context.
- Give resources an owner and cleanup path across success, failure, and cancellation.
  Define ordering for shared mutable state and overlapping work.
- Optimize measured bottlenecks using representative workloads. Give caches an
  explicit lifetime, key, and invalidation policy; avoid speculative complexity.
- Keep one authoritative explanation per topic and update affected setup, usage,
  contracts, and limitations. Preserve provenance and license notices; use synthetic
  examples instead of private operational details.
