import json
import re

filepath = 'src/data/kpsea-kiswahili-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace '* **' with '- **' for bullet points
fixed_text = text.replace('\n* **', '\n- **')
fixed_text = fixed_text.replace('\n* ', '\n- ')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Changed bullet points from '*' to '-' in kpsea-kiswahili-2023.js")
