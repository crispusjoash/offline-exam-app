with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Q43
content = content.replace(
    'lower back and hamstrings."sit and reach\\" box is a standardized piece of equipment used specifically to measure the flexibility of the lower back and hamstring muscles.\\"',
    'lower back and hamstrings."'
)
content = content.replace(
    'lower back and hamstrings."sit and reach\\" box is a standardized piece of equipment used specifically to measure the flexibility of the lower back and hamstring muscles."',
    'lower back and hamstrings."'
)

# Fix Q49
content = content.replace(
    'Score is a **Point**.\\"Goal\\". \\"Gun\\" is not a scoring term in any of these sports; it is an unrelated word.\\"',
    'Score is a **Point**."'
)
content = content.replace(
    'Score is a **Point**.\\"Goal\\". \\"Gun\\" is not a scoring term in any of these sports; it is an unrelated word."',
    'Score is a **Point**."'
)


with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(content)
