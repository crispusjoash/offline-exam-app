import json
import os
import shutil
import re

# 1. Split the JSON
filepath = 'public/data/kjsea-creative-arts-sports-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Section A
data_a = {
    "id": "kjsea-creative-arts-sports-sectiona-2025",
    "title": "KJSEA 2025 Creative Arts & Sports (Section A)",
    "portal": "KJSEA",
    "subject": "Creative Arts and Sports",
    "year": 2025,
    "timeAllowed": 60,
    "sectionA": data.get("sectionA", []),
    "sectionB": []
}

# Section B
data_b = {
    "id": "kjsea-creative-arts-sports-sectionb-2025",
    "title": "KJSEA 2025 Creative Arts & Sports (Section B)",
    "portal": "KJSEA",
    "subject": "Creative Arts and Sports",
    "year": 2025,
    "timeAllowed": 60,
    "sectionA": [],
    "sectionB": data.get("sectionB", [])
}

with open('public/data/kjsea-creative-arts-sports-sectiona-2025.json', 'w', encoding='utf-8') as f:
    json.dump(data_a, f, indent=2, ensure_ascii=True)
with open('public/data/kjsea-creative-arts-sports-sectionb-2025.json', 'w', encoding='utf-8') as f:
    json.dump(data_b, f, indent=2, ensure_ascii=True)

# Also copy to electron/app/data
os.makedirs('electron/app/data', exist_ok=True)
shutil.copy('public/data/kjsea-creative-arts-sports-sectiona-2025.json', 'electron/app/data/kjsea-creative-arts-sports-sectiona-2025.json')
shutil.copy('public/data/kjsea-creative-arts-sports-sectionb-2025.json', 'electron/app/data/kjsea-creative-arts-sports-sectionb-2025.json')


# 2. Update pastPapersMeta.js
meta_path = 'src/data/pastPapersMeta.js'
with open(meta_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove the old single entry from KJSEA array
content = re.sub(
    r'\s*\{\s*"id":\s*"kjsea-creative-arts-sports-2025",[^}]*"fileName":\s*"kjsea-creative-arts-sports-2025\.json"\s*\},',
    '',
    content
)

# Then, insert the new parent and subpapers
new_papers = """      {
        "id": "kjsea-creative-arts-sports-2025",
        "title": "KJSEA 2025 Creative Arts & Sports",
        "subject": "Creative Arts and Sports",
        "year": "2025",
        "isSubPaper": false,
        "isParentPaper": true,
        "durationMinutes": 120,
        "timeAllowed": 120
      },
      {
        "id": "kjsea-creative-arts-sports-sectiona-2025",
        "title": "KJSEA 2025 Creative Arts & Sports (Section A)",
        "subject": "Creative Arts & Sports (Section A)",
        "year": "2025",
        "isSubPaper": true,
        "isParentPaper": false,
        "durationMinutes": 60,
        "timeAllowed": 60,
        "exportName": "kjseaCreativeArtsSportsSectionA2025",
        "fileName": "kjsea-creative-arts-sports-sectiona-2025.json"
      },
      {
        "id": "kjsea-creative-arts-sports-sectionb-2025",
        "title": "KJSEA 2025 Creative Arts & Sports (Section B)",
        "subject": "Creative Arts & Sports (Section B)",
        "year": "2025",
        "isSubPaper": true,
        "isParentPaper": false,
        "durationMinutes": 60,
        "timeAllowed": 60,
        "exportName": "kjseaCreativeArtsSportsSectionB2025",
        "fileName": "kjsea-creative-arts-sports-sectionb-2025.json"
      },
"""

content = re.sub(r'("KJSEA": \[\n)', r'\1' + new_papers, content)

# 3. Update PAPER_FILE_MAP
# Remove the old map entry
content = re.sub(
    r',\s*"kjsea-creative-arts-sports-2025":\s*\{\s*"fileName":\s*"kjsea-creative-arts-sports-2025\.json",\s*"exportName":\s*"kjseaCreativeArtsSports2025"\s*\}',
    '',
    content
)

new_map_entries = """,
  "kjsea-creative-arts-sports-sectiona-2025": {
    "fileName": "kjsea-creative-arts-sports-sectiona-2025.json",
    "exportName": "kjseaCreativeArtsSportsSectionA2025"
  },
  "kjsea-creative-arts-sports-sectionb-2025": {
    "fileName": "kjsea-creative-arts-sports-sectionb-2025.json",
    "exportName": "kjseaCreativeArtsSportsSectionB2025"
  }
"""
if content.endswith('};\n'):
    content = content[:-3] + new_map_entries + '};\n'
elif content.endswith('};'):
    content = content[:-2] + new_map_entries + '};'

with open(meta_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Clean up old single files
try:
    os.remove('public/data/kjsea-creative-arts-sports-2025.json')
    os.remove('electron/app/data/kjsea-creative-arts-sports-2025.json')
except:
    pass

print("Successfully split paper into Section A and B and updated metadata.")
