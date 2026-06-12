from __future__ import annotations
from pathlib import Path
import json, yaml, hashlib

ROOT = Path(__file__).resolve().parents[1]
RULE_DIRS = [ROOT / 'industry', ROOT / 'ruslan']

def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding='utf-8'))

def dump_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120), encoding='utf-8')

def rule_files():
    for base in RULE_DIRS:
        if not base.exists():
            continue
        for p in base.rglob('*.yaml'):
            if p.name in {'README.yaml'}:
                continue
            data = load_yaml(p)
            if isinstance(data, dict) and 'id' in data and 'validation' in data:
                yield p, data

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()
