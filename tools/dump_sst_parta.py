import json

filepath = 'src/data/kpsea-sst-parta-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

clean_text = text.replace('export const kpseaSstParta2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)

with open('sst_parta_dump.txt', 'w', encoding='utf-8') as out:
    for q in data.get('sectionA', []):
        out.write(f"=== Q{q['questionNumber']} (id: {q['id']}) ===\n")
        out.write(f"QuestionText: {q.get('questionText')}\n")
        if 'questionList' in q:
            out.write(f"QuestionList: {q.get('questionList')}\n")
        if 'questionSuffix' in q:
            out.write(f"QuestionSuffix: {q.get('questionSuffix')}\n")
        out.write(f"Options: {q.get('options')}\n")
        out.write(f"Current Explanation: {q.get('explanation')}\n\n")

print("Dumped 35 questions of Social Studies & Creative Arts (Part A)")
