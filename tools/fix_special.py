with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Bold 'special' in the animals passage
old = 'This is because they have special abilities which human beings do not have.'
new = 'This is because they have **special** abilities which human beings do not have.'

if old in text:
    text = text.replace(old, new)
    print('Bolded "special" in passage!')
else:
    print('ERROR: could not find target sentence')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(text)
