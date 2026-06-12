#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json
from _common import ROOT

NOW = '2026-06-12T00:00:00Z'

def main() -> int:
    report_dir = ROOT / 'updater' / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)
    digest_report = report_dir / 'source-digest-check.json'
    findings = json.loads(digest_report.read_text(encoding='utf-8')).get('findings', []) if digest_report.exists() else []
    candidate = {
        'schema_version': '1.0',
        'status': 'draft',
        'created_at': NOW,
        'activation': 'manual_review_required',
        'findings': findings,
        'recommendation': 'No automatic activation. Review source digest report and propose rule changes by PR.'
    }
    (report_dir / 'candidate-update.json').write_text(json.dumps(candidate, indent=2) + '\n', encoding='utf-8')
    md = ['# Candidate standards update', '', f'Created at: {NOW}', '', 'This PR contains a candidate update report. It does not activate rules automatically.', '', f'Sources checked: {len(findings)}', '', '## Review checklist', '', '- [ ] Review source digests', '- [ ] Review proposed rule changes', '- [ ] Run canary generation', '- [ ] Approve or quarantine candidate', '']
    (report_dir / 'candidate-update-pr.md').write_text('\n'.join(md), encoding='utf-8')
    print('Created candidate update report')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
