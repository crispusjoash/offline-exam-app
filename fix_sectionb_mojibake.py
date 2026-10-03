import json
import re
import shutil

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# The file contains literally the characters ðŸ“Œ which might be represented as unicode escapes or literal string.
# Since we used ensure_ascii=True, it's saved as unicode escapes like \u00f0\u0178\u201c\u0152
# Let's replace the mojibake directly in the string
text = text.replace('\\u00f0\\u0178\\u201c\\u0152', '📌')
# And just in case it's literal
text = text.replace('ðŸ“Œ', '📌')
# Also the bulb
text = text.replace('\\u00f0\\u0178\\u2019\\u00a1', '📌')
text = text.replace('ðŸ’¡', '📌')

# Let's parse and re-dump with ensure_ascii=True to get \ud83d\udccc
data = json.loads(text)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')

print("Fixed Section B mojibake!")
