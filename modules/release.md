# Versioning and releases

## Core

- Follow existing versioning, tag, release, changelog, and publication conventions;
  inspect them before proposing changes. Introduce or change these or release
  automation only with user approval. Suggest absent conventions only for a relevant,
  briefly explained benefit.
- Increment versions only under existing policy or explicit authorization. Where
  SemVer 2.0.0 is adopted, classify the declared public API from `1.0.0`: MAJOR for
  incompatible changes, MINOR for compatible additions or deprecations, PATCH for
  compatible fixes. Reset lower components on MAJOR or MINOR increments; `0.y.z`
  offers no stable API guarantee. Document user-visible changes and migrations.
- Before publishing, verify applicable project-required checks and artifacts for
  the release revision; never rely on another commit's status or an unchecked tip.
- Publish only within granted authorization. Preserve published tags, notes, and
  assets; use a new release for corrections unless explicitly authorized to change
  published history. New paid publication services or recurring publication cost
  increases require explicit approval.

## Task guidance

- Where used, follow SemVer pre-release syntax and ordering: `-alpha.1` precedes
  its normal release; numeric identifiers have no leading zeroes; `+build` metadata
  does not affect precedence. Do not invent pre-release conventions where absent.
