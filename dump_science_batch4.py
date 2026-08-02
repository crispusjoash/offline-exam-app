import re, json

with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'"sectionA":\s*(\[.*?\])\s*\n\};', content, re.DOTALL)
if match:
    section_a = json.loads(match.group(1))
    for q in section_a[30:40]:
        print(f"--- Q{q['questionNumber']} ---")
        print(f"ID: {q['id']}")
        print(f"Old Expl: {q.get('explanation')}")
        print("Options:")
        for opt in q['options']:
            print(f"  {opt['text']} (Correct: {opt['isCorrect']})")
else:
    print("Failed to match sectionA array.")
