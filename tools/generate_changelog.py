from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    version = (ROOT/'VERSION').read_text(encoding='utf-8').strip()
    print(f'# Changelog entry for {version}')
    print('- Update Matrix Definitions pack.')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
