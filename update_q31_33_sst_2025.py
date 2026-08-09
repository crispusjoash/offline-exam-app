import json
import re
import shutil

src_image = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51\media__1786263744839.png"
dst_image = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\sst_2025_q31_33.png"

shutil.copyfile(src_image, dst_image)

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

data["sharedContexts"]["ctx-sst-2025-q31-33"] = {
    "type": "image",
    "imagePath": "/assets/sst_2025_q31_33.png",
    "title": "Map of Eastern Africa",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q31":
        q["questionText"] = "Study the following map of Eastern Africa and use it to answer questions 31 to 33."
        q["questionSuffix"] = "Identify the shaded climatic region marked K."
        q["contextRef"] = "ctx-sst-2025-q31-33"
    elif q["id"] == "q32":
        q["contextRef"] = "ctx-sst-2025-q31-33"
    elif q["id"] == "q33":
        q["contextRef"] = "ctx-sst-2025-q31-33"

new_content = "export const kpseaSstParta2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Q31-33 updated successfully.")
