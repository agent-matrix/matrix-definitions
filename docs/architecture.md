# Architecture

Matrix Definitions is not a code generator. It is a versioned, signed policy and contract repository consumed by generators and product surfaces.

## System architecture

```text
matrix-definitions
  -> signed standards pack
  -> agent-generator
  -> Matrix Builder
  -> AI coder adapters
  -> validation and repair loop
  -> MatrixHub publication
```

## Control principle

The AI coder is never the architect. The architecture is fixed by:

1. `MATRIX_BLUEPRINT.yaml`
2. `MATRIX_STANDARDS.lock`
3. `MATRIX_TASKS.md`
4. `MATRIX_ALLOWED_CHANGES.md`
5. `MATRIX_ACCEPTANCE_CRITERIA.md`
6. `MATRIX_VALIDATION.md`

## Main layers

### Source rules

Editable definitions live in:

```text
industry/
ruslan/
matrixhub/
profiles/
mappings/
```

### Compiled pack

Tools consume:

```text
packs/current/combined.pack.yaml
```

### Contracts

Generated projects include:

```text
MATRIX_BLUEPRINT.yaml
MATRIX_STANDARDS.lock
```

### Prompt packs

Prompt packs are derived from the same contract for Claude Code, Cursor, Codex/ChatGPT, IBM Bob, GitPilot, and generic AI coders.

### Validation

Validation enforces:

- no architecture drift,
- allowed files only,
- approved dependencies only,
- required files present,
- standards report present,
- tests and validation commands pass,
- repair prompt generated when needed.

## Production trust chain

```text
rule files
  -> schema validation
  -> pack build
  -> checksum generation
  -> SBOM/provenance
  -> signature/attestation
  -> agent-generator verification
  -> controlled generation
```
