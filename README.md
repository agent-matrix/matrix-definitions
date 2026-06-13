<div align="center">

# Matrix Definitions

### The signed source of truth for controlled AI coding.

**Locked standards, rules, and blueprints that AI coding tools verify before they write a line of code.**

[![License: MIT](https://img.shields.io/badge/License-MIT-22c878?labelColor=02170f)](LICENSE)
[![Pack](https://img.shields.io/badge/pack-2026.06.0-22c878?labelColor=02170f)](packs/current/manifest.json)
[![Signed](https://img.shields.io/badge/signed-cosign%20%C2%B7%20SLSA%20provenance-53f39d?labelColor=02170f)](#trust--supply-chain)
[![CI](https://github.com/agent-matrix/matrix-definitions/actions/workflows/ci.yml/badge.svg)](https://github.com/agent-matrix/matrix-definitions/actions/workflows/ci.yml)
[![Works with](https://img.shields.io/badge/feeds-Matrix%20Builder%20·%20agent--generator%20·%20MatrixHub%20·%20GitPilot-53f39d?labelColor=02170f)](#who-consumes-it)

[**The standard (live)**](https://agent-matrix.github.io/matrix-definitions/definitions/) · [**Current pack**](packs/current/manifest.json) · [**Docs**](docs/) · [**Sponsor**](https://github.com/sponsors/ruslanmv)

</div>

---

## What it is

**Matrix Definitions** is the signed, versioned **contract layer** for the Matrix controlled‑AI‑coding
ecosystem — **Matrix Builder**, **agent‑generator**, **MatrixHub**, and **GitPilot**. It turns
industry best practices into machine‑readable rules, blueprints, and quality profiles, packages them
into one **verifiable pack**, and lets every AI coding tool consume the *same* source of truth.

> AI coders shouldn't generate random code. They should implement **locked blueprints** using
> **signed, validated, current standards**.

## Why it exists

Direct prompts drift: models change the architecture, add unapproved dependencies, skip tests, or
quietly redefine the goal. Matrix Definitions inserts a control layer so the **blueprint stays the
architect and the AI coder is the worker**:

```text
Idea → Blueprint candidates → MATRIX_BLUEPRINT.yaml → MATRIX_STANDARDS.lock
     → task-scoped AI-coder prompts → validation & drift detection → repair or approval
```

## Who consumes it

| Consumer | How it uses this repo |
|---|---|
| **agent‑generator** | Verifies and loads the signed pack, compiles controlled blueprints, emits scaffolds, prompt packs, and validation reports. |
| **Matrix Builder** | Shows which standards and definitions governed a generated blueprint. |
| **MatrixHub** | Publishes only artifacts that satisfy the standards lock, validation, and publication gates. |
| **GitPilot** | Drives task‑scoped, approval‑aware coding sessions from the same control policies. |
| **Claude Code · Cursor · Codex · IBM Bob** | Receive task‑scoped prompts derived from the same contracts. |

## Quality profiles

| Profile | For | Adds |
|---|---|---|
| **Starter** | quick local projects | clear README, env example, basic controls |
| **Standard** | the Matrix Builder default | tests, Docker, CI, Dependabot, standards report, AI‑coder control files |
| **Production** | real workloads | hardened security, SBOM/provenance, observability, stricter validation |
| **Enterprise** | regulated teams | audit, policy gates, approval requirements, signing, provenance, MatrixHub hardening |

## Trust & supply chain

Every release is a **signed standards pack** — built so a security team can verify exactly what their
AI tooling consumes:

- **Signed** with Cosign (keyless, GitHub OIDC) + GitHub artifact attestations.
- **SLSA provenance** and an **SBOM** accompany each release.
- **Checksummed**, content‑addressed, and reproducible.
- Verification is the gate — tools load only a pack that passes it.

```text
packs/current/
├── manifest.json        # pack id, version, compatibility, signature + checksum pointers
├── combined.pack.yaml   # the compiled standards tools consume
├── checksums.txt        # integrity
└── signatures/          # cosign bundle · GitHub attestation · provenance
```

Details: [release‑automation](docs/release-automation.md) · [pack‑verification](docs/pack-verification.md) · [signing‑and‑provenance](docs/signing-and-provenance.md).

## Quick start

```bash
python -m pip install pyyaml jsonschema pytest
python tools/validate_schemas.py     # schemas + contracts
python tools/validate_rules.py
python tools/validate_canaries.py    # blueprints really compile with agent-generator
python tools/build_pack.py           # build packs/current
python tools/verify_pack.py          # verify checksums + signatures
pytest -q
```

## How tools should consume it

Load **only the compiled, verified pack** — never loose YAML:

```text
verify manifest → verify checksums/signature → load combined.pack.yaml
→ select quality profile → compile MATRIX_BLUEPRINT.yaml → create MATRIX_STANDARDS.lock
→ generate task-scoped prompt pack → validate output
```

Integration walk‑through: [`docs/agent-generator-integration-guide.md`](docs/agent-generator-integration-guide.md).

## Repository map

<details>
<summary>Directory layout</summary>

```text
schemas/         JSON Schemas for rules, packs, blueprints, locks, validation reports
sources/         Trusted source registry + source-tier policy
industry/        Machine-readable industry rules
ruslan/          Ruslan Magana Definitions (controlled AI-coder behavior)
matrixhub/       MatrixHub template + publication rules
profiles/        Starter · Standard · Production · Enterprise quality profiles
mappings/        standards → generator actions → validation checks → template files
matrix-control/  AI-coder control templates and policies
packs/current/   the compiled, signed pack tools consume
release/         release, signing, and verification policies
updater/         standards update-candidate process
examples/        human-readable examples and prompt packs
canaries/        canary blueprints for integration testing
tools/           validate / build / sign / verify / canary scripts
tests/           repository tests
definitions/     the public landing site (GitHub Pages)
```

</details>

## The ecosystem

| Project | Role |
|---|---|
| **Matrix Definitions** | the signed standards — the source of truth (this repo) |
| **Matrix Builder** | idea → controlled Matrix Bundle → validate → publish |
| **agent‑generator** | the deterministic engine that compiles + validates |
| **MatrixHub** | the registry of trusted, validated bundles |
| **GitPilot** | a Matrix‑native AI coder |

## Versioning

Current pack: **2026.06.0** (`status: stable`). Packs are date‑versioned (`YYYY.MM.patch`) and each
carries explicit `compatibility` ranges for the tools that consume it.

---

<div align="center">

**Give AI coders a contract, not a prompt.**

Maintained in the open by **[Ruslan Magana](https://ruslanmv.com)** · MIT License · [Sponsor](https://github.com/sponsors/ruslanmv)

Generated artifacts carry: _“Built with Matrix Builder using Ruslan Magana Definitions and Matrix Definitions.”_

</div>
