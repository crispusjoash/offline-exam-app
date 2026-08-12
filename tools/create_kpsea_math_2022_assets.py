import os

assets_dir = 'public/assets'
os.makedirs(assets_dir, exist_ok=True)

# 1. Q6 SVG Diagram: Rectangle + Triangle
q6_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <!-- Rectangle -->
  <rect x="50" y="50" width="160" height="120" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>
  
  <!-- Triangle -->
  <polygon points="210,50 440,110 210,170" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>
  
  <!-- Right Angle Markers -->
  <polyline points="50,65 65,65 65,50" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <polyline points="195,170 195,155 210,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <polyline points="210,125 225,125 225,110" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  
  <!-- Height Dotted Line -->
  <line x1="210" y1="110" x2="440" y2="110" stroke="#0f172a" stroke-width="2" stroke-dasharray="6,4"/>
  
  <!-- Labels -->
  <text x="25" y="115" font-family="Outfit, Inter, sans-serif" font-size="18" font-weight="700" fill="#0f172a">4 m</text>
  <text x="120" y="200" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="18" font-weight="700" fill="#0f172a">5 m</text>
  <text x="310" y="100" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="18" font-weight="700" fill="#0f172a">8 m</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q6.svg'), 'w', encoding='utf-8') as f:
    f.write(q6_svg)


# 2. Q13 SVG Diagram: Slanted Line AB
q13_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 180" width="100%" height="100%">
  <!-- Slanted Line Segment -->
  <line x1="60" y1="140" x2="430" y2="40" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Endpoint Markers -->
  <circle cx="60" cy="140" r="4" fill="#0f172a"/>
  <circle cx="430" cy="40" r="4" fill="#0f172a"/>
  
  <!-- Labels A and B -->
  <text x="50" y="165" font-family="Outfit, Inter, sans-serif" font-size="22" font-weight="800" fill="#0f172a">A</text>
  <text x="440" y="35" font-family="Outfit, Inter, sans-serif" font-size="22" font-weight="800" fill="#0f172a">B</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q13.svg'), 'w', encoding='utf-8') as f:
    f.write(q13_svg)


# 3. Q19 SVG Diagram: Clean Vector Timetable
q19_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="100%" height="100%">
  <!-- Table Outer Box -->
  <rect x="20" y="20" width="460" height="160" fill="#ffffff" stroke="#0f172a" stroke-width="2" rx="8"/>
  
  <!-- Header Row Fill -->
  <path d="M 20 20 L 480 20 L 480 60 L 20 60 Z" fill="#f1f5f9"/>
  
  <!-- Horizontal Grid Lines -->
  <line x1="20" y1="60" x2="480" y2="60" stroke="#0f172a" stroke-width="2"/>
  <line x1="20" y1="100" x2="480" y2="100" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="20" y1="140" x2="480" y2="140" stroke="#cbd5e1" stroke-width="1.5"/>
  
  <!-- Vertical Grid Lines -->
  <line x1="140" y1="20" x2="140" y2="180" stroke="#0f172a" stroke-width="2"/>
  <line x1="310" y1="20" x2="310" y2="180" stroke="#0f172a" stroke-width="2"/>
  
  <!-- Header Text -->
  <text x="80" y="46" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="17" font-weight="800" fill="#0f172a">Town</text>
  <text x="225" y="46" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="17" font-weight="800" fill="#0f172a">Arrival time</text>
  <text x="395" y="46" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="17" font-weight="800" fill="#0f172a">Departure time</text>
  
  <!-- Row 1: Town P -->
  <text x="80" y="86" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="700" fill="#0f172a">P</text>
  <text x="225" y="86" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" fill="#94a3b8">—</text>
  <text x="395" y="86" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">9.00 a.m.</text>
  
  <!-- Row 2: Town Q -->
  <text x="80" y="126" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="700" fill="#0f172a">Q</text>
  <text x="225" y="126" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">11.30 a.m.</text>
  <text x="395" y="126" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">12 noon</text>
  
  <!-- Row 3: Town R -->
  <text x="80" y="166" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="700" fill="#0f172a">R</text>
  <text x="225" y="166" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" font-weight="600" fill="#0f172a">3.30 p.m.</text>
  <text x="395" y="166" text-anchor="middle" font-family="Outfit, Inter, sans-serif" font-size="16" fill="#94a3b8">—</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q19.svg'), 'w', encoding='utf-8') as f:
    f.write(q19_svg)

print("Created SVGs for Q6, Q13, and Q19!")
