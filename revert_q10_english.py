import json

filepath = 'src/data/kpsea-english-2022.js'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read().replace('export const kpseaEnglish2022 = ', '').strip(';\n')

js = json.loads(data)

for q in js['sectionA']:
    if q['questionNumber'] == 10:
        for opt in q['options']:
            opt['isCorrect'] = (opt['text'] == 'He did not want Hassan to forget any item.')
        
        q['explanation'] = "The correct answer is **He did not want Hassan to forget any item.**\n\n**Analysis of the Correct Answer:**\nWhen someone is sent to buy a number of items, a list is written so they remember everything they need to buy. This is a logical inference based on the text.\n\n**Why Other Options Are Incorrect:**\n* **He did not want Hassan to delay in the shop.:** While a list might make shopping faster, the primary reason for a shopping list is to remember the items.\n* **He wanted Hassan to learn Mathematics.:** Hassan's father did the math himself (the total came to Ksh 425), so this wasn't a math test for Hassan.\n* **He wanted Hassan to do the totals of the cost of the items.:** The father had already calculated the total cost before giving Hassan the money.\n\n📌 **Key Learning Note:**\nSometimes questions require you to make logical inferences (deductions) based on everyday situations presented in the passage."

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('export const kpseaEnglish2022 = ' + json.dumps(js, indent=2, ensure_ascii=False) + ';\n')

print('Reverted Q10 successfully.')
