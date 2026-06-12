# MatrixHub Publication Guide

MatrixHub is the registry for validated blueprints, templates, prompt packs, and agents.

## Publication rule

A project cannot be published to MatrixHub unless it includes:

- `MATRIX_BLUEPRINT.yaml`
- `MATRIX_STANDARDS.lock`
- `docs/standards-report.md`
- `README.md`
- license metadata
- validation report
- artifact manifest
- checksums
- SBOM for Production and Enterprise profiles
- provenance/attestation for Production and Enterprise profiles

## Publication states

```text
draft -> validated -> signed -> published -> deprecated
```

## MatrixHub metadata

Each artifact should include:

```yaml
matrixhub:
  artifact_type: blueprint
  name: GitHub Repo Intelligence Agent
  quality_level: standard
  definitions_pack: 2026.06.0
  ruslan_definitions: 1.0.0
  generated_by: Matrix Builder
  engine: agent-generator
```

## Remix requirements

A MatrixHub template must explain how another developer can safely remix it without breaking the blueprint contract.

## Validation before publish

MatrixHub should call the same validation checks as Matrix Builder:

- standards lock exists,
- control files exist,
- no drift detected,
- dependency policy passes,
- standards report present,
- profile-specific checks pass.
