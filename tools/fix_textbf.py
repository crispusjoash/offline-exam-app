import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace \\textbf{...} with just the content inside it
# The regex handles one level of nested braces (e.g. \text{ cm})
pattern = r'\\\\textbf\{((?:[^{}]|\{[^{}]*\})*)\}'
content = re.sub(pattern, r'\1', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("textbf formatting fixed.")
