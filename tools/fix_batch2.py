import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Batch 2: Q11 to Q20
for i in range(11, 21):
    pattern = r'("questionNumber": ' + str(i) + r',.*?"explanation": ")(.*?)(")'
    def repl(m):
        fixed_text = m.group(2).replace('\\\\n', '\\n')
        return m.group(1) + fixed_text + m.group(3)
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 2 formatting fixed.")
