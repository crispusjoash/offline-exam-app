import json
import re

for name in ['kjsea-science-sectiona-2025.json', 'kjsea-science-sectionb-2025.json']:
    filepath = f'public/data/{name}'
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"Scanning {name}...")
    
    # Find all non-ASCII characters or common mojibake sequences
    # Since we saved with ensure_ascii=True, all non-ASCII should have been escaped?
    # Wait, ensure_ascii=True escapes non-ASCII characters into \uXXXX when writing the JSON string.
    # But when we f.read(), it reads the \uXXXX literally.
    # So the mojibake `Â` is actually saved as `\u00c2`.
    # Let's decode the JSON first to work with actual strings
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    def scan_string(s, path):
        matches = re.findall(r'[^\x00-\x7F]', s)
        for m in matches:
            print(f"Found {repr(m)} in {path}")
            
    def traverse(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                traverse(v, path + "." + k)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                traverse(v, path + f"[{i}]")
        elif isinstance(obj, str):
            scan_string(obj, path)
            
    traverse(data)
