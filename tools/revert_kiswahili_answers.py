import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

def swap_correct(text, text_wrong, text_correct):
    pattern_wrong = r'("text":\s*"' + re.escape(text_wrong) + r'",\s*"isCorrect":\s*)true'
    text = re.sub(pattern_wrong, r'\g<1>false', text)
    
    pattern_correct = r'("text":\s*"' + re.escape(text_correct) + r'",\s*"isCorrect":\s*)false'
    text = re.sub(pattern_correct, r'\g<1>true', text)
    
    return text

# We are REVERTING the answers back to the original ones.
# Q1: Make 'Masalkheri?' true, 'Shikamoo?' false
text = swap_correct(text, 'Shikamoo?', 'Masalkheri?')
# Q7: Make 'imepewa mamlaka kikatiba.' true, 'ni muhimu kuhakikisha matumizi yafaayo ya fedha.' false
text = swap_correct(text, 'ni muhimu kuhakikisha matumizi yafaayo ya fedha.', 'imepewa mamlaka kikatiba.')
# Q13: Make 'Jumatatu.' true, 'Jumapili.' false
text = swap_correct(text, 'Jumapili.', 'Jumatatu.')
# Q23: Make 'msalani.' true, 'chumbani.' false
text = swap_correct(text, 'chumbani.', 'msalani.')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Answers reverted to original!')
