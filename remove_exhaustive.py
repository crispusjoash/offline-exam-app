import json
import os
import shutil
import glob

data_dir = 'public/data'
electron_dir = 'electron/app/data'

# Find all KJSEA Section B files
files = glob.glob(os.path.join(data_dir, 'kjsea-*-sectionb-2025.json'))

def replace_text(text):
    if not isinstance(text, str):
        return text
    # Replace the target phrase
    return text.replace("an exhaustive list", "a list")

updated_files_count = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    for q in data.get('sectionB', []):
        if 'modelAnswer' in q and isinstance(q['modelAnswer'], str):
            new_ans = replace_text(q['modelAnswer'])
            if new_ans != q['modelAnswer']:
                q['modelAnswer'] = new_ans
                modified = True
                
        if 'subQuestions' in q:
            for sub in q['subQuestions']:
                if 'modelAnswer' in sub and isinstance(sub['modelAnswer'], str):
                    new_ans = replace_text(sub['modelAnswer'])
                    if new_ans != sub['modelAnswer']:
                        sub['modelAnswer'] = new_ans
                        modified = True
                        
    if modified:
        # Write back to public/data
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Copy to electron/app/data
        filename = os.path.basename(filepath)
        electron_filepath = os.path.join(electron_dir, filename)
        shutil.copy(filepath, electron_filepath)
        print(f"Updated {filename}")
        updated_files_count += 1

print(f"Successfully updated {updated_files_count} files.")
