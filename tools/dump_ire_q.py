import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ire = data['kpsea-sst-ire-2023']['sectionA']
for q in ire:
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for o in q['options']:
        print(f"   {'[*]' if o.get('isCorrect') else '[ ]'} {o['text']}")
