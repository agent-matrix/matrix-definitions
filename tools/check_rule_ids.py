from __future__ import annotations
from _common import rule_files, ROOT

def main():
    seen = {}
    errors = []
    for path, data in rule_files():
        rid = data.get('id')
        if rid in seen:
            errors.append(f'Duplicate rule id {rid}: {seen[rid]} and {path}')
        seen[rid] = path
    if errors:
        for e in errors: print(e)
        return 1
    print(f'OK unique rule IDs: {len(seen)} rules')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
