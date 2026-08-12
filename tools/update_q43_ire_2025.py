import json
import re

svg_content = """<svg width="450" height="180" xmlns="http://www.w3.org/2000/svg">
  <style>
    .name { font-family: 'Times New Roman', serif; font-size: 20px; fill: #4a423f; }
    .action { font-family: 'Times New Roman', serif; font-size: 20px; fill: #4a423f; }
  </style>
  <rect width="100%" height="100%" fill="transparent" />
  
  <text x="20" y="30" class="name">Ali:</text>
  <text x="90" y="30" class="action">said Bismillah before eating</text>

  <text x="20" y="65" class="name">Musa:</text>
  <text x="90" y="65" class="action">ate with his right hand</text>

  <text x="20" y="100" class="name">Said:</text>
  <text x="90" y="100" class="action">ate while the food was very hot</text>

  <text x="20" y="135" class="name">Salim:</text>
  <text x="90" y="135" class="action">ate what was nearest to him on the</text>
  <text x="90" y="165" class="action">plate</text>
</svg>"""

with open('public/assets/ire_2025_q43.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-sst-ire-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-ire-2025-q43"] = {
    "type": "image",
    "imagePath": "/assets/ire_2025_q43.svg",
    "title": "Learners eating actions",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q43":
        q["questionText"] = "A teacher observed the following as his learners took lunch:"
        q["questionSuffix"] = "Who among the learners did not apply the etiquette of eating according to the Hadith of the Prophet (P.b.u.h)?"
        q["contextRef"] = "ctx-ire-2025-q43"

new_content = "export const kpseaSstIre2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q43 updated successfully.")
