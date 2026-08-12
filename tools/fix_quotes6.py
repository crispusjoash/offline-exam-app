import re

with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

# For Q43:
content = re.sub(
    r'lower back and hamstrings\."sit and reach\\".*?muscles\."?',
    r'lower back and hamstrings."',
    content
)

# For Q49:
content = re.sub(
    r'Score is a \*\*Point\*\*\."Goal\\".*?matched\."?',
    r'Score is a **Point**."',
    content
)

with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(content)
