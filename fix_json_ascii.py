import json
import shutil

for name in ['kjsea-science-sectiona-2025.json', 'kjsea-science-sectionb-2025.json']:
    filepath = f'public/data/{name}'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
        
    shutil.copy(filepath, f'electron/app/data/{name}')

print("Fixed JSONs to use ASCII escapes for emojis!")
