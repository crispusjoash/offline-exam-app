import json
import shutil

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionB', []):
    if q.get('id') == 'q34':
        # Fix parentQuestionText
        q['parentQuestionText'] = "The following diagram shows states of matter."
        
        # Fix subquestions
        for sub in q.get('subQuestions', []):
            if sub.get('id') == 'q34a':
                sub['modelAnswer'] = "Here is a list of acceptable states of matter:\n\n1. **A:** Solid\n2. **B:** Gas"
            elif sub.get('id') == 'q34b':
                sub['modelAnswer'] = "Here is a list of acceptable processes:\n\n1. **X:** Sublimation (changing from solid to gas)\n2. **Y:** Deposition (changing from gas to solid)"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')
print("Successfully patched Question 34!")
