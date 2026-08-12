import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'export const kpseaEnglish2023 = (\{.*\});?', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    for q in data["sectionA"]:
        if "explanation" in q:
            exp = q["explanation"]
            for line in exp.split('\n'):
                if '*' in line and '"' in line:
                    print(line)
