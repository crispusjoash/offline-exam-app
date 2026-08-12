import json
import re

file_path = 'src/data/kpsea-science-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(export const kpseaScience2025 = )(\{.*\});?\s*$', content, re.DOTALL)
prefix = match.group(1)
data = json.loads(match.group(2))

section_key = "sectionA" if "sectionA" in data else "questions"
for q in data.get(section_key, []):
    if q.get("explanation") and not q["explanation"].startswith("The correct answer"):
        # Find the correct option text
        correct_option_text = "Unknown"
        for opt in q.get("options", []):
            if opt.get("isCorrect"):
                correct_option_text = opt.get("text", "").strip()
                break
        
        old_expl = q["explanation"].strip()
        new_expl = f"The correct answer is **{correct_option_text}**.\n\n**Analysis of the Correct Answer:**\n{old_expl}"
        q["explanation"] = new_expl

new_content = prefix + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Explanations formatted!")
