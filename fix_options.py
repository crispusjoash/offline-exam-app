import json
import shutil
import re

filepath = 'public/data/kjsea-creative-arts-sports-sectiona-2025.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

for q in data.get('sectionA', []):
    if 'options' in q and isinstance(q['options'][0], str):
        new_options = []
        for opt in q['options']:
            # Strip "A. ", "B. ", etc.
            text = re.sub(r'^[A-D]\.\s*', '', opt)
            new_options.append({'text': text})
        q['options'] = new_options
    
    if 'correctAnswer' in q:
        ans = q['correctAnswer'].strip().upper()
        if ans in letter_to_idx:
            q['correctOptionIndex'] = letter_to_idx[ans]
        # del q['correctAnswer'] # Optionally remove the old key, but it's fine to leave it.

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

# Copy to electron
dest = 'electron/app/data/kjsea-creative-arts-sports-sectiona-2025.json'
shutil.copy(filepath, dest)

print("Fixed options formatting for Section A.")
