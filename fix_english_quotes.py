import json

filepath = 'src/data/kpsea-english-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the asterisks next to quotes just like we did for Kiswahili
fixed_text = text.replace('*\\"', '\\"').replace('\\"*', '\\"')
fixed_text = fixed_text.replace('*"', '"').replace('"*', '"')
fixed_text = fixed_text.replace('(*', '(').replace('*)', ')')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Fixed quotes and asterisks in kpsea-english-2023.js")
