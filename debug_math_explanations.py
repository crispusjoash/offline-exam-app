import json
import re

with open('src/data/kpsea-math-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract explanations
matches = re.finditer(r'"questionNumber": (\d+),.*?"explanation": "(.*?)"\n    }', content, re.DOTALL)
for m in matches:
    q_num = int(m.group(1))
    if q_num in [4, 5, 6, 9, 10, 13, 14, 15, 17, 18, 19, 21, 22, 23, 24, 26, 27]:
        print(f"--- Q{q_num} ---")
        print(m.group(2))
