import re
import json

def clean_asterisks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # The file is a JS file exporting an object.
    # We will just do a global text replacement, but to be extremely safe,
    # we only want to apply this to the string values of explanations or just globally.
    # Actually, applying it globally is safe as long as we protect `* ` bullets and `/*` comments.
    
    # Protect JS block comments `/*` and `*/` (though unlikely in data)
    text = text.replace('/*', 'BLOCK_COMMENT_START_MARKER')
    text = text.replace('*/', 'BLOCK_COMMENT_END_MARKER')
    
    # Protect bullet points (must match start of line or after newline)
    text = re.sub(r'(?m)^(\s*)\*\s', r'\1BULLET_POINT_MARKER ', text)
    
    # Now replace any remaining sequence of 1 or more asterisks with exactly two asterisks
    text = re.sub(r'\*+', '**', text)
    
    # Restore everything
    text = text.replace('BULLET_POINT_MARKER ', '* ')
    text = text.replace('BLOCK_COMMENT_START_MARKER', '/*')
    text = text.replace('BLOCK_COMMENT_END_MARKER', '*/')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

clean_asterisks('src/data/kpsea-english-2023.js')
clean_asterisks('src/data/kpsea-kiswahili-2023.js')
print("Asterisks normalized successfully.")
