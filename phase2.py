import json
import re
import shutil

def process_section_a(start_idx, end_idx):
    filepath = 'public/data/kjsea-science-sectiona-2025.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data.get('sectionA', [])[start_idx:end_idx]:
        if 'explanation' not in q:
            continue
            
        exp = q['explanation']
        
        # 1. Replace "The correct answer is **A**." with "The correct answer is **[Correct Option Text]**."
        correct_text = ""
        for opt in q.get('options', []):
            if opt.get('isCorrect'):
                correct_text = opt['text'].strip()
                # Remove leading 'A. ', 'B. ' if present
                correct_text = re.sub(r'^[A-D]\.\s*', '', correct_text)
                break
                
        exp = re.sub(r'The correct answer is \*\*[A-D]\*\*\.', f'The correct answer is **{correct_text}**.', exp)
        
        # 2. Remove double newlines
        exp = exp.replace('\n\n', '\n')
        
        # 3. Replace "* **B (Principal axis):**" with "* **Principal axis:**"
        # We need to find patterns like `* **[A-D] ([Something]):**` and replace with `* **[Something]:**`
        exp = re.sub(r'\*\s*\*\*?[A-D]\s*\(([^)]+)\)\s*\*\*\s*:', r'* **\1:**', exp)
        
        # Or sometimes it's `* **A (Decaying matter):**`
        exp = re.sub(r'\*\s*\*\*?[A-D]\s+([^:*]+)\s*\*\*\s*:', r'* **\1:**', exp)
        
        # Sometimes it's `* **[A-D] - something:**`
        exp = re.sub(r'\*\s*\*\*?[A-D]\s*-\s*([^:*]+)\s*\*\*\s*:', r'* **\1:**', exp)
        
        # Some are `* **[A-D]:**` where it didn't include the text. In that case, we can't easily guess. 
        # I'll add a generic one just in case they have `* **A:**` but it might be harder to replace perfectly.
        
        q['explanation'] = exp

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
    print(f"Processed Section A from {start_idx} to {end_idx}")

# We will run this in continuous progressive batches
process_section_a(0, 10)
process_section_a(10, 20)
process_section_a(20, 30)
process_section_a(30, 40)
