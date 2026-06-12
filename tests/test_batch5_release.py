import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / 'VERSION').read_text().strip()

def run(cmd):
    result = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    return result

def test_release_bundle_and_verification():
    run(['tools/build_pack.py'])
    run(['tools/generate_sbom.py'])
    run(['tools/generate_provenance.py'])
    run(['tools/sign_pack.py'])
    run(['tools/create_release_bundle.py'])
    run(['tools/verify_pack.py'])
    release = ROOT / 'releases' / VERSION
    assert (release / f'matrix-definitions-{VERSION}.tar.gz').exists()
    assert (release / f'matrix-definitions-{VERSION}.zip').exists()
    assert (release / 'checksums.txt').exists()
    assert (ROOT / 'releases' / 'current.json').exists()

def test_sbom_is_cyclonedx():
    run(['tools/generate_sbom.py'])
    sbom = json.loads((ROOT / 'packs' / 'current' / 'reports' / 'sbom.cdx.json').read_text())
    assert sbom['bomFormat'] == 'CycloneDX'
    assert sbom['components']

def test_candidate_update_report():
    run(['tools/check_standards_updates.py'])
    run(['tools/create_candidate_update.py'])
    report = json.loads((ROOT / 'updater' / 'reports' / 'candidate-update.json').read_text())
    assert report['activation'] == 'manual_review_required'
