import subprocess
import sys


def test_canaries_validate():
    result = subprocess.run([sys.executable, 'tools/validate_canaries.py'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
