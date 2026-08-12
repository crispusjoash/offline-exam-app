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
            
            lines = exp.split('\n')
            new_lines = []
            for line in lines:
                # Replace bullet points '*' with '-'
                line = re.sub(r'^(\s*)\* ', r'\1- ', line)
                
                # If there's a double quote, completely remove any remaining asterisks
                if '"' in line:
                    line = line.replace('**', '')
                    line = line.replace('*', '')
                
                new_lines.append(line)
            
            q["explanation"] = '\n'.join(new_lines)
            
    new_content = "export const kpseaEnglish2023 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully cleaned up asterisks on lines with quotes.")
else:
    print("Could not match JS object")
