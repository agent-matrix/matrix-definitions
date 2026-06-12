from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(path):
    return json.loads(path.read_text()) if path.suffix == ".json" else yaml.safe_load(path.read_text())


def validator(name):
    return Draft202012Validator(load(SCHEMAS / name))


def test_valid_matrix_blueprint_contract():
    validator("matrix-blueprint.schema.json").validate(load(ROOT / "examples/schemas/valid/matrix-blueprint.yaml"))


def test_valid_matrix_standards_lock():
    validator("matrix-standards-lock.schema.json").validate(load(ROOT / "examples/schemas/valid/matrix-standards.lock.yaml"))


def test_valid_validation_report():
    validator("validation-report.schema.json").validate(load(ROOT / "examples/schemas/valid/validation-report.json"))


def test_invalid_rule_fixture_fails():
    with __import__('pytest').raises(ValidationError):
        validator("standards-rule.schema.json").validate(load(ROOT / "examples/schemas/invalid/standards-rule-missing-validation.yaml"))


def test_invalid_blueprint_fixture_fails():
    with __import__('pytest').raises(ValidationError):
        validator("matrix-blueprint.schema.json").validate(load(ROOT / "examples/schemas/invalid/matrix-blueprint-missing-stack.yaml"))
