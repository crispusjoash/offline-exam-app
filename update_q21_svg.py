import json
import shutil

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 250" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; text-decoration: underline; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  
  <rect x="20" y="20" width="460" height="200" fill="white" stroke="black" stroke-width="2" />
  
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="20" y1="140" x2="480" y2="140" class="line" />
  <line x1="20" y1="180" x2="480" y2="180" class="line" />
  
  <line x1="150" y1="20" x2="150" y2="220" class="line" />
  
  <text x="85" y="45" class="header" text-anchor="middle">Flower</text>
  <text x="315" y="45" class="header" text-anchor="middle">Characteristics</text>
  
  <text x="85" y="85" class="text" text-anchor="middle">Q</text>
  <text x="170" y="85" class="text" text-anchor="start">Small in size</text>
  
  <text x="85" y="125" class="text" text-anchor="middle">R</text>
  <text x="170" y="125" class="text" text-anchor="start">Sweet scented</text>
  
  <text x="85" y="165" class="text" text-anchor="middle">S</text>
  <text x="170" y="165" class="text" text-anchor="start">Long stamen</text>
  
  <text x="85" y="205" class="text" text-anchor="middle">T</text>
  <text x="170" y="205" class="text" text-anchor="start">Brightly coloured petals</text>
</svg>"""

with open('public/assets/kjsea_science_2025_q21.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
    
shutil.copy('public/assets/kjsea_science_2025_q21.svg', 'electron/app/assets/kjsea_science_2025_q21.svg')

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('id') == 'q21':
        q['imagePath'] = "/assets/kjsea_science_2025_q21.svg"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully generated SVG and updated JSON for Q21!")
