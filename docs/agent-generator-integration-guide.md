# agent-generator Integration Guide

This guide describes how `agent-generator` should consume Matrix Definitions.

## Required behavior

`agent-generator` must treat Matrix Definitions as a signed source of truth.

It should:

1. verify `packs/current/manifest.json`,
2. verify `packs/current/checksums.txt`,
3. verify signatures/attestations when available,
4. load `packs/current/combined.pack.yaml`,
5. select a quality profile,
6. compile `MATRIX_BLUEPRINT.yaml`,
7. generate `MATRIX_STANDARDS.lock`,
8. generate task-scoped prompt packs,
9. validate generated artifacts,
10. reject or repair drift.

## Minimal Python integration

```python
from pathlib import Path
import yaml

from agent_generator import AgentGenerator

DEFINITIONS = Path("../matrix-definitions")

engine = AgentGenerator(definitions_root=DEFINITIONS)

candidates = engine.generate_blueprint_candidates(
    idea="Build an AI app that analyzes GitHub repositories",
    target_user="developers",
    goal="portfolio project",
    preferred_stack="Next.js + FastAPI + SQLite",
)

result = engine.generate_controlled_blueprint(
    selected_candidate=candidates[0],
    quality_level="standard",
    ai_coders=["claude-code", "cursor", "codex", "gitpilot"],
)

result.export_zip("github-repo-intelligence-agent.zip")
```

## Expected generated files

```text
MATRIX_BLUEPRINT.yaml
MATRIX_STANDARDS.lock
MATRIX_TASKS.md
MATRIX_ALLOWED_CHANGES.md
MATRIX_ACCEPTANCE_CRITERIA.md
MATRIX_VALIDATION.md
docs/architecture.md
docs/security.md
docs/standards-report.md
prompts/claude-code.md
prompts/cursor.md
prompts/codex-chatgpt.md
prompts/gitpilot.md
```

## Verification contract

Before using a pack, `agent-generator` should fail closed:

```text
if checksum invalid -> reject pack
if signature required and missing -> reject pack
if pack version incompatible -> reject pack
if schema validation fails -> reject pack
```

## Validation contract

After generation, `agent-generator` should return:

```python
{
  "status": "approved" | "needs_repair" | "rejected",
  "checks": [...],
  "warnings": [...],
  "errors": [...],
  "repair_prompt": "..."
}
```
