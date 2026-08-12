import json
import glob
import re

files = [
    'src/data/kpsea-math-2023.js',
    'src/data/kpsea-science-2023.js',
    'src/data/kpsea-sst-2023.js',
    'src/data/kpsea-sst-parta-2023.js',
    'src/data/kpsea-english-2023.js',
    'src/data/kpsea-kiswahili-2023.js'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    var_name = re.search(r'export const (\w+) =', text).group(1)
    clean_text = text.replace(f'export const {var_name} = ', '').strip().rstrip(';')
    data = json.loads(clean_text)
    print(f"{filepath}: durationMinutes={data.get('durationMinutes')}, timeAllowed={data.get('timeAllowed')}")
