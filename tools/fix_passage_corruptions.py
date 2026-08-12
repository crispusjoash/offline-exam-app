import re

def fix_corruption(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean up English corruptions
    text = re.sub(r'\*+P\*+upil:\*\*', '**Pupil:**', text)
    text = re.sub(r'P\*+upil:\*\*', '**Pupil:**', text)
    text = re.sub(r'Class \*+teacher:\*\*', 'Class teacher:**', text)
    
    # Clean up Kiswahili corruptions
    text = re.sub(r'L\*+eni:\*\*', '**Leni:**', text)
    text = re.sub(r'\*+L\*+eni:\*\*', '**Leni:**', text)
    text = re.sub(r'K\*+ibo:\*\*', '**Kibo:**', text)
    text = re.sub(r'\*+K\*+ibo:\*\*', '**Kibo:**', text)
    
    # Clean up any other weird ones like `**Answer:**` that got multiple `**` 
    # (Though we ran `run_all.py` to restore explanations, `sharedContexts` was the only thing holding the corrupted passages)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_corruption('src/data/kpsea-english-2023.js')
fix_corruption('src/data/kpsea-kiswahili-2023.js')
print("Fixed passage corruptions.")
