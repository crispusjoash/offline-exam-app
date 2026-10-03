import json
import os

svg_q41 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="100%" height="100%">
  <!-- White background for visibility -->
  <rect width="100%" height="100%" fill="white" />
  <style>
    .staff { stroke: black; stroke-width: 1.5; }
    .note { fill: transparent; stroke: black; stroke-width: 2.5; }
    .accidental { font-family: serif; font-size: 32px; font-weight: bold; }
    .clef { font-family: serif; font-size: 80px; }
  </style>
  
  <!-- Staff lines (5 lines, spaced 12px apart) -->
  <g transform="translate(50, 70)">
    <line x1="0" y1="0" x2="500" y2="0" class="staff"/>
    <line x1="0" y1="12" x2="500" y2="12" class="staff"/>
    <line x1="0" y1="24" x2="500" y2="24" class="staff"/>
    <line x1="0" y1="36" x2="500" y2="36" class="staff"/>
    <line x1="0" y1="48" x2="500" y2="48" class="staff"/>
    
    <!-- Treble Clef -->
    <text x="10" y="48" class="clef" fill="black">&#119070;</text>

    <!-- Notes (Semibreves / Whole notes) 
         F4 (bottom space) = y=42
         G4 (2nd line up) = y=36
         A4 (2nd space up) = y=30
         Bb4 (3rd line up) = y=24
         C5 (3rd space up) = y=18
         D5 (4th line up) = y=12
         E5 (4th space up) = y=6
         F5 (top line) = y=0
    -->
    <ellipse cx="100" cy="42" rx="7" ry="5" class="note" transform="rotate(-15 100 42)"/>
    <ellipse cx="150" cy="36" rx="7" ry="5" class="note" transform="rotate(-15 150 36)"/>
    <ellipse cx="200" cy="30" rx="7" ry="5" class="note" transform="rotate(-15 200 30)"/>
    
    <!-- Flat sign for Bb -->
    <text x="235" y="32" class="accidental" fill="black">&#9837;</text>
    <ellipse cx="260" cy="24" rx="7" ry="5" class="note" transform="rotate(-15 260 24)"/>
    
    <ellipse cx="310" cy="18" rx="7" ry="5" class="note" transform="rotate(-15 310 18)"/>
    <ellipse cx="360" cy="12" rx="7" ry="5" class="note" transform="rotate(-15 360 12)"/>
    <ellipse cx="410" cy="6" rx="7" ry="5" class="note" transform="rotate(-15 410 6)"/>
    <ellipse cx="460" cy="0" rx="7" ry="5" class="note" transform="rotate(-15 460 0)"/>
  </g>
</svg>"""

svg_q42 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200" width="100%" height="100%">
  <!-- White background for visibility -->
  <rect width="100%" height="100%" fill="white" />
  <style>
    .staff { stroke: black; stroke-width: 1.5; }
    .note { fill: black; }
    .stem { stroke: black; stroke-width: 1.5; }
    .barline { stroke: black; stroke-width: 2; }
    .text { font-family: sans-serif; font-size: 14px; fill: #475569; font-style: italic; }
    .clef { font-family: serif; font-size: 80px; }
    .time { font-family: serif; font-size: 24px; font-weight: bold; }
  </style>
  
  <g transform="translate(40, 80)">
    <!-- 5 lines -->
    <line x1="0" y1="0" x2="620" y2="0" class="staff"/>
    <line x1="0" y1="12" x2="620" y2="12" class="staff"/>
    <line x1="0" y1="24" x2="620" y2="24" class="staff"/>
    <line x1="0" y1="36" x2="620" y2="36" class="staff"/>
    <line x1="0" y1="48" x2="620" y2="48" class="staff"/>
    
    <text x="5" y="48" class="clef" fill="black">&#119070;</text>
    <text x="55" y="22" class="time" fill="black">4</text>
    <text x="55" y="44" class="time" fill="black">4</text>

    <!-- Bar 1: C4 D4 E4 F4 -->
    <circle cx="100" cy="54" r="5" class="note"/>
    <line x1="104" y1="54" x2="104" y2="24" class="stem"/>
    <line x1="94" y1="54" x2="106" y2="54" class="staff"/> <!-- ledger line for C4 -->

    <circle cx="140" cy="48" r="5" class="note"/>
    <line x1="144" y1="48" x2="144" y2="18" class="stem"/>

    <circle cx="180" cy="42" r="5" class="note"/>
    <line x1="184" y1="42" x2="184" y2="12" class="stem"/>

    <circle cx="220" cy="36" r="5" class="note"/>
    <line x1="224" y1="36" x2="224" y2="6" class="stem"/>

    <line x1="250" y1="0" x2="250" y2="48" class="barline"/>
    
    <!-- Bar 2: G4 (Minim) + rest -->
    <ellipse cx="280" cy="30" rx="6" ry="4" fill="transparent" stroke="black" stroke-width="2" transform="rotate(-15 280 30)"/>
    <line x1="285" y1="30" x2="285" y2="0" class="stem"/>
    <!-- Half rest on 3rd line -->
    <rect x="320" y="20" width="12" height="4" fill="black" />

    <line x1="360" y1="0" x2="360" y2="48" class="barline"/>
    <text x="120" y="-20" class="text">Antecedent Phrase</text>

    <!-- Bar 3: A4 G4 F4 E4 -->
    <circle cx="390" cy="24" r="5" class="note"/>
    <line x1="394" y1="24" x2="394" y2="-6" class="stem"/>
    <circle cx="430" cy="30" r="5" class="note"/>
    <line x1="434" y1="30" x2="434" y2="0" class="stem"/>
    <circle cx="470" cy="36" r="5" class="note"/>
    <line x1="474" y1="36" x2="474" y2="6" class="stem"/>
    <circle cx="510" cy="42" r="5" class="note"/>
    <line x1="514" y1="42" x2="514" y2="12" class="stem"/>

    <line x1="540" y1="0" x2="540" y2="48" class="barline"/>

    <!-- Bar 4: C4 (Semibreve) -->
    <ellipse cx="580" cy="54" rx="7" ry="5" fill="transparent" stroke="black" stroke-width="2" transform="rotate(-15 580 54)"/>
    <line x1="570" y1="54" x2="590" y2="54" class="staff"/> <!-- ledger line for C4 -->
    
    <line x1="615" y1="0" x2="615" y2="48" class="barline"/>
    <line x1="620" y1="0" x2="620" y2="48" class="barline" style="stroke-width: 4;" />
    
    <text x="430" y="-20" class="text" fill="#059669">Answering Phrase (Resolves to Tonic)</text>
  </g>
</svg>"""

base_dir = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app"

files = [
    os.path.join(base_dir, "public", "assets", "kjsea_cas_2025_q41_model.svg"),
    os.path.join(base_dir, "electron", "app", "assets", "kjsea_cas_2025_q41_model.svg")
]
for f in files:
    with open(f, "w", encoding="utf-8") as out:
        out.write(svg_q41)

files2 = [
    os.path.join(base_dir, "public", "assets", "kjsea_cas_2025_q42_model.svg"),
    os.path.join(base_dir, "electron", "app", "assets", "kjsea_cas_2025_q42_model.svg")
]
for f in files2:
    with open(f, "w", encoding="utf-8") as out:
        out.write(svg_q42)

# Update JSON
json_path = os.path.join(base_dir, "public", "data", "kjsea-creative-arts-sports-sectionb-2025.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data.get("sectionB", []):
    for sub in q.get("subQuestions", []):
        if sub["id"] == "q41a":
            sub["modelAnswer"] = "/assets/kjsea_cas_2025_q41_model.svg"
        if sub["id"] == "q42a":
            sub["modelAnswer"] = "/assets/kjsea_cas_2025_q42_model.svg"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

json_path2 = os.path.join(base_dir, "electron", "app", "data", "kjsea-creative-arts-sports-sectionb-2025.json")
with open(json_path2, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("SVGs created and JSON updated.")
