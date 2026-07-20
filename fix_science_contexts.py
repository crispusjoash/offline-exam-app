import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find("title: 'KPSEA 2023 Integrated Science'")
if start_idx == -1:
    print("Could not find Integrated Science")
    exit()

end_idx = text.find("KJSEA:", start_idx)

science_block = text[start_idx:end_idx]

# 1. We need to extract all imagePath lines and their question numbers
# They look like:
# imagePath: "/assets/q2_roots.png",
#         questionText: "..."

# Let's use a function to modify each question block
# Wait, it's easier to use a regex that matches questionNumber: (\d+) and looks for imagePath: "(.*?)" within the same block

# Actually, let's parse the sharedContexts object which is currently empty:
# sharedContexts: {},

shared_contexts_str = "sharedContexts: {\n"

# Find all occurrences of questionNumber and imagePath
matches = re.finditer(r'questionNumber:\s*(\d+),\s*id:\s*\'[^\']+\',\s*imagePath:\s*"(.*?)",', science_block)
for m in matches:
    qnum = m.group(1)
    img_path = m.group(2)
    shared_contexts_str += f"""    'ctx-sci-q{qnum}': {{
      type: 'image',
      imagePath: '{img_path}',
      title: 'Diagram for Question {qnum}'
    }},
"""

shared_contexts_str += "  },"

# Replace sharedContexts: {},
science_block = science_block.replace("sharedContexts: {},", shared_contexts_str)

# Now, replace `imagePath: "...",` with `contextRef: 'ctx-sci-qX',`
def replace_img_with_context(match):
    qnum = match.group(1)
    img_path = match.group(2)
    return f"questionNumber: {qnum},\n        id: 'sci-q{qnum}',\n        contextRef: 'ctx-sci-q{qnum}',"

science_block = re.sub(r'questionNumber:\s*(\d+),\s*id:\s*\'[^\']+\',\s*imagePath:\s*"(.*?)",', replace_img_with_context, science_block)

new_text = text[:start_idx] + science_block + text[end_idx:]

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Science contexts fixed!")
