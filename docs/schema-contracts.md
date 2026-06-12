# Batch 2 schema contracts

Batch 2 makes `matrix-definitions` machine-readable and enforceable.

The repo now validates every YAML and JSON data file through `schemas/schema-registry.yaml`.
The registry maps repository paths to schemas and is consumed by `tools/validate_schemas.py`.

Core production contracts:

- `standards-rule.schema.json` — industry rule format.
- `rmd-rule.schema.json` — Ruslan Magana Definition format.
- `standards-pack.schema.json` — compiled pack format loaded by agent-generator.
- `pack-manifest.schema.json` — signed release manifest format.
- `blueprint.schema.json` — high-level blueprint spec.
- `blueprint-candidate.schema.json` — candidate blueprint returned before selection.
- `matrix-blueprint.schema.json` — locked AI-coder control contract.
- `matrix-standards-lock.schema.json` — lock file freezing packs, rules, and control-file checksums.
- `validation-report.schema.json` — output of template, blueprint, or AI-coder patch validation.

The goal is to make agent-generator safe to integrate:

```text
verify pack → load manifest → load combined pack → compile blueprint → write lock → validate output
```

No engine should consume loose YAML files directly. Engines should consume `packs/current/manifest.json` and `packs/current/combined.pack.yaml` after validation and signature/checksum verification.
