import os
import glob
import re

files = glob.glob('src/data/*.js')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    match = re.search(r'"durationMinutes":\s*(\d+)', content)
    if match:
        print(f"{os.path.basename(f)}: durationMinutes = {match.group(1)}")
    else:
        print(f"{os.path.basename(f)}: No durationMinutes found")
