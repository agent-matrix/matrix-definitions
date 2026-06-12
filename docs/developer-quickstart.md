# Developer Quickstart

This guide explains how to use Matrix Definitions as a developer or future tool builder.

## 1. Validate the repository

```bash
python -m pip install pyyaml jsonschema pytest
python tools/validate_schemas.py
python tools/validate_rules.py
python tools/check_rule_ids.py
python tools/validate_contracts.py
python tools/validate_canaries.py
pytest -q
```

## 2. Build the current pack

```bash
python tools/build_pack.py
python tools/sign_pack.py
python tools/verify_pack.py
```

## 3. Inspect the generated pack

```text
packs/current/manifest.json
packs/current/combined.pack.yaml
packs/current/checksums.txt
```

## 4. Use a canary blueprint

Canary fixtures live in:

```text
canaries/blueprints/
```

Each canary contains a blueprint, standards lock, validation report, and prompt pack. They are intentionally small but representative.

## 5. Integrate from agent-generator

Read:

```text
docs/agent-generator-integration-guide.md
```

The first integration target is to load `packs/current/manifest.json`, verify the pack, and produce `MATRIX_BLUEPRINT.yaml` and `MATRIX_STANDARDS.lock` for generated projects.
