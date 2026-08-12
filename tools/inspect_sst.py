import json

def inspect_file(filename, export_name):
    filepath = f'src/data/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = text.replace(f'export const {export_name} = ', '').strip().rstrip(';')
    data = json.loads(clean_text)
    print(f"File: {filename}")
    print(f"  Title: {data.get('title')}")
    print(f"  Questions count: {len(data.get('sectionA', []))}")

inspect_file('kpsea-sst-parta-2023.js', 'kpseaSstParta2023')
inspect_file('kpsea-sst-2023.js', 'kpseaSst2023')
inspect_file('kpsea-sst-cre-2023.js', 'kpseaSstCre2023')
