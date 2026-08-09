import json
import re

def fix_newlines(file_path, obj_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'(export const ' + obj_name + r' = )(\{.*\});?\s*$', content, re.DOTALL)
    prefix = match.group(1)
    data = json.loads(match.group(2))
    
    def process_strings(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str):
                    # Replace multiple newlines with single newline
                    obj[k] = re.sub(r'\n{2,}', '\n', v)
                else:
                    process_strings(v)
        elif isinstance(obj, list):
            for i in range(len(obj)):
                if isinstance(obj[i], str):
                    obj[i] = re.sub(r'\n{2,}', '\n', obj[i])
                else:
                    process_strings(obj[i])

    process_strings(data)
    
    # Fix the Q42-43 context to ensure list formatting
    if "sharedContexts" in data and "ctx-science-2025-q42-43" in data["sharedContexts"]:
        ctx = data["sharedContexts"]["ctx-science-2025-q42-43"]
        if "text" in ctx:
            text = ctx["text"]
            # Add newlines before (i), (ii), etc., if they don't have them
            text = re.sub(r'\s*(\(ii\))', r'\n\1', text)
            text = re.sub(r'\s*(\(iii\))', r'\n\1', text)
            text = re.sub(r'\s*(\(iv\))', r'\n\1', text)
            ctx["text"] = text

    new_content = prefix + json.dumps(data, indent=2) + ";\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed newlines in {file_path}")

fix_newlines('src/data/kpsea-science-2025.js', 'kpseaScience2025')
fix_newlines('src/data/kpsea-math-2025.js', 'kpseaMath2025')
