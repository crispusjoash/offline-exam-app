import re
import sys

with open('src/data/kpsea-science-2023.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
for i, line in enumerate(lines):
    if '"explanation": "' in line:
        m = re.match(r'^(\s*"explanation"\s*:\s*"(?:[^"\\]|\\.)*")([^,\s].*)$', line)
        if m:
            print(f"Line {i+1} has extra text after quote.")
            line = m.group(1)
    new_lines.append(line)

with open('src/data/kpsea-science-2023.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Cleaned kpsea-science-2023.js")
