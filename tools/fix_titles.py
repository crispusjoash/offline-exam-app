import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Kiswahili titles: 'Swali la 1 hadi la 5\\nSoma kifungu...'
# They currently look like:
# "title": "Swali la 1 hadi la 5\
# Soma kifungu kifuatacho kisha ujibu maswali.",
# We replace the line continuation with a newline escape
text = re.sub(r'(hadi la \d+)\\\n(Soma kifungu)', r'\1\\n\2', text)

# 2. Fix English titles: they currently have '\\n' which means the file literally has two backslashes.
# In JS, '\\\\n' evaluates to '\n' (literally a backslash and an n).
# We want it to be a single backslash and an n in the file, which in python strings is '\\n'
text = text.replace(r'\\\\n', r'\\n')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Titles and English newlines fixed!')
