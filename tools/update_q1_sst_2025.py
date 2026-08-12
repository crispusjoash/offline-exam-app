import json
import re

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q1"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q1.svg",
    "title": "Colour Wheel",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q1":
        q["questionText"] = "The following chart shows primary and secondary colours."
        q["questionSuffix"] = "Name the colours in the parts labelled W and X."
        q["contextRef"] = "ctx-sst-2025-q1"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q1 updated successfully.")
