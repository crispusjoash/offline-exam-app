import json
import re

def fix_broken_asterisks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Fix the specific 'Pupil:**' error in the English passage
    fixed_text = text.replace('Pupil:**', '**Pupil:**')
    
    # Are there any other words ending with :** that are missing the opening **?
    # e.g., Word:**
    # Regex to find `Word:**` that is NOT preceded by `**`
    # We can just look for them visually by printing them out
    matches = re.findall(r'(?<!\*\*)([A-Za-z]+:\*\*)', fixed_text)
    if matches:
        print(f"Found other broken ones in {filepath}: {matches}")
        for match in matches:
            fixed_text = fixed_text.replace(match, f"**{match}")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

fix_broken_asterisks('src/data/kpsea-english-2023.js')
fix_broken_asterisks('src/data/kpsea-kiswahili-2023.js')

print("Fixed broken passage asterisks.")
