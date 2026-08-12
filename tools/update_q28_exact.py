import json
import re

file_path = 'src/data/kpsea-math-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const kpseaMath2022 = (\{.*\});', text, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    data["sharedContexts"]["ctx-math-2022-q28"] = {
        "title": "Bar Graph of Trees Planted",
        "type": "image",
        "imagePath": "/assets/kpsea_math_2022_q28.jpg",
        "caption": "Number of trees planted by learners of a school in four years.",
        "scanEffect": False,
        "cssFilter": "none"
    }

    js_content = f"export const kpseaMath2022 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Updated q28 sharedContext cleanly!")
