# agent-generator verification contract

Before `agent-generator` loads a standards pack, it should perform these steps:

1. Read `packs/current/manifest.json`.
2. Verify version compatibility.
3. Verify checksums in `packs/current/checksums.txt`.
4. Verify `combined.pack.yaml` exists and parses.
5. Verify signature/provenance metadata exists.
6. In production, verify release archive Cosign bundle and GitHub artifact attestation.
7. Reject the pack if verification fails.

Minimum Python integration:

```python
from pathlib import Path
from agent_generator.standards import verify_pack, load_pack

root = Path("matrix-definitions")
report = verify_pack(root, strict=True)
if not report.ok:
    raise RuntimeError(report.errors)
pack = load_pack(root / "packs" / "current" / "combined.pack.yaml")
```
