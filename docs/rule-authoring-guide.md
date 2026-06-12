# Rule Authoring Guide

Rules are the core of Matrix Definitions. Every rule must be machine-readable, testable, and useful to a generator.

## Rule categories

| Category | Folder | Schema |
|---|---|---|
| Industry standards | `industry/**.yaml` | `standards-rule.schema.json` |
| Ruslan Magana Definitions | `ruslan/**.yaml` | `rmd-rule.schema.json` |
| MatrixHub policies | `matrixhub/**.yaml` | `matrixhub-template.schema.json` |
| Profiles | `profiles/*.yaml` | `profile.schema.json` |

## Minimum rule fields

A rule must include:

```yaml
id: PY-001
title: Use pyproject.toml for Python projects
domain: python
severity: high
status: stable
version: "1.0.0"
summary: Short actionable description.
source_refs:
  - python.packaging-pyproject
applies_to:
  project_types:
    - python-agent
generator:
  required_files:
    - pyproject.toml
validation:
  kind: file_required
  required_files:
    - pyproject.toml
agent_generator:
  enforcement:
    starter: warn
    standard: fail
    production: fail
    enterprise: fail
```

## Good rule design

A good rule tells the engine:

1. when it applies,
2. what to create,
3. what to reject,
4. how severe the failure is,
5. how quality profiles enforce it.

## Bad rule design

Avoid vague rules:

```yaml
id: BAD-001
title: Make the app secure
```

This is not enforceable.

## Source references

Industry rules should reference `sources/trusted-sources.yaml` entries. RMD rules may use `ruslanmv.definitions` as their source of authority.

## Exceptions

Exceptions must be time-limited and documented in `exceptions/`.

Permanent hidden bypasses are not allowed.
