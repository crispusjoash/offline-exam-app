import json
import shutil

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('id') == 'q12':
        # Update options
        for opt in q['options']:
            if opt['text'] == '(i)':
                opt['isCorrect'] = True
            else:
                opt['isCorrect'] = False
        
        # Update explanation
        q['explanation'] = "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nSoft water forms lather easily with soap, requiring very little soap solution. Hard water contains dissolved calcium and magnesium ions that react with soap to form scum, meaning a lot of soap is wasted before lather forms. Sample **(i)** used the least volume of soap (1.2 cm³), meaning it is the softest.\n\n**Why Other Options Are Incorrect:**\n* **B, C, D:** These samples required more soap (1.5, 3.4, and 12 cm³ respectively), indicating higher levels of water hardness. Sample (iv) is the hardest water.\n\n💡 **Key Learning Note:**\nThe amount of soap required to form a permanent lather is a direct indicator of water hardness; the less soap needed, the softer the water."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully updated Q12 answers!")
