import json
d = json.load(open('public/data/kjsea-pretech-2025.json', 'r', encoding='utf-8'))
for q in d['sectionA'][20:30]:
    print(f"Q{q['questionNumber']}: {q.get('questionText')}")
    print(f"Correct Option Index: {q.get('correctOptionIndex')}")
    for i, o in enumerate(q.get('options', [])):
        print(f"  {i}: {o['text']}")
    print('-'*20)
