# Security and dependencies

## Core

- Validate untrusted input at trust boundaries: config, paths, URLs, payload
  sizes, and external responses. Parse safely, parameterize queries, and escape
  output for its destination; input filtering alone is insufficient.
- Enforce authentication and resource-level authorization for protected
  operations on the trusted server across all transports. Deny unless explicitly
  allowed; client UI, CORS, and hidden endpoints cannot authorize access.
- Never commit credentials, including passwords, API keys, tokens, and private
  keys. Keep secrets and private data out of client bundles, URLs, logs, CI
  output, errors, and public artifacts. Use established secret management,
  protected runtime config, least-privilege credentials, limited lifetimes where
  supported, and redacted diagnostics. Access only task-required secrets; do not
  rely on automatic log masking.
- Before committing or sharing, review relevant changed and staged content for
  secrets, private contacts, identifiers, internal config, and unintended
  disclosures. Include affected config and environment files, docs, fixtures,
  logs, and generated artifacts; `.gitignore` is insufficient. Use placeholders
  and synthetic example data. Preserve intentional public contacts, required
  attribution, and legitimate project metadata.
- Report exposed secrets by location without reproducing values; recommend
  prompt revocation or rotation. History cleanup separately requires explicit
  authorization; file deletion neither invalidates credentials nor removes other
  copies.
- Use maintained cryptography and authentication implementations. Preserve
  secure randomness, constant-time verification where required, and certificate
  validation. Never invent protocols or disable protections to fix integration
  failures.
- Match browser protections to threats: safe DOM sinks, restricted content
  policy, secure cookie attributes, CSRF defenses, and deliberate
  authenticated-response caching. Do not treat browser storage as a secret
  vault.
- Use supported dependencies and ecosystem lockfiles or constraints for
  reproducibility. Before adoption or upgrades, review transitive changes,
  advisories, install scripts, provenance, platform support, and license
  obligations.
- Prioritize exploitable vulnerabilities and affected deployment paths. Keep
  accepted exceptions scoped, justified, and revisitable. Distinguish scanner
  failure from clean results; never suppress findings just to pass CI. Reuse
  security checks; propose scanners only for concrete risks or coverage gaps
  without overlapping checks or config noise.
