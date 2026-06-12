# Repair Prompts

Repair prompts are generated after validation fails.

They must be minimal and bounded:

- list exact violations
- list allowed files
- list exact fixes
- forbid architecture changes
- forbid new dependencies unless approved
- include validation commands

Repair prompts must not ask for broad rewrites.
