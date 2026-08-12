def restore_bullets(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # In the JS file, newlines inside explanation strings are stored as literal '\' and 'n'
    # The corrupted bullet points now look like `\\n** **` or `\\n** `
    # We want to change them back to `\\n* **` or `\\n* `
    
    text = text.replace('\\n** ', '\\n* ')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

restore_bullets('src/data/kpsea-english-2023.js')
restore_bullets('src/data/kpsea-kiswahili-2023.js')

print("Restored bullet points.")
