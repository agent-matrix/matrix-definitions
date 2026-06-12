# GitPilot Adapter

GitPilot is treated as a controlled AI-coder backend in the Matrix Builder ecosystem.

## Adapter goal

The GitPilot adapter should translate Matrix control files into a task-scoped GitPilot session.

## Required inputs

```text
MATRIX_BLUEPRINT.yaml
MATRIX_STANDARDS.lock
MATRIX_TASKS.md
MATRIX_ALLOWED_CHANGES.md
MATRIX_ACCEPTANCE_CRITERIA.md
MATRIX_VALIDATION.md
```

## Recommended mode

Use approval-first behavior for high-impact actions.

## Prompt structure

The generated GitPilot prompt must include:

1. repository context boundary,
2. selected task only,
3. allowed files,
4. forbidden files,
5. acceptance criteria,
6. validation commands,
7. required diff summary,
8. stop conditions.

## Matrix rule

GitPilot should not change architecture, add dependencies, or modify control files unless explicitly approved by Matrix Builder.
