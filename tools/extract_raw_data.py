import re
import json

files = {
    'science': 'src/data/kpsea-science-2023.js',
    'english': 'src/data/kpsea-english-2023.js',
    'kiswahili': 'src/data/kpsea-kiswahili-2023.js',
    'sst_parta': 'src/data/kpsea-sst-parta-2023.js',
    'sst_cre': 'src/data/kpsea-sst-cre-2023.js',
    'sst_ire': 'src/data/kpsea-sst-ire-2023.js',
    'sst_hre': 'src/data/kpsea-sst-hre-2023.js'
}

all_raw = {}

for key, fpath in files.items():
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract questions array using regex or block parsing
    # Let's find sectionA: [ ... ]
    sec_idx = content.find('"sectionA":')
    if sec_idx == -1:
        print("Could not find sectionA in", fpath)
        continue
    
    arr_start = content.find('[', sec_idx)
    arr_end = content.rfind(']')
    
    # We can parse question blocks using regex:
    # Each question object has questionNumber, questionText, options
    # Let's write a simple JS execution via node script to get pure JSON!
