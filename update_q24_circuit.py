import json
import shutil

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['sectionA']:
    if q['id'] == 'q24':
        q['options'] = [
            { "text": "Cells: Parallel, Bulbs: Parallel", "isCorrect": False },
            { "text": "Cells: Parallel, Bulbs: Series", "isCorrect": True },
            { "text": "Cells: Series, Bulbs: Parallel", "isCorrect": False },
            { "text": "Cells: Series, Bulbs: Series", "isCorrect": False }
        ]
        q['explanation'] = "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nIn the diagram, the **cells** are arranged one below the other with their positive terminals connected to the same junction and their negative terminals connected to another junction. This is a **parallel** arrangement of cells. The two **bulbs** are placed side-by-side along the same single path of wire at the bottom, which means the current has to flow through one bulb to get to the other. This is a **series** arrangement of bulbs.\n\n**Why Other Options Are Incorrect:**\n* **Cells in series** would be connected end-to-end (positive to negative).\n* **Bulbs in parallel** would be on separate branches of the circuit.\n\n📌 **Key Learning Note:**\nConnecting cells in parallel increases the capacity (how long the battery lasts) but keeps the voltage the same. Connecting bulbs in series means that if one bulb blows, the circuit is broken and the other bulb goes out."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully updated Q24 to Parallel Cells, Series Bulbs!")
