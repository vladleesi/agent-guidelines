# Kotlin, Android, and Multiplatform

- Prefer precise types, immutable values, and explicit nullability. Use sealed
  hierarchies or enums for closed state sets; avoid unchecked casts, unnecessary
  `!!`, and scope-function chains that obscure control flow.
- Keep common source sets free of platform APIs. Put platform behavior behind a
  small interface or `expect`/`actual` only when shared code needs it. Confirm each
  dependency and API supports every affected target and source set.
- Use structured concurrency with an owner whose lifetime matches the work. Keep
  blocking I/O off UI/event-loop threads and inject dispatchers when substitution
  is needed. Do not add unowned scopes to bypass lifecycle cancellation.
- Preserve cancellation: rethrow `CancellationException` when catching broad
  exceptions, including in `runCatching` recovery. Handle expected failures explicitly
  and release resources on cancellation. Define how overlapping requests affect state.
- Expose read-only state and keep mutations with their owner. Use atomic updates
  or synchronization for concurrent changes; model loading, empty, success, and
  failure when the UI or caller distinguishes them.
- On Android, respect lifecycle, process recreation, permissions, and background
  execution constraints. Persist only state that must survive recreation; do not
  retain activities or views in longer-lived owners.
- Reuse the Gradle wrapper and existing dependency catalog/conventions. Keep plugin,
  Kotlin, runtime, SDK, and compiler compatibility aligned. Scope experimental
  opt-ins narrowly and verify migrations against supported targets.
- Put portable behavior tests in common tests and platform contracts in the relevant
  platform tests. Compile affected source sets; success on one target does not prove
  compatibility with the others.
