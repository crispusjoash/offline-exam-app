import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kisw = data['kpsea-kiswahili-2023']['sectionA']
for q in kisw:
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for o in q['options']:
        print(f"   {'[*]' if o.get('isCorrect') else '[ ]'} {o['text']}")
