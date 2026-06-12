# Batch 5 completion — Updater, signing, and release automation

Batch 5 makes `matrix-definitions` production-release ready.

## Added

- Real release workflow design.
- Release bundle creation.
- Expanded checksums.
- CycloneDX SBOM generation.
- SLSA-style provenance metadata generation.
- Cosign signing workflow for keyless GitHub Actions releases.
- GitHub artifact attestation workflow templates.
- Pack verification workflow.
- Standards update check workflow.
- Candidate update process.
- Exception approval process.
- Release notes generator.
- agent-generator verification contract.

## Local vs production signing

Local scripts generate deterministic development metadata so tests and downstream integrations can run without cloud credentials. Production signing is done by GitHub Actions using OIDC, Cosign, and GitHub artifact attestations.

## Exit criteria

- A signed standards pack can be released through `.github/workflows/release-pack.yml`.
- `agent-generator` can verify manifest, checksums, release metadata, SBOM, provenance, and signature metadata before loading the pack.
