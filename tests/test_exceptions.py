from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]

def test_sample_exception_has_expiry():
    data = yaml.safe_load((ROOT/'exceptions/examples/sample-exception.yaml').read_text(encoding='utf-8'))
    assert data['expires_at']
    assert data['rule_id']
