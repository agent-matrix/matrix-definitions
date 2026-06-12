from __future__ import annotations
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT/'packs/current/manifest.json').read_text(encoding='utf-8'))
    (ROOT/'releases/current.json').write_text(json.dumps({'current': manifest['version'], 'manifest': 'packs/current/manifest.json'}, indent=2)+'\n')
    print('Updated releases/current.json')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
