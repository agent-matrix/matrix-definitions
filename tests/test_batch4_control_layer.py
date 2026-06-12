from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_matrix_control_templates_exist():
    required = [
        'matrix-control/templates/MATRIX_BLUEPRINT.yaml',
        'matrix-control/templates/MATRIX_STANDARDS.lock',
        'matrix-control/templates/MATRIX_TASKS.md',
        'matrix-control/templates/MATRIX_ALLOWED_CHANGES.md',
        'matrix-control/templates/MATRIX_ACCEPTANCE_CRITERIA.md',
        'matrix-control/templates/MATRIX_VALIDATION.md',
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel


def test_ai_coder_adapter_policies_exist():
    for adapter in ['claude-code','codex-chatgpt','cursor','ibm-bob','gitpilot','generic-ai-coder']:
        assert (ROOT / 'matrix-control' / 'coder-policies' / f'{adapter}.yaml').exists()
        assert (ROOT / 'matrix-control' / 'prompt-templates' / f'{adapter}.md').exists()


def test_batch4_rmd_rules_present():
    ids = set()
    for path in (ROOT / 'ruslan' / 'ai-coder-control').glob('*.yaml'):
        data = yaml.safe_load(path.read_text())
        if isinstance(data, dict) and 'id' in data:
            ids.add(data['id'])
    for rid in [f'RMD-{i:03d}' for i in range(107, 121)]:
        assert rid in ids


def test_standard_profile_requires_control_layer():
    data = yaml.safe_load((ROOT / 'profiles' / 'standard.yaml').read_text())
    for rid in ['RMD-107','RMD-108','RMD-115','RMD-116','RMD-119','RMD-120']:
        assert rid in data['required_rules']
