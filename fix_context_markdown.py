import json
import re

file_path = 'src/data/kpsea-science-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(export const kpseaScience2025 = )(\{.*\});?\s*$', content, re.DOTALL)
prefix = match.group(1)
data = json.loads(match.group(2))

# Fix the Q42-43 context to ensure list formatting in ReactMarkdown
if "sharedContexts" in data and "ctx-science-2025-q42-43" in data["sharedContexts"]:
    ctx = data["sharedContexts"]["ctx-science-2025-q42-43"]
    if "text" in ctx:
        text = ctx["text"]
        # Add double newlines before (i), (ii), etc. for ReactMarkdown to render as paragraphs
        text = re.sub(r'\s*(\(i\))', r'\n\n\1', text)
        text = re.sub(r'\s*(\(ii\))', r'\n\n\1', text)
        text = re.sub(r'\s*(\(iii\))', r'\n\n\1', text)
        text = re.sub(r'\s*(\(iv\))', r'\n\n\1', text)
        ctx["text"] = text.strip()

new_content = prefix + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
