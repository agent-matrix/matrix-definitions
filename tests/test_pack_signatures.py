import subprocess, sys

def test_pack_verifies_after_build():
    subprocess.run([sys.executable, 'tools/build_pack.py'], check=True)
    subprocess.run([sys.executable, 'tools/sign_pack.py'], check=True)
    result = subprocess.run([sys.executable, 'tools/verify_pack.py'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
