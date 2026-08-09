import json
import re
import shutil

# Copy the image artifact to assets
source_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786274245700.png"
dest_img = r"public/assets/science_2025_q3.png"
shutil.copyfile(source_img, dest_img)

# Update the JS data file
file_path = 'src/data/kpsea-science-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add context image path
data["sharedContexts"]["ctx-science-2025-q3"] = {
    "type": "image",
    "imagePath": "/assets/science_2025_q3.png",
    "title": "Human Digestive System",
    "cssFilter": "none",
    "scanEffect": False
}

# Update Q3
for q in data["sectionA"]:
    if q["id"] == "q3":
        q["contextRef"] = "ctx-science-2025-q3"
        q["questionText"] = "The following diagram represents the human digestive system.\n\nIdentify the part labeled G."
        break

new_content = "export const kpseaScience2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Science Q3 image!")
