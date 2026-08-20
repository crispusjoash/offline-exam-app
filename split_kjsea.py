import json
import os
import shutil

subjects = ['agric-nutrition', 'math', 'pretech', 'sst']
data_dir = 'public/data'
electron_dir = 'electron/app/data'

for subj in subjects:
    parent_filename = f'kjsea-{subj}-2025.json'
    parent_path = os.path.join(data_dir, parent_filename)
    
    with open(parent_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Extract Section A
    section_a_data = {
        'id': f'kjsea-{subj}-sectiona-2025',
        'title': data.get('title', '') + ' (Section A)',
        'subject': data.get('subject', ''),
        'sectionA': data.get('sectionA', []),
        'sharedContexts': data.get('sharedContexts', {})
    }
    a_filename = f'kjsea-{subj}-sectiona-2025.json'
    a_path = os.path.join(data_dir, a_filename)
    with open(a_path, 'w', encoding='utf-8') as f:
        json.dump(section_a_data, f, indent=2, ensure_ascii=False)
    
    # Extract Section B
    section_b_data = {
        'id': f'kjsea-{subj}-sectionb-2025',
        'title': data.get('title', '') + ' (Section B)',
        'subject': data.get('subject', ''),
        'sectionA': [], # Force empty sectionA so ExamSession routes to sectionB
        'sectionB': data.get('sectionB', []),
        'sharedContexts': data.get('sharedContexts', {})
    }
    b_filename = f'kjsea-{subj}-sectionb-2025.json'
    b_path = os.path.join(data_dir, b_filename)
    with open(b_path, 'w', encoding='utf-8') as f:
        json.dump(section_b_data, f, indent=2, ensure_ascii=False)
        
    # Copy to electron
    shutil.copy(a_path, os.path.join(electron_dir, a_filename))
    shutil.copy(b_path, os.path.join(electron_dir, b_filename))

print('Successfully generated Section A and Section B sub-papers.')
