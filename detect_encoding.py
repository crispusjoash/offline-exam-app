import json

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find what the corrupted string looks like
import re
matches = set(re.findall(r'.{0,5}\*\*Key Learning Note:\*\*', text))
print("Corrupted strings found:")
for m in matches:
    print(repr(m))

# Let's also check for the Marking Scheme Guide
matches2 = set(re.findall(r'.{0,5}\*\*Marking Scheme Guide:\*\*', text))
print("Corrupted strings found 2:")
for m in matches2:
    print(repr(m))

