import json
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    prefix = 'export const ' + filepath.split('/')[-1].replace('.js', '').replace('-', ' ').title().replace(' ', '')
    prefix = prefix[0].lower() + prefix[1:] + ' = '
    
    # We can't rely on simple prefix manipulation since it's hard to guess the exact export name
    # Let's just do direct string replacements on the raw file text
    
    # 1. Restore bullet points from '- ' back to '* '
    fixed_text = text.replace('\n- **', '\n* **')
    fixed_text = fixed_text.replace('\n- ', '\n* ')
    
    # 2. To highlight the key words/quotes, let's look for things in quotes that are part of the explanation.
    # The user wants key words to be highlighted. In the explanations, I had `*"word"*`. Then I removed it to `"word"`.
    # Let's just manually re-inject `**` around quotes that are passage excerpts. 
    # Actually, it's safer to just use regex to wrap ALL quotes in the explanations with `**`, EXCEPT where it would break something.
    # Wait, it's better to just re-generate the data with the proper `**"..."**` format from my python dictionary if I still had it.
    
    # Wait, I can just use regex to find `"..."` in the explanation blocks and wrap them in `**` if they aren't already.
    # But some quotes are just normal quotes.
    # The user said: "I think it's ment to show that its suposed to be either in bold or italic because it is a key word".
    # I can just revert the `*"..."*` removal, but change it to `**"..."**`.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

process_file('src/data/kpsea-english-2023.js')
process_file('src/data/kpsea-kiswahili-2023.js')

print("Bullets restored to '* ' in both English and Kiswahili.")
