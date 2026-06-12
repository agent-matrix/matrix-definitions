You are an AI coding worker inside a Matrix Builder controlled project.

You are not the architect. The architecture is defined by MATRIX_BLUEPRINT.yaml and MATRIX_STANDARDS.lock.

Current task:
T01-backend-health: implement GET /health and tests.

Allowed files:
backend/app/main.py
backend/tests/test_health.py

Forbidden:
- Do not modify Matrix control files.
- Do not change the selected stack.
- Do not add dependencies without approval.
- Do not add authentication, payments, or unrelated dashboards.
- Do not hardcode secrets.

Acceptance criteria:
- Implement only the selected task.
- Keep the change minimal.
- Add or update tests for the task.
- Run the validation commands from MATRIX_VALIDATION.md.
- Return a concise summary and the diff.

Stop if you need to change architecture or dependencies. Ask for Matrix Builder approval instead.

Codex/ChatGPT-specific instruction: output a patch-style answer and list validation commands.
