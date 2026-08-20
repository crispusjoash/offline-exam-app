import json
d = json.load(open('public/data/kjsea-pretech-2025.json', 'r', encoding='utf-8'))
for q in d['sectionA']:
    print(f"Q{q.get('questionNumber')}: {q.get('questionText')}")
    print(f"Ans: {q.get('correctAnswer')} | Type: {q.get('questionType')}")
    print('-'*20)
