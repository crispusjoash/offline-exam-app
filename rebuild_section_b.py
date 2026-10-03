import json
import re
import shutil

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionB', []):
    # Fix parent text
    if 'questionText' in q:
        text = q['questionText']
        if re.match(r'^Questions?\s+\d+\s+(involves|covers).*$', text, re.IGNORECASE):
            del q['questionText']
        else:
            q['parentQuestionText'] = text
            del q['questionText']
            
    # Fix subquestions
    for sub in q.get('subQuestions', []):
        if 'label' in sub:
            label = sub['label']
            sub['subNumber'] = f"({label})"
            del sub['label']
            
        # Place subNumber after id to match CRE format ordering roughly
        # We can just construct a new dict to preserve key ordering if we want, but it's not strictly necessary.
        
        qType = sub.get('questionType', '')
        if qType in ['short-answer', 'long-answer']:
            sub['questionType'] = 'structured'

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')

print("Rebuilt Section B successfully!")
