# Standards Pack Format

A standards pack is a compiled rule bundle. It contains metadata, profile names, included packs, rule references, and reports.

Production tools should use:

```text
packs/current/manifest.json
packs/current/combined.pack.yaml
packs/current/checksums.txt
```

Future production releases should verify cryptographic signatures before activation.
