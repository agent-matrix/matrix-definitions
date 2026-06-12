from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]


def _rule_ids():
    ids = set()
    for base in ['industry', 'ruslan']:
        for p in (ROOT / base).rglob('*.yaml'):
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
            if isinstance(data, dict) and data.get('id'):
                ids.add(data['id'])
    return ids


def test_quality_profiles_exist_and_reference_existing_rules():
    ids = _rule_ids()
    for name in ['starter', 'standard', 'production', 'enterprise']:
        p = ROOT / 'profiles' / f'{name}.yaml'
        assert p.exists()
        data = yaml.safe_load(p.read_text(encoding='utf-8'))
        assert data['profile'] == name
        assert data['required_rules']
        missing = [rid for rid in data['required_rules'] if rid not in ids]
        assert not missing, f'{name} references missing rules: {missing}'


def test_quality_profile_progression_is_strictly_increasing():
    sizes = []
    for name in ['starter', 'standard', 'production', 'enterprise']:
        data = yaml.safe_load((ROOT / 'profiles' / f'{name}.yaml').read_text(encoding='utf-8'))
        sizes.append(len(data['required_rules']))
    assert sizes == sorted(sizes)
    assert sizes[0] < sizes[-1]
