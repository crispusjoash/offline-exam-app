import json

filepath = 'src/data/kpsea-english-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

clean_text = text.replace('export const kpseaEnglish2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)

q_nums = [5, 7, 16, 19, 20, 21, 22, 25, 26, 27, 30]
with open('debug_q.txt', 'w', encoding='utf-8') as f:
    for q in data['sectionA']:
        if q['questionNumber'] in q_nums:
            f.write(f"\n--- Q{q['questionNumber']} ---\n")
            f.write(q['explanation'])
