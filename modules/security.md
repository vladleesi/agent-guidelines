# Security and dependencies

- Validate untrusted input at trust boundaries, including configuration, paths,
  URLs, payload sizes, and external responses. Use safe parsing and parameterized
  queries; escape output for its destination rather than relying on input filtering.
- For protected operations, enforce authentication and resource-level authorization
  on the trusted server across all transports. Deny access unless explicitly allowed;
  client UI, CORS, and hidden endpoints are not authorization controls.
- Keep secrets and sensitive data out of source, client bundles, URLs, logs,
  artifacts, and error responses. Use protected runtime configuration, least-privilege
  credentials, and redacted diagnostics. Avoid unnecessary secret access and rotate
  exposed credentials.
- Use maintained cryptographic and authentication implementations. Preserve secure
  randomness, constant-time verification where required, and certificate validation;
  do not invent protocols or disable protections to resolve an integration failure.
- Choose browser protections for the threat model: safe DOM sinks, restricted
  content policy, secure cookie attributes, CSRF defenses, and deliberate caching
  of authenticated responses. Never assume browser storage is a secret vault.
- Use supported dependencies and ecosystem lockfiles or constraints for reproducible
  resolution. Before adoption or upgrade, review transitive changes, advisories,
  install scripts, provenance, platform support, and license obligations.
- Prioritize exploitable vulnerabilities and affected deployment paths. Keep any
  accepted exception scoped, justified, and revisitable; distinguish scanner failure
  from a clean result. Never suppress a finding solely to satisfy CI.
