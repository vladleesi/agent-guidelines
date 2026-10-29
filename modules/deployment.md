# Deployment and infrastructure

## Core

- Before infrastructure or deployment changes, inspect the setup and current
  settings. For existing deployments, read applicable operational guidance. If
  required guidance or settings are unavailable, stop the affected change and
  report what is missing.
- Reuse resources and choose the smallest safe change. Preserve hosting, domains,
  and deployment configuration unless the task requires otherwise. Assess security,
  availability, compatibility, data preservation, rollback, and financial impact.
  Avoid speculative scaling; use protected environments where supported.
- Deploy a validated revision or artifact. Deployments (including production),
  website publication, and infrastructure provisioning require existing authorization
  or explicit approval. Explain material cost and operational consequences before
  seeking approval.
- Get explicit approval before enabling paid services or increasing recurring costs,
  including compute and minimum instances, storage, databases, networking, paid APIs,
  service tiers, build minutes, and managed services.
  Performance optimization or deployment requests do not themselves authorize
  higher recurring costs. Resolve unknown billing impact before applying a
  potentially cost-increasing change.
