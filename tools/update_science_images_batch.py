import json
import re
import shutil

artifact_dir = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51"

images = {
    "q7": {
        "source": "media__1786274467134.png",
        "dest": "science_2025_q7.png",
        "title": "Modified Root",
        "regex": r"\n\n\[Image: A carrot\]"
    },
    "q9": {
        "source": "media__1786274529958.png",
        "dest": "science_2025_q9.png",
        "title": "Compost Pit",
        "regex": r"\n\n\[Image: A compost pit with organic waste\]"
    },
    "q12": {
        "source": "media__1786274572989.png",
        "dest": "science_2025_q12.png",
        "title": "Air Components",
        "regex": r"\n\n\[Image: Blocks F \(largest\), G, H, J \(smallest\)\]"
    },
    "q13": {
        "source": "media__1786274635021.png",
        "dest": "science_2025_q13.png",
        "title": "Objects in Water",
        "regex": r"\n\n\[Image: A trough with water. Inside, a Wooden plank floats, a Plastic ruler floats, a Pencil floats, and a Coin is at the bottom\]"
    },
    "q15": {
        "source": "media__1786274690293.png",
        "dest": "science_2025_q15.png",
        "title": "Light Travel Set-up",
        "regex": r"\n\n\[Image: A hollow curved pipe. One end has a candle flame, the other end has the learner's eye. The pipe is curved.\]"
    }
}

for q_id, info in images.items():
    source_path = f"{artifact_dir}\\{info['source']}"
    dest_path = f"public/assets/{info['dest']}"
    shutil.copyfile(source_path, dest_path)

file_path = 'src/data/kpsea-science-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add shared contexts and update questions
for q_id, info in images.items():
    ctx_id = f"ctx-science-2025-{q_id}"
    data["sharedContexts"][ctx_id] = {
        "type": "image",
        "imagePath": f"/assets/{info['dest']}",
        "title": info['title'],
        "cssFilter": "none",
        "scanEffect": False
    }
    
    for q in data["sectionA"]:
        if q["id"] == q_id:
            q["contextRef"] = ctx_id
            q["questionText"] = re.sub(info["regex"], "", q["questionText"])
            break

new_content = "export const kpseaScience2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch of Science images updated successfully!")
