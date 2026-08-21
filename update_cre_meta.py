import os

filepath = 'src/data/pastPapersMeta.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add paper objects to KJSEA array
paper_objects = '''    {
      "id": "kjsea-cre-sectiona-2025",
      "title": "KJSEA 2025 Christian Religious Education (Section A)",
      "subject": "Christian Religious Education (Section A)",
      "year": "2025",
      "isSubPaper": true,
      "isParentPaper": false,
      "durationMinutes": 60,
      "timeAllowed": 60,
      "exportName": "kjseaCreSectionA2025",
      "fileName": "kjsea-cre-sectiona-2025.json"
    },
    {
      "id": "kjsea-cre-sectionb-2025",
      "title": "KJSEA 2025 Christian Religious Education (Section B)",
      "subject": "Christian Religious Education (Section B)",
      "year": "2025",
      "isSubPaper": true,
      "isParentPaper": false,
      "durationMinutes": 60,
      "timeAllowed": 60,
      "exportName": "kjseaCreSectionB2025",
      "fileName": "kjsea-cre-sectionb-2025.json"
    },
    {
      "id": "kjsea-cre-2025",
      "title": "KJSEA 2025 Christian Religious Education",
      "subject": "Christian Religious Education",
      "year": "2025",
      "isSubPaper": false,
      "isParentPaper": true,
      "durationMinutes": 60,
      "timeAllowed": 60
    }'''

split_meta = content.split('export const PAPER_FILE_MAP = {')
meta_part = split_meta[0]
map_part = split_meta[1]

# Insert before the end of the KJSEA array
insertion_point = meta_part.rfind('  ]\n};')
if insertion_point != -1:
    meta_part = meta_part[:insertion_point] + ',\n' + paper_objects + '\n' + meta_part[insertion_point:]

# 2. Add paper file map
map_objects = '''  "kjsea-cre-sectiona-2025": {
    "fileName": "kjsea-cre-sectiona-2025.json",
    "exportName": "kjseaCreSectionA2025"
  },
  "kjsea-cre-sectionb-2025": {
    "fileName": "kjsea-cre-sectionb-2025.json",
    "exportName": "kjseaCreSectionB2025"
  }'''

insertion_point2 = map_part.rfind('};')
if insertion_point2 != -1:
    map_part = map_part[:insertion_point2] + ',\n' + map_objects + '\n' + map_part[insertion_point2:]

content = meta_part + 'export const PAPER_FILE_MAP = {' + map_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('pastPapersMeta.js successfully updated with CRE papers.')
