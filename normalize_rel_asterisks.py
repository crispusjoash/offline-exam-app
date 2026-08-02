import re

def clean_asterisks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Protect JS block comments `/*` and `*/`
    text = text.replace('/*', 'BLOCK_COMMENT_START_MARKER')
    text = text.replace('*/', 'BLOCK_COMMENT_END_MARKER')
    
    # Protect escaped bullet points `\\n* `
    text = text.replace('\\n* ', '\\nBULLET_POINT_MARKER ')
    
    # Protect bullet points (start of line)
    text = re.sub(r'(?m)^(\s*)\*\s', r'\1BULLET_POINT_MARKER ', text)
    
    # Replace any remaining sequence of 1 or more asterisks with exactly two asterisks
    text = re.sub(r'\*+', '**', text)
    
    # Restore everything
    text = text.replace('\\nBULLET_POINT_MARKER ', '\\n* ')
    text = text.replace('BULLET_POINT_MARKER ', '* ')
    text = text.replace('BLOCK_COMMENT_START_MARKER', '/*')
    text = text.replace('BLOCK_COMMENT_END_MARKER', '*/')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

clean_asterisks('src/data/kpsea-sst-cre-2023.js')
clean_asterisks('src/data/kpsea-sst-ire-2023.js')
clean_asterisks('src/data/kpsea-sst-hre-2023.js')
print("Religious Ed papers normalized successfully.")
