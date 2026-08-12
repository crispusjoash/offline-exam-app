import json

with open('src/data/kpsea-kiswahili-2023.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('export const kpseaKiswahili2023 = ', '').strip()
if text.endswith(';'):
    text = text[:-1]

data = json.loads(text)

with open('kiswahili_dump.txt', 'w', encoding='utf-8') as out:
    out.write("Shared Contexts:\n")
    for ckey, cval in data.get('sharedContexts', {}).items():
        out.write(f"=== {ckey} ({cval.get('title')}) ===\n")
        out.write(f"{cval.get('text')}\n\n")

    out.write("\nQuestions:\n")
    for q in data['sectionA']:
        out.write(f"=== Q{q['questionNumber']} ===\n")
        out.write(f"Text: {q['questionText']}\n")
        if 'contextRef' in q:
            out.write(f"ContextRef: {q['contextRef']}\n")
        out.write("Options:\n")
        for opt in q['options']:
            mark = " (CORRECT)" if opt.get('isCorrect') else ""
            out.write(f"  - {opt['text']}{mark}\n")
        out.write("Current Explanation:\n")
        out.write(f"{q.get('explanation')}\n")
        out.write("-" * 50 + "\n\n")

print("Dumped to kiswahili_dump.txt successfully.")
