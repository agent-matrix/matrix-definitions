#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, shutil, tarfile, zipfile, hashlib
from _common import ROOT

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
NOW = '2026-06-12T00:00:00Z'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def add_dir_to_tar(tar: tarfile.TarFile, base: Path, arcbase: str):
    for p in sorted(base.rglob('*')):
        tar.add(p, arcname=f'{arcbase}/{p.relative_to(base).as_posix()}')

def add_dir_to_zip(zf: zipfile.ZipFile, base: Path, arcbase: str):
    for p in sorted(base.rglob('*')):
        if p.is_file():
            zf.write(p, f'{arcbase}/{p.relative_to(base).as_posix()}')

def main() -> int:
    current = ROOT / 'packs' / 'current'
    release = ROOT / 'releases' / VERSION
    release.mkdir(parents=True, exist_ok=True)
    # Copy pack files and reports/signatures into release directory.
    for name in ['manifest.json','checksums.txt','industry.pack.yaml','ruslan.pack.yaml','matrixhub.pack.yaml','combined.pack.yaml']:
        shutil.copy2(current / name, release / name)
    for src, dest in [
        (current / 'reports' / 'sbom.cdx.json', release / 'sbom.cdx.json'),
        (current / 'reports' / 'provenance.json', release / 'provenance.json'),
        (current / 'signatures' / 'provenance.intoto.jsonl', release / 'provenance.intoto.jsonl'),
        (current / 'signatures' / 'cosign.bundle.json', release / 'cosign.bundle.json'),
        (current / 'signatures' / 'github-attestation.json', release / 'github-attestation.json'),
    ]:
        if src.exists():
            shutil.copy2(src, dest)
    tar_path = release / f'matrix-definitions-{VERSION}.tar.gz'
    zip_path = release / f'matrix-definitions-{VERSION}.zip'
    if tar_path.exists(): tar_path.unlink()
    if zip_path.exists(): zip_path.unlink()
    with tarfile.open(tar_path, 'w:gz') as tar:
        add_dir_to_tar(tar, current, f'matrix-definitions-{VERSION}/packs/current')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        add_dir_to_zip(zf, current, f'matrix-definitions-{VERSION}/packs/current')
    # Release checksums include archives and copied release metadata.
    lines = []
    for p in sorted(release.iterdir()):
        if p.is_file() and p.name != 'checksums.txt':
            lines.append(f'{sha256(p)}  {p.name}')
    (release / 'checksums.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    current_json = {
        'schema_version': '1.0', 'version': VERSION, 'status': 'stable', 'created_at': NOW,
        'release_dir': f'releases/{VERSION}',
        'artifacts': {'tar_gz': tar_path.name, 'zip': zip_path.name, 'checksums': 'checksums.txt'},
        'pack_manifest': 'packs/current/manifest.json'
    }
    (ROOT / 'releases' / 'current.json').write_text(json.dumps(current_json, indent=2) + '\n', encoding='utf-8')
    print(f'Created release bundle {VERSION}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
