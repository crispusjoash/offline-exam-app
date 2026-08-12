import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
fixed_lines = []
in_broken_string = False

for line in lines:
    if in_broken_string:
        if '",' in line or '"' in line[-2:] or '"]' in line:
            fixed_lines[-1] += '\\\\n' + line
            in_broken_string = False
        else:
            fixed_lines[-1] += '\\\\n' + line
    else:
        # Check if line has an unclosed double quote.
        # A simple check: starts with a key but does not end with closing quote
        stripped = line.strip()
        if (stripped.startswith('explanation: "') or stripped.startswith('text: "') or stripped.startswith('title: "')) and not stripped.endswith('",') and not stripped.endswith('"') and not stripped.endswith('"]'):
            fixed_lines.append(line)
            in_broken_string = True
        else:
            fixed_lines.append(line)

content = '\n'.join(fixed_lines)
with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Syntax fixed!')
