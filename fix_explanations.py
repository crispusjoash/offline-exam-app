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
    
    # 1. Fix the corrupted emoji before Key Learning Note
    # We want to replace anything like "\u00f0... **Key Learning Note:**" or "ðŸ“Œ **Key Learning Note:**" 
    # or "?o' **Key Learning Note:**" with "💡 **Key Learning Note:**"
    # Just look for "**Key Learning Note:**" and replace the line it's on.
    # Actually, we can just replace any weird characters before it.
    exp = re.sub(r'^.*?\*\*Key Learning Note:\*\*', '💡 **Key Learning Note:**', exp, flags=re.MULTILINE)
    
    # 2. Fix the Incorrect Options bullets
    # The bullets might look like "* **B:**" or "B:" or "* **B (some text):**"
    # We want to replace them with "* **[Option Text]:**"
    
    # Create a mapping of letter to option text
    opt_map = {}
    for i, opt in enumerate(q.get('options', [])):
        letter = chr(ord('A') + i)
        text = opt['text'].strip()
        text = re.sub(r'^[A-D]\.\s*', '', text) # remove 'A. ' if present
        opt_map[letter] = text
        
    # We will process line by line to fix the bullets
    lines = exp.split('\n')
    new_lines = []
    for line in lines:
        # Match lines like "* **B:**" or "B:" or "* **B, C:**"
        # Let's try to match the letters at the start of the line (after optional '* ' and '**')
        # Examples:
        # "* **B:** For a cut..."
        # "B: For a cut..."
        # "* **B, C:** The nucleus contains..."
        # "* **A (Glass), B (Wood), and D (Plastic):**"
        
        # This is a bit complex, let's just do a simple replacement for the most common ones:
        # Match "* **X:**" or "X:"
        m = re.match(r'^(\*\s*\*\*)?([A-D])(\*\*\s*)?:(.*)', line)
        if m:
            letter = m.group(2)
            rest = m.group(4)
            option_text = opt_map.get(letter, letter)
            line = f"* **{option_text}:**{rest}"
        else:
            # Handle combinations like "* **B, C:**" or "B, C:"
            m = re.match(r'^(\*\s*\*\*)?([A-D])\s*,\s*([A-D])(\*\*\s*)?:(.*)', line)
            if m:
                l1, l2 = m.group(2), m.group(3)
                rest = m.group(5)
                t1, t2 = opt_map.get(l1, l1), opt_map.get(l2, l2)
                line = f"* **{t1} and {t2}:**{rest}"
        
        new_lines.append(line)
        
    exp = '\n'.join(new_lines)
    
    q['explanation'] = exp

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully fixed emojis and option labels!")
