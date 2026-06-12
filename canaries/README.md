# Canary Blueprints

Canaries are small, stable blueprints used to prove that `matrix-definitions` can be consumed by `agent-generator` and future tools.

Run:

```bash
python tools/validate_canaries.py
pytest tests/test_canaries.py
```
