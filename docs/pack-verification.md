# Pack verification

Verification is intentionally layered.

## Local verification

Local verification checks:

- manifest exists and matches `VERSION`
- all pack files exist
- all checksums match
- reports exist
- signatures/provenance metadata exists

```bash
python tools/verify_pack.py
```

## Strict production verification

Strict mode is intended for release automation and `agent-generator` production loading:

```bash
python tools/verify_pack.py --strict
```

Strict mode requires non-placeholder signature metadata and release artifacts. GitHub Actions adds the actual Cosign bundle and artifact attestations.

## Why not trust signatures alone?

A signature proves origin/integrity. It does not prove that the rules are good. The pack must also pass schema, rule, contract, and canary checks.
