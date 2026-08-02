import re

with open('src/data/kpsea-math-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'"questionNumber": (\d+),.*?"explanation": "(.*?)"\n    }', content, re.DOTALL)

with open('math_2022_exps.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        q_num = int(m.group(1))
        out.write(f"--- Q{q_num} ---\n{m.group(2)}\n\n")
