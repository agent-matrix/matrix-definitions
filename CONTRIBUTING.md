# Contributing

Thank you for helping improve Matrix Definitions.

## Before contributing

Read:

- `docs/rule-model.md`
- `docs/governance.md`
- `docs/standards-pack-format.md`
- `docs/exception-process.md`

## Rule contribution checklist

Every rule must include:

- Stable `id`.
- Human-readable `title` and `summary`.
- `domain`, `severity`, `status`, and `version`.
- `source_refs` or explicit Ruslan Magana ownership.
- `applies_to` scope.
- Generator behavior.
- Validation behavior.
- Enforcement per profile.
- Report message.

## Rule ID conventions

- Ruslan Magana Definitions: `RMD-###`
- GitHub Actions: `GHA-###`
- Docker: `DOCKER-###`
- Supply chain: `SLSA-###` or `SUPPLY-###`
- Python: `PY-###`
- FastAPI: `FASTAPI-###`
- Agent safety: `AGENT-###`
- Application security: `ASVS-###`
- Secure development: `SSDF-###`

## Local validation

```bash
python tools/validate_schemas.py
python tools/validate_rules.py
python tools/check_rule_ids.py
python tools/build_pack.py
python tools/verify_pack.py
pytest
```
