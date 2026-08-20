import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

for q in d['sectionB']:
    if str(q.get('questionNumber')) == '47':
        for sq in q.get('subQuestions', []):
            if sq.get('id') == 'q47a':
                sq['modelAnswer'] = "Here is the detailed function of the keys:\n\n* **Key P (Enter / Return Key):**\n  1. Executing a command or confirming an input/selection.\n  2. Moving the cursor to the beginning of a new line or starting a new paragraph in word processing.\n  3. Submitting online forms or accepting dialog box prompts.\n\n* **Key Q (Backspace Key):**\n  - Deleting the character immediately to the left of the insertion point or cursor."
                
                sq['rubric'] = "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating the correct function of Key P, and 1 mark for Key Q (Max 2 marks).\n* **Flexibility:** Accept any accurate description of Enter (executing commands / new line) and Backspace (erasing character to the left)."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Q47a modelAnswer and rubric updated.')
