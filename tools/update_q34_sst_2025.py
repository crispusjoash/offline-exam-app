import json
import re

svg_content = """<svg width="400" height="320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="dots" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
      <circle fill="#555" cx="3" cy="3" r="1.5"></circle>
    </pattern>
  </defs>

  <!-- Trough left side liquid -->
  <path d="M 50 200 Q 60 190 70 190 L 155 190 L 155 280 L 50 280 Z" fill="url(#dots)" stroke="black" stroke-width="2"/>
  
  <!-- Trough right side liquid -->
  <path d="M 195 190 L 280 190 Q 290 190 300 200 L 300 280 L 195 280 Z" fill="url(#dots)" stroke="black" stroke-width="2"/>

  <!-- Liquid inside the tube -->
  <path d="M 155 100 Q 175 75 195 100 L 195 280 L 155 280 Z" fill="url(#dots)" stroke="black" stroke-width="2"/>

  <!-- Trough outlines (left, bottom, right) -->
  <polyline points="50,160 50,280 300,280 300,160" fill="none" stroke="black" stroke-width="2"/>

  <!-- Glass Tube -->
  <path d="M 155 280 L 155 50 A 20 20 0 0 1 195 50 L 195 280" fill="none" stroke="#333" stroke-width="3"/>

  <!-- Labels -->
  <line x1="195" y1="65" x2="230" y2="65" stroke="black" stroke-width="2"/>
  <text x="235" y="71" font-family="sans-serif" font-size="20" fill="#444">Glass Tube</text>

  <line x1="175" y1="125" x2="230" y2="125" stroke="black" stroke-width="2"/>
  <text x="235" y="132" font-family="sans-serif" font-size="20" fill="#444">X</text>
</svg>"""

with open('public/assets/sst_2025_q34.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q34"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q34.svg",
    "title": "Barometer Diagram",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q34":
        q["questionText"] = "The following diagram shows an instrument used to measure an element of weather."
        q["questionSuffix"] = "The substance marked X is"
        q["contextRef"] = "ctx-sst-2025-q34"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q34 updated successfully.")
