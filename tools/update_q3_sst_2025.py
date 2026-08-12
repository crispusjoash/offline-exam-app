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

data["sharedContexts"]["ctx-sst-2025-q3"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q3.svg",
    "title": "Scores Matching",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q3":
        q["contextRef"] = "ctx-sst-2025-q3"
        # Since the image contains the options, we simplify the text options to avoid duplication
        q["options"][0]["text"] = "A"
        q["options"][1]["text"] = "B"
        q["options"][2]["text"] = "C"
        q["options"][3]["text"] = "D"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q3 updated successfully.")
