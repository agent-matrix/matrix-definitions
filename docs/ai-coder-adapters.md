# AI Coder Adapters

AI-coder adapters translate a Matrix Blueprint into a prompt format suitable for a specific coding assistant while preserving the same control model.

Adapters included in Batch 4:

- Claude Code
- Codex / ChatGPT coding workflows
- Cursor
- IBM Bob
- Gitpilot by RuslanMV
- Generic AI coder

Every adapter must include:

1. role boundary
2. active blueprint summary
3. active task
4. allowed files
5. forbidden changes
6. acceptance criteria
7. validation commands
8. stop conditions
9. expected output format

The adapter can change wording, but it cannot change the contract.
