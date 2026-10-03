import json
import shutil

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['sectionA']:
    if q['id'] == 'q20':
        q['options'] = [
            { "text": "decaying matter", "isCorrect": False },
            { "text": "flesh", "isCorrect": True },
            { "text": "vegetation", "isCorrect": False },
            { "text": "vegetation and flesh.", "isCorrect": False }
        ]
        q['explanation'] = "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nThe skull clearly shows very prominent, sharp, and pointed canine teeth, as well as specialized shearing teeth (carnassials) at the back. This dentition is characteristic of **carnivores**, meaning the animal feeds strictly on **flesh**.\n\n**Why Other Options Are Incorrect:**\n* **C (Vegetation):** Herbivores have a large gap (diastema) and broad, flat molars for grinding plant material, lacking such sharp canines.\n* **D (Vegetation and flesh):** Omnivores have a mix of teeth, but the extreme specialization of these canines points strongly to a strict carnivore.\n* **A (Decaying matter):** Detritivores/scavengers may have similar teeth, but 'flesh' is the primary dietary classification for this dentition structure.\n\n📌 **Key Learning Note:**\nAnimal dentition is highly adapted to their diet. Sharp canines are used for piercing and tearing flesh, while flat molars are used for chewing and grinding."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully updated Q20 to carnivore!")
