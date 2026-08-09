import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Batch 1: Q1 to Q10
for i in range(1, 11):
    pattern = r'("questionNumber": ' + str(i) + r',.*?"explanation": ")(.*?)(")'
    def repl(m):
        # Replace \\n with \n
        fixed_text = m.group(2).replace('\\\\n', '\\n')
        return m.group(1) + fixed_text + m.group(3)
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 1 formatting fixed.")
