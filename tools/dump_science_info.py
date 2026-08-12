import json

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

science_qs = data['kpsea-science-2023']['sectionA']

with open('science_questions_info.txt', 'w', encoding='utf-8') as f:
    for q in science_qs:
        f.write(f"Question Number: {q['questionNumber']}\n")
        f.write(f"Question Text: {q['questionText']}\n")
        if 'questionList' in q:
            f.write(f"Question List: {q['questionList']}\n")
        if 'questionSuffix' in q:
            f.write(f"Question Suffix: {q['questionSuffix']}\n")
        f.write("Options:\n")
        for o in q['options']:
            f.write(f"  - {o['text']} (isCorrect: {o['isCorrect']})\n")
        f.write(f"Current Explanation:\n{q.get('explanation', '')}\n")
        f.write("="*80 + "\n\n")

print("Dumped Science questions info to science_questions_info.txt")
