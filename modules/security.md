# Security and dependencies

## Core

- Validate untrusted config, paths, URLs, payload sizes, and external responses at
  trust boundaries. Parse safely, parameterize queries, and escape for the output
  destination; input filtering is insufficient.
- Enforce authentication and resource-level authorization on the trusted server
  across all transports for protected operations. Deny by default; client UI,
  CORS, and hidden endpoints cannot authorize access.
- Never commit credentials. Keep secrets and private data out of client bundles,
  URLs, logs, CI output, errors, and public artifacts. Use established secret
  management, protected runtime config, least privilege, limited lifetimes where
  supported, and redacted diagnostics. Access only task-required secrets; do not
  rely on automatic log masking.
- Before committing or sharing, review changed/staged content for secrets, private
  contacts/identifiers, internal config, and unintended disclosures. Include affected
  config/environment files, docs, fixtures, logs, and generated artifacts;
  `.gitignore` is insufficient. Use placeholders/synthetic examples; preserve
  intentional public contacts, required attribution, and legitimate project metadata.
- Report exposed secrets' locations without values; recommend prompt revocation/
  rotation. History cleanup requires separate explicit authorization; deletion
  neither invalidates credentials nor removes copies.
- Use maintained cryptography/authentication implementations; preserve secure
  randomness, required constant-time verification, and certificate validation.
  Never invent protocols or disable protections to fix integration failures.
- Match browser defenses to threats: safe DOM sinks, restricted content policy,
  secure cookie attributes, CSRF protection, and deliberate authenticated-response
  caching. Browser storage is not a secret vault.
- Use supported dependencies and ecosystem lockfiles/constraints. Before adoption
  or upgrades, review transitive changes, advisories, install scripts, provenance,
  platform support, and licenses.
- Record provenance, licenses, and required notices for copied code, fonts, icons,
  assets, and data using existing project mechanisms. Verify intended use and
  redistribution permissions; the project license need not cover third-party work.
- Prioritize exploitable vulnerabilities and affected deployment paths; scope,
  justify, and revisit exceptions. Distinguish scanner failure from clean results;
  never suppress findings to pass CI. Reuse checks; propose scanners only for concrete
  risks or coverage gaps without overlapping checks/config noise.
