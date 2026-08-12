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
            # Remove all asterisks completely to avoid any markdown parser bugs/leaks in UI
            exp = exp.replace('*', '')
            q["explanation"] = exp
            
    new_content = "export const kpseaEnglish2023 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully removed ALL asterisks from explanations!")
else:
    print("Could not match JS object")
