#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib, os
from _common import ROOT

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
NOW = '2026-06-12T00:00:00Z'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    current = ROOT / 'packs' / 'current'
    sig = current / 'signatures'
    sig.mkdir(parents=True, exist_ok=True)
    combined = current / 'combined.pack.yaml'
    dev_signature = {
        'schema_version': '1.0',
        'status': 'placeholder',
        'mode': 'development-metadata',
        'warning': 'This is not a production cryptographic signature. Production releases use Cosign keyless signing in GitHub Actions.',
        'created_at': NOW,
        'subject': [{'name': 'packs/current/combined.pack.yaml', 'digest': {'sha256': sha256(combined)}}]
    }
    (sig / 'cosign.bundle.json').write_text(json.dumps(dev_signature, indent=2) + '\n', encoding='utf-8')
    (sig / 'github-attestation.json').write_text(json.dumps({
        'schema_version': '1.0', 'status': 'placeholder', 'mode': 'development-metadata',
        'warning': 'GitHub artifact attestation is created by release-pack.yml in production.',
        'created_at': NOW, 'subject': dev_signature['subject']
    }, indent=2) + '\n', encoding='utf-8')
    # Preserve provenance if generate_provenance already ran; otherwise write minimal metadata.
    prov = sig / 'provenance.intoto.jsonl'
    if not prov.exists():
        prov.write_text(json.dumps({'_type':'https://in-toto.io/Statement/v1','predicateType':'https://slsa.dev/provenance/v1','subject':dev_signature['subject'], 'predicate': {'builder': {'id': 'local'}, 'metadata': {'buildFinishedOn': NOW}}}) + '\n', encoding='utf-8')
    print('Wrote development signing metadata; production signing happens in GitHub Actions with Cosign.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
