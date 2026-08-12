import json
import re

def rebuild_files():
    scripts = [
        'update_kiswahili_complete.py',
        'update_english_batch1.py',
        'update_english_batch2.py',
        'update_english_batch3.py',
        'update_english_batch4.py',
        'update_english_batch5.py',
        'update_english_batch6.py'
    ]
    
    for script in scripts:
        with open(script, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We want to ensure that any quote that is bolded or italicized uses exactly TWO asterisks.
        # So we find any combination of asterisks touching a quote and replace it with **" or "**
        # E.g. `*"`, `**"`, `***"` -> `**"`
        content = re.sub(r'\*+"', '**"', content)
        content = re.sub(r'"\*+', '"**', content)
        
        # Also fix `(*` and `*)` to `(**` and `**)`
        content = re.sub(r'\(\*+', '(**', content)
        content = re.sub(r'\*+\)', '**)', content)
        
        with open(script, 'w', encoding='utf-8') as f:
            f.write(content)

rebuild_files()
print("Fixed generator scripts to use exactly ** for all highlighted quotes.")
