# Versioning and releases

## Core

- Inspect and follow versioning, tag, release, changelog, and publication conventions.
  Introduce/change them or release automation only with user approval; suggest absent
  conventions only with a relevant, briefly explained benefit. Increment versions
  only under existing policy or explicit authorization.
- Before publishing, verify project-required checks and artifacts for the release
  revision; never rely on another commit's status or an unchecked tip.
- Publish only within granted authorization. Preserve published tags, notes, and
  assets; correct via a new release unless explicitly authorized to change history.
  New paid publication services or recurring cost increases require explicit approval.

## Task guidance

- Where SemVer 2.0.0 is adopted, classify the declared public API from `1.0.0`:
  MAJOR for incompatible changes, MINOR for compatible additions/deprecations,
  PATCH for compatible fixes. Reset lower components on MAJOR/MINOR increments;
  `0.y.z` offers no stable API guarantee. Document user-visible changes and migrations.
- For SemVer pre-releases where used, `-alpha.1` precedes its normal release;
  numeric identifiers have no leading zeroes; `+build` metadata does not affect
  precedence. Do not introduce pre-release conventions where absent.
