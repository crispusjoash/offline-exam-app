import os

file_content = """export const kpseaScience2022 = {
  "id": "kpsea-science-2022",
  "title": "KPSEA 2022 Integrated Science",
  "subject": "Integrated Science",
  "year": "2022",
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": [
"""

os.makedirs('src/data', exist_ok=True)
with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(file_content)

print("kpsea-science-2022.js initialized successfully.")
