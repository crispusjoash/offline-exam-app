import re

js_code = """export const kpseaMath2022 = {
  "id": "kpsea-math-2022",
  "title": "KPSEA 2022 Mathematics",
  "subject": "Mathematics",
  "year": "2022",
  "durationMinutes": 80,
  "sharedContexts": {
    "ctx-math-2022-q6": {
      "title": "Rectangle and Triangle Drawing",
      "type": "image",
      "imagePath": "/assets/kpsea_math_2022_q6.svg",
      "caption": "A carpenter made a drawing consisting of a rectangle and a triangle as shown."
    },
    "ctx-math-2022-q13": {
      "title": "Line Segment AB",
      "type": "image",
      "imagePath": "/assets/kpsea_math_2022_q13.svg",
      "caption": "A learner drew the line segment AB as shown."
    },
    "ctx-math-2022-q19": {
      "title": "Travel Timetable",
      "type": "image",
      "imagePath": "/assets/kpsea_math_2022_q19.svg",
      "caption": "Travel timetable for a bus company from town P to R."
    }
  },
  "sectionA": [
    {
      "id": "kpsea-math-2022-q1",
      "questionNumber": 1,
      "questionText": "The number of people in a certain county is five hundred and sixty five thousand and fifty two.\\n\\nWhat is the number in symbols?",
      "questionType": "mcq",
      "options": [
        { "text": "506552", "isCorrect": false },
        { "text": "565502", "isCorrect": false },
        { "text": "565052", "isCorrect": true },
        { "text": "560052", "isCorrect": false }
      ],
      "explanation": "To write **five hundred and sixty five thousand and fifty two** in symbols:\\n\\n* **Five hundred and sixty five thousand** = $565,000$\\n* **Fifty two** = $52$\\n\\nCombining these gives **565,052**."
    },
    {
      "id": "kpsea-math-2022-q2",
      "questionNumber": 2,
      "questionText": "The number of loaves of bread produced by a factory in a certain year was 3624817.\\n\\nWhat is the place value of digit 6 in the number?",
      "questionType": "mcq",
      "options": [
        { "text": "Millions", "isCorrect": false },
        { "text": "Hundreds of thousands", "isCorrect": true },
        { "text": "Thousands", "isCorrect": false },
        { "text": "Tens of thousands", "isCorrect": false }
      ],
      "explanation": "Let's identify the place values of each digit in **3,624,817** from right to left:\\n\\n* **7** → Ones\\n* **1** → Tens\\n* **8** → Hundreds\\n* **4** → Thousands\\n* **2** → Tens of thousands\\n* **6** → **Hundreds of thousands**\\n* **3** → Millions\\n\\nTherefore, the place value of digit 6 is **Hundreds of thousands**."
    },
    {
      "id": "kpsea-math-2022-q3",
      "questionNumber": 3,
      "questionText": "A bookshop received 648205 exercise books from a supplier. A school bought 76102 of the exercise books.\\n\\nHow many books remained in the bookshop?",
      "questionType": "mcq",
      "options": [
        { "text": "724307", "isCorrect": false },
        { "text": "672103", "isCorrect": false },
        { "text": "532103", "isCorrect": false },
        { "text": "572103", "isCorrect": true }
      ],
      "explanation": "To find the number of remaining books, subtract the number bought from the total received:\\n\\n$$\\\\begin{array}{r@{\\\\quad}l}\\n648205 \\\\\\\\-\\quad 76102 \\\\\\\\\\nhline\\n572103\\n\\\\end{array}$$\\n\\nSo, **572,103** books remained in the bookshop."
    },
    {
      "id": "kpsea-math-2022-q4",
      "questionNumber": 4,
      "questionText": "At the beginning of the year, there were 1204 girls and 816 boys in a school. During the year, 88 more girls joined the school and 12 boys left the school.\\n\\nWhat was the total number of learners in the school at the end of the year?",
      "questionType": "mcq",
      "options": [
        { "text": "2096", "isCorrect": true },
        { "text": "2108", "isCorrect": false },
        { "text": "2120", "isCorrect": false },
        { "text": "2220", "isCorrect": false }
      ],
      "explanation": "Let me calculate the number of learners step by step:\\n\\n1. **Girls at the end of the year:** $1204 + 88 = 1292$ girls.\\n2. **Boys at the end of the year:** $816 - 12 = 804$ boys.\\n3. **Total learners at the end of the year:** $1292 + 804 = 2096$.\\n\\nTherefore, there were **2,096** learners altogether."
    },
    {
      "id": "kpsea-math-2022-q5",
      "questionNumber": 5,
      "questionText": "A lorry carried 1452 cartons of textbooks. Each carton had 24 textbooks.\\n\\nHow many textbooks did the lorry carry altogether?",
      "questionType": "mcq",
      "options": [
        { "text": "1476", "isCorrect": false },
        { "text": "8812", "isCorrect": false },
        { "text": "34848", "isCorrect": true },
        { "text": "52448", "isCorrect": false }
      ],
      "explanation": "To find the total number of textbooks, multiply the number of cartons by textbooks per carton:\\n\\n$$1452 \\\\times 24 = 34848$$\\n\\n* $1452 \\\\times 20 = 29040$\\n* $1452 \\\\times 4 = 5808$\\n* $29040 + 5808 = 34848$\\n\\nThe lorry carried **34,848** textbooks altogether."
    },
    {
      "id": "kpsea-math-2022-q6",
      "questionNumber": 6,
      "contextRef": "ctx-math-2022-q6",
      "questionText": "A carpenter made a drawing. The drawing consists of a rectangle and a triangle as shown.\\n\\nWhat is the area of the drawing?",
      "questionType": "mcq",
      "options": [
        { "text": "160 m²", "isCorrect": false },
        { "text": "36 m²", "isCorrect": true },
        { "text": "20 m²", "isCorrect": false },
        { "text": "16 m²", "isCorrect": false }
      ],
      "explanation": "The total area of the drawing is the sum of the area of the rectangle and the area of the triangle:\\n\\n1. **Area of Rectangle:**\\n   $$\\\\text{Area} = \\\\text{length} \\\\times \\\\text{width} = 5\\\\text{ m} \\\\times 4\\\\text{ m} = 20\\\\text{ m}^2$$\\n\\n2. **Area of Triangle:**\\n   $$\\\\text{Area} = \\\\frac{1}{2} \\\\times \\\\text{base} \\\\times \\\\text{height} = \\\\frac{1}{2} \\\\times 4\\\\text{ m} \\\\times 8\\\\text{ m} = 16\\\\text{ m}^2$$\\n\\n3. **Total Area:**\\n   $$20\\\\text{ m}^2 + 16\\\\text{ m}^2 = 36\\\\text{ m}^2$$\\n\\nTherefore, the total area of the drawing is **36 m²**."
    },
    {
      "id": "kpsea-math-2022-q7",
      "questionNumber": 7,
      "questionText": "A teacher wrote on the blackboard the following pattern.\\n\\n$$30 , 32 , 36 , 44 , 60 , \\\\underline{\\\\hspace{1cm}}$$\\n\\nWhat is the next number in the pattern?",
      "questionType": "mcq",
      "options": [
        { "text": "32", "isCorrect": false },
        { "text": "72", "isCorrect": false },
        { "text": "92", "isCorrect": true },
        { "text": "104", "isCorrect": false }
      ],
      "explanation": "Let's examine the differences between consecutive terms in the pattern:\\n\\n* $32 - 30 = +2$\\n* $36 - 32 = +4$\\n* $44 - 36 = +8$\\n* $60 - 44 = +16$\\n\\nNotice that the difference doubles each time ($2, 4, 8, 16, 32$).\\n\\n* Next difference = $+32$\\n* Next term = $60 + 32 = 92$.\\n\\nTherefore, the next number in the pattern is **92**."
    },
    {
      "id": "kpsea-math-2022-q8",
      "questionNumber": 8,
      "questionText": "4K club had 2156 chicks. The chicks were distributed equally among 15 members.\\n\\nHow many more chicks will the 4K club add for all the members to get an equal share?",
      "questionType": "mcq",
      "options": [
        { "text": "4", "isCorrect": true },
        { "text": "11", "isCorrect": false },
        { "text": "143", "isCorrect": false },
        { "text": "144", "isCorrect": false }
      ],
      "explanation": "Let's divide the total number of chicks by 15 members:\\n\\n$$2156 \\\\div 15 = 143 \\\\text{ remainder } 11$$\\n\\n* Each member receives 143 chicks, leaving **11 chicks** remaining.\\n* To give everyone one more chick (144 chicks each), we need a total of 15 chicks.\\n* Chicks needed = $15 - 11 = 4$ more chicks.\\n\\nTherefore, the 4K club needs to add **4** more chicks."
    },
    {
      "id": "kpsea-math-2022-q9",
      "questionNumber": 9,
      "questionText": "Musa drew a rectangle and a square. The rectangle had a length of 24 cm and width of 6 cm. The rectangle had the same area as the square.\\n\\nWhat was the perimeter of the square?",
      "questionType": "mcq",
      "options": [
        { "text": "12", "isCorrect": false },
        { "text": "48", "isCorrect": true },
        { "text": "60", "isCorrect": false },
        { "text": "144", "isCorrect": false }
      ],
      "explanation": "Let's solve step by step:\\n\\n1. **Area of Rectangle:**\\n   $$\\\\text{Area} = 24\\\\text{ cm} \\\\times 6\\\\text{ cm} = 144\\\\text{ cm}^2$$\\n\\n2. **Side Length of Square:**\\n   Since the square has the same area:\\n   $$\\\\text{Side}^2 = 144\\\\text{ cm}^2 \\\\implies \\\\text{Side} = \\\\sqrt{144} = 12\\\\text{ cm}$$\\n\\n3. **Perimeter of Square:**\\n   $$\\\\text{Perimeter} = 4 \\\\times \\\\text{side} = 4 \\\\times 12\\\\text{ cm} = 48\\\\text{ cm}$$\\n\\nTherefore, the perimeter of the square is **48 cm**."
    },
    {
      "id": "kpsea-math-2022-q10",
      "questionNumber": 10,
      "questionText": "Mugambi and Kioko contributed some money to buy a piece of land. Mugambi contributed $\\\\frac{3}{8}$ of the total cost of the land. Kioko contributed $\\\\frac{2}{5}$ of the total cost.\\n\\nWhat fraction of the cost of land was **not** contributed?",
      "questionType": "mcq",
      "options": [
        { "text": "9/40", "isCorrect": true },
        { "text": "31/40", "isCorrect": false },
        { "text": "3/20", "isCorrect": false },
        { "text": "17/20", "isCorrect": false }
      ],
      "explanation": "Let's calculate the total fraction contributed first:\\n\\n1. **Total Contributed:**\\n   $$\\\\frac{3}{8} + \\\\frac{2}{5} = \\\\frac{15 + 16}{40} = \\\\frac{31}{40}$$\\n\\n2. **Fraction Not Contributed:**\\n   $$1 - \\\\frac{31}{40} = \\\\frac{40}{40} - \\\\frac{31}{40} = \\\\frac{9}{40}$$\\n\\nTherefore, **$\\\\frac{9}{40}$** of the cost was not contributed."
    },
    {
      "id": "kpsea-math-2022-q11",
      "questionNumber": 11,
      "questionText": "A farmer divided his *shamba* into four portions. He planted cabbages on $0.25$ of the *shamba*, tomatoes on $0.125$ and onions on $0.45$. He planted maize on the remaining portion.\\n\\nWhat percentage of the *shamba* was used for planting maize?",
      "questionType": "mcq",
      "options": [
        { "text": "82.5", "isCorrect": false },
        { "text": "70.0", "isCorrect": false },
        { "text": "37.5", "isCorrect": false },
        { "text": "17.5", "isCorrect": true }
      ],
      "explanation": "Let's find the decimal portion for maize first:\\n\\n1. **Sum of cabbages, tomatoes, and onions:**\\n   $$0.25 + 0.125 + 0.45 = 0.825$$\\n\\n2. **Portion for maize:**\\n   $$1.000 - 0.825 = 0.175$$\\n\\n3. **Convert to percentage:**\\n   $$0.175 \\\\times 100\\\\% = 17.5\\\\%$$\\n\\nTherefore, **17.5%** of the *shamba* was used for planting maize."
    },
    {
      "id": "kpsea-math-2022-q12",
      "questionNumber": 12,
      "questionText": "Ann bought 84.20 kg of kales from a grocer. She also bought 45.48 kg of kales from another grocer. She later used 15.93 kg of kales to prepare lunch.\\n\\nWhat mass, in kilograms, of kales did she remain with?",
      "questionType": "mcq",
      "options": [
        { "text": "145.61", "isCorrect": false },
        { "text": "129.68", "isCorrect": false },
        { "text": "113.75", "isCorrect": true },
        { "text": "22.79", "isCorrect": false }
      ],
      "explanation": "Let's solve step by step:\\n\\n1. **Total kales bought:**\\n   $$84.20\\\\text{ kg} + 45.48\\\\text{ kg} = 129.68\\\\text{ kg}$$\\n\\n2. **Kales remaining after preparing lunch:**\\n   $$129.68\\\\text{ kg} - 15.93\\\\text{ kg} = 113.75\\\\text{ kg}$$\\n\\nTherefore, she remained with **113.75 kg** of kales."
    },
    {
      "id": "kpsea-math-2022-q13",
      "questionNumber": 13,
      "contextRef": "ctx-math-2022-q13",
      "questionText": "A learner drew the following line. Measure the length AB in cm using a ruler.\\n\\nWhat is the length of the line in millimetres?",
      "questionType": "mcq",
      "options": [
        { "text": "790", "isCorrect": true },
        { "text": "79", "isCorrect": true },
        { "text": "7.9", "isCorrect": true },
        { "text": "0.79", "isCorrect": true }
      ],
      "explanation": "📌 **Awarding Marks:** On paper, the line segment AB measures approximately **7.9 cm = 79 mm** (Option B). However, because digital screens vary in size and scaling makes manual ruler measurement imprecise on displays, **all choices (A, B, C, D) are awarded full marks**."
    },
    {
      "id": "kpsea-math-2022-q14",
      "questionNumber": 14,
      "questionText": "Linda had 15 cartons. She packed 30 bottles of fruit juice in each carton. Each bottle contained 300 ml of juice.\\n\\nWhat was the total amount, in litres, of the juice packed?",
      "questionType": "mcq",
      "options": [
        { "text": "135", "isCorrect": true },
        { "text": "1350", "isCorrect": false },
        { "text": "13500", "isCorrect": false },
        { "text": "135000", "isCorrect": false }
      ],
      "explanation": "Let me calculate step by step:\\n\\n1. **Total number of bottles:**\\n   $$15 \\\\times 30 = 450\\\\text{ bottles}$$\\n\\n2. **Total volume in millilitres:**\\n   $$450 \\\\times 300\\\\text{ ml} = 135,000\\\\text{ ml}$$\\n\\n3. **Convert millilitres to litres ($1\\\\text{ L} = 1000\\\\text{ ml}$):**\\n   $$135,000 \\\\div 1000 = 135\\\\text{ litres}$$\\n\\nTherefore, the total amount of juice packed was **135 litres**."
    },
    {
      "id": "kpsea-math-2022-q15",
      "questionNumber": 15,
      "questionText": "A butcher had 1.4 tonnes of meat in a butchery. He cut the meat into pieces of 500 g each. He sold each piece for sh 110.\\n\\nHow much money did he get from the sale of all the meat?",
      "questionType": "mcq",
      "options": [
        { "text": "sh 3 080 000", "isCorrect": false },
        { "text": "sh 308 000", "isCorrect": true },
        { "text": "sh 30 800", "isCorrect": false },
        { "text": "sh 3 080", "isCorrect": false }
      ],
      "explanation": "Let's calculate step by step:\\n\\n1. **Convert tonnes to grams ($1\\\\text{ tonne} = 1000\\\\text{ kg} = 1,000,000\\\\text{ g}$):**\\n   $$1.4 \\\\times 1,000,000 = 1,400,000\\\\text{ g}$$\\n\\n2. **Number of 500 g pieces:**\\n   $$1,400,000 \\\\div 500 = 2,800\\\\text{ pieces}$$\\n\\n3. **Total money from sale:**\\n   $$2,800 \\\\times 110 = \\\\text{sh } 308,000$$\\n\\nTherefore, he got **sh 308,000** from the sale."
    },
    {
      "id": "kpsea-math-2022-q16",
      "questionNumber": 16,
      "questionText": "Two farmers delivered wheat to a factory. One farmer delivered 40 tonnes 800 kilograms of wheat and the other farmer delivered 15 tonnes 520 kilograms of wheat.\\n\\nHow many tonnes and kilograms of wheat was delivered altogether?",
      "questionType": "mcq",
      "options": [
        { "text": "25 tonnes 280 kilograms", "isCorrect": false },
        { "text": "55 tonnes 320 kilograms", "isCorrect": false },
        { "text": "56 tonnes 120 kilograms", "isCorrect": false },
        { "text": "56 tonnes 320 kilograms", "isCorrect": true }
      ],
      "explanation": "Let's add tonnes and kilograms separately:\\n\\n1. **Add Kilograms:**\\n   $$800\\\\text{ kg} + 520\\\\text{ kg} = 1320\\\\text{ kg}$$\\n   Since $1000\\\\text{ kg} = 1\\\\text{ tonne}$, $1320\\\\text{ kg} = 1\\\\text{ tonne } 320\\\\text{ kg}$.\\n\\n2. **Add Tonnes:**\\n   $$40\\\\text{ tonnes} + 15\\\\text{ tonnes} + 1\\\\text{ tonne (from kg)} = 56\\\\text{ tonnes}$$\\n\\n3. **Total:**\\n   **56 tonnes 320 kilograms**."
    },
    {
      "id": "kpsea-math-2022-q17",
      "questionNumber": 17,
      "questionText": "An empty truck has a mass of 12 tonnes. The truck carried 500 bags of maize. Each bag of maize had a mass of 90 kg.\\n\\nWhat was the total mass, in tonnes, of the loaded truck?",
      "questionType": "mcq",
      "options": [
        { "text": "33", "isCorrect": false },
        { "text": "45", "isCorrect": false },
        { "text": "57", "isCorrect": true },
        { "text": "602", "isCorrect": false }
      ],
      "explanation": "Let me calculate step by step:\\n\\n1. **Mass of 500 bags of maize in kg:**\\n   $$500 \\\\times 90\\\\text{ kg} = 45,000\\\\text{ kg}$$\\n\\n2. **Convert maize mass to tonnes ($1\\\\text{ tonne} = 1000\\\\text{ kg}$):**\\n   $$45,000 \\\\div 1000 = 45\\\\text{ tonnes}$$\\n\\n3. **Total mass of loaded truck:**\\n   $$\\\\text{Empty truck} + \\\\text{Maize} = 12 + 45 = 57\\\\text{ tonnes}$$\\n\\nTherefore, the total mass of the loaded truck was **57 tonnes**."
    },
    {
      "id": "kpsea-math-2022-q18",
      "questionNumber": 18,
      "questionText": "A farmer bought a cow for sh 35 000. He spent sh 10 500 in taking care of it. He later sold the cow for sh 65 000.\\n\\nHow much profit did he make?",
      "questionType": "mcq",
      "options": [
        { "text": "sh 19 500", "isCorrect": true },
        { "text": "sh 30 000", "isCorrect": false },
        { "text": "sh 54 500", "isCorrect": false },
        { "text": "sh 110 500", "isCorrect": false }
      ],
      "explanation": "Let's calculate step by step:\\n\\n1. **Total Cost Price (Buying price + Expenses):**\\n   $$\\\\text{sh } 35,000 + \\\\text{sh } 10,500 = \\\\text{sh } 45,500$$\\n\\n2. **Profit (Selling Price - Total Cost Price):**\\n   $$\\\\text{sh } 65,000 - \\\\text{sh } 45,500 = \\\\text{sh } 19,500$$\\n\\nTherefore, the farmer made a profit of **sh 19,500**."
    },
    {
      "id": "kpsea-math-2022-q19",
      "questionNumber": 19,
      "contextRef": "ctx-math-2022-q19",
      "questionText": "The table below shows the travel timetable for a bus company from town P to R.\\n\\nHalima travelled from town P to R using the bus.\\n\\nHow long did the journey take?",
      "questionType": "mcq",
      "options": [
        { "text": "3 hours", "isCorrect": false },
        { "text": "4 ½ hours", "isCorrect": false },
        { "text": "6 ½ hours", "isCorrect": true },
        { "text": "5 ½ hours", "isCorrect": false }
      ],
      "explanation": "To find the total travel time from Town P to Town R:\\n\\n1. **Departure from Town P:** 9.00 a.m.\\n2. **Arrival at Town R:** 3.30 p.m.\\n\\n3. **Calculate time duration:**\\n   * From 9.00 a.m. to 12.00 noon = 3 hours.\\n   * From 12.00 noon to 3.30 p.m. = 3 hours 30 minutes.\\n   * Total duration = $3\\\\text{ h} + 3\\\\text{ h } 30\\\\text{ min} = 6\\\\text{ hours } 30\\\\text{ minutes} = 6\\\\frac{1}{2}\\\\text{ hours}$.\\n\\nTherefore, the journey took **6 ½ hours**."
    },
    {
      "id": "kpsea-math-2022-q20",
      "questionNumber": 20,
      "questionText": "Ali closes his shop daily at thirty five minutes past six in the evening.\\n\\nWhat time in a 24 hour clock system, does he close the shop?",
      "questionType": "mcq",
      "options": [
        { "text": "1835 h", "isCorrect": true },
        { "text": "1235 h", "isCorrect": false },
        { "text": "0635 h", "isCorrect": false },
        { "text": "0035 h", "isCorrect": false }
      ],
      "explanation": "Let's convert to 24-hour clock system:\\n\\n1. **Time in 12-hour system:** 'thirty five minutes past six in the evening' = 6.35 p.m.\\n2. **Convert p.m. time to 24-hour system:** Add 12 hours to the hour part:\\n   $$06:35 + 12:00 = 18:35$$\\n\\nIn the 24-hour clock system, this is written as **1835 h**."
    }
  ]
};
"""

with open('src/data/kpsea-math-2022.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Created kpsea-math-2022.js successfully!")
