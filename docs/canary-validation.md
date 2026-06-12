# Canary Validation

Canary blueprints prove that Matrix Definitions can be consumed by tools without manual interpretation.

## Location

```text
canaries/blueprints/
```

Each canary contains:

```text
MATRIX_BLUEPRINT.yaml
MATRIX_STANDARDS.lock
validation-report.json
prompts/
  claude-code.md
  cursor.md
  codex-chatgpt.md
  gitpilot.md
```

## Run validation

```bash
python tools/validate_canaries.py
pytest tests/test_canaries.py
```

## What canaries check

- blueprint schema validity,
- standards lock schema validity,
- validation report schema validity,
- required control files exist,
- prompt packs exist for supported AI coders,
- blueprint required files are represented,
- standards lock references critical RMD controls.

## Why this matters

A future `agent-generator` integration can run canaries first. If canaries fail, the definitions pack should not be used in production.
