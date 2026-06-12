#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib, os
from _common import ROOT

VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
NOW = '2026-06-12T00:00:00Z'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def subject(path: Path) -> dict:
    return {'name': path.relative_to(ROOT).as_posix(), 'digest': {'sha256': sha256(path)}}

def main() -> int:
    current = ROOT / 'packs' / 'current'
    subjects = [subject(current / name) for name in ['manifest.json','combined.pack.yaml','checksums.txt'] if (current / name).exists()]
    predicate = {
        'builder': {
            'id': os.environ.get('GITHUB_SERVER_URL', 'local') + '/' + os.environ.get('GITHUB_REPOSITORY', 'ruslanmv/matrix-definitions'),
            'version': VERSION
        },
        'buildType': 'https://ruslanmv.com/matrix-definitions/build-pack/v1',
        'invocation': {
            'configSource': {
                'uri': os.environ.get('GITHUB_SERVER_URL', 'local') + '/' + os.environ.get('GITHUB_REPOSITORY', 'ruslanmv/matrix-definitions'),
                'digest': {'sha1': os.environ.get('GITHUB_SHA', 'local')},
                'entryPoint': 'tools/create_release_bundle.py'
            }
        },
        'metadata': {'buildStartedOn': NOW, 'buildFinishedOn': NOW, 'reproducible': False},
        'materials': subjects
    }
    statement = {
        '_type': 'https://in-toto.io/Statement/v1',
        'subject': subjects,
        'predicateType': 'https://slsa.dev/provenance/v1',
        'predicate': predicate
    }
    out_jsonl = current / 'signatures' / 'provenance.intoto.jsonl'
    out_json = current / 'reports' / 'provenance.json'
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_jsonl.write_text(json.dumps(statement) + '\n', encoding='utf-8')
    out_json.write_text(json.dumps(statement, indent=2) + '\n', encoding='utf-8')
    print('Generated provenance metadata')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
