# MATRIX_ACCEPTANCE_CRITERIA

A task is accepted only if all criteria pass.

## Required criteria

- The implementation stays inside allowed files.
- The selected stack is unchanged.
- No hardcoded secrets are introduced.
- Required API routes are present.
- Required tests are added or updated.
- Validation commands pass.
- Standards report remains consistent with `MATRIX_STANDARDS.lock`.

## Rejection criteria

Reject the task if the AI coder:

- modifies control files
- changes the architecture
- adds unapproved dependencies
- removes tests
- skips validation commands
- creates features not requested by the blueprint
- returns a complete rewrite when a patch was requested
