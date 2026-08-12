import json

master_data = {
  "id": "kpsea-sst-2024",
  "title": "KPSEA 2024 Social Studies & Creative Arts",
  "subject": "Social Studies & Creative Arts",
  "year": "2024",
  "isParentPaper": True,
  "durationMinutes": 100,
  "timeAllowed": 100,
  "sectionA": []
}

with open('src/data/kpsea-sst-2024.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSst2024 = ' + json.dumps(master_data, indent=2) + ';\n')

# Now update pastPapers.js
import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add imports
imports_to_add = """
import { kpseaSst2024 } from './kpsea-sst-2024.js';
import { kpseaSstParta2024 } from './kpsea-sst-parta-2024.js';
import { kpseaSstCre2024 } from './kpsea-sst-cre-2024.js';
import { kpseaSstIre2024 } from './kpsea-sst-ire-2024.js';
import { kpseaSstHre2024 } from './kpsea-sst-hre-2024.js';
"""
content = imports_to_add.strip() + '\n' + content

# Add to KPSEA array
content = re.sub(
    r'(KPSEA:\s*\[)', 
    r'\1\n    kpseaSst2024,\n    kpseaSstParta2024,\n    kpseaSstCre2024,\n    kpseaSstIre2024,\n    kpseaSstHre2024,', 
    content
)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated pastPapers.js and created master paper!")
