import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sst = data['kpsea-sst-parta-2023']['sectionA']
for q in sst[:10]:
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for o in q['options']:
        print(f"   - {o['text']}")
