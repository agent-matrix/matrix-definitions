# Generator Mappings

Batch 3 expands the mapping layer so `agent-generator` can consume Matrix Definitions deterministically.

The important mapping files are:

- `mappings/standards-to-generator-rules.yaml` — tells the engine what to create or enforce.
- `mappings/standards-to-validation-checks.yaml` — tells the validator what check to run for each rule.
- `mappings/standards-to-template-files.yaml` — tells the template compiler which files must exist.
- `mappings/standards-to-blueprint-fields.yaml` — tells Matrix Builder which blueprint fields are affected by a rule.
- `mappings/standards-to-matrixhub-metadata.yaml` — tells MatrixHub which metadata and gates are required.

This is the key distinction from uncontrolled AI coding: rules are compiled into generator actions and validation checks before an AI coder receives a prompt.
