with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Q34
content = content.replace(
    'Wash symbol."Do not bleach\\".\\"',
    'Wash symbol."'
)
content = content.replace(
    'Wash symbol."Do not bleach\\"."',
    'Wash symbol."'
)

# Fix Q35
content = content.replace(
    'fabrics together."make\\" the scarf fabric from scratch.\\"',
    'fabrics together."'
)
content = content.replace(
    'fabrics together."make\\" the scarf fabric from scratch."',
    'fabrics together."'
)

with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(content)
