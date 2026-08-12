import re

file_path = 'src/data/kpsea-math-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix trailing fragment after q30
idx_q30_end = text.find('Therefore, **Option C** is the correct stack."')
if idx_q30_end != -1:
    end_of_block = text.find('}', idx_q30_end)
    text = text[:end_of_block+1] + '\n  ]\n};\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully cleaned kpsea-math-2022.js!")
