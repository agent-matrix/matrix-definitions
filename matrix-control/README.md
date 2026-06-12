# Matrix Control Layer

This folder defines how Matrix Builder controls external AI coders.

The control layer exists because AI coding tools can be powerful but can also drift away from the original architecture. Matrix Builder mitigates that risk by creating a locked blueprint, a standards lock, scoped tasks, allowed file boundaries, acceptance criteria, validation commands, drift checks, and repair prompts.

Supported AI coder adapters in this batch:

- Claude Code
- Codex / ChatGPT coding workflows
- Cursor
- IBM Bob
- Gitpilot by RuslanMV
- Generic AI coder

The rule is simple:

```text
AI coders are workers, not architects.
```

They implement scoped tasks inside the blueprint contract.
