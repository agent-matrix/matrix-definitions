# Matrix Definitions

**Matrix Definitions** is the signed source of truth for **Matrix Builder**, **agent-generator**, **MatrixHub**, **GitPilot**, and the RuslanMV controlled AI-coding ecosystem.

The goal is simple:

> AI coders should not generate random code. They should implement locked blueprints using signed, validated, current standards.

Matrix Definitions contains:

- industry standards mapped into generator rules,
- Ruslan Magana Definitions (RMD) for controlled AI-coder behavior,
- MatrixHub publication requirements,
- quality profiles from Starter to Enterprise,
- schemas for machine-readable contracts,
- examples for Claude Code, Cursor, Codex/ChatGPT, GitPilot, IBM Bob, and generic AI coders,
- canary blueprints used to prove that packs can be consumed by `agent-generator`.

## Why this exists

AI coding tools are powerful, but direct prompts often go out of control. They may change architecture, add unapproved dependencies, ignore tests, introduce hidden services, or silently change the original idea.

Matrix Builder solves this by inserting a control layer:

```text
Idea
  -> Blueprint candidates
  -> Selected MATRIX_BLUEPRINT.yaml
  -> MATRIX_STANDARDS.lock
  -> Task-scoped AI-coder prompts
  -> Validation and drift detection
  -> Repair prompt or approval
```

The AI coder becomes the worker. The blueprint remains the architect.

## Main consumers

| Consumer | How it uses this repo |
|---|---|
| `agent-generator` | Loads signed packs, compiles controlled blueprints, generates scaffold files, prompt packs, and validation reports. |
| Matrix Builder | Shows the user which standards and Ruslan Magana Definitions controlled a generated blueprint. |
| MatrixHub | Publishes only artifacts that include required metadata, standards locks, validation reports, and publication gates. |
| GitPilot | Uses prompt and control policies for task-scoped, approval-aware coding sessions. |
| Claude Code / Cursor / Codex / IBM Bob | Receive task-scoped prompts derived from the same contracts. |

## Repository map

```text
schemas/          JSON Schemas for rules, packs, blueprints, locks, and validation reports
sources/          Trusted source registry and source-tier policy
industry/         Machine-readable industry rules
ruslan/           Ruslan Magana Definitions
matrixhub/        MatrixHub template and publication rules
profiles/         Starter, Standard, Production, Enterprise quality profiles
mappings/         Standards -> generator actions -> validation checks -> template files
matrix-control/   AI-coder control templates and policies
packs/current/    Compiled standards pack consumed by tools
release/          Release, signing, and verification policies
updater/          Standards update candidate process
examples/         Human-readable examples and prompt packs
canaries/         Canary blueprints for integration testing
tools/            Validation, pack build, signing, verification, canary scripts
tests/            Repository tests
```

## Quick start

```bash
python -m pip install pyyaml jsonschema pytest
python tools/validate_schemas.py
python tools/validate_rules.py
python tools/check_rule_ids.py
python tools/validate_contracts.py
python tools/validate_canaries.py
python tools/build_pack.py
python tools/verify_pack.py
pytest -q
```

Expected result:

```text
All schemas and contracts pass.
The current pack is built and verified.
Canary blueprints are valid.
```

## How `agent-generator` should consume this repo

`agent-generator` should load only the compiled and verified pack:

```text
packs/current/manifest.json
packs/current/combined.pack.yaml
packs/current/checksums.txt
packs/current/signatures/
```

It should not load random loose YAML files directly. The safe flow is:

```text
verify manifest
verify checksums/signature
load combined.pack.yaml
select quality profile
compile MATRIX_BLUEPRINT.yaml
create MATRIX_STANDARDS.lock
generate task-scoped prompt pack
validate output
```

A minimal integration example is in [`docs/agent-generator-integration-guide.md`](docs/agent-generator-integration-guide.md).

## Quality profiles

| Profile | Purpose |
|---|---|
| Starter | Minimal local project with clear README, environment example, and basic controls. |
| Standard | Default Matrix Builder level: tests, Docker, GitHub Actions, Dependabot, standards report, AI-coder control files. |
| Production | Adds stronger security, SBOM/provenance, observability, stricter validations. |
| Enterprise | Adds audit, policy gates, approval requirements, signing, provenance, and MatrixHub publication hardening. |

## Release model

Releases are built as signed standards packs. Local development signing files are placeholders, while production releases should use GitHub OIDC, Cosign keyless signing, artifact attestations, checksums, SBOM, and provenance metadata.

See:

- [`docs/release-automation.md`](docs/release-automation.md)
- [`docs/pack-verification.md`](docs/pack-verification.md)
- [`docs/signing-and-provenance.md`](docs/signing-and-provenance.md)

## Version

Current target release: **2026.06.0**

## Brand and attribution

This repository defines **Ruslan Magana Definitions** for the RuslanMV ecosystem and should be presented publicly at:

```text
https://ruslanmv.com/definitions
```

Generated artifacts should include attribution similar to:

```text
Generated with Matrix Builder using Ruslan Magana Definitions and Matrix Definitions.
```
