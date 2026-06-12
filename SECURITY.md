# Security Policy

## Supported definitions

Only the `packs/current/` pack and published releases listed in `releases/current.json` are supported.

## Reporting a vulnerability

Report security issues privately to the maintainer before opening public issues. Include:

- Affected rule, pack, schema, tool, or workflow.
- Impact on Matrix Builder, agent-generator, MatrixHub, or generated artifacts.
- Reproduction steps or a minimal example.
- Suggested mitigation if known.

## Security model

This repository does not execute generated applications. It defines rules. The main security risks are:

- Malicious or incorrect rule changes.
- Standards-pack tampering.
- Rule/schema drift.
- Unsafe automatic updater behavior.
- Weak MatrixHub publication gates.

## Production rules

- All releases must be validated.
- All releases must have checksums.
- Production deployments should require signed packs.
- Critical rule changes require owner review.
- Exceptions must expire.
