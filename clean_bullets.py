import json
import re
import shutil

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if 'explanation' not in q:
        continue
    
    exp = q['explanation']
    
    # Clean up artifacts like ":**** " -> ":** "
    exp = exp.replace(':**** ', ':** ')
    
    # Clean up artifacts like ".:** " -> ":** " (if option text ended in a period)
    exp = exp.replace('.:** ', ':** ')
    
    # Clean up artifacts like "**:****" -> "**:**"
    exp = exp.replace('**:****', '**:**')
    
    # In case there's something like "* **cut:**:** For a cut..."
    exp = exp.replace(':**:** ', ':** ')
    
    # Also, some options might have been parsed weirdly, e.g. B: For a cut...
    # Let's just make sure the markdown is clean
    
    q['explanation'] = exp

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Cleaned up bullet points!")
