from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]

def iter_rules():
    for base in [ROOT/'industry', ROOT/'ruslan']:
        for p in base.rglob('*.yaml'):
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
            if isinstance(data, dict) and 'id' in data and 'validation' in data:
                yield p, data

def test_rule_ids_unique():
    seen = {}
    for p, d in iter_rules():
        assert d['id'] not in seen, f'duplicate {d["id"]}: {seen.get(d["id"])} and {p}'
        seen[d['id']] = p
    assert len(seen) >= 30
