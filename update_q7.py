import json
import shutil

filepath = 'public/data/kjsea-creative-arts-sports-sectiona-2025.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('questionNumber') == 7:
        q['options'] = [{'text': 'A'}, {'text': 'B'}, {'text': 'C'}, {'text': 'D'}]
        # Need to ensure correctOptionIndex is correctly set if it was pointing to A, B, C, D
        break

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

# Copy to electron
dest = 'electron/app/data/kjsea-creative-arts-sports-sectiona-2025.json'
shutil.copy(filepath, dest)

print("Updated Question 7 options.")
