# Testing and validation

- Choose focused checks for changed behavior. Broaden coverage for shared APIs,
  packaging, or platform changes. Documentation-only changes normally need link,
  example, and diff review unless project requirements call for broader validation.
- Test observable contracts with meaningful success, boundary, and failure cases.
  Avoid tests that restate implementation or lock down incidental structure.
- For a bug, reproduce the failure and add a regression test when practical. Test
  the shared cause and affected integration points, not only the immediate symptom.
- Keep tests deterministic and isolated from live services and user data. Use test
  credentials, temporary resources, controlled clocks, and explicit cleanup.
  Exercise concurrency with synchronization rather than timing guesses.
- Mock external boundaries when appropriate, retaining integration tests for
  serialization, persistence, framework behavior, and other contracts mocks can hide.
- Check cancellation, retries, authorization failures, and data-loss paths when
  affected. Verify migrations against representative disposable data.
- For UI changes, use interaction, visual, browser, or device checks where static
  tests cannot establish correctness; cover the affected states and platforms.
- Validate the actual distributable when build output or delivery changes. Do not
  infer production behavior or performance from a development server alone.
- Fix failures without weakening assertions or budgets just to pass.
