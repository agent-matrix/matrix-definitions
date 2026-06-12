from __future__ import annotations
import sys, yaml
from pathlib import Path

def ids(path):
    data = yaml.safe_load((Path(path) / 'combined.pack.yaml').read_text(encoding='utf-8'))
    return {r['id'] for r in data.get('rules', [])}

def main():
    if len(sys.argv) != 3:
        print('usage: diff_packs.py OLD_PACK_DIR NEW_PACK_DIR')
        return 2
    old, new = ids(sys.argv[1]), ids(sys.argv[2])
    print('Added:', sorted(new-old))
    print('Removed:', sorted(old-new))
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
