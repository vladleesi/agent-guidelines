# Testing and validation

## Core

- Keep tests deterministic and isolated from live services/user data. Use test
  credentials, temporary resources, controlled clocks, and cleanup; synchronize
  concurrency tests rather than guessing timing.
- Check affected cancellation, retry, authorization-failure, and data-loss paths;
  verify migrations with representative disposable data.
- Validate distributables when build output or delivery changes; a dev server
  cannot establish production behavior/performance.
- Fix failures without weakening assertions or budgets just to pass.

## Task guidance

- Focus checks on changed behavior; broaden for shared APIs, packaging, or
  platform changes. Docs-only edits normally need link, example, and diff review
  unless project policy requires more.
- Test observable success, boundary, and failure contracts, not incidental structure.
  Reproduce bugs and add regression tests when practical; cover shared causes and
  affected integrations beyond the symptom.
- Mock external boundaries where appropriate; retain integration coverage for
  serialization, persistence, framework behavior, and contracts mocks can hide.
- Use interaction, visual, browser, or device checks where static tests cannot
  establish UI correctness; cover affected states and platforms.
