import shutil
import json
import re

# 1. Copy image
src_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\f792ea54-54ae-49d1-a665-6f5c779624ea\media__1785660520255.png"
dst_img = r"C:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\kpsea_science_2022_q2.png"
shutil.copy(src_img, dst_img)

# 2. Update JSON
file_path = 'src/data/kpsea-science-2022.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match_section = re.search(r'"sectionA":\s*(\[.*\])\s*\}', content, re.DOTALL)
if not match_section:
    print("Could not find sectionA")
    exit(1)

section_a = json.loads(match_section.group(1))

for q in section_a:
    if q.get("questionNumber") == 2:
        q["questionText"] = "Grade 5 learners in a certain primary school grouped fungi with their use. Which of the following fungi was correctly matched to its use?"
        q["contextRef"] = "ctx-science-2022-q2"
        q["options"] = [
            {"text": "A", "isCorrect": False},
            {"text": "B", "isCorrect": False},
            {"text": "C", "isCorrect": False},
            {"text": "D", "isCorrect": True}
        ]

new_section_a_str = json.dumps(section_a, indent=6)
new_section_a_str = "    " + new_section_a_str.replace('\n', '\n    ')

new_shared_contexts = """"sharedContexts": {
    "ctx-science-2022-q2": {
      "title": "Fungi and their Uses",
      "type": "image",
      "imagePath": "/assets/kpsea_science_2022_q2.png",
      "caption": "Table matching fungi with their uses",
      "cssFilter": "grayscale(100%) contrast(150%) brightness(105%)"
    }
  },"""

content = re.sub(r'"sharedContexts":\s*\{\},', new_shared_contexts, content)

# Use string replace instead of re.sub for the big array to avoid backslash escape issues
prefix = content[:match_section.start(0)]
content = prefix + '"sectionA": ' + new_section_a_str.strip() + '\n}\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Q2 updated and image copied successfully.")
