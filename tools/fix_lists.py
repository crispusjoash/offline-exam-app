import json
import re

files = ['src/data/kpsea-science-2025.js', 'src/data/kpsea-math-2025.js']

def process_text(text):
    if "(i)" not in text and "(I)" not in text and "(a)" not in text:
        return text, None, None
        
    lines = text.split('\n')
    text_part = []
    list_part = []
    suffix_part = []
    state = 0
    
    for line in lines:
        if line.strip() == '':
            if state == 1:
                state = 2
            continue
            
        is_list_item = False
        if re.match(r'^\([ivxIVX]+\)\s', line.strip()) or re.match(r'^\([a-d]\)\s', line.strip()):
            is_list_item = True
            
        if is_list_item:
            state = 1
            list_part.append(line.strip())
        else:
            if state == 0:
                text_part.append(line.strip())
            else:
                state = 2
                suffix_part.append(line.strip())
                
    if not list_part:
        return text, None, None
        
    return ' '.join(text_part).strip(), list_part, ' '.join(suffix_part).strip()

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(export const \w+ = )(\{.*\});?\s*$', content, re.DOTALL)
    if not match:
        print(f"Could not parse file {file_path}")
        continue
    
    prefix = match.group(1)
    data = json.loads(match.group(2))

    section_key = "sectionA" if "sectionA" in data else "questions"
    for q in data.get(section_key, []):
        if "questionText" in q:
            q_text, q_list, q_suffix = process_text(q["questionText"])
            if q_list:
                q["questionText"] = q_text
                q["questionList"] = q_list
                if q_suffix:
                    q["questionSuffix"] = q_suffix

    new_content = prefix + json.dumps(data, indent=2) + ";\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Lists fixed!")
