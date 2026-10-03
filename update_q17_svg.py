import json
import shutil

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  
  <rect x="20" y="20" width="560" height="200" fill="white" stroke="black" stroke-width="2" />
  
  <line x1="20" y1="60" x2="580" y2="60" class="line" />
  <line x1="20" y1="100" x2="580" y2="100" class="line" />
  <line x1="20" y1="140" x2="580" y2="140" class="line" />
  <line x1="20" y1="180" x2="580" y2="180" class="line" />
  
  <line x1="80" y1="20" x2="80" y2="220" class="line" />
  <line x1="300" y1="20" x2="300" y2="220" class="line" />
  
  <text x="50" y="45" class="header" text-anchor="middle"></text>
  <text x="190" y="45" class="header" text-anchor="middle">Molecule moving</text>
  <text x="440" y="45" class="header" text-anchor="middle">Type of membrane</text>
  
  <text x="50" y="85" class="text" text-anchor="middle">A.</text>
  <text x="190" y="85" class="text" text-anchor="middle">Water</text>
  <text x="440" y="85" class="text" text-anchor="middle">Semi-permeable</text>
  
  <text x="50" y="125" class="text" text-anchor="middle">B.</text>
  <text x="190" y="125" class="text" text-anchor="middle">Oxygen</text>
  <text x="440" y="125" class="text" text-anchor="middle">Semi-permeable</text>
  
  <text x="50" y="165" class="text" text-anchor="middle">C.</text>
  <text x="190" y="165" class="text" text-anchor="middle">Water</text>
  <text x="440" y="165" class="text" text-anchor="middle">Permeable</text>
  
  <text x="50" y="205" class="text" text-anchor="middle">D.</text>
  <text x="190" y="205" class="text" text-anchor="middle">Oxygen</text>
  <text x="440" y="205" class="text" text-anchor="middle">Permeable</text>
</svg>"""

with open('public/assets/kjsea_science_2025_q17.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
    
shutil.copy('public/assets/kjsea_science_2025_q17.svg', 'electron/app/assets/kjsea_science_2025_q17.svg')

filepath = 'public/data/kjsea-science-sectiona-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionA', []):
    if q.get('id') == 'q17':
        q['imagePath'] = "/assets/kjsea_science_2025_q17.svg"
        # Update options to just A, B, C, D
        for opt in q['options']:
            if "A." in opt['text']:
                opt['text'] = "A"
            elif "B." in opt['text']:
                opt['text'] = "B"
            elif "C." in opt['text']:
                opt['text'] = "C"
            elif "D." in opt['text']:
                opt['text'] = "D"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectiona-2025.json')
print("Successfully generated SVG and updated JSON for Q17!")
