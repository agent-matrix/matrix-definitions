# Changelog

## 2026.06.0 - 2026-06-12

### Added

- Initial production-ready Batch 1 definitions.
- Core schemas for standards rules, packs, blueprints, standards locks, validation reports, sources, exceptions, and MatrixHub templates.
- First Ruslan Magana Definitions covering blueprint contracts, standards locks, AI-coder boundaries, repair loops, agent permissions, and MatrixHub publication gates.
- First industry rules for secure development, application security, GitHub Actions, Docker, supply chain, Python, FastAPI, and AI-agent safety.
- Quality profiles for Starter, Standard, Production, Enterprise, Local First, Open Source, and MatrixHub Publishable.
- Pack build, validation, diff, signing stub, verification stub, and documentation-generation tools.
- CI workflows for validation, release-pack building, signing, verification, updater check, and docs publishing.

### Notes

This release is a definitions pack foundation. It is suitable for local engine integration and CI validation. Real cryptographic signing must be configured in the release environment before public production use.


## Batch 2 - Strict schemas and contracts

- Added strict JSON Schemas for standards rules, RMD rules, packs, manifests, blueprints, control contracts, standards locks, validation reports, profiles, mappings, MatrixHub policy files, exceptions, and updater files.
- Added `schemas/schema-registry.yaml` so every YAML/JSON data file is mapped to a schema.
- Added repository-wide schema validation in `tools/validate_schemas.py`.
- Added Matrix control contract validation in `tools/validate_contracts.py`.
- Added schema examples and invalid fixtures for CI.
- Updated validation workflow to fail on invalid contracts.


## Batch 4 — Matrix control layer

- Added Matrix control-file templates: `MATRIX_BLUEPRINT.yaml`, `MATRIX_STANDARDS.lock`, `MATRIX_TASKS.md`, `MATRIX_ALLOWED_CHANGES.md`, `MATRIX_ACCEPTANCE_CRITERIA.md`, and `MATRIX_VALIDATION.md`.
- Added AI-coder control policies for Claude Code, Codex/ChatGPT, Cursor, IBM Bob, Gitpilot, and generic AI coders.
- Added repair-prompt policy, drift-detection policy, dependency-approval policy, and patch-based workflow rules.
- Added additional Ruslan Magana Definitions RMD-107 through RMD-120.
- Added Batch 4 examples, mappings, documentation, and tests.

## Batch 5 — Updater, signing, and release automation

- Added release policy, signing policy, and verification policy.
- Added SBOM generation, provenance generation, release bundle creation, and release notes generation.
- Added Cosign keyless signing workflow and GitHub artifact attestation workflow templates.
- Added candidate standards update process and exception approval process.
- Added pack verification suitable for agent-generator pre-load checks.



## Batch 6 — Docs, examples, and canary validation

- Completed developer-facing README and quickstart.
- Added architecture, rule authoring, RMD, MatrixHub, agent-generator, GitPilot, and canary documentation.
- Added controlled blueprint examples and AI-coder prompts.
- Added canary blueprint fixtures for GitHub Repo Intelligence Agent, Document Q&A Agent, and Developer Portfolio Reviewer.
- Added `tools/validate_canaries.py` and `tests/test_canaries.py`.
