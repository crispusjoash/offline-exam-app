import json
import os

base_dir = r'c:\Users\JOASH\Desktop\CBC\offline-exam-app'
paths = [
    os.path.join(base_dir, 'public', 'data', 'kjsea-creative-arts-sports-sectionb-2025.json'),
    os.path.join(base_dir, 'electron', 'app', 'data', 'kjsea-creative-arts-sports-sectionb-2025.json')
]

for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for q in data.get('sectionB', []):
        if q.get('questionNumber') == 41:
            q['parentQuestionText'] = "PART I: PERFORMING ARTS\n\nAnswer all questions in this part in the spaces provided.\n\nUsing semi-breves, write the ascending scale of F major without key signature on treble staff."
                    
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

print('Updated Q41 to display text in parentQuestionText.')
