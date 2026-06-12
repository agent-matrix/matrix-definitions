import subprocess, sys

def test_pack_builds():
    result = subprocess.run([sys.executable, 'tools/build_pack.py'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
