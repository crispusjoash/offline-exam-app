import json

filepath = 'src/data/kpsea-science-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

clean_text = text.replace('export const kpseaScience2023 = ', '').strip().rstrip(';')
data = json.loads(clean_text)

for q in data.get('sectionA', [])[:5]:
    print(json.dumps(q, indent=2))
