file_path = 'src/data/kpsea-science-2022.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find any single newline followed by a list item and replace with a double newline
# Since the file contains literal string \n, we look for '\\n'
content = content.replace('\\n* (i)', '\\n\\n* (i)')
# Fix any double replacements if they were already correct
content = content.replace('\\n\\n\\n* (i)', '\\n\\n* (i)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Formatting fixed!")
