import json
import shutil
import os

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 250" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  
  <rect x="20" y="20" width="460" height="200" fill="white" stroke="black" stroke-width="2" />
  
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="20" y1="140" x2="480" y2="140" class="line" />
  <line x1="20" y1="180" x2="480" y2="180" class="line" />
  
  <line x1="250" y1="20" x2="250" y2="220" class="line" />
  
  <text x="135" y="45" class="header" text-anchor="middle">Sample of water</text>
  <text x="365" y="45" class="header" text-anchor="middle">Volume of soap used (cm³)</text>
  
  <text x="135" y="85" class="text" text-anchor="middle">(i)</text>
  <text x="365" y="85" class="text" text-anchor="middle">1.2</text>
  
  <text x="135" y="125" class="text" text-anchor="middle">(ii)</text>
  <text x="365" y="125" class="text" text-anchor="middle">1.5</text>
  
  <text x="135" y="165" class="text" text-anchor="middle">(iii)</text>
  <text x="365" y="165" class="text" text-anchor="middle">3.4</text>
  
  <text x="135" y="205" class="text" text-anchor="middle">(iv)</text>
  <text x="365" y="205" class="text" text-anchor="middle">12</text>
</svg>"""

with open('public/assets/kjsea_science_2025_q12.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
    
shutil.copy('public/assets/kjsea_science_2025_q12.svg', 'electron/app/assets/kjsea_science_2025_q12.svg')

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('id') == 'q12':
        q['imagePath'] = "/assets/kjsea_science_2025_q12.svg"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully generated SVG and updated JSON for Q12!")
