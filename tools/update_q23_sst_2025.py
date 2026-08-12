import json
import re
import shutil

src_image = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786263143779.png"
dst_image = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\sst_2025_q23.png"

shutil.copyfile(src_image, dst_image)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q23"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q23.png",
    "title": "Recorders fingering",
    "cssFilter": "grayscale(100%) contrast(150%) brightness(105%)",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q23":
        q["questionText"] = "Which letter names are represented by the following fingering of a descant recorder?"
        q["contextRef"] = "ctx-sst-2025-q23"
        q["options"][0]["text"] = "A"
        q["options"][1]["text"] = "B"
        q["options"][2]["text"] = "C"
        q["options"][3]["text"] = "D"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q23 updated successfully.")
