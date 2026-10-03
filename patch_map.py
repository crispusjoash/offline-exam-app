import re

filepath = 'src/data/pastPapersMeta.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_entry = """,
  "kjsea-creative-arts-sports-2025": {
    "fileName": "kjsea-creative-arts-sports-2025.json",
    "exportName": "kjseaCreativeArtsSports2025"
  }
};"""

# Replace the last }; with the new entry + };
if content.endswith('};\n'):
    content = content[:-3] + new_entry + '\n'
elif content.endswith('};'):
    content = content[:-2] + new_entry
else:
    # Use regex to find the last };
    content = re.sub(r'\};\s*$', new_entry + '\n', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated PAPER_FILE_MAP successfully.")
