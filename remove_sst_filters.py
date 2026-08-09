import json
import re

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON part
match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add cssFilter: "none" and scanEffect: false to the newly added images
targets = ["ctx-sst-2024-q1", "ctx-sst-2024-q3", "ctx-sst-2024-q10", 
           "ctx-sst-2024-q11", "ctx-sst-2024-q30", "ctx-sst-2024-q31-32"]

for target in targets:
    if target in data.get("sharedContexts", {}):
        data["sharedContexts"][target]["cssFilter"] = "none"
        data["sharedContexts"][target]["scanEffect"] = False

# Write it back
new_content = "export const kpseaSstParta2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully removed filters for SST 2024 images.")
