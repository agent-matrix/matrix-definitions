#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path, PurePosixPath
from fnmatch import fnmatch
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY = SCHEMAS / "schema-registry.yaml"


def load_yaml_or_json(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def normalize_keys(value):
    # PyYAML 1.1 may parse GitHub Actions "on:" as True. Convert all keys to strings for JSON Schema.
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if k is True:
                key = "on"
            elif k is False:
                key = "off"
            else:
                key = str(k)
            out[key] = normalize_keys(v)
        return out
    if isinstance(value, list):
        return [normalize_keys(v) for v in value]
    return value


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_registry():
    registry = normalize_keys(load_yaml_or_json(REGISTRY))
    schema = load_yaml_or_json(SCHEMAS / "schema-registry.schema.json")
    Draft202012Validator(schema).validate(registry)
    return registry


def should_exclude(path: Path, registry: dict) -> bool:
    r = rel(path)
    for pattern in registry.get("exclude", []):
        if fnmatch(r, pattern):
            return True
    return False


def schema_for(path: Path, registry: dict) -> str | None:
    r = rel(path)
    for mapping in registry.get("mappings", []):
        if fnmatch(r, mapping["glob"]):
            return mapping["schema"]
    return registry.get("default_schema")


def iter_data_files(registry: dict):
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in {".yaml", ".yml", ".json"}:
            continue
        if ".pytest_cache" in path.parts:
            continue
        if should_exclude(path, registry):
            continue
        yield path


def main() -> int:
    # Validate all schemas against Draft 2020-12 metaschema.
    meta = Draft202012Validator.META_SCHEMA
    meta_validator = Draft202012Validator(meta)
    schema_cache = {}
    errors = []
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        try:
            schema = load_yaml_or_json(schema_path)
            meta_validator.validate(schema)
            schema_cache[schema_path.name] = schema
        except Exception as exc:
            errors.append(f"{rel(schema_path)}: invalid JSON Schema: {exc}")

    registry = load_registry()
    schema_cache["json-schema-meta"] = meta

    for path in sorted(iter_data_files(registry)):
        sname = schema_for(path, registry)
        if not sname:
            errors.append(f"{rel(path)}: no schema mapping")
            continue
        if sname == "json-schema-meta":
            continue
        schema = schema_cache.get(sname)
        if not schema:
            errors.append(f"{rel(path)}: schema {sname} is missing")
            continue
        try:
            data = normalize_keys(load_yaml_or_json(path))
            Draft202012Validator(schema).validate(data)
        except Exception as exc:
            errors.append(f"{rel(path)}: failed {sname}: {exc}")

    if errors:
        print("Schema validation failed:")
        for err in errors:
            print(" -", err)
        return 1
    print("All schemas and YAML/JSON data files validate against schema-registry.yaml")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
