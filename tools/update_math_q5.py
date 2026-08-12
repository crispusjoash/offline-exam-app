import json
import re

svg_content = """<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label { font-family: 'Times New Roman', serif; font-size: 18px; font-weight: bold; fill: #4a423f; }
    .line { stroke: #4a423f; stroke-width: 2; fill: none; }
  </style>

  <!-- Labels -->
  <text x="200" y="35" text-anchor="middle" class="label">20 cm</text>
  <text x="200" y="270" text-anchor="middle" class="label">20 cm</text>
  <text x="45" y="155" text-anchor="middle" class="label">18 cm</text>
  <text x="355" y="155" text-anchor="middle" class="label">18 cm</text>

  <!-- Rectangle -->
  <rect x="80" y="50" width="240" height="200" class="line" />
  
  <!-- Diagonal -->
  <line x1="80" y1="50" x2="320" y2="250" class="line" />

  <!-- Flowers Pattern -->
  <defs>
    <g id="flower">
      <circle cx="0" cy="-3" r="2.5" fill="none" stroke="#4a423f" stroke-width="1.5" />
      <circle cx="0" cy="3" r="2.5" fill="none" stroke="#4a423f" stroke-width="1.5" />
      <circle cx="-3" cy="0" r="2.5" fill="none" stroke="#4a423f" stroke-width="1.5" />
      <circle cx="3" cy="0" r="2.5" fill="none" stroke="#4a423f" stroke-width="1.5" />
    </g>
  </defs>

  <!-- Flowers in the bottom-left triangle -->
  <use href="#flower" x="95" y="90" />
  <use href="#flower" x="120" y="110" />
  <use href="#flower" x="95" y="135" />
  
  <use href="#flower" x="135" y="130" />
  <use href="#flower" x="155" y="145" />
  
  <use href="#flower" x="105" y="170" />
  <use href="#flower" x="130" y="175" />
  <use href="#flower" x="160" y="180" />
  <use href="#flower" x="185" y="170" />
  
  <use href="#flower" x="95" y="205" />
  <use href="#flower" x="125" y="200" />
  <use href="#flower" x="150" y="210" />
  <use href="#flower" x="180" y="205" />
  <use href="#flower" x="205" y="195" />
  <use href="#flower" x="225" y="205" />
  
  <use href="#flower" x="110" y="235" />
  <use href="#flower" x="140" y="230" />
  <use href="#flower" x="170" y="235" />
  <use href="#flower" x="195" y="230" />
  <use href="#flower" x="220" y="235" />
  <use href="#flower" x="245" y="225" />
  <use href="#flower" x="270" y="235" />
  <use href="#flower" x="290" y="230" />

  <use href="#flower" x="250" y="205" />

</svg>
"""

with open("public/assets/math_2025_q5.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# Add shared context
data["sharedContexts"]["ctx-math-2025-q5"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q5.svg",
    "title": "Decorated Rectangular Mat",
    "cssFilter": "none",
    "scanEffect": False
}

data["sharedContexts"]["ctx-math-2025-q22"] = {
    "type": "image",
    "imagePath": "/assets/math_2025_q22.svg",
    "title": "Triangle Angle",
    "cssFilter": "none",
    "scanEffect": False
}

# Update question 5 and 22
for q in data["sectionA"]:
    if q["id"] == "q5":
        q["contextRef"] = "ctx-math-2025-q5"
        q["questionText"] = "The following figure represents a rectangular table mat. A part of the mat is decorated with flowers."
        q["explanation"] = "The decorated part is a right-angled triangle with base $20\\text{ cm}$ and height $18\\text{ cm}$. Area = $\\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 20 \\times 18 = 180\\text{ cm}^2$."
    if q["id"] == "q22":
        q["contextRef"] = "ctx-math-2025-q22"
        q["questionText"] = "The following figure shows a triangle drawn accurately. A learner used a protractor to measure the angle marked r.\n\nWhat is the size of angle r?"
        
svg_content_q22 = """<svg width="400" height="250" viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label { font-family: 'Times New Roman', serif; font-size: 26px; font-weight: normal; fill: #4a423f; }
    .line { stroke: #4a423f; stroke-width: 2.5; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  </style>
  
  <polygon points="50,220 350,220 150,50" class="line" />
  
  <!-- Arc for angle r -->
  <path d="M 85 220 A 35 35 0 0 0 102 140" class="line" />
  <!-- Wait, angle r is at the bottom left vertex (50,220). Let's trace it.
       The line goes from (50,220) to (350,220) (angle 0)
       and from (50,220) to (150,50) (dx=100, dy=-170 => angle is roughly 60 degrees. (tan 60 = 1.732))
       So an arc of radius 40 from the bottom line to the slanted line:
       Bottom line point: (90, 220)
       Slanted line point: (50 + 40*cos(60), 220 - 40*sin(60)) = (50 + 20, 220 - 34.6) = (70, 185.4)
  -->
  <path d="M 95 220 A 45 45 0 0 0 73 143.5" class="line" />
  <!-- Wait, 45 radius:
       cos(59.5 degrees) ~ 0.5. 50 + 45*0.5 = 72.5
       sin(59.5 degrees) ~ 0.86. 220 - 45*0.86 = 181.3
  -->
  <!-- Let's just use a simple path for the arc -->
  <path d="M 100 220 Q 98 185 75 178" class="line" />
  
  <text x="105" y="195" class="label">r</text>

</svg>
"""

with open("public/assets/math_2025_q22.svg", "w", encoding="utf-8") as f:
    f.write(svg_content_q22)

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SVG created and linked for Q5 and Q22")
