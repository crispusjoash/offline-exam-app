import json
import re

svg_content = """<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font-family: 'Times New Roman', serif; font-size: 24px; font-weight: bold; fill: #4a423f; }
    .row { font-family: 'Times New Roman', serif; font-size: 24px; fill: #4a423f; }
    .line { stroke: #4a423f; stroke-width: 2; fill: none; }
  </style>

  <!-- Headers -->
  <text x="30" y="40" class="header">Item</text>
  <line x1="30" y1="46" x2="85" y2="46" class="line" />
  
  <text x="270" y="40" text-anchor="middle" class="header">Cost in shillings</text>
  <line x1="180" y1="46" x2="360" y2="46" class="line" />
  
  <!-- Row 1 -->
  <text x="30" y="95" class="row">Mathematical set</text>
  <text x="270" y="95" text-anchor="middle" class="row">250</text>
  
  <!-- Row 2 -->
  <text x="30" y="145" class="row">Pen</text>
  <text x="270" y="145" text-anchor="middle" class="row">45</text>
  
  <!-- Row 3 -->
  <text x="30" y="195" class="row">Pencil</text>
  <text x="270" y="195" text-anchor="middle" class="row">25</text>

</svg>
"""

with open("public/assets/math_2025_q21.svg", "w", encoding="utf-8") as f:
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
data["sharedContexts"]["ctx-math-2025-q21"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q21.svg",
    "title": "Shop Items List",
    "cssFilter": "none",
    "scanEffect": False
}

# Update question 21
for q in data["sectionA"]:
    if q["id"] == "q21":
        q["contextRef"] = "ctx-math-2025-q21"
        q["questionText"] = "Peter bought the following items from a shop.\nHe paid for all the items using a one-thousand shilling note.\nHow much balance did he receive?"
        
new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SVG created and linked for Q21")
