from __future__ import annotations
from _common import ROOT, rule_files

def main():
    out = ROOT / 'docs' / 'generated-rule-index.md'
    lines = ['# Generated Rule Index', '']
    for path, data in sorted(rule_files(), key=lambda x: x[1].get('id','')):
        lines.append(f"- **{data['id']}** — {data.get('title')} (`{path.relative_to(ROOT)}`)")
    out.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'wrote {out}')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
