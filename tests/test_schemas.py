from pathlib import Path
import json
import subprocess
import sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def test_json_schemas_are_valid_draft_2020_12():
    meta = Draft202012Validator.META_SCHEMA
    for path in (ROOT / "schemas").glob("*.schema.json"):
        Draft202012Validator(meta).validate(json.loads(path.read_text()))


def test_all_yaml_json_files_validate_against_registry():
    result = subprocess.run([sys.executable, "tools/validate_schemas.py"], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
