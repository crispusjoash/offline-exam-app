import json
import re

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

def fix_text(text):
    if not isinstance(text, str): return text
    # Fix mixed numbers first: e.g. "1 19/31" -> "$1 \\frac{19}{31}$"
    # Negative lookbehind to not match inside another math block or string
    res = re.sub(r'(?<!\$)\b(\d+) (\d+)/(\d+)\b(?!\$)', r'$\1 \\frac{\2}{\3}$', text)
    # Fix regular fractions: e.g. "5/8" -> "$\\frac{5}{8}$"
    res = re.sub(r'(?<!\$)\b(\d+)/(\d+)\b(?!\$)', r'$\\frac{\1}{\2}$', res)
    return res

for q in data["sectionA"]:
    if "questionText" in q:
        q["questionText"] = fix_text(q["questionText"])
    if "explanation" in q:
        # Revert my previous half fix for Q5 to keep it consistent if needed, but let's just run fix_text on it
        q["explanation"] = fix_text(q["explanation"])
    if "options" in q:
        for opt in q["options"]:
            opt["text"] = fix_text(opt["text"])

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fractions fixed in Math 2025!")
