import json
import re

filepath = 'src/data/kpsea-english-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace '* **' with '- **' for bullet points
fixed_text = text.replace('\n* **', '\n- **')
fixed_text = fixed_text.replace('\n* ', '\n- ')

# Also let's clean any rogue `*"` or `*" ` just in case
fixed_text = re.sub(r'\*\s*"', '"', fixed_text)
fixed_text = re.sub(r'"\s*\*+', '"', fixed_text)
# remove any single asterisks around quotes
fixed_text = fixed_text.replace('*"', '"').replace('"*', '"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Changed bullet points from '*' to '-' and cleaned up rogue asterisks in kpsea-english-2023.js")
