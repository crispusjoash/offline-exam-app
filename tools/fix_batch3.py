import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Batch 3: Q21 to Q30
for i in range(21, 31):
    pattern = r'("questionNumber": ' + str(i) + r',.*?"explanation": ")(.*?)(")'
    def repl(m):
        fixed_text = m.group(2).replace('\\\\n', '\\n')
        return m.group(1) + fixed_text + m.group(3)
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 3 formatting fixed.")
