import json
import re

svg_content = """<svg width="450" height="320" xmlns="http://www.w3.org/2000/svg">
  <style>
    .opt { font-family: 'Times New Roman', serif; font-size: 19px; fill: #4a423f; }
    .label { font-family: 'Times New Roman', serif; font-size: 19px; fill: #4a423f; font-weight: normal; }
  </style>
  <rect width="100%" height="100%" fill="transparent" />
  
  <text x="20" y="30" class="label">A. Member 1:</text>
  <text x="140" y="30" class="opt">The body of the performer</text>
  <text x="140" y="55" class="opt">is supported by the legs</text>
  <text x="140" y="80" class="opt">only.</text>

  <text x="20" y="125" class="label">B. Member 2:</text>
  <text x="140" y="125" class="opt">The stomach faces down</text>
  <text x="140" y="150" class="opt">during the performance.</text>

  <text x="20" y="195" class="label">C. Member 3:</text>
  <text x="140" y="195" class="opt">The performer lies flat on</text>
  <text x="140" y="220" class="opt">the ground while facing up.</text>

  <text x="20" y="265" class="label">D. Member 4:</text>
  <text x="140" y="265" class="opt">The performer is supported</text>
  <text x="140" y="290" class="opt">by both hands and feet.</text>
</svg>"""

with open('public/assets/sst_2025_q18.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q18"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q18.svg",
    "title": "Members descriptions",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q18":
        q["contextRef"] = "ctx-sst-2025-q18"
        q["options"][0]["text"] = "A"
        q["options"][1]["text"] = "B"
        q["options"][2]["text"] = "C"
        q["options"][3]["text"] = "D"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q18 updated successfully.")
