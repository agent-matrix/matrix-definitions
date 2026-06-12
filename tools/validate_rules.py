#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(path: Path):
    if path.suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validator(name: str):
    return Draft202012Validator(load(SCHEMAS / name))


def main() -> int:
    errors = []
    std_validator = validator("standards-rule.schema.json")
    rmd_validator = validator("rmd-rule.schema.json")
    source_ids = set()
    trusted = load(ROOT / "sources" / "trusted-sources.yaml")
    for src in trusted.get("sources", []):
        source_ids.add(src["id"])

    rule_ids = set()
    for path in sorted((ROOT / "industry").rglob("*.yaml")):
        data = load(path)
        if not isinstance(data, dict) or "id" not in data:
            continue
        errs = sorted(std_validator.iter_errors(data), key=lambda e: e.path)
        for e in errs:
            errors.append(f"{path.relative_to(ROOT)}: {e.message}")
        if data.get("id") in rule_ids:
            errors.append(f"duplicate rule id {data.get('id')} in {path.relative_to(ROOT)}")
        rule_ids.add(data.get("id"))
        for ref in data.get("source_refs", []) or []:
            if ref and ref not in source_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown source_ref {ref}")

    for path in sorted((ROOT / "ruslan").rglob("*.yaml")):
        data = load(path)
        if not isinstance(data, dict) or "id" not in data:
            continue
        errs = sorted(rmd_validator.iter_errors(data), key=lambda e: e.path)
        for e in errs:
            errors.append(f"{path.relative_to(ROOT)}: {e.message}")
        if data.get("id") in rule_ids:
            errors.append(f"duplicate rule id {data.get('id')} in {path.relative_to(ROOT)}")
        rule_ids.add(data.get("id"))

    if errors:
        print("Rule validation failed:")
        for err in errors:
            print(" -", err)
        return 1
    print(f"Validated {len(rule_ids)} standards and RMD rules")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
