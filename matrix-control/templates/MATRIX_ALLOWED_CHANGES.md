# MATRIX_ALLOWED_CHANGES

AI coders may edit only the files explicitly listed in the active task.

## Immutable control files

These files are immutable unless Matrix Builder creates a new blueprint version:

- `MATRIX_BLUEPRINT.yaml`
- `MATRIX_STANDARDS.lock`
- `MATRIX_TASKS.md`
- `MATRIX_ALLOWED_CHANGES.md`
- `MATRIX_ACCEPTANCE_CRITERIA.md`
- `MATRIX_VALIDATION.md`

## Dependency policy

New dependencies are forbidden unless the active task includes an approved dependency change record.

## Architecture policy

The AI coder must not change:

- selected frontend framework
- selected backend framework
- database mode
- API route names
- quality profile
- standards pack version
- MatrixHub publication policy
