# Python

- Use the project's supported interpreter and isolated environment. Declare runtime
  and development dependencies explicitly; keep imports free of avoidable network,
  filesystem, and configuration side effects.
- Use type annotations on public boundaries and non-obvious data structures. Prefer
  standard collection types and small explicit models; validate external values at
  runtime because annotations alone do not validate data.
- Catch specific exceptions when possible. Preserve causal context with exception
  chaining; allow cancellation and process-termination signals to propagate.
- Use context managers for files, locks, sessions, and temporary resources. Give
  iterators and asynchronous tasks a clear lifetime; avoid mutable default arguments
  and hidden shared request state.
- Keep blocking work out of async handlers. Use async-compatible dependencies or
  deliberate thread/process boundaries; do not add `async` to synchronous work
  without a concurrency benefit.
- Invoke subprocesses with argument lists and handle expected exit codes explicitly.
  Specify text encoding for persistent formats and use path APIs for filesystem work;
  never build shell commands from untrusted input.
- Reuse the project's formatter, linter, type checker, and test runner. Scope
  suppressions to justified exceptions and exercise real import/entry-point behavior
  when packaging or startup changes.
