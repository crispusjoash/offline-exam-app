import json
import re
import shutil
import os

# 1. Copy the image artifact to assets
source_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786267358671.png"
dest_img = r"public/assets/math_2025_q22.png"
shutil.copyfile(source_img, dest_img)

# 2. Remove the SVG if it exists
svg_path = r"public/assets/math_2025_q22.svg"
if os.path.exists(svg_path):
    os.remove(svg_path)

# 3. Update the JS data file
file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Update context image path
if "ctx-math-2025-q22" in data["sharedContexts"]:
    data["sharedContexts"]["ctx-math-2025-q22"]["imagePath"] = "/assets/math_2025_q22.png"

# Update explanation for Q5
for q in data["sectionA"]:
    if q["id"] == "q5":
        q["explanation"] = "The decorated part is a right-angled triangle with base 20 cm and height 18 cm. Area = ½ × base × height = ½ × 20 × 18 = 180 cm²."
        break

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Q22 image and Q5 fraction!")
