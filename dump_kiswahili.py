import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kis = data['kpsea-kiswahili-2023']['sectionA']
for q in kis:
    opts = [f"{'[CORRECT] ' if o.get('isCorrect') else '[INCORRECT] '}{o['text']}" for o in q['options']]
    print(f"Q{q['questionNumber']}: {q['questionText']}")
    for opt in opts:
        print(f"   {opt}")
