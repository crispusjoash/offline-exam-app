import json
import shutil

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionB', []):
    if q.get('id') == 'q40':
        for subq in q.get('subQuestions', []):
            if subq.get('id') == 'q40b':
                subq['modelAnswer'] = "Here is a list of acceptable indications:\n\n1. **A curve landing in between:** The water jet from the new hole at point R (which is vertically between the top and bottom holes) would travel a horizontal distance greater than the top jet but less than the bottom jet, landing exactly between them.\n\n*(Note: As this is an interactive app, students would draw a curve matching this description).* "
                subq['rubric'] = "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for a drawn curve that lands between the water jets of the top hole and the bottom hole (Max 1 mark)."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')
print("Successfully updated Q40b to reflect point R's vertical position!")
