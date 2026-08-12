import os

assets_dir = 'public/assets'

# Q19 SVG matching exact exam table format:
# Columns: Town (width ~90), Arrival time (width ~180), Departure time (width ~180)
# Headers: Town, Arrival time, Departure time (Bold)
# Rows:
# P | [blank] | 9.00 a.m.
# Q | 11.30 a.m. | 12 noon
# R | 3.30 p.m. | [blank]

q19_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 160" width="100%" height="100%">
  <!-- Table Outer Box -->
  <rect x="10" y="10" width="440" height="140" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Horizontal Lines -->
  <line x1="10" y1="45" x2="450" y2="45" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="10" y1="80" x2="450" y2="80" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="10" y1="115" x2="450" y2="115" stroke="#1e293b" stroke-width="1.5"/>
  
  <!-- Vertical Lines -->
  <line x1="100" y1="10" x2="100" y2="150" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="270" y1="10" x2="270" y2="150" stroke="#1e293b" stroke-width="1.5"/>
  
  <!-- Header Row -->
  <text x="22" y="34" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="800" fill="#0f172a">Town</text>
  <text x="112" y="34" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="800" fill="#0f172a">Arrival time</text>
  <text x="282" y="34" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="800" fill="#0f172a">Departure time</text>
  
  <!-- Row 1: P -->
  <text x="22" y="69" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="600" fill="#0f172a">P</text>
  <!-- Arrival is blank -->
  <text x="282" y="69" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">9.00 a.m.</text>
  
  <!-- Row 2: Q -->
  <text x="22" y="104" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="600" fill="#0f172a">Q</text>
  <text x="112" y="104" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">11.30 a.m.</text>
  <text x="282" y="104" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">12 noon</text>
  
  <!-- Row 3: R -->
  <text x="22" y="139" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="600" fill="#0f172a">R</text>
  <text x="112" y="139" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">3.30 p.m.</text>
  <!-- Departure is blank -->
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q19.svg'), 'w', encoding='utf-8') as f:
    f.write(q19_svg)


# Q22 SVG matching exact exam table format:
# Columns: Item (width ~260), Cost (width ~180)
# Headers: Item, Cost (Bold)
# Rows:
# 1 kg sugar | sh 110
# 1 litre cooking oil | sh 360
# 2 kg packet maize flour | sh 105

q22_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 160" width="100%" height="100%">
  <!-- Table Outer Box -->
  <rect x="10" y="10" width="440" height="140" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Horizontal Lines -->
  <line x1="10" y1="45" x2="450" y2="45" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="10" y1="80" x2="450" y2="80" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="10" y1="115" x2="450" y2="115" stroke="#1e293b" stroke-width="1.5"/>
  
  <!-- Vertical Line -->
  <line x1="270" y1="10" x2="270" y2="150" stroke="#1e293b" stroke-width="1.5"/>
  
  <!-- Header Row -->
  <text x="22" y="34" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="800" fill="#0f172a">Item</text>
  <text x="282" y="34" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="800" fill="#0f172a">Cost</text>
  
  <!-- Row 1 -->
  <text x="22" y="69" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">1 kg sugar</text>
  <text x="282" y="69" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">sh 110</text>
  
  <!-- Row 2 -->
  <text x="22" y="104" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">1 litre cooking oil</text>
  <text x="282" y="104" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">sh 360</text>
  
  <!-- Row 3 -->
  <text x="22" y="139" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">2 kg packet maize flour</text>
  <text x="282" y="139" font-family="Outfit, Inter, Arial, sans-serif" font-size="16" font-weight="500" fill="#0f172a">sh 105</text>
</svg>
"""

with open(os.path.join(assets_dir, 'kpsea_math_2022_q22.svg'), 'w', encoding='utf-8') as f:
    f.write(q22_svg)

print("Redrew SVG tables for Q19 and Q22 to match exact exam paper format!")
