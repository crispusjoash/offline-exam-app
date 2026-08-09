import json
import re
import shutil

# Copy the image artifact to assets
source_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786272831610.png"
dest_img = r"public/assets/math_2025_q24.png"
shutil.copyfile(source_img, dest_img)

# Update the JS data file
file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add context image path
data["sharedContexts"]["ctx-math-2025-q24"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q24.png",
    "title": "Rabbit Hutch",
    "cssFilter": "none",
    "scanEffect": False
}

# Update Q24
for q in data["sectionA"]:
    if q["id"] == "q24":
        q["contextRef"] = "ctx-math-2025-q24"
        break

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Q24 image!")
