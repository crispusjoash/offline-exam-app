import json
import shutil
import os

# Copy the image file
src_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\9d39c76d-2c71-4969-8f52-1885f6f7bfde\.user_uploaded\media_1787406690549.png"
dst_img1 = "public/assets/kjsea_science_2025_q27.png"
dst_img2 = "electron/app/assets/kjsea_science_2025_q27.png"
shutil.copy(src_img, dst_img1)
shutil.copy(src_img, dst_img2)

# Update JSON
filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('id') == 'q27':
        q['imagePath'] = "/assets/kjsea_science_2025_q27.png"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')

print("Successfully replaced Q27 image and updated JSON!")
