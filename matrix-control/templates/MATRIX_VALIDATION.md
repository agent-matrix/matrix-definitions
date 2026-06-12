# MATRIX_VALIDATION

Matrix Builder and agent-generator must validate AI-coder output before approval.

## Validation sequence

1. Parse `MATRIX_BLUEPRINT.yaml`.
2. Parse `MATRIX_STANDARDS.lock`.
3. Compare modified files against active task allowed files.
4. Check immutable control-file hashes.
5. Check architecture drift.
6. Check dependency drift.
7. Run schema validation.
8. Run tests.
9. Run security checks.
10. Produce validation report.
11. If validation fails, generate a bounded repair prompt.

## Validation result values

- `approved`
- `needs_repair`
- `rejected`
