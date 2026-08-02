import json
import re

filepath = 'src/data/kpsea-kiswahili-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# The JS file has format: export const kpseaKiswahili2023 = { ... };
# We will just do a string replace for the problematic markdown italic quotes
# The user said they see * whenever someone is quoted speaking.
# So `*"Ni jioni... "*` or `*"Mwandani wangu... "*` etc.

fixed_text = text.replace('*\\"', '\\"').replace('\\"*', '\\"')
fixed_text = fixed_text.replace('*"', '"').replace('*"', '"').replace('"*', '"')
fixed_text = fixed_text.replace('(*', '(').replace('*)', ')')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Fixed quotes and italics in kpsea-kiswahili-2023.js")
