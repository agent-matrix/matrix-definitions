# Matrix Control Layer

The Matrix Control Layer solves the out-of-control AI coder problem.

Traditional AI coding flow:

```text
Idea → broad prompt → unpredictable implementation
```

Matrix Builder flow:

```text
Idea → blueprint candidates → selected blueprint → standards lock → controlled scaffold → task-scoped AI-coder prompt → diff validation → repair or approval
```

## Control files

- `MATRIX_BLUEPRINT.yaml` is the architecture contract.
- `MATRIX_STANDARDS.lock` freezes the rules and definition pack.
- `MATRIX_TASKS.md` sequences implementation into small tasks.
- `MATRIX_ALLOWED_CHANGES.md` defines file boundaries.
- `MATRIX_ACCEPTANCE_CRITERIA.md` defines acceptance and rejection conditions.
- `MATRIX_VALIDATION.md` defines validation sequence and commands.

## Supported AI coders

Batch 4 defines policies for Claude Code, Codex/ChatGPT, Cursor, IBM Bob, Gitpilot by RuslanMV, and generic AI coders.

## Rule

AI coders are workers, not architects.
