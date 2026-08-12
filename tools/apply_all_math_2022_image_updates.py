import json
import re

# 1. Update SVGs for Q19 and Q22
import update_q19_q22_svgs

file_path = 'src/data/kpsea-math-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Load data JSON
match = re.search(r'export const kpseaMath2022 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()

data = json.loads(match.group(1))

# Update sharedContexts
data["sharedContexts"]["ctx-math-2022-q25"] = {
    "title": "Triangles PQS and SQR",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q25.png",
    "caption": "Two triangles PQS and SQR drawn accurately.",
    "cssFilter": "grayscale(100%) contrast(150%) brightness(105%)"
}

data["sharedContexts"]["ctx-math-2022-q28"] = {
    "title": "Bar Graph of Trees Planted",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q28.png",
    "caption": "Number of trees planted by learners from 2017 to 2020."
}

data["sharedContexts"]["ctx-math-2022-q30"] = {
    "title": "Cube Stack Options",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q30.png",
    "caption": "Stack options A, B, C, and D made using 18 cubes.",
    "cssFilter": "grayscale(100%) contrast(150%) brightness(105%)"
}

# Update questions
for q in data["sectionA"]:
    if q["id"] == "kpsea-math-2022-q30":
        q["contextRef"] = "ctx-math-2022-q30"
        q["options"] = [
            { "text": "A", "isCorrect": False },
            { "text": "B", "isCorrect": False },
            { "text": "C", "isCorrect": True },
            { "text": "D", "isCorrect": False }
        ]
        q["explanation"] = "Let's count the total cubes in each option shown in the diagram:\n\n* **Option A:** 3 cubes wide × 3 cubes deep × 3 layers high = 27 cubes.\n* **Option B:** 3 cubes wide × 2 cubes deep × 2 layers high = 12 cubes.\n* **Option C:** 3 cubes wide × 3 cubes deep × 2 layers high = **18 cubes** (Matches Mwakio's 18 cubes!).\n* **Option D:** 2 cubes wide × 3 cubes deep × 3 layers high = 18 cubes.\n\nTherefore, **Option C** represents the correct stack."

js_content = f"export const kpseaMath2022 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully applied all image, filter, and option updates to KPSEA Math 2022!")
