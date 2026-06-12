# Release automation

This folder defines how `matrix-definitions` turns editable standards, Ruslan Magana Definitions, and MatrixHub publication rules into a signed release pack.

The release process is intentionally conservative:

1. Validate all schemas and rules.
2. Build the current pack.
3. Generate checksums.
4. Generate an SBOM.
5. Generate provenance metadata.
6. Create tar.gz and zip release artifacts.
7. Sign artifacts with Cosign in GitHub Actions.
8. Generate GitHub artifact attestations.
9. Verify the release before publishing.

Local development uses deterministic development metadata. Public releases must use GitHub Actions OIDC, Cosign, and GitHub artifact attestations.
