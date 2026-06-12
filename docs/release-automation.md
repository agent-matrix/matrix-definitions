# Release automation

Batch 5 adds release automation so `matrix-definitions` can publish a signed standards pack.

## Release flow

```text
validate schemas
→ validate rules
→ validate contracts
→ build pack
→ generate checksums
→ generate SBOM
→ generate provenance
→ create release archives
→ sign with Cosign
→ attest with GitHub artifact attestations
→ verify release
→ publish GitHub release
```

## Trust rule for agent-generator

`agent-generator` must not load arbitrary YAML files. It should load only a compiled pack from:

```text
packs/current/manifest.json
packs/current/combined.pack.yaml
packs/current/checksums.txt
packs/current/signatures/
```

For production usage, `agent-generator` should verify release artifacts from `releases/<version>/` before activating a pack.
