import json

file_path = 'src/data/kpsea-math-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Load JSON data
import re
match = re.search(r'export const kpseaMath2022 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()

data = json.loads(match.group(1))

# Detailed, perfectly formatted explanations with robust KaTeX LaTeX
explanations = {
    1: """To write **five hundred and sixty five thousand and fifty two** in symbols:

* **Five hundred and sixty five thousand** = $565,000$
* **Fifty two** = $52$

Combining these gives **565,052**.""",

    2: """Let's identify the place values of each digit in **3,624,817** from right to left:

* **7** → Ones
* **1** → Tens
* **8** → Hundreds
* **4** → Thousands
* **2** → Tens of thousands
* **6** → **Hundreds of thousands**
* **3** → Millions

Therefore, the place value of digit 6 is **Hundreds of thousands**.""",

    3: """To find the number of remaining books, subtract the number bought from the total received:

$$648,205 - 76,102 = 572,103$$

Therefore, **572,103** books remained in the bookshop.""",

    4: """Let's calculate the number of learners step by step:

1. **Girls at the end of the year:**
   $$1,204 + 88 = 1,292\\text{ girls}$$

2. **Boys at the end of the year:**
   $$816 - 12 = 804\\text{ boys}$$

3. **Total learners at the end of the year:**
   $$1,292 + 804 = 2,096\\text{ learners}$$

Therefore, there were **2,096** learners altogether.""",

    5: """To find the total number of textbooks, multiply the number of cartons by the number of textbooks per carton:

$$1,452 \\times 24 = 34,848$$

**Breakdown:**
* $1,452 \\times 20 = 29,040$
* $1,452 \\times 4 = 5,808$
* $29,040 + 5,808 = 34,848$

The lorry carried **34,848** textbooks altogether.""",

    6: """The total area of the drawing is the sum of the area of the rectangle and the area of the triangle:

1. **Area of Rectangle:**
   $$\\text{Area} = \\text{length} \\times \\text{width} = 5\\text{ m} \\times 4\\text{ m} = 20\\text{ m}^2$$

2. **Area of Triangle:**
   $$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 4\\text{ m} \\times 8\\text{ m} = 16\\text{ m}^2$$

3. **Total Area:**
   $$20\\text{ m}^2 + 16\\text{ m}^2 = 36\\text{ m}^2$$

Therefore, the total area of the drawing is **36 m²**.""",

    7: """Let's examine the differences between consecutive terms in the pattern:

* $32 - 30 = +2$
* $36 - 32 = +4$
* $44 - 36 = +8$
* $60 - 44 = +16$

Notice that the difference doubles each time ($+2, +4, +8, +16, +32$).

* **Next difference:** $+32$
* **Next term:** $60 + 32 = 92$

Therefore, the next number in the pattern is **92**.""",

    8: """Let's divide the total number of chicks by 15 members:

$$2,156 \\div 15 = 143\\text{ remainder } 11$$

* Each member receives $143$ chicks, leaving **$11$ chicks** remaining.
* To give everyone one more chick ($144$ chicks each), we need a total of $15$ chicks.
* **Chicks needed:** $15 - 11 = 4\\text{ more chicks}$.

Therefore, the 4K club needs to add **4** more chicks.""",

    9: """Let's solve step by step:

1. **Area of Rectangle:**
   $$\\text{Area} = 24\\text{ cm} \\times 6\\text{ cm} = 144\\text{ cm}^2$$

2. **Side Length of Square:**
   Since the square has the same area:
   $$\\text{Side}^2 = 144\\text{ cm}^2 \\implies \\text{Side} = \\sqrt{144} = 12\\text{ cm}$$

3. **Perimeter of Square:**
   $$\\text{Perimeter} = 4 \\times \\text{side} = 4 \\times 12\\text{ cm} = 48\\text{ cm}$$

Therefore, the perimeter of the square is **48 cm**.""",

    10: """Let's calculate the total fraction contributed first:

1. **Total Contributed:**
   $$\\frac{3}{8} + \\frac{2}{5} = \\frac{15 + 16}{40} = \\frac{31}{40}$$

2. **Fraction Not Contributed:**
   $$1 - \\frac{31}{40} = \\frac{40}{40} - \\frac{31}{40} = \\frac{9}{40}$$

Therefore, **$\\frac{9}{40}$** of the cost of land was not contributed.""",

    11: """Let's find the decimal portion for maize first:

1. **Sum of cabbages, tomatoes, and onions:**
   $$0.25 + 0.125 + 0.45 = 0.825$$

2. **Portion for maize:**
   $$1.000 - 0.825 = 0.175$$

3. **Convert to percentage:**
   $$0.175 \\times 100\\% = 17.5\\%$$

Therefore, **17.5%** of the *shamba* was used for planting maize.""",

    12: """Let's solve step by step:

1. **Total kales bought:**
   $$84.20\\text{ kg} + 45.48\\text{ kg} = 129.68\\text{ kg}$$

2. **Kales remaining after preparing lunch:**
   $$129.68\\text{ kg} - 15.93\\text{ kg} = 113.75\\text{ kg}$$

Therefore, she remained with **113.75 kg** of kales.""",

    13: """📌 **Awarding Marks:** On paper, the line segment AB measures approximately **$7.9\\text{ cm} = 79\\text{ mm}$** (Option B). However, because digital screens vary in size and scaling makes manual ruler measurement imprecise on displays, **all choices (A, B, C, D) are awarded full marks**.""",

    14: """Let me calculate step by step:

1. **Total number of bottles:**
   $$15 \\times 30 = 450\\text{ bottles}$$

2. **Total volume in millilitres:**
   $$450 \\times 300\\text{ ml} = 135,000\\text{ ml}$$

3. **Convert millilitres to litres ($1\\text{ L} = 1000\\text{ ml}$):**
   $$135,000 \\div 1000 = 135\\text{ litres}$$

Therefore, the total amount of juice packed was **135 litres**.""",

    15: """Let's calculate step by step:

1. **Convert tonnes to grams ($1\\text{ tonne} = 1,000\\text{ kg} = 1,000,000\\text{ g}$):**
   $$1.4 \\times 1,000,000 = 1,400,000\\text{ g}$$

2. **Number of 500 g pieces:**
   $$1,400,000 \\div 500 = 2,800\\text{ pieces}$$

3. **Total money from sale:**
   $$2,800 \\times \\text{sh } 110 = \\text{sh } 308,000$$

Therefore, he got **sh 308,000** from the sale of all the meat.""",

    16: """Let's add tonnes and kilograms separately:

1. **Add Kilograms:**
   $$800\\text{ kg} + 520\\text{ kg} = 1,320\\text{ kg}$$
   Since $1,000\\text{ kg} = 1\\text{ tonne}$, $1,320\\text{ kg} = 1\\text{ tonne } 320\\text{ kg}$.

2. **Add Tonnes:**
   $$40\\text{ tonnes} + 15\\text{ tonnes} + 1\\text{ tonne (from kg)} = 56\\text{ tonnes}$$

3. **Total:**
   **56 tonnes 320 kilograms**.""",

    17: """Let me calculate step by step:

1. **Mass of 500 bags of maize in kg:**
   $$500 \\times 90\\text{ kg} = 45,000\\text{ kg}$$

2. **Convert maize mass to tonnes ($1\\text{ tonne} = 1,000\\text{ kg}$):**
   $$45,000 \\div 1,000 = 45\\text{ tonnes}$$

3. **Total mass of loaded truck:**
   $$\\text{Empty truck} + \\text{Maize} = 12\\text{ tonnes} + 45\\text{ tonnes} = 57\\text{ tonnes}$$

Therefore, the total mass of the loaded truck was **57 tonnes**.""",

    18: """Let's calculate step by step:

1. **Total Cost Price (Buying price + Expenses):**
   $$\\text{sh } 35,000 + \\text{sh } 10,500 = \\text{sh } 45,500$$

2. **Profit (Selling Price - Total Cost Price):**
   $$\\text{sh } 65,000 - \\text{sh } 45,500 = \\text{sh } 19,500$$

Therefore, the farmer made a profit of **sh 19,500**.""",

    19: """To find the total travel time from Town P to Town R:

1. **Departure from Town P:** 9.00 a.m.
2. **Arrival at Town R:** 3.30 p.m.

3. **Calculate time duration:**
   * From 9.00 a.m. to 12.00 noon = $3\\text{ hours}$
   * From 12.00 noon to 3.30 p.m. = $3\\text{ hours } 30\\text{ minutes}$
   * Total duration = $3\\text{ h} + 3\\text{ h } 30\\text{ min} = 6\\text{ hours } 30\\text{ minutes} = 6\\frac{1}{2}\\text{ hours}$

Therefore, the journey took **6 ½ hours**.""",

    20: """Let's convert to 24-hour clock system:

1. **Time in 12-hour system:** 'thirty five minutes past six in the evening' = 6.35 p.m.
2. **Convert p.m. time to 24-hour system:** Add 12 hours to the hour part:
   $$06:35 + 12:00 = 18:35$$

In the 24-hour clock system, this is written as **1835 h**.""",

    21: """Let's calculate step by step:

1. **Convert tonnes to kilograms ($1\\text{ tonne} = 1,000\\text{ kg}$):**
   $$28\\text{ tonnes } 685\\text{ kg} = 28,000\\text{ kg} + 685\\text{ kg} = 28,685\\text{ kg}$$

2. **Divide by 5 lorries:**
   $$28,685 \\div 5 = 5,737\\text{ kg}$$

Therefore, each lorry carried **5,737 kg** of garbage.""",

    22: """Let's calculate step by step:

1. **Cost of items bought:**
   * **3 kg sugar:** $3 \\times \\text{sh } 110 = \\text{sh } 330$
   * **1 litre cooking oil:** $1 \\times \\text{sh } 360 = \\text{sh } 360$
   * **4 packets maize flour:** $4 \\times \\text{sh } 105 = \\text{sh } 420$
   * **Total Cost:** $\\text{sh } 330 + \\text{sh } 360 + \\text{sh } 420 = \\text{sh } 1,110$

2. **Money given:**
   $$3 \\times \\text{sh } 500 = \\text{sh } 1,500$$

3. **Balance:**
   $$\\text{sh } 1,500 - \\text{sh } 1,110 = \\text{sh } 390$$

Therefore, the balance was **sh 390**.""",

    23: """Let me calculate step by step:

1. **Total length of wire she has:**
   $$11\\text{ m } 85\\text{ cm} + 8\\text{ m } 90\\text{ cm} = 19\\text{ m } 175\\text{ cm} = 20\\text{ m } 75\\text{ cm}$$

2. **Wire still required:**
   * Convert to cm for easy subtraction:
     * $40\\text{ m } 20\\text{ cm} = 4,020\\text{ cm}$
     * $20\\text{ m } 75\\text{ cm} = 2,075\\text{ cm}$
     * $4,020\\text{ cm} - 2,075\\text{ cm} = 1,945\\text{ cm} = 19\\text{ m } 45\\text{ cm}$

Therefore, Sandra requires **19 m 45 cm** more barbed wire.""",

    24: """Let's calculate step by step:

1. **Three quarters ($\\frac{3}{4}$) of milk in 500 ml bottles:**
   * $\\frac{3}{4} \\times 24\\text{ L} = 18\\text{ L} = 18,000\\text{ ml}$
   * Number of 500 ml bottles = $18,000 \\div 500 = 36\\text{ bottles}$

2. **Remaining milk ($\\frac{1}{4}$) in 250 ml bottles:**
   * $24\\text{ L} - 18\\text{ L} = 6\\text{ L} = 6,000\\text{ ml}$
   * Number of 250 ml bottles = $6,000 \\div 250 = 24\\text{ bottles}$

3. **Total bottles used:**
   * $36 + 24 = 60\\text{ bottles}$

Therefore, she used a total of **60** bottles.""",

    25: """Using a protractor aligned with vertex Q and baseline QR:

* The inner scale reading from ray QR to ray QS measures **50°**.

Therefore, the size of angle SQR is **50°**.""",

    26: """Let's calculate step by step:

1. **Balance received:**
   $$\\text{sh } 1,000 - \\text{sh } 400 = \\text{sh } 600$$

2. **Equal number ($n$) of sh 200 and sh 100 notes:**
   $$n \\times \\text{sh } 200 + n \\times \\text{sh } 100 = \\text{sh } 600$$
   $$300n = 600 \\implies n = 2$$

3. **Total notes received:**
   * $2\\text{ notes of sh } 200 + 2\\text{ notes of sh } 100 = 4\\text{ notes}$

Therefore, he received **4** notes in total.""",

    27: """Let's calculate step by step:

1. **Guests carried per combined trip (1 bus trip + 1 matatu trip):**
   $$24 + 8 = 32\\text{ guests per trip}$$

2. **Total number of trips required:**
   $$128 \\div 32 = 4\\text{ trips}$$

Therefore, the matatu made **4** trips.""",

    28: """From the bar graph:

1. **Highest number of trees planted (2019):** 800
2. **Lowest number of trees planted (2018):** 200
3. **Difference:**
   $$800 - 200 = 600$$

Therefore, the difference is **600**.""",

    29: """Let's form the equation step by step:

* **Bananas Akinyi has** = $y$
* **Bananas Charo has** = $3 \\times y = 3y$
* **Total bananas altogether:** $3y + y = 36$

Therefore, the correct equation is **$3y + y = 36$**.""",

    30: """Let's count the total cubes in each option shown in the diagram:

* **Option A:** $3 \\text{ cubes wide} \\times 3 \\text{ cubes deep} \\times 3 \\text{ layers high} = 27 \\text{ cubes}$
* **Option B:** $3 \\text{ cubes wide} \\times 2 \\text{ cubes deep} \\times 2 \\text{ layers high} = 12 \\text{ cubes}$
* **Option C:** $3 \\text{ cubes wide} \\times 3 \\text{ cubes deep} \\times 2 \\text{ layers high} = 18 \\text{ cubes}$ (Matches Mwakio's 18 cubes!)
* **Option D:** $2 \\text{ cubes wide} \\times 3 \\text{ cubes deep} \\times 3 \\text{ layers high} = 18 \\text{ cubes}$

Therefore, **Option C** represents the correct stack."""
}

# Update explanations in data["sectionA"]
for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

# Also ensure options for fractions like Q10 look clean
for q in data["sectionA"]:
    if q["questionNumber"] == 10:
        q["options"] = [
            { "text": "$\\dfrac{9}{40}$", "isCorrect": True },
            { "text": "$\\dfrac{31}{40}$", "isCorrect": False },
            { "text": "$\\dfrac{3}{20}$", "isCorrect": False },
            { "text": "$\\dfrac{17}{20}$", "isCorrect": False }
        ]
        q["questionText"] = "Mugambi and Kioko contributed some money to buy a piece of land. Mugambi contributed $\\dfrac{3}{8}$ of the total cost of the land. Kioko contributed $\\dfrac{2}{5}$ of the total cost.\n\nWhat fraction of the cost of land was **not** contributed?"

js_content = f"export const kpseaMath2022 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully fixed all math formatting in explanations across KPSEA Math 2022!")
