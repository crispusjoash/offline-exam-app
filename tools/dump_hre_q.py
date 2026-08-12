import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

hre = data['kpsea-sst-hre-2023']['sectionA']
for q in hre:
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for o in q['options']:
        print(f"   {'[*]' if o.get('isCorrect') else '[ ]'} {o['text']}")
