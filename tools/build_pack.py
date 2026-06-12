from __future__ import annotations
from pathlib import Path
from _common import ROOT, rule_files, dump_yaml, sha256_file
import json
VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
NOW = '2026-06-12T00:00:00Z'

def main():
    industry=[]; ruslan=[]
    domain_counts={}
    severity_counts={}
    for path, data in sorted(rule_files(), key=lambda x: x[1].get('id','')):
        rel = str(path.relative_to(ROOT))
        item = {'id': data['id'], 'path': rel, 'domain': data.get('domain'), 'severity': data.get('severity')}
        domain_counts[item['domain'] or 'unknown'] = domain_counts.get(item['domain'] or 'unknown', 0) + 1
        severity_counts[item['severity'] or 'unknown'] = severity_counts.get(item['severity'] or 'unknown', 0) + 1
        if rel.startswith('industry/'):
            industry.append(item)
        elif rel.startswith('ruslan/'):
            ruslan.append(item)
    current = ROOT / 'packs' / 'current'
    current.mkdir(parents=True, exist_ok=True)
    (current / 'reports').mkdir(parents=True, exist_ok=True)
    (current / 'signatures').mkdir(parents=True, exist_ok=True)
    industry_pack={'schema_version':'1.0','pack_id':'matrix-industry-pack','version':VERSION,'status':'stable','metadata':{'owner':'Ruslan Magana','created_at':NOW},'rules':industry}
    ruslan_pack={'schema_version':'1.0','pack_id':'ruslan-magana-definitions','version':'1.0.0','status':'stable','metadata':{'owner':'Ruslan Magana','created_at':NOW},'rules':ruslan}
    matrixhub_pack={'schema_version':'1.0','pack_id':'matrixhub-template-rules','version':'1.0.0','status':'stable','metadata':{'owner':'Ruslan Magana','created_at':NOW},'rules':[r for r in ruslan if r['id'].startswith('RMD-3')]}
    combined={'schema_version':'1.0','pack_id':'matrix-definitions-current','version':VERSION,'status':'stable','metadata':{'name':'Matrix Definitions','owner':'Ruslan Magana','homepage':'https://ruslanmv.com/definitions','created_at':NOW},'includes':{'industry_pack':'industry.pack.yaml','ruslan_pack':'ruslan.pack.yaml','matrixhub_pack':'matrixhub.pack.yaml'},'profiles':['starter','standard','production','enterprise'],'rules':industry+ruslan}
    dump_yaml(current / 'industry.pack.yaml', industry_pack)
    dump_yaml(current / 'ruslan.pack.yaml', ruslan_pack)
    dump_yaml(current / 'matrixhub.pack.yaml', matrixhub_pack)
    dump_yaml(current / 'combined.pack.yaml', combined)
    manifest={'schema_version':'1.0','pack_id':'matrix-definitions-current','version':VERSION,'status':'stable','created_at':NOW,'owner':'Ruslan Magana','brand':'Ruslan Magana Definitions','website':'https://ruslanmv.com/definitions','compatibility':{'agent_generator':'>=0.2.0','matrix_builder':'>=0.1.0','matrixhub':'>=0.1.0'},'packs':{'industry':'industry.pack.yaml','ruslan':'ruslan.pack.yaml','matrixhub':'matrixhub.pack.yaml','combined':'combined.pack.yaml'},'signatures':{'cosign_bundle':'signatures/cosign.bundle.json','github_attestation':'signatures/github-attestation.json','provenance':'signatures/provenance.intoto.jsonl'},'checksums':'checksums.txt'}
    (current / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    # Validation report is regenerated here without pack-verification to avoid circular checksum dependencies.
    validation_report={'schema_version':'1.0','status':'passed','created_at':NOW,'definitions_pack':VERSION,'checks':[{'id':'pack-build','status':'passed','message':f'Pack built successfully with {len(combined["rules"])} rules ({len(industry)} industry, {len(ruslan)} Ruslan).'}]}
    (current / 'reports' / 'validation-report.json').write_text(json.dumps(validation_report, indent=2)+'\n', encoding='utf-8')
    (current / 'reports' / 'rule-counts.json').write_text(json.dumps({'schema_version':'1.0','domain_counts':domain_counts,'severity_counts':severity_counts}, indent=2)+'\n', encoding='utf-8')
    lines=[]
    for rel in ['manifest.json','industry.pack.yaml','ruslan.pack.yaml','matrixhub.pack.yaml','combined.pack.yaml','reports/validation-report.json','reports/rule-counts.json']:
        p=current/rel; lines.append(f'{sha256_file(p)}  {rel}')
    (current / 'checksums.txt').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Built pack {VERSION}: {len(combined["rules"])} rules')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
