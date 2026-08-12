import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'export const kpseaEnglish2023 = (\{.*\});?', content, re.DOTALL)
if match:
    json_str = match.group(1)
    data = json.loads(json_str)
    
    for q in data["sectionA"]:
        if "explanation" in q:
            exp = q["explanation"]
            
            # Remove italics from quoted option headers
            # e.g. (*"Who are you?"*) -> ("Who are you?")
            exp = re.sub(r'\(\*\"(.*?)\"\*\)', r'("\1")', exp)
            
            # e.g. *"A pet is an animal kept for pleasure..."* -> "A pet is an animal kept for pleasure..."
            # Careful not to strip bold or legitimate italics, just those wrapping quotes.
            exp = re.sub(r'\*\"(.*?)\"\*', r'"\1"', exp)
            
            # Also handle single quotes if any
            exp = re.sub(r"\*\('(.*?)'\)\*", r"('\1')", exp)
            exp = re.sub(r"\*'(.*?)'\*", r"'\1'", exp)
            
            q["explanation"] = exp
            
    new_content = "export const kpseaEnglish2023 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully removed italics around quotes.")
else:
    print("Could not match JS object")
