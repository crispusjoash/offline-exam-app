import glob
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the export line
    match = re.match(r'^(export\s+const\s+\w+\s*=\s*)([\s\S]+)(;\s*)$', content.strip())
    if not match:
        print(f"Skipping {filepath}, pattern not matched")
        return False

    prefix, body, suffix = match.groups()

    # Fix raw newlines within double quotes in JS object literals
    # We iterate character by character through body
    in_string = False
    escaped = False
    fixed_chars = []

    for char in body:
        if char == '"' and not escaped:
            in_string = not in_string
            fixed_chars.append(char)
        elif char == '\n' and in_string:
            fixed_chars.append('\\n')
        elif char == '\r' and in_string:
            pass # skip carriage returns in string
        else:
            fixed_chars.append(char)
            if char == '\\' and not escaped:
                escaped = True
                continue
        escaped = False

    new_content = prefix + ''.join(fixed_chars) + suffix

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed string newlines in {filepath}")
        return True
    return False

for f in sorted(glob.glob('src/data/*.js')):
    if 'pastPapers' in f:
        continue
    fix_file(f)
