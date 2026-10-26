# Security and dependencies

- Validate untrusted input at trust boundaries, including configuration, paths,
  URLs, payload sizes, and external responses. Use safe parsing and parameterized
  queries; escape output for its destination rather than relying on input filtering.
- For protected operations, enforce authentication and resource-level authorization
  on the trusted server across all transports. Deny access unless explicitly allowed;
  client UI, CORS, and hidden endpoints are not authorization controls.
- Never commit passwords, API keys, tokens, private keys, or other credentials.
  Keep secrets and private data out of client bundles, URLs, logs, CI output,
  error messages, and public artifacts. Use established secret-management mechanisms,
  protected runtime configuration, least-privilege credentials with limited lifetimes
  where supported, and redacted diagnostics. Access only secrets needed for the task;
  do not rely on automatic log masking.
- Before committing or sharing, review relevant changed and staged content for
  secrets, private contact details, identifiers, internal configuration, and other
  unintended disclosures. Include configuration and environment files, documentation,
  fixtures, logs, and generated artifacts when affected; `.gitignore` is not sufficient
  protection. Use placeholders and synthetic data in examples. Preserve intentional
  public contact information, required attribution, and legitimate project metadata.
- Report an exposed secret safely, identifying its location without reproducing
  its value, and recommend prompt revocation or rotation. Treat history cleanup as
  a separate operation requiring explicit authorization; deleting a file does not
  invalidate credentials or remove other copies.
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
  from a clean result. Never suppress a finding solely to satisfy CI. Reuse existing
  security checks; propose additional scanners only for a concrete risk or coverage
  gap, avoiding overlapping checks and configuration noise.
