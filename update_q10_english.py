import json
import os

filepath = 'src/data/kpsea-english-2022.js'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read().replace('export const kpseaEnglish2022 = ', '').strip(';\n')

js = json.loads(data)

for q in js['sectionA']:
    if q['questionNumber'] == 10:
        for opt in q['options']:
            opt['isCorrect'] = (opt['text'] == 'He wanted Hassan to do the totals of the cost of the items.')
        q['explanation'] = "The correct answer is **He wanted Hassan to do the totals of the cost of the items.**\n\n**Analysis of the Correct Answer:**\nThe passage specifies that Hassan's father wrote \"the **prices** of the items on a list.\" If the father only wanted to make sure Hassan didn't forget the items, he would have only written the names of the items. Because he took the extra step to write the *prices*, it implies he wanted Hassan to calculate the total cost (which came to Ksh 425) and figure out his expected balance.\n\n**Why Other Options Are Incorrect:**\n* **He did not want Hassan to forget any item.:** While a list helps you remember, the specific detail that the father wrote the *prices* points more strongly to calculating totals.\n* **He did not want Hassan to delay in the shop.:** Writing prices doesn't necessarily prevent delay.\n* **He wanted Hassan to learn Mathematics.:** While calculating totals is math, the specific immediate goal was doing the totals for this shop visit.\n\n📌 **Key Learning Note:**\nPay attention to specific details in the text. The fact that the father wrote the **prices** (not just the items) is the key clue to answering this question correctly."

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('export const kpseaEnglish2022 = ' + json.dumps(js, indent=2, ensure_ascii=False) + ';\n')

print('Updated Q10 successfully.')
