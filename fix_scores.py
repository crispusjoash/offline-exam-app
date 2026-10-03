import json
import re
import os
import glob
import shutil

# Regex to match marks in the format (2 marks), (1 mark), (2mks), (3 mks)
mark_pattern = re.compile(r'\(\s*(\d+)\s*m(?:ar)?ks?\s*\)', re.IGNORECASE)

# Find all sectionb JSON files
data_dir = 'public/data'
files = glob.glob(os.path.join(data_dir, '*sectionb*.json'))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for q in data.get('sectionB', []):
        # Process parent question (if it's not just a parent without subquestions)
        # But wait, usually marks are on the question that is actually answered.
        # Let's process subQuestions if they exist, else process the parent.
        
        # In case the parent itself has marks and no subquestions
        if 'questionText' in q and not q.get('subQuestions'):
            match = mark_pattern.search(q['questionText'])
            if match:
                score = int(match.group(1))
                q['maxScore'] = score
                # Remove the marks from the question text
                q['questionText'] = mark_pattern.sub('', q['questionText']).strip()
                
        # Process subQuestions
        for sub in q.get('subQuestions', []):
            if 'questionText' in sub:
                match = mark_pattern.search(sub['questionText'])
                if match:
                    score = int(match.group(1))
                    sub['maxScore'] = score
                    # Remove the marks from the subquestion text
                    sub['questionText'] = mark_pattern.sub('', sub['questionText']).strip()

    # Write back to public/data
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
        
    # Copy to electron/app/data
    dest = os.path.join('electron/app/data', os.path.basename(filepath))
    shutil.copy(filepath, dest)

print("Processed all Section B files to extract maxScore and remove duplicate marks from text!")
