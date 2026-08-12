import json
import re
import shutil

src_image = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786263618615.png"
dst_image = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\sst_2025_q28.png"

shutil.copyfile(src_image, dst_image)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q28"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q28.png",
    "title": "Pieces of wood for mitre joint",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q28":
        q["questionText"] = "A learner wants to make a mitre joint using the following pieces of wood."
        q["questionSuffix"] = "Which two materials should the learner use to make the joint strong?"
        q["contextRef"] = "ctx-sst-2025-q28"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q28 updated successfully.")
