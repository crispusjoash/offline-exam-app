import json
import base64

svg_table = """<svg viewBox="0 0 600 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font-weight: bold; font-family: sans-serif; font-size: 14px; }
    .row { font-family: sans-serif; font-size: 14px; }
    .line { stroke: black; stroke-width: 1; }
  </style>
  <rect width="600" height="300" fill="white"/>
  <!-- Vertical lines -->
  <line x1="10" y1="10" x2="10" y2="290" class="line"/>
  <line x1="150" y1="10" x2="150" y2="290" class="line"/>
  <line x1="240" y1="10" x2="240" y2="290" class="line"/>
  <line x1="330" y1="10" x2="330" y2="290" class="line"/>
  <line x1="420" y1="10" x2="420" y2="290" class="line"/>
  <line x1="510" y1="10" x2="510" y2="290" class="line"/>
  <line x1="590" y1="10" x2="590" y2="290" class="line"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="10" x2="590" y2="10" class="line" stroke-width="2"/>
  <line x1="10" y1="50" x2="590" y2="50" class="line" stroke-width="2"/>
  <line x1="10" y1="84" x2="590" y2="84" class="line"/>
  <line x1="10" y1="118" x2="590" y2="118" class="line"/>
  <line x1="10" y1="152" x2="590" y2="152" class="line"/>
  <line x1="10" y1="186" x2="590" y2="186" class="line"/>
  <line x1="10" y1="220" x2="590" y2="220" class="line"/>
  <line x1="10" y1="254" x2="590" y2="254" class="line"/>
  <line x1="10" y1="288" x2="590" y2="288" class="line" stroke-width="2"/>

  <!-- Headers -->
  <text x="20" y="35" class="header">Klabu</text>
  <text x="160" y="35" class="header">Jumatatu</text>
  <text x="250" y="35" class="header">Jumanne</text>
  <text x="340" y="35" class="header">Jumatano</text>
  <text x="430" y="35" class="header">Alhamisi</text>
  <text x="525" y="35" class="header">Ijumaa</text>

  <defs>
    <path id="check" d="M -5 0 L 0 5 L 10 -10" stroke="black" stroke-width="2" fill="none"/>
  </defs>

  <!-- Skauti -->
  <text x="20" y="72" class="row">Skauti</text>
  <use href="#check" x="195" y="70" />
  <use href="#check" x="285" y="70" />
  <use href="#check" x="465" y="70" />

  <!-- Michezo -->
  <text x="20" y="106" class="row">Michezo</text>
  <use href="#check" x="375" y="104" />

  <!-- Densi -->
  <text x="20" y="140" class="row">Densi</text>
  <use href="#check" x="195" y="138" />
  <use href="#check" x="465" y="138" />

  <!-- Majadiliano -->
  <text x="20" y="174" class="row">Majadiliano</text>
  <use href="#check" x="195" y="172" />
  <use href="#check" x="285" y="172" />
  <use href="#check" x="465" y="172" />
  <use href="#check" x="550" y="172" />

  <!-- Kilimo -->
  <text x="20" y="208" class="row">Kilimo</text>
  <use href="#check" x="375" y="206" />
  <use href="#check" x="550" y="206" />

  <!-- Mazingira -->
  <text x="20" y="242" class="row">Mazingira</text>
  <use href="#check" x="195" y="240" />
  <use href="#check" x="285" y="240" />
  <use href="#check" x="375" y="240" />
  <use href="#check" x="465" y="240" />
  <use href="#check" x="550" y="240" />

  <!-- Upishi -->
  <text x="20" y="276" class="row">Upishi</text>
  <use href="#check" x="285" y="274" />
  <use href="#check" x="550" y="274" />
</svg>"""

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

# Fix Q4
for q in data["sectionA"]:
    if q["id"] == "q4":
        q["questionText"] = "Chagua jibu linaloonyesha mfuatano sahihi wa matukio katika kifungu."
        q["questionList"] = [
            "(i) Sonita kuwapigia wazazi simu.",
            "(ii) Sonita kuwaeleza yaliyojiri.",
            "(iii) Sonita kuagana na wenzake.",
            "(iv) Sonita kunyakua mtoto."
        ]

# Encode SVG to Base64
encoded_svg = base64.b64encode(svg_table.encode('utf-8')).decode('utf-8')
markdown_image = f"![Ratiba ya Klabu](data:image/svg+xml;base64,{encoded_svg})"

# Fix Context
data["sharedContexts"]["ctx-kisw-2025-q18-20"]["text"] = "Wanafunzi wa shule ya Junia huwa na ratiba ya Klabu mbalimbali kila siku ya wiki kama ilivyo kwenye jedwali lifuatalo:\n\n" + markdown_image

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
