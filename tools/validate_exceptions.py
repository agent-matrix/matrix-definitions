#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys, yaml
from datetime import date
from _common import ROOT


def main() -> int:
    errors = []
    for base in [ROOT / 'exceptions' / 'active', ROOT / 'exceptions' / 'examples']:
        if not base.exists():
            continue
        for p in base.glob('*.yaml'):
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
            if not isinstance(data, dict):
                continue
            if 'expires_at' not in data:
                errors.append(f'{p}: missing expires_at')
            if data.get('severity') == 'critical' and 'Ruslan Magana' not in data.get('approved_by', []):
                errors.append(f'{p}: critical exception requires Ruslan Magana approval')
            if data.get('status') == 'active' and data.get('expires_at'):
                try:
                    if date.fromisoformat(str(data['expires_at'])) < date(2026, 6, 12):
                        errors.append(f'{p}: expired exception is still active')
                except Exception:
                    errors.append(f'{p}: expires_at must be YYYY-MM-DD')
    if errors:
        print('Exception validation failed:')
        for err in errors:
            print(' -', err)
        return 1
    print('Exception policy validation passed')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
