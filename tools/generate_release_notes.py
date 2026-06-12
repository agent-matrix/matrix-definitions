#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, yaml
from _common import ROOT, rule_files

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()

def main() -> int:
    rules = list(rule_files())
    counts = {}
    for _, data in rules:
        counts[data.get('domain', 'unknown')] = counts.get(data.get('domain', 'unknown'), 0) + 1
    release = ROOT / 'releases' / VERSION
    release.mkdir(parents=True, exist_ok=True)
    body = ['# Matrix Definitions ' + VERSION, '', '## Summary', '', f'- Rules: {len(rules)}', '- Signed standards pack release flow added.', '- SBOM and provenance metadata generation added.', '- Pack verification workflow added.', '- Candidate standards update process added.', '', '## Rule counts by domain', '']
    for domain, count in sorted(counts.items()):
        body.append(f'- {domain}: {count}')
    body.extend(['', '## Verification', '', 'Run:', '', '```bash', 'python tools/verify_pack.py', '```', ''])
    (release / 'release-notes.md').write_text('\n'.join(body), encoding='utf-8')
    print(f'Generated release notes for {VERSION}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
