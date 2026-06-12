#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(path: Path):
    return json.loads(path.read_text()) if path.suffix == ".json" else yaml.safe_load(path.read_text())


def validate(path: Path, schema_name: str):
    Draft202012Validator(load(SCHEMAS / schema_name)).validate(load(path))


def main() -> int:
    validate(ROOT / "examples" / "matrix-blueprint.yaml", "matrix-blueprint.schema.json")
    validate(ROOT / "examples" / "matrix-standards.lock.yaml", "matrix-standards-lock.schema.json")
    validate(ROOT / "examples" / "control" / "MATRIX_BLUEPRINT.yaml", "matrix-blueprint.schema.json")
    validate(ROOT / "examples" / "control" / "MATRIX_STANDARDS.lock.yaml", "matrix-standards-lock.schema.json")
    validate(ROOT / "examples" / "validation-report.json", "validation-report.schema.json")
    print("Matrix control contract examples are valid")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
