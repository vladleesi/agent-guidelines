# Backend services

## Core

- Reject unsupported inputs; map failures to stable protocol errors without
  sensitive details.
- Evolve schemas/APIs under their compatibility contract. Prefer staged,
  backward-compatible migrations when deployments coexist; protect existing data
  and verify recovery before destructive transitions.
- Key caches by all representation and security variants; prevent shared caches
  from exposing private responses.

## Task guidance

- Define request/response contracts. Bound requests, upstream calls, queues, and
  connections with timeouts/resource limits. Propagate cancellation; close clients,
  sessions, and background tasks through the application lifecycle.
- Retry appropriate transient failures with bounded backoff. Make mutations
  idempotent where retries/duplicate delivery are possible; order acknowledgement
  and persistence to prevent silent data loss.
- Enforce cross-write invariants with transactions/database constraints; handle
  concurrent updates across replicas, beyond process-local locks. Use deterministic
  ordering and pagination for growing collections.
- Distinguish UTC instants from local dates/times at storage/API boundaries;
  define precision and ordering rather than relying on driver defaults.
- Keep caches, rate limits, and session validity correct across processes/replicas.
- Keep liveness/readiness checks inexpensive and purpose-specific; measure boundary
  latency/errors without verbose production logs.
