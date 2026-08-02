import os

target_files = [
    'src/data/kpsea-english-2023.js',
    'src/data/kpsea-science-2023.js',
    'src/data/kpsea-sst-parta-2023.js',
    'src/data/kpsea-sst-cre-2023.js',
    'src/data/kpsea-sst-ire-2023.js',
    'src/data/kpsea-sst-hre-2023.js'
]

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        # Replace Detailed Analysis of the Correct Answer with Analysis of the Correct Answer
        fixed_text = text.replace('**Detailed Analysis of the Correct Answer:**', '**Analysis of the Correct Answer:**')
        fixed_text = fixed_text.replace('Detailed Analysis of the Correct Answer:', 'Analysis of the Correct Answer:')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_text)
            
        print(f"Updated {filepath}")

print("Removed 'Detailed' from all target paper explanations!")
