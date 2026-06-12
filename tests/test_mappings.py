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


def test_mapping_files_parse():
    for p in (ROOT/'mappings').glob('*.yaml'):
        data = yaml.safe_load(p.read_text(encoding='utf-8'))
        assert data.get('schema_version') == '1.0'
        assert 'mappings' in data


def test_core_mapping_files_reference_existing_rules():
    ids = _rule_ids()
    for filename in [
        'standards-to-generator-rules.yaml',
        'standards-to-validation-checks.yaml',
        'standards-to-template-files.yaml',
        'standards-to-blueprint-fields.yaml',
        'standards-to-matrixhub-metadata.yaml',
    ]:
        data = yaml.safe_load((ROOT/'mappings'/filename).read_text(encoding='utf-8'))
        missing = []
        for item in data.get('mappings', []):
            rid = item.get('rule')
            if rid and rid not in ids:
                missing.append(rid)
        assert not missing, f'{filename} references missing rules: {missing}'


def test_generator_and_validation_mappings_cover_all_rules():
    ids = _rule_ids()
    generator = yaml.safe_load((ROOT/'mappings'/'standards-to-generator-rules.yaml').read_text(encoding='utf-8'))
    validation = yaml.safe_load((ROOT/'mappings'/'standards-to-validation-checks.yaml').read_text(encoding='utf-8'))
    gen_ids = {m['rule'] for m in generator['mappings'] if 'rule' in m}
    val_ids = {m['rule'] for m in validation['mappings'] if 'rule' in m}
    missing_gen = sorted(ids - gen_ids)
    missing_val = sorted(ids - val_ids)
    assert not missing_gen, missing_gen
    assert not missing_val, missing_val
