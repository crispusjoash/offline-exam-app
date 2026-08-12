import json
import re
import shutil

artifact_dir = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\bc14a1be-6912-4ec6-90fd-f3a7be1eaf51"

images = {
    "q16": {
        "source": "media__1786274765922.png",
        "dest": "science_2025_q16.png",
        "title": "Lifting a Load",
        "regex": r"\n\n\[Image: A: Man lifting block directly with a rope over a single fixed pulley. B: Man lifting block with a single movable pulley system. C: Man pushing a block up a short steep inclined plane. D: Man lifting the block directly on his head\]"
    },
    "q17": {
        "source": "media__1786274839128.png",
        "dest": "science_2025_q17.png",
        "title": "Volleyball",
        "regex": r"\n\n\[Image: A learner hitting a volleyball upwards\]"
    },
    "q20": {
        "source": "media__1786274888524.png",
        "dest": "science_2025_q20.png",
        "title": "Shoe Sole",
        "regex": r"\n\n\[Image: The sole of a shoe, completely worn out and smooth\]"
    },
    "q21": {
        "source": "media__1786274948089.png",
        "dest": "science_2025_q21.png",
        "title": "Circulatory System",
        "regex": r"\n\n\[Image: Diagram of circulatory system with Lungs, Heart, and Body Organs. L connects lungs to the left side of heart. M is the left auricle. N connects the left ventricle to Body Organs. K connects Body Organs to the right side of the heart.\]"
    },
    "q22": {
        "source": "media__1786275051222.png",
        "dest": "science_2025_q22.png",
        "title": "Hammer Lever",
        "regex": r"\n\n\[Image: A hand holding a hammer handle at M, pulling a nail at P out of wood Q. N is the neck of the hammer resting on the wood.\]"
    },
    "q23": {
        "source": "media__1786275115596.png",
        "dest": "science_2025_q23.png",
        "title": "Heat Transfer",
        "regex": r"\n\n\[Image: A hand holding a wooden rod, the other end of the rod is in a candle flame.\]"
    },
    "q24": {
        "source": "media__1786275168616.png",
        "dest": "science_2025_q24.png",
        "title": "Cooking",
        "regex": r"\n\n\[Image: A person cooking using a frying pan over a gas flame\]"
    },
    "q26": {
        "source": "media__1786275202615.png",
        "dest": "science_2025_q26.png",
        "title": "Special Seedbed",
        "regex": r"\n\n\[Image: A crop grown in sunken beds dug below the ground level.\]"
    },
    "q32": {
        "source": "media__1786275254631.png",
        "dest": "science_2025_q32.png",
        "title": "Innovative Garden",
        "regex": r"\n\n\[Image: A farmer watering a garden constructed from stacked tyres\]"
    },
    "q37": {
        "source": "media__1786275301012.png",
        "dest": "science_2025_q37.png",
        "title": "Panga",
        "regex": r"\n\n\[Image: A panga or machete\]"
    },
    "q49": {
        "source": "media__1786275463872.png",
        "dest": "science_2025_q49.png",
        "title": "Stitches",
        "regex": r"\n\n\[Image: A diagram showing vertical stitches connected along the top edge\]"
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

# Map q33 and q34 to q32's context
for q in data["sectionA"]:
    if q["id"] in ["q33", "q34"]:
        q["contextRef"] = "ctx-science-2025-q32"
    if q["id"] == "q38":
        q["contextRef"] = "ctx-science-2025-q37"

# Also handle Q14 SVG
ctx_id_14 = "ctx-science-2025-q14"
data["sharedContexts"][ctx_id_14] = {
    "type": "image",
    "imagePath": "/assets/science_2025_q14.svg",
    "title": "Properties of Matter Table",
    "cssFilter": "none",
    "scanEffect": False
}

for q in data["sectionA"]:
    if q["id"] == "q14":
        q["contextRef"] = ctx_id_14
        for opt in q["options"]:
            if "has weight" in opt["text"]:
                opt["text"] = "A"
            elif "has definite mass" in opt["text"]:
                opt["text"] = "B"
            elif "has definite shape" in opt["text"]:
                opt["text"] = "C"
            elif "has definite volume" in opt["text"]:
                opt["text"] = "D"
        break

new_content = "export const kpseaScience2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch of Science images 2 updated successfully!")
