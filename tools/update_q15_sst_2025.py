import json
import re

svg_content = """<svg width="450" height="380" xmlns="http://www.w3.org/2000/svg">
  <style>
    .opt { font-family: 'Times New Roman', serif; font-size: 18px; fill: #4a423f; }
    .label { font-family: 'Times New Roman', serif; font-size: 18px; fill: #4a423f; font-weight: normal; }
  </style>
  <rect width="100%" height="100%" fill="transparent" />
  
  <text x="20" y="30" class="label">A. Learner 1:</text>
  <text x="130" y="30" class="opt">Cycling of arms and legs</text>
  <text x="130" y="55" class="opt">while in flight phase of</text>
  <text x="130" y="80" class="opt">long jump.</text>

  <text x="20" y="120" class="label">B. Learner 2:</text>
  <text x="130" y="120" class="opt">Stretching and lengthening</text>
  <text x="130" y="145" class="opt">of the body while in the air</text>
  <text x="130" y="170" class="opt">in preparation for landing.</text>

  <text x="20" y="210" class="label">C. Learner 3:</text>
  <text x="130" y="210" class="opt">Lifting the legs and</text>
  <text x="130" y="235" class="opt">stretching hands into a toe</text>
  <text x="130" y="260" class="opt">touching position after</text>
  <text x="130" y="285" class="opt">taking off.</text>

  <text x="20" y="325" class="label">D. Learner 4:</text>
  <text x="130" y="325" class="opt">Gaining speed and taking</text>
  <text x="130" y="350" class="opt">off from one foot at the</text>
  <text x="130" y="375" class="opt">take-off board.</text>
</svg>"""

with open('public/assets/sst_2025_q15.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q15"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q15.svg",
    "title": "Learners descriptions",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q15":
        q["contextRef"] = "ctx-sst-2025-q15"
        q["options"][0]["text"] = "A"
        q["options"][1]["text"] = "B"
        q["options"][2]["text"] = "C"
        q["options"][3]["text"] = "D"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q15 updated successfully.")
