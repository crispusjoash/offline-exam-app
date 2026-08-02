import os
import glob
import subprocess

jsx_files = glob.glob('src/**/*.jsx', recursive=True) + glob.glob('src/**/*.js', recursive=True)

print(f"Found {len(jsx_files)} JS/JSX files.")

for f in jsx_files:
    # Test syntax with node --check or babel if available, or basic node evaluation
    res = subprocess.run(['node', '-c', f], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Syntax error in {f}:\n{res.stderr}")
