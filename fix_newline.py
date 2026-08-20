import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

for section in ['sectionA', 'sectionB']:
    for q in d.get(section, []):
        if 'questionText' in q and r'\n' in q['questionText']:
            q['questionText'] = q['questionText'].replace(r'\n', '\n')
            
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Fixed literal \\n in question text using raw string.')
