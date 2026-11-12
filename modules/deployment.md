# Deployment and infrastructure

## Core

- Before infrastructure/deployment changes, inspect setup and current settings;
  for existing deployments, read applicable operational guidance. If required
  guidance or settings are unavailable, stop the affected change and report gaps.
- Reuse resources and choose the smallest safe change. Preserve hosting, domains,
  and deployment configuration unless the task requires otherwise. Assess security,
  availability, compatibility, data preservation, rollback, and financial impact.
  Avoid speculative scaling; use protected environments where supported.
- Deploy validated revisions/artifacts. Deployment (including production), website
  publication, and infrastructure provisioning require existing authorization or
  explicit approval. Explain material cost and operational consequences first.
- Get explicit approval before enabling paid services or increasing recurring costs
  (compute/minimum instances, storage, databases, networking, APIs, tiers, build
  minutes, managed services). Optimization/deployment requests alone do not authorize
  higher costs. Resolve unknown billing impact before potentially increasing costs.
