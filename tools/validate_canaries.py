#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
CANARIES = ROOT / "canaries" / "blueprints"
REQUIRED_PROMPTS = ["claude-code.md", "cursor.md", "codex-chatgpt.md", "gitpilot.md"]
REQUIRED_LOCK_RULES = {"RMD-001", "RMD-002", "RMD-004", "RMD-005", "RMD-101", "RMD-102"}


def load(path: Path):
    if path.suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def schema(name: str):
    return load(SCHEMAS / name)


def validate_file(path: Path, schema_name: str):
    Draft202012Validator(schema(schema_name)).validate(load(path))


def validate_canary(path: Path) -> list[str]:
    errors = []
    blueprint_path = path / "MATRIX_BLUEPRINT.yaml"
    lock_path = path / "MATRIX_STANDARDS.lock.yaml"
    report_path = path / "validation-report.json"
    if not blueprint_path.exists():
        errors.append(f"{path.name}: missing MATRIX_BLUEPRINT.yaml")
    if not lock_path.exists():
        errors.append(f"{path.name}: missing MATRIX_STANDARDS.lock.yaml")
    if not report_path.exists():
        errors.append(f"{path.name}: missing validation-report.json")
    if errors:
        return errors
    for f, s in [
        (blueprint_path, "matrix-blueprint.schema.json"),
        (lock_path, "matrix-standards-lock.schema.json"),
        (report_path, "validation-report.schema.json"),
    ]:
        try:
            validate_file(f, s)
        except Exception as exc:
            errors.append(f"{path.name}: {f.name} failed {s}: {exc}")
    blueprint = load(blueprint_path)
    lock = load(lock_path)
    for required in ["MATRIX_BLUEPRINT.yaml", "MATRIX_STANDARDS.lock", "MATRIX_TASKS.md", "MATRIX_ALLOWED_CHANGES.md", "MATRIX_ACCEPTANCE_CRITERIA.md", "MATRIX_VALIDATION.md"]:
        if required not in blueprint.get("required_files", []) and required not in lock.get("control_files", []):
            errors.append(f"{path.name}: required control file not represented: {required}")
    rules = set(lock.get("rules", []))
    missing_rules = sorted(REQUIRED_LOCK_RULES - rules)
    if missing_rules:
        errors.append(f"{path.name}: missing required RMD rules in standards lock: {missing_rules}")
    for prompt in REQUIRED_PROMPTS:
        if not (path / "prompts" / prompt).exists():
            errors.append(f"{path.name}: missing prompt {prompt}")
    return errors


def main() -> int:
    errors = []
    if not CANARIES.exists():
        print("No canaries directory found")
        return 1
    for path in sorted(p for p in CANARIES.iterdir() if p.is_dir()):
        errors.extend(validate_canary(path))
    if errors:
        print("Canary validation failed:")
        for e in errors:
            print(" -", e)
        return 1
    print(f"Validated {len(list(CANARIES.iterdir()))} canary blueprints")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
