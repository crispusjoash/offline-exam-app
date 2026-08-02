import json
import re

file_path = 'src/data/kpsea-math-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const kpseaMath2022 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()

data = json.loads(match.group(1))

# Add new sharedContexts
data["sharedContexts"]["ctx-math-2022-q22"] = {
    "title": "Shop Price List",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q22.svg",
    "caption": "Price list for sugar, cooking oil, and maize flour."
}
data["sharedContexts"]["ctx-math-2022-q25"] = {
    "title": "Triangles PQS and SQR",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q25.svg",
    "caption": "Two triangles PQS and SQR drawn accurately."
}
data["sharedContexts"]["ctx-math-2022-q28"] = {
    "title": "Bar Graph of Trees Planted",
    "type": "image",
    "imagePath": "/assets/kpsea_math_2022_q28.svg",
    "caption": "Number of trees planted by learners from 2017 to 2020."
}

# New questions 21 to 30
new_questions = [
    {
      "id": "kpsea-math-2022-q21",
      "questionNumber": 21,
      "questionText": "A given number of lorries collected 28 tonnes 685 kilograms of garbage from the market. The garbage was loaded equally onto 5 similar lorries.\n\nHow many kilograms of garbage did each lorry carry?",
      "questionType": "mcq",
      "options": [
        { "text": "193", "isCorrect": False },
        { "text": "697", "isCorrect": False },
        { "text": "6970", "isCorrect": False },
        { "text": "5737", "isCorrect": True }
      ],
      "explanation": "Let's calculate step by step:\n\n1. **Convert tonnes to kilograms ($1\\text{ tonne} = 1000\\text{ kg}$):**\n   $$28\\text{ tonnes } 685\\text{ kg} = 28,000\\text{ kg} + 685\\text{ kg} = 28,685\\text{ kg}$$\n\n2. **Divide by 5 lorries:**\n   $$28,685 \\div 5 = 5,737\\text{ kg}$$\n\nTherefore, each lorry carried **5,737 kg** of garbage."
    },
    {
      "id": "kpsea-math-2022-q22",
      "questionNumber": 22,
      "contextRef": "ctx-math-2022-q22",
      "questionText": "The price list for a shop is shown below.\n\nNyaboke bought 3 kg of sugar, 1 litre of cooking oil and 4 packets of maize flour from the shop. She gave the shopkeeper 3 five hundred shilling notes.\n\nWhat was the balance?",
      "questionType": "mcq",
      "options": [
        { "text": "sh 390", "isCorrect": True },
        { "text": "sh 945", "isCorrect": False },
        { "text": "sh 1 110", "isCorrect": False },
        { "text": "sh 2 610", "isCorrect": False }
      ],
      "explanation": "Let's calculate step by step:\n\n1. **Cost of items bought:**\n   * **3 kg sugar:** $3 \\times \\text{sh } 110 = \\text{sh } 330$\n   * **1 litre cooking oil:** $1 \\times \\text{sh } 360 = \\text{sh } 360$\n   * **4 packets maize flour:** $4 \\times \\text{sh } 105 = \\text{sh } 420$\n   * **Total Cost:** $\\text{sh } 330 + \\text{sh } 360 + \\text{sh } 420 = \\text{sh } 1,110$\n\n2. **Money given:**\n   $$3 \\times \\text{sh } 500 = \\text{sh } 1,500$$\n\n3. **Balance:**\n   $$\\text{sh } 1,500 - \\text{sh } 1,110 = \\text{sh } 390$$\n\nTherefore, the balance was **sh 390**."
    },
    {
      "id": "kpsea-math-2022-q23",
      "questionNumber": 23,
      "questionText": "Sandra requires 40 m 20 cm of barbed wire to fence her garden. She had two pieces of barbed wire measuring 11 m 85 cm and 8 m 90 cm.\n\nHow much more length of barbed wire does Sandra require?",
      "questionType": "mcq",
      "options": [
        { "text": "60 m 95 cm", "isCorrect": False },
        { "text": "27 m 75 cm", "isCorrect": False },
        { "text": "19 m 55 cm", "isCorrect": False },
        { "text": "19 m 45 cm", "isCorrect": True }
      ],
      "explanation": "Let me calculate step by step:\n\n1. **Total length of wire she has:**\n   * $11\\text{ m } 85\\text{ cm} + 8\\text{ m } 90\\text{ cm} = 19\\text{ m } 175\\text{ cm} = 20\\text{ m } 75\\text{ cm}$\n\n2. **Wire still required:**\n   * Convert to cm for easy subtraction:\n     * $40\\text{ m } 20\\text{ cm} = 4020\\text{ cm}$\n     * $20\\text{ m } 75\\text{ cm} = 2075\\text{ cm}$\n     * $4020\\text{ cm} - 2075\\text{ cm} = 1945\\text{ cm} = 19\\text{ m } 45\\text{ cm}$\n\nTherefore, Sandra requires **19 m 45 cm** more barbed wire."
    },
    {
      "id": "kpsea-math-2022-q24",
      "questionNumber": 24,
      "questionText": "A salesperson had 24 litres of milk. She packed the milk in 500 ml and 250 ml bottles. She packed three quarters of the milk in 500 ml bottles and the rest in 250 ml bottles.\n\nWhat was the total number of bottles she used?",
      "questionType": "mcq",
      "options": [
        { "text": "60", "isCorrect": True },
        { "text": "36", "isCorrect": False },
        { "text": "32", "isCorrect": False },
        { "text": "24", "isCorrect": False }
      ],
      "explanation": "Let's calculate step by step:\n\n1. **Three quarters (¾) of milk in 500 ml bottles:**\n   * $\\frac{3}{4} \\times 24\\text{ L} = 18\\text{ L} = 18,000\\text{ ml}$\n   * Number of 500 ml bottles = $18,000 \\div 500 = 36\\text{ bottles}$\n\n2. **Remaining milk (¼) in 250 ml bottles:**\n   * $24\\text{ L} - 18\\text{ L} = 6\\text{ L} = 6,000\\text{ ml}$\n   * Number of 250 ml bottles = $6,000 \\div 250 = 24\\text{ bottles}$\n\n3. **Total bottles used:**\n   * $36 + 24 = 60\\text{ bottles}$\n\nTherefore, she used a total of **60** bottles."
    },
    {
      "id": "kpsea-math-2022-q25",
      "questionNumber": 25,
      "contextRef": "ctx-math-2022-q25",
      "questionText": "The figure below shows two triangles drawn accurately. Measure the angle SQR using a protractor.\n\nWhat is the size of angle SQR?",
      "questionType": "mcq",
      "options": [
        { "text": "35°", "isCorrect": False },
        { "text": "50°", "isCorrect": True },
        { "text": "70°", "isCorrect": False },
        { "text": "95°", "isCorrect": False }
      ],
      "explanation": "Using a protractor aligned with vertex Q and baseline QR:\n\n* The inner scale reading from ray QR to ray QS measures **50°**.\n\nTherefore, the size of angle SQR is **50°**."
    },
    {
      "id": "kpsea-math-2022-q26",
      "questionNumber": 26,
      "questionText": "Kigen bought goods worth sh 400. He gave the shopkeeper a sh 1 000 note. He received the balance in equal number of sh 200 and sh 100 notes.\n\nWhat was the total number of notes that he received?",
      "questionType": "mcq",
      "options": [
        { "text": "3", "isCorrect": False },
        { "text": "4", "isCorrect": True },
        { "text": "5", "isCorrect": False },
        { "text": "6", "isCorrect": False }
      ],
      "explanation": "Let's calculate step by step:\n\n1. **Balance received:**\n   $$\\text{sh } 1,000 - \\text{sh } 400 = \\text{sh } 600$$\n\n2. **Equal number ($n$) of sh 200 and sh 100 notes:**\n   $$n \\times \\text{sh } 200 + n \\times \\text{sh } 100 = \\text{sh } 600$$\n   $$300n = 600 \\implies n = 2$$\n\n3. **Total notes received:**\n   * 2 notes of sh 200 + 2 notes of sh 100 = **4 notes**.\n\nTherefore, he received **4** notes in total."
    },
    {
      "id": "kpsea-math-2022-q27",
      "questionNumber": 27,
      "questionText": "A bus and a matatu were to transport 128 guests to a wedding ceremony. The bus can carry 24 guests and the matatu 8 guests. Both vehicles made the same number of trips.\n\nHow many trips did the matatu make?",
      "questionType": "mcq",
      "options": [
        { "text": "2", "isCorrect": False },
        { "text": "4", "isCorrect": True },
        { "text": "8", "isCorrect": False },
        { "text": "16", "isCorrect": False }
      ],
      "explanation": "Let's calculate step by step:\n\n1. **Guests carried per combined trip (1 bus trip + 1 matatu trip):**\n   $$24 + 8 = 32\\text{ guests per trip}$$\n\n2. **Total number of trips required:**\n   $$128 \\div 32 = 4\\text{ trips}$$\n\nTherefore, the matatu made **4** trips."
    },
    {
      "id": "kpsea-math-2022-q28",
      "questionNumber": 28,
      "contextRef": "ctx-math-2022-q28",
      "questionText": "The bar graph below represents the number of trees planted by learners of a school in four years.\n\nWhat is the difference between the highest and lowest number of trees that were planted in the four years?",
      "questionType": "mcq",
      "options": [
        { "text": "800", "isCorrect": False },
        { "text": "700", "isCorrect": False },
        { "text": "600", "isCorrect": True },
        { "text": "200", "isCorrect": False }
      ],
      "explanation": "From the bar graph:\n\n1. **Highest number of trees planted (2019):** 800\n2. **Lowest number of trees planted (2018):** 200\n3. **Difference:**\n   $$800 - 200 = 600$$\n\nTherefore, the difference is **600**."
    },
    {
      "id": "kpsea-math-2022-q29",
      "questionNumber": 29,
      "questionText": "Charo and Akinyi have some bananas. Charo has three times as many bananas as Akinyi. They have 36 bananas altogether. Let the number of bananas that Akinyi has be represented by $y$.\n\nWhich of the following equations correctly represents the information given?",
      "questionType": "mcq",
      "options": [
        { "text": "3y + y = 36", "isCorrect": True },
        { "text": "y + y + y = 36", "isCorrect": False },
        { "text": "y + y + 3 = 36", "isCorrect": False },
        { "text": "y/3 + 3 = 36", "isCorrect": False }
      ],
      "explanation": "Let's form the equation step by step:\n\n* Bananas Akinyi has = $y$\n* Bananas Charo has = $3 \\times y = 3y$\n* Total bananas altogether = $3y + y = 36$\n\nTherefore, the correct equation is **$3y + y = 36$**."
    },
    {
      "id": "kpsea-math-2022-q30",
      "questionNumber": 30,
      "questionText": "Mwakio had 18 cubes with the same shape and size. He made a stack using all the cubes.\n\nWhich of the following represents the correct stack that he made?",
      "questionType": "mcq",
      "options": [
        { "text": "A stack 3 cubes wide, 3 cubes deep, and 3 layers high (27 cubes)", "isCorrect": False },
        { "text": "A stack 3 cubes wide, 2 cubes deep, and 2 layers high (12 cubes)", "isCorrect": False },
        { "text": "A stack 3 cubes wide, 3 cubes deep, and 2 layers high (18 cubes)", "isCorrect": True },
        { "text": "A stack 2 cubes wide, 2 cubes deep, and 3 layers high (12 cubes)", "isCorrect": False }
      ],
      "explanation": "Let's count the total cubes in each stack structure:\n\n* **Option A:** $3 \\times 3 \\times 3 = 27$ cubes.\n* **Option B:** $3 \\times 2 \\times 2 = 12$ cubes.\n* **Option C:** $3 \\times 3 \\times 2 = 18$ cubes (Matches Mwakio's 18 cubes!).\n* **Option D:** $2 \\times 2 \\times 3 = 12$ cubes.\n\nTherefore, **Option C** is the correct stack."
    }
]

data["sectionA"].extend(new_questions)

js_content = f"export const kpseaMath2022 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully appended Questions 21 to 30 to KPSEA Math 2022 dataset!")
