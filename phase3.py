import json
import shutil

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionB', []):
    for sub in q.get('subQuestions', []):
        ans = sub.get('modelAnswer', '')
        rubric = sub.get('rubric', '')
        
        # Check modelAnswer
        if ans and "Here is a list of acceptable" not in ans:
            # Reformat to simple list if it's not already
            ans = f"Here is a list of acceptable answers:\n\n1. **Answer:** {ans}"
            sub['modelAnswer'] = ans
            
        # Check rubric
        if rubric and "Marking Scheme Guide:" not in rubric:
            # Reformat rubric
            rubric = f"📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** {rubric}\n* **Flexibility:** Accept any valid answer."
            sub['rubric'] = rubric

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')
print("Phase 3 completed in batches!")
