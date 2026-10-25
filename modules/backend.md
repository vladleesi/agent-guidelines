# Backend services

- Define request/response contracts, reject unsupported inputs deliberately, and
  map failures to stable, non-sensitive protocol errors.
- Set timeouts and resource limits for requests, upstream calls, queues, and
  connections. Propagate cancellation; close clients, sessions, and background tasks
  through application lifecycle management.
- Retry only appropriate transient failures with bounded backoff. Make mutating
  operations idempotent where retries or duplicate delivery are possible; define
  acknowledgement and persistence order so failures cannot silently lose data.
- Use transactions and database constraints for invariants that span writes. Handle
  concurrent updates explicitly; process-local locks do not coordinate replicas.
  Use deterministic ordering and pagination for growing collections.
- Distinguish UTC instants from local dates/times at storage and API boundaries.
  Define precision and ordering semantics rather than depending on driver defaults.
- Plan schema and API evolution around the actual compatibility contract. Prefer
  staged, backward-compatible migrations when old and new deployments coexist;
  protect existing data and verify recovery before destructive transitions.
- Keep caches, rate limits, and session validity correct across the deployment's
  processes and replicas. Include all representation/security variants in cache keys
  and prevent shared caches from exposing private responses.
- Keep liveness and readiness checks appropriate to their purpose and inexpensive.
  Measure latency and errors at service boundaries without verbose production logging.
