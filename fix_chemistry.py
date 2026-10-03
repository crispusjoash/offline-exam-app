import json
import re
import shutil

replacements = {
    r'\bH2O\b': 'H₂O',
    r'\bCO2\b': 'CO₂',
    r'\bNH3\b': 'NH₃',
    r'\bNO2\b': 'NO₂',
    r'\bO2\b': 'O₂',
    r'\bH2\b': 'H₂',
    r'\bN2\b': 'N₂',
    r'\bSO2\b': 'SO₂',
    r'\bcm3\b': 'cm³',
    r'\bcm2\b': 'cm²',
    r'\bm2\b': 'm²',
    r'\bm3\b': 'm³',
    r'->': '→',
    r'\bO2-\b': 'O²⁻',
    r'\bH\+\b': 'H⁺',
    r'\bOH-\b': 'OH⁻',
}

def fix_text(text):
    if not isinstance(text, str):
        return text
    
    for old, new in replacements.items():
        text = re.sub(old, new, text)
        
    return text

# Section A
filepath_a = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath_a, 'r', encoding='utf-8') as f:
    data_a = json.load(f)

for q in data_a.get('sectionA', []):
    if 'explanation' in q:
        q['explanation'] = fix_text(q['explanation'])
    if 'questionText' in q:
        q['questionText'] = fix_text(q['questionText'])
    for opt in q.get('options', []):
        if 'text' in opt:
            opt['text'] = fix_text(opt['text'])

with open(filepath_a, 'w', encoding='utf-8') as f:
    json.dump(data_a, f, indent=2, ensure_ascii=True)
shutil.copy(filepath_a, 'electron/app/data/kjsea-science-sectiona-2025.json')

# Section B
filepath_b = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath_b, 'r', encoding='utf-8') as f:
    data_b = json.load(f)

for q in data_b.get('sectionB', []):
    if 'questionText' in q:
        q['questionText'] = fix_text(q['questionText'])
    for sub in q.get('subQuestions', []):
        if 'questionText' in sub:
            sub['questionText'] = fix_text(sub['questionText'])
        if 'modelAnswer' in sub:
            sub['modelAnswer'] = fix_text(sub['modelAnswer'])
        if 'rubric' in sub:
            sub['rubric'] = fix_text(sub['rubric'])

with open(filepath_b, 'w', encoding='utf-8') as f:
    json.dump(data_b, f, indent=2, ensure_ascii=True)
shutil.copy(filepath_b, 'electron/app/data/kjsea-science-sectionb-2025.json')

print("Fixed chemical formulas and mathematical symbols!")
