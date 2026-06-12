#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib, yaml
from _common import ROOT

NOW = '2026-06-12T00:00:00Z'

def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main() -> int:
    trusted = ROOT / 'sources' / 'trusted-sources.yaml'
    data = yaml.safe_load(trusted.read_text(encoding='utf-8')) if trusted.exists() else {}
    sources = data.get('sources', []) if isinstance(data, dict) else []
    findings = []
    for src in sources:
        stable_repr = json.dumps(src, sort_keys=True)
        findings.append({'id': src.get('id', 'unknown'), 'name': src.get('name', 'unknown'), 'tier': src.get('tier', 'unknown'), 'digest': digest_text(stable_repr), 'status': 'checked_metadata_only'})
    out = ROOT / 'updater' / 'reports' / 'source-digest-check.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({'schema_version': '1.0', 'checked_at': NOW, 'findings': findings}, indent=2) + '\n', encoding='utf-8')
    print(f'Checked {len(findings)} source metadata records')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
