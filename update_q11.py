import json
import shutil

filepath = 'public/data/kjsea-creative-arts-sports-sectiona-2025.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('questionNumber') == 11:
        q['options'] = [
            {'text': r'flat sign ($\flat$) - raises the pitch by a semitone'},
            {'text': r'sharp sign ($\sharp$) - lowers the pitch by a semitone'},
            {'text': r'natural sign ($\natural$) - restores the pitch by a semitone'},
            {'text': r'$\textit{f}$ - reduces the pitch by a semitone'}
        ]
        break

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

# Copy to electron
dest = 'electron/app/data/kjsea-creative-arts-sports-sectiona-2025.json'
shutil.copy(filepath, dest)

print("Updated Question 11 options.")
