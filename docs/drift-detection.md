# Drift Detection

Drift detection compares AI-coder output against `MATRIX_BLUEPRINT.yaml` and `MATRIX_STANDARDS.lock`.

Reject output when it changes:

- project type
- frontend stack
- backend stack
- database mode
- quality level
- required routes
- required files
- standards pack version
- MatrixHub publication policy

The result is one of:

- approved
- needs_repair
- rejected
