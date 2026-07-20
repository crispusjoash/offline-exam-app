import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

def swap_correct(text, text_wrong, text_correct):
    pattern_wrong = r'("text":\s*"' + re.escape(text_wrong) + r'",\s*"isCorrect":\s*)true'
    text = re.sub(pattern_wrong, r'\g<1>false', text)
    
    pattern_correct = r'("text":\s*"' + re.escape(text_correct) + r'",\s*"isCorrect":\s*)false'
    text = re.sub(pattern_correct, r'\g<1>true', text)
    
    return text

text = swap_correct(text, 'Masalkheri?', 'Shikamoo?')
text = swap_correct(text, 'imepewa mamlaka kikatiba.', 'ni muhimu kuhakikisha matumizi yafaayo ya fedha.')
text = swap_correct(text, 'Jumatatu.', 'Jumapili.')
text = swap_correct(text, 'msalani.', 'chumbani.')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Answers updated!')
