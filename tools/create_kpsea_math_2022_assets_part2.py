import os

assets_dir = 'public/assets'
os.makedirs(assets_dir, exist_ok=True)

# 1. Q22 SVG Table (Price List)
q22_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 180" width="100%" height="100%">
  <rect x="20" y="20" width="460" height="140" fill="#ffffff" stroke="#0f172a" stroke-width="2" rx="8"/>
  <path d="M 20 20 L 480 20 L 480 55 L 20 55 Z" fill="#f1f5f9"/>
  <line x1="20" y1="55" x2="480" y2="55" stroke="#0f172a" stroke-width="2"/>
  <line x1="20" y1="90" x2="480" y2="90" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="20" y1="125" x2="480" y2="125" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="280" y1="20" x2="280" y2="160" stroke="#0f172a" stroke-width="2"/>
  
  <text x="150" y="43" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="17" font-weight="800" fill="#0f172a">Item</text>
  <text x="380" y="43" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="17" font-weight="800" fill="#0f172a">Cost</text>
  
  <text x="40" y="78" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">1 kg sugar</text>
  <text x="380" y="78" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">sh 110</text>
  
  <text x="40" y="113" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">1 litre cooking oil</text>
  <text x="380" y="113" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">sh 360</text>
  
  <text x="40" y="148" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">2 kg packet maize flour</text>
  <text x="380" y="148" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">sh 105</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q22.svg'), 'w', encoding='utf-8') as f:
    f.write(q22_svg)


# 2. Q25 SVG Diagram (Triangles PQS and SQR)
q25_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <!-- Triangle PQS and Triangle SQR -->
  <polygon points="40,90 110,180 240,40" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>
  <polygon points="110,180 240,40 460,180" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>
  
  <!-- Labels P, Q, S, R -->
  <text x="20" y="90" font-family="Outfit, Inter, sans-serif" font-size="20" font-weight="800" fill="#0f172a">P</text>
  <text x="100" y="205" font-family="Outfit, Inter, sans-serif" font-size="20" font-weight="800" fill="#0f172a">Q</text>
  <text x="240" y="28" font-family="Outfit, Inter, sans-serif" font-size="20" font-weight="800" fill="#0f172a">S</text>
  <text x="470" y="195" font-family="Outfit, Inter, sans-serif" font-size="20" font-weight="800" fill="#0f172a">R</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q25.svg'), 'w', encoding='utf-8') as f:
    f.write(q25_svg)


# 3. Q28 SVG Bar Graph
q28_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 320" width="100%" height="100%">
  <!-- Background Grid -->
  <rect x="70" y="30" width="430" height="220" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
  
  <!-- Horizontal Grid Lines -->
  <line x1="70" y1="85" x2="500" y2="85" stroke="#e2e8f0" stroke-width="1.5"/>
  <line x1="70" y1="140" x2="500" y2="140" stroke="#e2e8f0" stroke-width="1.5"/>
  <line x1="70" y1="195" x2="500" y2="195" stroke="#e2e8f0" stroke-width="1.5"/>
  
  <!-- Y-Axis Labels -->
  <text x="55" y="35" text-anchor="end" font-family="Outfit, sans-serif" font-size="14" font-weight="700" fill="#0f172a">800</text>
  <text x="55" y="90" text-anchor="end" font-family="Outfit, sans-serif" font-size="14" font-weight="700" fill="#0f172a">600</text>
  <text x="55" y="145" text-anchor="end" font-family="Outfit, sans-serif" font-size="14" font-weight="700" fill="#0f172a">400</text>
  <text x="55" y="200" text-anchor="end" font-family="Outfit, sans-serif" font-size="14" font-weight="700" fill="#0f172a">200</text>
  <text x="55" y="255" text-anchor="end" font-family="Outfit, sans-serif" font-size="14" font-weight="700" fill="#0f172a">0</text>
  
  <!-- Axis Titles -->
  <text x="25" y="130" text-anchor="middle" font-family="Outfit, sans-serif" font-size="14" font-weight="800" fill="#0f172a" transform="rotate(-90 25 130)">Number of trees</text>
  <text x="285" y="295" text-anchor="middle" font-family="Outfit, sans-serif" font-size="15" font-weight="800" fill="#0f172a">Years</text>
  
  <!-- Bars -->
  <!-- 2017: 300 trees (height = 300/800 * 220 = 82.5, y = 250 - 82.5 = 167.5) -->
  <rect x="95" y="167.5" width="75" height="82.5" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>
  
  <!-- 2018: 200 trees (height = 200/800 * 220 = 55, y = 250 - 55 = 195) -->
  <rect x="195" y="195" width="75" height="55" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>
  
  <!-- 2019: 800 trees (height = 800/800 * 220 = 220, y = 30) -->
  <rect x="295" y="30" width="75" height="220" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>
  
  <!-- 2020: 700 trees (height = 700/800 * 220 = 192.5, y = 250 - 192.5 = 57.5) -->
  <rect x="395" y="57.5" width="75" height="192.5" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>
  
  <!-- X-Axis Labels -->
  <text x="132.5" y="272" text-anchor="middle" font-family="Outfit, sans-serif" font-size="15" font-weight="700" fill="#0f172a">2017</text>
  <text x="232.5" y="272" text-anchor="middle" font-family="Outfit, sans-serif" font-size="15" font-weight="700" fill="#0f172a">2018</text>
  <text x="332.5" y="272" text-anchor="middle" font-family="Outfit, sans-serif" font-size="15" font-weight="700" fill="#0f172a">2019</text>
  <text x="432.5" y="272" text-anchor="middle" font-family="Outfit, sans-serif" font-size="15" font-weight="700" fill="#0f172a">2020</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q28.svg'), 'w', encoding='utf-8') as f:
    f.write(q28_svg)

print("Created SVGs for Q22, Q25, and Q28!")
