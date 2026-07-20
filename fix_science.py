import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find("title: 'KPSEA 2023 Integrated Science'")
if start_idx == -1:
    print("Could not find Integrated Science")
    exit()

end_idx = text.find("KJSEA:", start_idx)

science_block = text[start_idx:end_idx]

# 1. Add id: 'sci-qX',
def add_id(match):
    q_num = match.group(1)
    return f"questionNumber: {q_num},\n        id: 'sci-q{q_num}',"

science_block = re.sub(r"questionNumber:\s*(\d+),", add_id, science_block)

# 2. Extract markdown image and add imagePath
def fix_image_with_after(match):
    before_text = match.group(1)
    alt = match.group(2)
    path = match.group(3)
    after_text = match.group(4)
    # The image path from my scripts started with /assets/
    # If the text has \n, we can keep the spacing or replace with single space if needed
    # It's better to just trim the \n entirely where the image was
    return f'imagePath: "{path}",\n        questionText: "{before_text}\\n{after_text}"'

def fix_image_no_after(match):
    before_text = match.group(1)
    alt = match.group(2)
    path = match.group(3)
    return f'imagePath: "{path}",\n        questionText: "{before_text}"'


science_block = re.sub(r'questionText:\s*"(.*?)\\n!\[(.*?)\]\((.*?)\)\\n(.*?)"', fix_image_with_after, science_block)
science_block = re.sub(r'questionText:\s*"(.*?)\\n!\[(.*?)\]\((.*?)\)"', fix_image_no_after, science_block)

new_text = text[:start_idx] + science_block + text[end_idx:]

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Science block fixed!")
