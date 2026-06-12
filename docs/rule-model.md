# Rule Model

A rule is a machine-readable definition that tells Matrix Builder and agent-generator how to generate, validate, report, and enforce a practice.

Every rule has:

- `id`
- `title`
- `domain`
- `severity`
- `status`
- `version`
- `summary`
- `source_refs` or RMD ownership
- `applies_to`
- `generator`
- `validation`
- `agent_generator.enforcement`

## Enforcement values

- `off`: not applied.
- `warn`: show in report but do not fail.
- `fail`: generation or validation must fail.
- `manual`: human review required.
