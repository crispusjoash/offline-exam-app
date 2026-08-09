import json
import re

svg_content = """<svg width="600" height="150" viewBox="0 0 600 150" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font-family: 'Times New Roman', serif; font-size: 24px; font-weight: bold; fill: #4a423f; }
    .cell { font-family: 'Times New Roman', serif; font-size: 24px; fill: #4a423f; }
    .line { stroke: #4a423f; stroke-width: 2; fill: none; }
  </style>

  <!-- Table borders -->
  <rect x="20" y="20" width="560" height="100" class="line" />
  <line x1="20" y1="70" x2="580" y2="70" class="line" />
  
  <line x1="160" y1="20" x2="160" y2="120" class="line" />
  <line x1="280" y1="20" x2="280" y2="120" class="line" />
  <line x1="410" y1="20" x2="410" y2="120" class="line" />
  <line x1="510" y1="20" x2="510" y2="120" class="line" />

  <!-- Text -->
  <text x="30" y="55" class="header">Day</text>
  <text x="170" y="55" class="cell">Tuesday</text>
  <text x="285" y="55" class="cell">Wednesday</text>
  <text x="415" y="55" class="cell">Thursday</text>
  <text x="515" y="55" class="cell">Friday</text>

  <text x="30" y="95" class="header">Number</text>
  <text x="30" y="115" class="header">of Patients</text>
  
  <text x="220" y="105" text-anchor="middle" class="cell">23</text>
  <text x="345" y="105" text-anchor="middle" class="cell">—</text>
  <text x="460" y="105" text-anchor="middle" class="cell">18</text>
  <text x="545" y="105" text-anchor="middle" class="cell">26</text>
</svg>
"""

with open("public/assets/math_2025_q26.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add shared context
data["sharedContexts"]["ctx-math-2025-q26"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q26.svg",
    "title": "Hospital Patients Table",
    "cssFilter": "none",
    "scanEffect": False
}

# Update question 26
for q in data["sectionA"]:
    if q["id"] == "q26":
        q["contextRef"] = "ctx-math-2025-q26"
        q["questionText"] = "A hospital received 101 patients between Tuesday and Friday. The number of patients received each day was recorded in the following table except for Wednesday.\nHow many patients were received on Wednesday?"
        
new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SVG created and linked for Q26")
