import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

hre = data['kpsea-sst-hre-2023']['sectionA']
for q in hre:
    opts = [f"{'[CORRECT] ' if o.get('isCorrect') else '[INCORRECT] '}{o['text']}" for o in q['options']]
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for opt in opts:
        print(f"   {opt}")
