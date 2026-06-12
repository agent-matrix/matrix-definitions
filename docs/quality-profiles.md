# Matrix Definitions Quality Profiles

Batch 3 makes quality profiles enforceable by mapping each level to concrete rule IDs.

## Starter
For local prototypes. It requires the Matrix blueprint contract, standards lock, README, safe environment examples, and basic agent-safety warnings.

## Standard
The default Matrix Builder level. It requires tests, CI, Docker basics, dependency policy, typed Python/FastAPI structure, and AI-agent control boundaries.

## Production
Adds strict supply-chain checks, release validation, SBOM/provenance requirements, Docker hardening, observability, and stronger API security.

## Enterprise
Requires the full control stack: all Ruslan Magana Definitions, AI-coder drift prevention, high-risk tool approval, audit events, signed artifacts, and MatrixHub publication gates.

These profiles let agent-generator decide what to create, what to warn about, and what to reject for each generated blueprint.
