# Claude Code Prompt Example

You are implementing a Matrix Builder blueprint. The architecture is locked by `MATRIX_BLUEPRINT.yaml` and standards are locked by `MATRIX_STANDARDS.lock`.

Implement TASK-001 only.

Allowed files:

- `backend/app/main.py`
- `backend/tests/test_health.py`

Forbidden:

- Do not modify Matrix control files.
- Do not add dependencies.
- Do not change architecture.

Acceptance criteria:

- `GET /health` returns `{ "status": "ok" }`.
- Tests pass.
