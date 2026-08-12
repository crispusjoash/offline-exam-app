import json
import re

svg_content = """<svg width="380" height="230" viewBox="0 0 380 230" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font-family: 'Times New Roman', serif; font-size: 22px; font-weight: bold; fill: #4a423f; }
    .row { font-family: 'Times New Roman', serif; font-size: 20px; fill: #4a423f; }
    .line { stroke: #4a423f; stroke-width: 1.5; fill: none; }
    .bg { fill: #fdfdfd; }
  </style>

  <rect x="20" y="20" width="340" height="190" class="bg line" />
  
  <!-- Horizontal Lines -->
  <line x1="20" y1="55" x2="360" y2="55" class="line" />
  
  <!-- Vertical Line -->
  <line x1="150" y1="20" x2="150" y2="210" class="line" />
  
  <!-- Headers -->
  <text x="30" y="45" class="header">Day</text>
  <text x="255" y="45" text-anchor="middle" class="header">Distance in metres</text>
  
  <!-- Row 1 -->
  <text x="30" y="82" class="row">Monday</text>
  <text x="255" y="82" text-anchor="middle" class="row">400</text>
  
  <!-- Row 2 -->
  <text x="30" y="112" class="row">Tuesday</text>
  <text x="255" y="112" text-anchor="middle" class="row">800</text>
  
  <!-- Row 3 -->
  <text x="30" y="142" class="row">Wednesday</text>
  <text x="255" y="142" text-anchor="middle" class="row">1 600</text>
  
  <!-- Row 4 -->
  <text x="30" y="172" class="row">Thursday</text>
  <text x="255" y="172" text-anchor="middle" class="row">3 200</text>
  
  <!-- Row 5 -->
  <text x="30" y="202" class="row">Friday</text>
  <text x="255" y="202" text-anchor="middle" class="row">—</text>

</svg>
"""

with open("public/assets/math_2025_q6.svg", "w", encoding="utf-8") as f:
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
data["sharedContexts"]["ctx-math-2025-q6"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q6.svg",
    "title": "Distance Table",
    "cssFilter": "none",
    "scanEffect": False
}

# Update question 6
for q in data["sectionA"]:
    if q["id"] == "q6":
        q["contextRef"] = "ctx-math-2025-q6"
        q["questionText"] = "An athlete ran different distances in metres everyday. The distance the athlete ran each day formed a pattern as shown in the table.\n\nWhat distance did the athlete run on Friday?"
        
new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SVG created and linked for Q6")
