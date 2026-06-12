#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib
from _common import ROOT

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
NOW = '2026-06-12T00:00:00Z'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def component_for(path: Path) -> dict:
    rel = path.relative_to(ROOT).as_posix()
    return {
        'type': 'file',
        'name': rel,
        'version': VERSION,
        'hashes': [{'alg': 'SHA-256', 'content': sha256(path)}],
        'purl': f'pkg:generic/matrix-definitions/{rel}@{VERSION}'
    }

def main() -> int:
    current = ROOT / 'packs' / 'current'
    files = [p for p in current.rglob('*') if p.is_file() and p.suffix in {'.json', '.yaml'} and 'signatures' not in p.parts]
    sbom = {
        'bomFormat': 'CycloneDX',
        'specVersion': '1.5',
        'serialNumber': f'urn:uuid:matrix-definitions-{VERSION}',
        'version': 1,
        'metadata': {
            'timestamp': NOW,
            'component': {'type': 'data', 'name': 'matrix-definitions', 'version': VERSION, 'supplier': {'name': 'Ruslan Magana'}},
            'tools': [{'vendor': 'RuslanMV', 'name': 'matrix-definitions tools/generate_sbom.py', 'version': VERSION}]
        },
        'components': [component_for(p) for p in sorted(files)]
    }
    for out in [ROOT / 'packs' / 'current' / 'reports' / 'sbom.cdx.json']:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(sbom, indent=2) + '\n', encoding='utf-8')
    print(f'Generated SBOM with {len(sbom["components"])} components')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
