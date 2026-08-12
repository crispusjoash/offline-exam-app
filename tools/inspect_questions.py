import json
import re
import os

files = [
    'src/data/kpsea-science-2023.js',
    'src/data/kpsea-english-2023.js',
    'src/data/kpsea-kiswahili-2023.js',
    'src/data/kpsea-sst-parta-2023.js',
    'src/data/kpsea-sst-cre-2023.js',
    'src/data/kpsea-sst-ire-2023.js',
    'src/data/kpsea-sst-hre-2023.js',
]

def parse_js_obj(content):
    # Remove export const ... = 
    idx = content.find('{')
    ridx = content.rfind('}')
    json_like = content[idx:ridx+1]
    # We can evaluate this with node or process it in python
    return json_like

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        q_matches = re.findall(r'"questionNumber"\s*:\s*(\d+)', content)
        print(f"{fpath}: {len(q_matches)} questions")
