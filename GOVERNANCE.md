# Governance

`matrix-definitions` is governed as a standards repository, not as an ordinary code repository.

## Roles

- **Owner**: Ruslan Magana. Owns Ruslan Magana Definitions and final release approval.
- **Standards Maintainers**: maintain industry and source mappings.
- **Engine Maintainers**: maintain generator-facing schemas and pack formats.
- **Security Maintainers**: review critical rules, workflows, signing, provenance, and exceptions.
- **MatrixHub Maintainers**: review publication and registry policies.

## Change classes

| Class | Examples | Review required |
|---|---|---|
| Editorial | docs typo, explanation update | 1 maintainer |
| Schema | JSON schema or pack format | engine maintainer |
| Industry rule | OWASP/NIST/SLSA/Docker/GitHub mapping | standards + security |
| RMD rule | Ruslan Magana Definition | owner |
| Critical rule | fail-level validation, immutable control file, publication gate | owner + security |
| Release | pack publication | owner + release maintainer |

## Non-negotiable rules

- No direct pushes to `main`.
- Critical rules require review.
- Workflow changes require CODEOWNERS approval.
- Exceptions must include reason, owner, and expiry.
- The updater may propose changes, but it must not silently activate production packs.
