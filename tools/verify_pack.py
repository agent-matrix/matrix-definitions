#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, sys
from _common import ROOT

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def verify_checksum_file(base: Path, checksum_file: Path, errors: list[str]):
    if not checksum_file.exists():
        errors.append(f'Missing checksum file: {checksum_file}')
        return
    for line in checksum_file.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            digest, rel = line.split('  ', 1)
        except ValueError:
            errors.append(f'Invalid checksum line: {line}')
            continue
        path = base / rel
        if not path.exists():
            errors.append(f'Checksum target missing: {path}')
        elif sha(path) != digest:
            errors.append(f'Checksum mismatch: {path}')

def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true', help='Require production signature/attestation metadata.')
    args = parser.parse_args(argv)
    errors: list[str] = []
    cur = ROOT / 'packs' / 'current'
    manifest_path = cur / 'manifest.json'
    if not manifest_path.exists():
        errors.append('Missing packs/current/manifest.json')
    else:
        manifest = load_json(manifest_path)
        if manifest.get('pack_id') != 'matrix-definitions-current':
            errors.append('Unexpected pack_id')
        if str(manifest.get('version')) != VERSION:
            errors.append('Manifest version does not match VERSION')
        for key, rel in manifest.get('packs', {}).items():
            if not (cur / rel).exists():
                errors.append(f'Missing pack file for {key}: {rel}')
    verify_checksum_file(cur, cur / 'checksums.txt', errors)
    for rel in ['reports/sbom.cdx.json', 'reports/provenance.json', 'signatures/cosign.bundle.json', 'signatures/github-attestation.json', 'signatures/provenance.intoto.jsonl']:
        if not (cur / rel).exists():
            errors.append(f'Missing metadata: packs/current/{rel}')
    release = ROOT / 'releases' / VERSION
    if release.exists():
        verify_checksum_file(release, release / 'checksums.txt', errors)
    else:
        if args.strict:
            errors.append(f'Missing release directory: releases/{VERSION}')
    if args.strict:
        for rel in ['signatures/cosign.bundle.json', 'signatures/github-attestation.json']:
            p = cur / rel
            if p.exists():
                try:
                    data = load_json(p)
                    if data.get('status') == 'placeholder':
                        errors.append(f'{rel} is placeholder metadata; production signature required')
                except Exception as exc:
                    errors.append(f'{rel} invalid JSON: {exc}')
        for artifact in [release / f'matrix-definitions-{VERSION}.tar.gz', release / f'matrix-definitions-{VERSION}.zip', release / 'sbom.cdx.json', release / 'provenance.intoto.jsonl']:
            if not artifact.exists():
                errors.append(f'Missing strict release artifact: {artifact}')
    report = {'ok': not errors, 'strict': args.strict, 'version': VERSION, 'errors': errors}
    out = cur / 'reports' / 'pack-verification.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    if errors:
        print('Pack verification failed:')
        for err in errors:
            print(' -', err)
        return 1
    print('OK pack verified')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
