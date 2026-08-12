import json
import os
import re

math_2025_data = {
  "id": "kpsea-math-2025",
  "title": "KPSEA 2025 Mathematics",
  "subject": "Mathematics",
  "year": "2025",
  "durationMinutes": 120,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "A piece of land was sold at sh 346 920.\nWhat is the price of the land in words?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Three hundred forty six thousand and ninety two shillings", "isCorrect": False },
        { "text": "Three hundred forty six thousand nine hundred and twenty shillings", "isCorrect": True },
        { "text": "Three hundred forty six thousand two hundred and ninety shillings", "isCorrect": False },
        { "text": "Three hundred forty six thousand nine hundred and two shillings", "isCorrect": False }
      ],
      "explanation": "346 920 in words is three hundred forty six thousand nine hundred and twenty."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "A school library has 49 361 books.\nWhat is the place value of digit 9 in the number?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Tens", "isCorrect": False },
        { "text": "Hundreds", "isCorrect": False },
        { "text": "Thousands", "isCorrect": True },
        { "text": "Tens of thousands", "isCorrect": False }
      ],
      "explanation": "In 49 361, 9 is in the thousands place."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "A learner wrote the following numbers on cards.\n[ 46 455 ] [ 62 326 ] [ 200 152 ] [ 59 441 ]\n\nThe cards were arranged in a descending order. What was the correct arrangement?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "200 152, 62 326, 59 441, 46 455", "isCorrect": True },
        { "text": "200 152, 59 441, 62 326, 46 455", "isCorrect": False },
        { "text": "46 455, 62 326, 59 441, 200 152", "isCorrect": False },
        { "text": "46 455, 59 441, 62 326, 200 152", "isCorrect": False }
      ],
      "explanation": "Descending order means from largest to smallest: 200 152, 62 326, 59 441, 46 455."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "A nursery bed has 91 rows of tree seedlings. Each row has 807 tree seedlings.\nHow many seedlings are in the nursery bed altogether?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "7 917", "isCorrect": False },
        { "text": "72 437", "isCorrect": False },
        { "text": "72 837", "isCorrect": False },
        { "text": "73 437", "isCorrect": True }
      ],
      "explanation": "91 rows \u00d7 807 seedlings/row = 73 437 seedlings."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "The following figure represents a rectangular table mat. A part of the mat is decorated with flowers.\nThe rectangle has a length of 20 cm and a width of 18 cm. A diagonal line divides it into two triangles, with one of the triangles decorated with flowers.\n\nWhat is the area of the part decorated with flowers?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "38 cm\u00b2", "isCorrect": False },
        { "text": "76 cm\u00b2", "isCorrect": False },
        { "text": "180 cm\u00b2", "isCorrect": True },
        { "text": "360 cm\u00b2", "isCorrect": False }
      ],
      "explanation": "The decorated part is a right-angled triangle with base 20 cm and height 18 cm. Area = 1/2 \u00d7 base \u00d7 height = 1/2 \u00d7 20 \u00d7 18 = 180 cm\u00b2."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "An athlete ran different distances in metres everyday. The distance the athlete ran each day formed a pattern as shown in the table.\nMonday: 400\nTuesday: 800\nWednesday: 1 600\nThursday: 3 200\nFriday: \u2014\n\nWhat distance did the athlete run on Friday?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "6 400", "isCorrect": True },
        { "text": "4 800", "isCorrect": False },
        { "text": "4 000", "isCorrect": False },
        { "text": "3 600", "isCorrect": False }
      ],
      "explanation": "The pattern is doubling the distance each day. 3 200 \u00d7 2 = 6 400 metres."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "Wanjala had a piece of land. He gave 5/8 of the land to the son and 1/4 to the brother to plant sugarcane.\nWhat fraction of the land did Wanjala give to the son and the brother altogether?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "1/8", "isCorrect": False },
        { "text": "1/2", "isCorrect": False },
        { "text": "3/8", "isCorrect": False },
        { "text": "7/8", "isCorrect": True }
      ],
      "explanation": "5/8 + 1/4 = 5/8 + 2/8 = 7/8."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "During a vaccination exercise in a certain county, 62% of the total population was vaccinated against COVID-19.\nWhat fraction of the population was vaccinated?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "19/50", "isCorrect": False },
        { "text": "31/50", "isCorrect": True },
        { "text": "1 19/31", "isCorrect": False },
        { "text": "19/31", "isCorrect": False }
      ],
      "explanation": "62% = 62/100, which simplifies to 31/50."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "What is 7/20 as a decimal?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "0.035", "isCorrect": False },
        { "text": "0.305", "isCorrect": False },
        { "text": "0.35", "isCorrect": True },
        { "text": "3.5", "isCorrect": False }
      ],
      "explanation": "7/20 = 35/100 = 0.35."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "A learner worked out the following task in an exercise book.\n0.345 - 0.236\nWhat was the correct answer?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "0.581", "isCorrect": False },
        { "text": "0.119", "isCorrect": False },
        { "text": "0.111", "isCorrect": False },
        { "text": "0.109", "isCorrect": True }
      ],
      "explanation": "0.345 - 0.236 = 0.109."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Tayari Farmers Society had 696 bags of fertilizer. The bags were shared equally among 12 farmers.\nRound off the two numbers, 696 and 12 to the nearest tens, then find the number of bags each farmer got.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "70", "isCorrect": True },
        { "text": "69", "isCorrect": False },
        { "text": "58", "isCorrect": False },
        { "text": "35", "isCorrect": False }
      ],
      "explanation": "696 rounded to the nearest ten is 700. 12 rounded to the nearest ten is 10. 700 / 10 = 70 bags."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "Nduta has two pieces of ropes measuring 123 cm 7 mm and 39 cm 2 mm.\nWhat is the total length of the ropes that she has?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "513 cm 9 mm", "isCorrect": False },
        { "text": "162 cm 9 mm", "isCorrect": True },
        { "text": "152 cm 9 mm", "isCorrect": False },
        { "text": "84 cm 5 mm", "isCorrect": False }
      ],
      "explanation": "(123 cm + 39 cm) = 162 cm; (7 mm + 2 mm) = 9 mm. Total is 162 cm 9 mm."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "Abdi drew a straight line measuring 6 centimetres 5 millimetres.\nWhat was the length of the line drawn in millimetres?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "650", "isCorrect": False },
        { "text": "605", "isCorrect": False },
        { "text": "65", "isCorrect": True },
        { "text": "6.5", "isCorrect": False }
      ],
      "explanation": "6 cm = 60 mm. 60 mm + 5 mm = 65 mm."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "A farmer had 2 156 chicks. The chicks were to be distributed equally among 15 families.\nHow many more chicks will the farmer add for all the families to get an equal share?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "4", "isCorrect": True },
        { "text": "11", "isCorrect": False },
        { "text": "143", "isCorrect": False },
        { "text": "144", "isCorrect": False }
      ],
      "explanation": "2 156 / 15 gives 143 with a remainder of 11 chicks. To make the remainder 15 (a full share), the farmer needs to add 4 chicks (15 - 11 = 4)."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "A learner made a hand washing container at home using a 20 litre jerrycan.\nWhat was the capacity of the container in millilitres?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "200", "isCorrect": False },
        { "text": "2 000", "isCorrect": False },
        { "text": "20 000", "isCorrect": True },
        { "text": "200 000", "isCorrect": False }
      ],
      "explanation": "1 litre = 1 000 millilitres. 20 \u00d7 1 000 = 20 000 ml."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "A lorry transported 4 500 kg of sand to a construction site.\nWhat was the mass of the sand in tonnes?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "450", "isCorrect": False },
        { "text": "45", "isCorrect": False },
        { "text": "4.5", "isCorrect": True },
        { "text": "0.45", "isCorrect": False }
      ],
      "explanation": "1 tonne = 1 000 kg. 4 500 / 1 000 = 4.5 tonnes."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Anne had 6.25 metres of a clothing material. She used 1.5 metres to make a dress.\nWhat fraction of the material was not used?\n(Give your answer in decimal)",
      "questionType": "multiple-choice",
      "options": [
        { "text": "0.24", "isCorrect": False },
        { "text": "0.76", "isCorrect": True },
        { "text": "0.024", "isCorrect": False },
        { "text": "0.976", "isCorrect": False }
      ],
      "explanation": "Material left = 6.25 - 1.5 = 4.75 metres. Fraction not used = 4.75 / 6.25 = 0.76."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "A Young Farmers Club in a school has 5 members. The members shared 65 kg 460 g of sawdust equally for their poultry project.\nWhat was the mass of the sawdust received by each member?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "327 kg 300 g", "isCorrect": False },
        { "text": "65 kg 455 g", "isCorrect": False },
        { "text": "13 kg 460 g", "isCorrect": False },
        { "text": "13 kg 92 g", "isCorrect": True }
      ],
      "explanation": "Divide the kilograms: 65 / 5 = 13 kg. Divide the grams: 460 / 5 = 92 g. Each member receives 13 kg 92 g."
    }
  ]
}

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaMath2025 = ' + json.dumps(math_2025_data, indent=2) + ';\n')

# Add to pastPapers.js
past_papers_path = 'src/data/pastPapers.js'
with open(past_papers_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'kpseaMath2025' not in content:
    content = "import { kpseaMath2025 } from './kpsea-math-2025.js';\n" + content
    content = re.sub(
        r'(KPSEA:\s*\[)', 
        r'\1\n    kpseaMath2025,', 
        content
    )
    with open(past_papers_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print("Created kpsea-math-2025.js and updated pastPapers.js!")
else:
    print("Created kpsea-math-2025.js but it was already in pastPapers.js.")
