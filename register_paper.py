import re
import shutil
import os

filepath = 'src/data/pastPapersMeta.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_paper = """      {
        "id": "kjsea-creative-arts-sports-2025",
        "title": "KJSEA 2025 Creative Arts & Sports",
        "subject": "Creative Arts and Sports",
        "year": "2025",
        "isSubPaper": false,
        "isParentPaper": false,
        "durationMinutes": 120,
        "timeAllowed": 120,
        "exportName": "kjseaCreativeArtsSports2025",
        "fileName": "kjsea-creative-arts-sports-2025.json"
      },
"""

# Insert the new paper at the beginning of the KJSEA array
content = re.sub(r'("KJSEA": \[\n)', r'\1' + new_paper, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Make sure the file exists in electron/app/data
src_json = 'public/data/kjsea-creative-arts-sports-2025.json'
dest_json = 'electron/app/data/kjsea-creative-arts-sports-2025.json'
os.makedirs(os.path.dirname(dest_json), exist_ok=True)
shutil.copy(src_json, dest_json)

print("Successfully injected the new paper into pastPapersMeta.js and copied JSON to electron folder.")
