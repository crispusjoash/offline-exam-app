import re
import json

file_path = 'src/data/kpsea-science-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update ctx-science-2024-q27-28
content = content.replace(
    '"title": "Gulley Erosion",\n      "cssFilter": "none"',
    '"title": "Gulley Erosion",\n      "text": "The following picture shows land destroyed by soil erosion. Use it to answer questions 27 and 28.",\n      "cssFilter": "none"'
)

# Update ctx-science-2024-q32-33
content = content.replace(
    '"title": "Cabbage Plants",\n      "cssFilter": "none"',
    '"title": "Cabbage Plants",\n      "text": "The following pictures show cabbage at different stages of growth. Use them to answer questions 32 and 33.",\n      "cssFilter": "none"'
)

# Update ctx-science-2024-q35-36
content = content.replace(
    '"title": "Hanging Pots",\n      "cssFilter": "none"',
    '"title": "Hanging Pots",\n      "text": "The following picture shows an innovative garden used by learners to grow indigenous vegetables. Use the picture to answer questions 35 and 36.",\n      "cssFilter": "none"'
)

# Add ctx-science-2024-q29-31
new_ctx = """
    "ctx-science-2024-q29-31": {
      "type": "text",
      "title": "Creeping Fruit Crop",
      "text": "A monkey was observed damaging a creeping fruit crop by feeding on mature fruits. Use this information to answer questions 29 to 31."
    }
"""

if '"ctx-science-2024-q29-31"' not in content:
    content = content.replace('  },\n  "sectionA": [', new_ctx + '  },\n  "sectionA": [')

texts_to_remove = [
    "The following picture shows land destroyed by soil erosion. Use it to answer questions **27** and **28**.",
    "The following picture shows land destroyed by soil erosion. Use it to answer questions 27 and 28.",
    "A monkey was observed damaging a creeping fruit crop by feeding on mature fruits. Use this information to answer questions **29** to **31**.",
    "A monkey was observed damaging a creeping fruit crop by feeding on mature fruits. Use this information to answer questions 29 to 31.",
    "The following pictures show cabbage at different stages of growth. Use them to answer questions **32** and **33**.",
    "The following pictures show cabbage at different stages of growth. Use them to answer questions 32 and 33.",
    "The following picture shows an innovative garden used by learners to grow indigenous vegetables. Use the picture to answer questions **35** and **36**.",
    "The following picture shows an innovative garden used by learners to grow indigenous vegetables. Use the picture to answer questions 35 and 36."
]

for t in texts_to_remove:
    # also handle escaped newlines
    content = content.replace(t + '\\n\\n', '')
    content = content.replace(t + '\\n', '')
    content = content.replace(t, '')

# Fix double newlines at the start of question text after removal
content = re.sub(r'"questionText": "\\\\n\\\\n', '"questionText": "', content)
content = re.sub(r'"questionText": "\\\\n', '"questionText": "', content)

# Make sure 29, 30, 31 have contextRef
for q in [29, 30, 31]:
    if f'"contextRef": "ctx-science-2024-q29-31"' not in content:
        content = re.sub(r'("questionNumber": ' + str(q) + r',\s*)"questionText"', r'\1"contextRef": "ctx-science-2024-q29-31",\n      "questionText"', content)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Contexts updated successfully.")
