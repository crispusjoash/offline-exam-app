import json
import re

svg_content = """<svg width="400" height="150" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(0, 30)">
    <!-- Minim -->
    <g transform="translate(50, 50)">
      <!-- Empty head for minim -->
      <ellipse cx="0" cy="0" rx="10" ry="7" transform="rotate(-20)" fill="white" stroke="black" stroke-width="2.5"/>
      <line x1="9" y1="-2" x2="9" y2="-50" stroke="black" stroke-width="2"/>
    </g>

    <!-- Beamed Quavers -->
    <g transform="translate(150, 50)">
      <ellipse cx="0" cy="0" rx="10" ry="7" transform="rotate(-20)" fill="black"/>
      <line x1="9" y1="-2" x2="9" y2="-50" stroke="black" stroke-width="2"/>
      
      <ellipse cx="40" cy="0" rx="10" ry="7" transform="rotate(-20)" fill="black"/>
      <line x1="49" y1="-2" x2="49" y2="-50" stroke="black" stroke-width="2"/>
      
      <!-- Beam -->
      <polygon points="9,-50 49,-50 49,-42 9,-42" fill="black"/>
    </g>

    <!-- Crotchet 1 -->
    <g transform="translate(250, 50)">
      <ellipse cx="0" cy="0" rx="10" ry="7" transform="rotate(-20)" fill="black"/>
      <line x1="9" y1="-2" x2="9" y2="-50" stroke="black" stroke-width="2"/>
    </g>
    
    <!-- Crotchet 2 -->
    <g transform="translate(320, 50)">
      <ellipse cx="0" cy="0" rx="10" ry="7" transform="rotate(-20)" fill="black"/>
      <line x1="9" y1="-2" x2="9" y2="-50" stroke="black" stroke-width="2"/>
    </g>
  </g>
</svg>"""

with open('public/assets/sst_2025_q17.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q17"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q17.svg",
    "title": "Musical Notes",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q17":
        q["questionText"] = "Which French rhythm names correspond with the following rhythmic pattern?"
        q["contextRef"] = "ctx-sst-2025-q17"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q17 updated successfully.")
