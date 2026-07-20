"""
Final fix: read pastPapers.js, find all broken multi-line explanation strings,
and collapse them to single-line \n-escaped JS strings.
Then write the correct explanations.
"""
import re, sys

with open("src/data/pastPapers.js", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: collapse ALL explanation strings (multi-line -> single-line)
# Strategy: find  explanation: "..."  where the string may span lines
# We do it character by character to handle edge cases
def collapse_all_explanations(content):
    result = []
    i = 0
    n = len(content)
    while i < n:
        # Look for:  explanation: "
        if content[i:i+14] == 'explanation: "':
            result.append('explanation: "')
            i += 14
            # Now consume until the closing unescaped "
            while i < n:
                ch = content[i]
                if ch == '\\':
                    result.append(ch)
                    i += 1
                    if i < n:
                        result.append(content[i])
                        i += 1
                elif ch == '"':
                    result.append('"')
                    i += 1
                    break
                elif ch == '\r':
                    # skip \r
                    i += 1
                elif ch == '\n':
                    result.append('\\n')
                    i += 1
                else:
                    result.append(ch)
                    i += 1
        else:
            result.append(content[i])
            i += 1
    return ''.join(result)

content = collapse_all_explanations(content)

# Step 2: now write correct explanations per question id
EXPS = {
    "q1":  "1. Write out the number: **84,072**\\n2. Break it into groups: 84 thousands, 0 hundreds, 7 tens, 2 ones.\\n3. Zero hundreds means we skip that part entirely.\\n4. Read it as: **Eighty four thousand and seventy two**.",
    "q2":  "1. Write out the number: **436,587**\\n2. Identify the digit **6** and find its position.\\n3. Counting from the right: ones, tens, hundreds, thousands — the 6 is in the **thousands** place.\\n4. Multiply: $6 \\\\times 1000 = 6000$.",
    "q3":  "1. Total seedlings in the nursery: **368,593**\\n2. Seedlings bought by customers: **27,364**\\n3. Subtract to find what remained: $368{,}593 - 27{,}364 = 341{,}229$",
    "q4":  "1. The number to round is **19,468**.\\n2. We are rounding to the nearest **thousand**, so look at the hundreds digit.\\n3. The hundreds digit is **4**, which is less than 5.\\n4. Since 4 < 5, we round **down** — replace everything after the thousands with zeros.\\n5. The answer is **19,000**.",
    "q5":  "1. Look at the pattern: $8,\\\\ 24,\\\\ 72,\\\\ 216,\\\\ ?$\\n2. Check the rule: $8 \\\\times 3 = 24$, $24 \\\\times 3 = 72$, $72 \\\\times 3 = 216$.\\n3. The pattern is **multiply by 3** each time.\\n4. Apply the rule: $216 \\\\times 3 = 648$.",
    "q6":  "1. The expression is: $24 \\\\div 3 + 9 \\\\times 6 - 4$\\n2. Apply **BODMAS** — Division and Multiplication before Addition and Subtraction.\\n3. Division first: $24 \\\\div 3 = 8$\\n4. Multiplication next: $9 \\\\times 6 = 54$\\n5. Rewrite the expression: $8 + 54 - 4$\\n6. Add and subtract left to right: $62 - 4 = 58$",
    "q7":  "1. Fraction spent on food: $\\\\dfrac{2}{5}$\\n2. Fraction spent on rent: $\\\\dfrac{1}{4}$\\n3. Find the LCM of 5 and 4, which is **20**.\\n4. Convert both: $\\\\dfrac{2}{5} = \\\\dfrac{8}{20}$ and $\\\\dfrac{1}{4} = \\\\dfrac{5}{20}$\\n5. Add them: $\\\\dfrac{8}{20} + \\\\dfrac{5}{20} = \\\\dfrac{13}{20}$",
    "q8":  "1. The expression is: $9\\\\dfrac{5}{6} - 1\\\\dfrac{1}{3}$\\n2. Find the LCM of 6 and 3, which is **6**.\\n3. Convert $1\\\\dfrac{1}{3}$ to sixths: $1\\\\dfrac{2}{6}$\\n4. Subtract whole numbers: $9 - 1 = 8$\\n5. Subtract fractions: $\\\\dfrac{5}{6} - \\\\dfrac{2}{6} = \\\\dfrac{3}{6}$\\n6. Simplify: $\\\\dfrac{3}{6} = \\\\dfrac{1}{2}$\\n7. Final answer: $8\\\\dfrac{1}{2}$",
    "q9":  "1. Total beads = **100%**\\n2. Red beads = **25%**\\n3. Green beads = $100\\\\% - 25\\\\% = 75\\\\%$\\n4. Convert to decimal: $75 \\\\div 100 = 0.75$",
    "q10": "1. The question asks for fabric used on **shirt and dress** combined.\\n2. Shirt: **0.287**, Dress: **0.45**\\n3. Add: $0.287 + 0.450 = 0.737$\\n4. The fabric for shorts (0.263) is not needed here.",
    "q11": "1. The increase in height is **5 cm**.\\n2. Recall: $1 \\\\text{ cm} = 10 \\\\text{ mm}$\\n3. Multiply: $5 \\\\times 10 = 50 \\\\text{ mm}$",
    "q12": "1. Perimeter = total distance around the **outside** of the shape.\\n2. Identify the outer side lengths from the diagram: 15 cm, 15 cm, 10 cm, 10 cm, and 8 cm.\\n3. Add all outer sides: $15 + 15 + 10 + 10 + 8 = 58 \\\\text{ cm}$",
    "q13": "1. Total ribbon length: **31 cm 6 mm**\\n2. Length cut off: **5 cm 3 mm**\\n3. Subtract the millimetres: $6 - 3 = 3 \\\\text{ mm}$\\n4. Subtract the centimetres: $31 - 5 = 26 \\\\text{ cm}$\\n5. Remaining ribbon: **26 cm 3 mm**",
    "q14": "1. The wall is made of a **rectangle** and a **triangle**.\\n2. Area of rectangle $= 65 \\\\times 74 = 4{,}810 \\\\text{ cm}^2$\\n3. Area of triangle $= \\\\dfrac{1}{2} \\\\times 65 \\\\times 24 = 780 \\\\text{ cm}^2$\\n4. Total area $= 4{,}810 + 780 = 5{,}590 \\\\text{ cm}^2$",
    "q15": "1. Kimeto drinks **3.7 litres** per day.\\n2. Recall: $1 \\\\text{ litre} = 1000 \\\\text{ ml}$\\n3. Multiply: $3.7 \\\\times 1000 = 3{,}700 \\\\text{ ml}$",
    "q16": "1. Mass of sand: **18 tonnes 481 kg**\\n2. Mass of small stones: **12 tonnes 394 kg**\\n3. Add kilograms: $481 + 394 = 875 \\\\text{ kg}$\\n4. Add tonnes: $18 + 12 = 30 \\\\text{ tonnes}$\\n5. Total mass: **30 tonnes 875 kilograms**",
    "q17": "1. Number of lorries: **4**, each carrying **24 tonnes 235 kg**.\\n2. Multiply kilograms: $235 \\\\times 4 = 940 \\\\text{ kg}$\\n3. Multiply tonnes: $24 \\\\times 4 = 96 \\\\text{ tonnes}$\\n4. Total mass distributed: **96 tonnes 940 kilograms**",
    "q18": "1. Mass of flowers exported: **4,850,000 kg**\\n2. Recall: $1 \\\\text{ tonne} = 1000 \\\\text{ kg}$\\n3. To convert kg to tonnes, divide by 1000.\\n4. $4{,}850{,}000 \\\\div 1000 = 4{,}850 \\\\text{ tonnes}$",
    "q19": "1. Look at the **short hand** (hour hand) — it points between **2 and 3**, so the hour is **2**.\\n2. Look at the **long hand** (minute hand) — it points to **7**, meaning $7 \\\\times 5 = 35$ minutes.\\n3. The time reads **2:35**.\\n4. The question states he performed **in the afternoon**.\\n5. Therefore the time is **2.35 p.m.**",
    "q20": "1. The train **departs Manga** at **6.15 a.m.**\\n2. The train **arrives at Pate** at **11.54 a.m.**\\n3. Subtract hours: $11 - 6 = 5$ hours.\\n4. Subtract minutes: $54 - 15 = 39$ minutes.\\n5. Journey duration: **5 hours 39 minutes**",
    "q21": "1. Selling Price = **sh 1,675**\\n2. Profit made = **sh 390**\\n3. Formula: $\\\\text{Buying Price} = \\\\text{Selling Price} - \\\\text{Profit}$\\n4. $1{,}675 - 390 = 1{,}285$\\n5. Buying Price = **sh 1,285**",
    "q22": "1. Area of the paper = $72 \\\\text{ cm}^2$, Length = **9 cm**.\\n2. Find Width: $\\\\text{Width} = \\\\dfrac{72}{9} = 8 \\\\text{ cm}$\\n3. Convert to mm ($1 \\\\text{ cm} = 10 \\\\text{ mm}$): $8 \\\\times 10 = 80 \\\\text{ mm}$",
    "q23": "1. Place the **centre mark** of the protractor exactly on vertex **M**.\\n2. Align the **baseline (0 degrees line)** of the protractor along line segment **LM**.\\n3. Look at where line **MN** crosses the curved scale of the protractor.\\n4. Read the scale starting at **0 degrees** from LM — it crosses at **40 degrees**.\\n5. Angle LMN = **40 degrees**",
    "q24": "1. The 3-D object shown is a **cuboid**.\\n2. The **dotted lines** indicate it is an **open cuboid** (no lid) — it has 5 faces instead of 6.\\n3. However, the question asks for the number of **edges**, not faces.\\n4. Count the frame edges: 4 at the base + 4 vertical + 4 at the top opening.\\n5. Total edges = **12**",
    "q25": "1. **Parallel lines** are lines that are always the same distance apart and never meet.\\n2. Pieces **n** (top horizontal) and **q** (bottom horizontal) run in exactly the same direction.\\n3. They are on opposite sides of the frame — they will never intersect.\\n4. Piece **r** is diagonal and crosses other pieces, so it is not parallel to any horizontal piece.\\n5. The correct answer is **n and q**.",
    "q26": "1. Find the bar for **Wednesday** on the horizontal axis.\\n2. Follow the top of that bar straight left to the vertical axis.\\n3. The bar stops exactly halfway between **1500** and **2000**.\\n4. Calculate: $1500 + \\\\dfrac{500}{2} = 1500 + 250 = 1{,}750$\\n5. Amount received on Wednesday = **sh 1,750**",
    "q27": "1. A **cylinder** has circular faces — not square faces.\\n2. A **cube** has square faces — not just rectangular.\\n3. A **cuboid** has rectangular faces — not circular.\\n4. A **pyramid** has a polygonal base and **triangular side faces** that all meet at a single apex.\\n5. The correct statement is: **A pyramid has a triangular face**.",
    "q28": "1. Count the tally marks carefully for each disease.\\n2. **Malaria**: Given directly = **12 patients**.\\n3. **Diabetes**: Four tally strokes (////) = **4 patients**.\\n4. **Tuberculosis**: One bundle of 5 + 1 extra = $5 + 1 = 6$ **patients**.\\n5. **HIV/AIDS**: Given directly = **8 patients**.\\n6. Total: $12 + 4 + 6 + 8 = 30$ **patients**",
    "q29": "1. Let $p$ = the original number of oranges Ngei had.\\n2. After giving out 4, he was left with $p - 4$.\\n3. He remained with **more than 6** oranges.\\n4. 'More than' is the **greater than** symbol: >\\n5. The correct inequality is: $p - 4 > 6$",
    "q30": "1. Let $x$ = the total amount of money to be shared.\\n2. Shared equally among **50 women**, so each receives $\\\\dfrac{x}{50}$.\\n3. Each woman received **sh 8,500**.\\n4. The correct equation is: $\\\\dfrac{x}{50} = 8500$",
}

for q_id, exp in EXPS.items():
    pattern = r'(id:\s*"' + re.escape(q_id) + r'"(?:(?!id:\s*").)*?explanation:\s*)"[^"]*"'
    replacement = r'\1"' + exp + '"'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content == content:
        print(f"WARNING: No match for {q_id}")
    else:
        content = new_content
        print(f"OK: {q_id}")

with open("src/data/pastPapers.js", "w", encoding="utf-8") as f:
    f.write(content)

print("\nAll done. File saved.")
