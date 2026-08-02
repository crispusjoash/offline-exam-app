import re
import json

def extract_from(filename, output_name):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'["\']?questionText["\']?\s*:\s*', content)
    
    out = []
    for i, part in enumerate(parts[1:]):
        q_match = re.search(r'^["\'](.*?)["\'],\s*["\']?options["\']?', part, re.DOTALL)
        if not q_match: 
            q_match = re.search(r'^["\'](.*?)["\']', part, re.DOTALL)
            if not q_match: continue
            
        q = q_match.group(1).replace('\n', ' ')
        
        opt_match = re.search(r'["\']?options["\']?\s*:\s*\[([\s\S]*?)\]', part)
        if opt_match:
            opts = opt_match.group(1)
            opts_list = re.findall(r'\{\s*["\']?text["\']?\s*:\s*["\'](.*?)["\'],\s*["\']?isCorrect["\']?\s*:\s*(true|false)\s*\}', opts)
            opts_text = [f"{t} {'(CORRECT)' if c=='true' else ''}".strip() for t, c in opts_list]
            out.append(f'Q{i+1}: {q}\nOptions: {opts_text}')
    
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(out))

extract_from('src/data/kpsea-science-2023.js', 'science_options.txt')
extract_from('src/data/kpsea-english-2023.js', 'english_options.txt')
extract_from('src/data/kpsea-sst-parta-2023.js', 'sst_parta_options.txt')
extract_from('src/data/kpsea-sst-cre-2023.js', 'sst_cre_options.txt')
extract_from('src/data/kpsea-sst-hre-2023.js', 'sst_hre_options.txt')
extract_from('src/data/kpsea-sst-ire-2023.js', 'sst_ire_options.txt')
extract_from('src/data/kpsea-kiswahili-2023.js', 'kiswahili_options.txt')

print("Extraction complete.")
