import json
import shutil
import os
import re

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="100%" height="100%">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#3B82F6"/>
    </marker>
  </defs>
  
  <style>
    .box { fill: #f8fafc; stroke: #3B82F6; stroke-width: 2px; rx: 8px; }
    .text { font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 600; fill: #0f172a; text-anchor: middle; dominant-baseline: middle; }
    .label { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 500; fill: #64748b; text-anchor: middle; }
    .line { stroke: #3B82F6; stroke-width: 2.5px; fill: none; marker-end: url(#arrow); }
  </style>

  <!-- Chain 1 -->
  <rect class="box" x="20" y="30" width="100" height="40"/>
  <text class="text" x="70" y="50">Plants</text>
  <text class="label" x="70" y="85">Producer</text>

  <path class="line" d="M 120 50 L 160 50"/>

  <rect class="box" x="170" y="30" width="100" height="40"/>
  <text class="text" x="220" y="50">Rat</text>
  <text class="label" x="220" y="85">Primary Cons.</text>

  <path class="line" d="M 270 50 L 310 50"/>

  <rect class="box" x="320" y="30" width="100" height="40"/>
  <text class="text" x="370" y="50">Snake</text>
  <text class="label" x="370" y="85">Secondary Cons.</text>

  <path class="line" d="M 420 50 L 460 50"/>

  <rect class="box" x="470" y="30" width="100" height="40"/>
  <text class="text" x="520" y="50">Hawk</text>
  <text class="label" x="520" y="85">Tertiary Cons.</text>

  <!-- Divider -->
  <line x1="20" y1="105" x2="570" y2="105" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="6,6" />

  <!-- Chain 2 -->
  <rect class="box" x="20" y="125" width="100" height="40"/>
  <text class="text" x="70" y="145">Plants</text>

  <path class="line" d="M 120 145 L 160 145"/>

  <rect class="box" x="170" y="125" width="100" height="40"/>
  <text class="text" x="220" y="145">Gazelle</text>

  <path class="line" d="M 270 145 L 310 145"/>

  <rect class="box" x="320" y="125" width="100" height="40"/>
  <text class="text" x="370" y="145">Snake</text>

  <path class="line" d="M 420 145 L 460 145"/>

  <rect class="box" x="470" y="125" width="100" height="40"/>
  <text class="text" x="520" y="145">Hawk</text>
</svg>"""

with open('public/assets/kjsea_science_2025_q36_model.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
with open('electron/app/assets/kjsea_science_2025_q36_model.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('sectionB', []):
    if q.get('id') == 'q36':
        for sub in q.get('subQuestions', []):
            if sub.get('id') == 'q36ai':
                # Add the modelImage
                sub['modelImage'] = '/assets/kjsea_science_2025_q36_model.svg'
                # Also fix the corrupted arrows while we are at it
                sub['modelAnswer'] = sub['modelAnswer'].replace('â†’', '→')

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)
    
shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')

print("Created SVG and updated Q36a(i) modelAnswer!")
