import json
import re

# 1. Update Mathematics
with open('src/data/kpsea-math-2023.js', 'r', encoding='utf-8') as f:
    text = f.read()
clean_text = text.replace('export const kpseaMath2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)
data['durationMinutes'] = 80
data['timeAllowed'] = 80
with open('src/data/kpsea-math-2023.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaMath2023 = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')
print("Updated kpsea-math-2023.js durationMinutes to 80")

# 2. Update Integrated Science
with open('src/data/kpsea-science-2023.js', 'r', encoding='utf-8') as f:
    text = f.read()
clean_text = text.replace('export const kpseaScience2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)
data['durationMinutes'] = 100
data['timeAllowed'] = 100
data['instructions'] = [
    "You have 1 hour 40 minutes to complete this paper.",
    "Read each question carefully before answering.",
    "Answer ALL the questions."
]
with open('src/data/kpsea-science-2023.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaScience2023 = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')
print("Updated kpsea-science-2023.js durationMinutes to 100")

# 3. Update Social Studies Parent
with open('src/data/kpsea-sst-2023.js', 'r', encoding='utf-8') as f:
    text = f.read()
clean_text = text.replace('export const kpseaSst2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)
data['durationMinutes'] = 100
data['timeAllowed'] = 100
with open('src/data/kpsea-sst-2023.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSst2023 = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')
print("Updated kpsea-sst-2023.js durationMinutes to 100")

# 4. Update Social Studies Part A
with open('src/data/kpsea-sst-parta-2023.js', 'r', encoding='utf-8') as f:
    text = f.read()
clean_text = text.replace('export const kpseaSstParta2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)
data['durationMinutes'] = 100
data['timeAllowed'] = 100
with open('src/data/kpsea-sst-parta-2023.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2023 = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')
print("Updated kpsea-sst-parta-2023.js durationMinutes to 100")
