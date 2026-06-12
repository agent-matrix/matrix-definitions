# Candidate update process

The updater creates candidate reports, not live production changes.

1. Read `sources/trusted-sources.yaml`.
2. Compute source digests.
3. Compare with previous update report.
4. Produce `updater/reports/candidate-update.json`.
5. Produce `updater/reports/candidate-update-pr.md`.
6. Run pack validation and canary checks.
7. Open a pull request for human review.

Activation requires a signed release pack.
