import re
import os

filepath = 'src/data/pastPapersMeta.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update isParentPaper for the 4 parent papers
parent_ids = ['kjsea-agric-nutrition-2025', 'kjsea-math-2025', 'kjsea-pretech-2025', 'kjsea-sst-2025']

for pid in parent_ids:
    # Find the block for this id and replace "isParentPaper": false with true
    # We will use regex to find the object with "id": "kjsea..." and change its isParentPaper
    pattern = re.compile(rf'("id":\s*"{pid}".*?"isParentPaper":\s*)false', re.DOTALL)
    content = pattern.sub(r'\g<1>true', content)

# 2. Prepare the new sub-papers
new_papers_array_items = []
new_file_map_items = []

for pid in parent_ids:
    subject_part = pid.replace('kjsea-', '').replace('-2025', '')
    if subject_part == 'agric-nutrition':
        title = "Agriculture & Nutrition"
    elif subject_part == 'math':
        title = "Mathematics"
    elif subject_part == 'pretech':
        title = "Pre-Technical Studies"
    elif subject_part == 'sst':
        title = "Social Studies"
        
    export_name = "kjsea" + "".join([x.capitalize() for x in subject_part.split('-')]) + "2025"
    
    # Section A
    id_a = f'kjsea-{subject_part}-sectiona-2025'
    file_a = f'{id_a}.js'
    exp_a = export_name.replace("2025", "SectionA2025")
    
    item_a = f'''    {{
      "id": "{id_a}",
      "title": "KJSEA 2025 {title} (Section A)",
      "subject": "{title} (Section A)",
      "year": "2025",
      "isSubPaper": true,
      "isParentPaper": false,
      "durationMinutes": 60,
      "timeAllowed": 60,
      "exportName": "{exp_a}",
      "fileName": "{file_a}"
    }}'''
    new_papers_array_items.append(item_a)
    
    map_a = f'''  "{id_a}": {{
    "fileName": "{file_a}",
    "exportName": "{exp_a}"
  }}'''
    new_file_map_items.append(map_a)
    
    # Section B
    id_b = f'kjsea-{subject_part}-sectionb-2025'
    file_b = f'{id_b}.js'
    exp_b = export_name.replace("2025", "SectionB2025")
    
    item_b = f'''    {{
      "id": "{id_b}",
      "title": "KJSEA 2025 {title} (Section B)",
      "subject": "{title} (Section B)",
      "year": "2025",
      "isSubPaper": true,
      "isParentPaper": false,
      "durationMinutes": 60,
      "timeAllowed": 60,
      "exportName": "{exp_b}",
      "fileName": "{file_b}"
    }}'''
    new_papers_array_items.append(item_b)
    
    map_b = f'''  "{id_b}": {{
    "fileName": "{file_b}",
    "exportName": "{exp_b}"
  }}'''
    new_file_map_items.append(map_b)

# Insert the new papers into the KJSEA array
# Find where the KJSEA array ends. We can look for the end of the KJSEA array before "};\n\nexport const PAPER_FILE_MAP"
split_meta = content.split('export const PAPER_FILE_MAP = {')
meta_part = split_meta[0]
map_part = split_meta[1]

# Insert into meta_part (before the closing bracket of KJSEA array)
# It usually ends with "\n  ]\n};\n\n"
insertion_point = meta_part.rfind('  ]\n};')
if insertion_point != -1:
    meta_part = meta_part[:insertion_point] + ',\n' + ',\n'.join(new_papers_array_items) + '\n' + meta_part[insertion_point:]

# Insert into map_part
insertion_point2 = map_part.rfind('};')
if insertion_point2 != -1:
    map_part = map_part[:insertion_point2] + ',\n' + ',\n'.join(new_file_map_items) + '\n' + map_part[insertion_point2:]

content = meta_part + 'export const PAPER_FILE_MAP = {' + map_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('pastPapersMeta.js updated successfully.')
