import json
import shutil
import os

# Q30 SVG
q30_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 14px; }
    .line { stroke: black; stroke-width: 2; fill: none; }
    .axis { stroke: black; stroke-width: 2; }
    .arrow { stroke: black; stroke-width: 1.5; fill: none; }
  </style>
  
  <line x1="50" y1="20" x2="50" y2="180" class="axis" />
  <text x="30" y="100" class="text" transform="rotate(-90 30 100)" text-anchor="middle">Displacement</text>
  
  <line x1="50" y1="100" x2="380" y2="100" class="axis" marker-end="url(#arrowhead)" />
  <text x="350" y="120" class="text" text-anchor="middle">Distance</text>
  
  <text x="40" y="105" class="text" text-anchor="middle">0</text>
  
  <path d="M 50 100 Q 100 0, 150 100 T 250 100" class="line" />
  <path d="M 250 100 Q 300 200, 350 100" class="line" />
  
  <line x1="150" y1="100" x2="150" y2="50" class="arrow" marker-start="url(#arrowhead-rev)" marker-end="url(#arrowhead)" />
  <text x="140" y="80" class="text" text-anchor="middle">L</text>
  
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <marker id="arrowhead-rev" markerWidth="10" markerHeight="7" refX="1" refY="3.5" orient="auto">
      <polygon points="10 0, 0 3.5, 10 7" />
    </marker>
  </defs>
</svg>"""

# Q31b SVG
q31_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 150" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  <rect x="20" y="20" width="460" height="120" fill="white" stroke="black" stroke-width="2" />
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="200" y1="20" x2="200" y2="140" class="line" />
  <text x="30" y="45" class="header">Physical Activity</text>
  <text x="210" y="45" class="header">SI Unit</text>
  <text x="30" y="85" class="text">Length</text>
  <text x="30" y="125" class="text">Time</text>
</svg>"""

# Q32 SVG
q32_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 150" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  <rect x="20" y="20" width="460" height="120" fill="white" stroke="black" stroke-width="2" />
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="200" y1="20" x2="200" y2="140" class="line" />
  <text x="30" y="45" class="header">Type of mixture</text>
  <text x="210" y="45" class="header">Substance(s)</text>
  <text x="30" y="85" class="text">Homogeneous</text>
  <text x="30" y="125" class="text">Heterogeneous</text>
</svg>"""

# Q33a SVG
q33_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 160" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  <rect x="20" y="20" width="460" height="120" fill="white" stroke="black" stroke-width="2" />
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="200" y1="20" x2="200" y2="140" class="line" />
  <text x="30" y="45" class="header">Element</text>
  <text x="210" y="45" class="header">Symbol</text>
  <text x="30" y="85" class="text">Carbon</text>
  <text x="30" y="125" class="text">Oxygen</text>
</svg>"""
# Wait, Q33a has Sodium as well, I need to make the SVG taller for 3 elements.
q33_svg_fixed = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="100%" height="100%">
  <style>
    .text { font-family: Arial, sans-serif; font-size: 16px; }
    .header { font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
    .line { stroke: black; stroke-width: 2; }
  </style>
  <rect x="20" y="20" width="460" height="160" fill="white" stroke="black" stroke-width="2" />
  <line x1="20" y1="60" x2="480" y2="60" class="line" />
  <line x1="20" y1="100" x2="480" y2="100" class="line" />
  <line x1="20" y1="140" x2="480" y2="140" class="line" />
  <line x1="200" y1="20" x2="200" y2="180" class="line" />
  <text x="30" y="45" class="header">Element</text>
  <text x="210" y="45" class="header">Symbol</text>
  <text x="30" y="85" class="text">Carbon</text>
  <text x="30" y="125" class="text">Oxygen</text>
  <text x="30" y="165" class="text">Sodium</text>
</svg>"""

def write_and_copy_svg(filename, content):
    p1 = f"public/assets/{filename}"
    p2 = f"electron/app/assets/{filename}"
    with open(p1, 'w') as f:
        f.write(content)
    shutil.copy(p1, p2)

write_and_copy_svg('kjsea_science_2025_q30.svg', q30_svg)
write_and_copy_svg('kjsea_science_2025_q31.svg', q31_svg)
write_and_copy_svg('kjsea_science_2025_q32.svg', q32_svg)
write_and_copy_svg('kjsea_science_2025_q33.svg', q33_svg_fixed)

# Handle Q34 Image
src_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\9d39c76d-2c71-4969-8f52-1885f6f7bfde\.user_uploaded\media_1787401015116.png"
if os.path.exists(src_img):
    shutil.copy(src_img, "public/assets/kjsea_science_2025_q34.png")
    shutil.copy(src_img, "electron/app/assets/kjsea_science_2025_q34.png")

# Update JSON for Section A (Q30)
with open('public/data/kjsea-science-sectiona-2025.json', 'r') as f:
    data_a = json.load(f)
for q in data_a.get('sectionA', []):
    if q['id'] == 'q30':
        q['imagePath'] = "/assets/kjsea_science_2025_q30.svg"
with open('public/data/kjsea-science-sectiona-2025.json', 'w') as f:
    json.dump(data_a, f, indent=2)
shutil.copy('public/data/kjsea-science-sectiona-2025.json', 'electron/app/data/kjsea-science-sectiona-2025.json')

# Update JSON for Section B (Q31, Q32, Q33, Q34)
with open('public/data/kjsea-science-sectionb-2025.json', 'r') as f:
    data_b = json.load(f)
for q in data_b.get('sectionB', []):
    if q['id'] == 'q31':
        # Add to subquestion b if possible, or main q
        for sub in q.get('subQuestions', []):
            if sub['id'] == 'q31b':
                sub['imagePath'] = "/assets/kjsea_science_2025_q31.svg"
    elif q['id'] == 'q32':
        for sub in q.get('subQuestions', []):
            if sub['id'] == 'q32a':
                sub['imagePath'] = "/assets/kjsea_science_2025_q32.svg"
    elif q['id'] == 'q33':
        for sub in q.get('subQuestions', []):
            if sub['id'] == 'q33a':
                sub['imagePath'] = "/assets/kjsea_science_2025_q33.svg"
    elif q['id'] == 'q34':
        q['imagePath'] = "/assets/kjsea_science_2025_q34.png"

with open('public/data/kjsea-science-sectionb-2025.json', 'w') as f:
    json.dump(data_b, f, indent=2)
shutil.copy('public/data/kjsea-science-sectionb-2025.json', 'electron/app/data/kjsea-science-sectionb-2025.json')

print("Phase 1 completed!")
