import json
import os

new_questions = [
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "A packet of milk is in the shape of a cuboid. The length of the packet is 8.5 cm, the width is 5 cm and the height is 12 cm. What is the capacity of the packet in litres?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "0.51 litres", "isCorrect": True },
        { "text": "5.1 litres", "isCorrect": False },
        { "text": "510 litres", "isCorrect": False },
        { "text": "510000 litres", "isCorrect": False }
      ],
      "explanation": "Volume of a cuboid = length \u00d7 width \u00d7 height. Volume = 8.5 cm \u00d7 5 cm \u00d7 12 cm = 510 cm\u00b3. Since 1000 cm\u00b3 = 1 litre, the capacity in litres is 510 / 1000 = 0.51 litres."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "The temperature of a liquid was recorded as 215 K. Which of the following calculations gives the correct temperature in degrees celsius?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "215 \u00d7 273", "isCorrect": False },
        { "text": "215 \u00f7 273", "isCorrect": False },
        { "text": "215 + 273", "isCorrect": False },
        { "text": "215 \u2212 273", "isCorrect": True }
      ],
      "explanation": "To convert temperature from Kelvin to Celsius, you subtract 273 from the Kelvin temperature. Therefore, the calculation is 215 \u2212 273."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "The following table shows the mobile money transaction charges for a mobile service provider.\n\nTransaction range (Ksh) | Sending charges (Ksh) | Withdrawal charges (Ksh)\n1 - 150 | Free | Free\n151 - 300 | 10 | 10\n301 - 500 | 15 | 23\n501 - 1 000 | 25 | 28\n1 001 - 2 500 | 30 | 35\nAbove 2 500 | 40 | 55\n\nLoima had Ksh 4 000 in his mobile money account. He sent Ksh 1 500 to his sister and then withdrew Ksh 800. How much money did Loima remain with in his mobile account?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "1 642", "isCorrect": True },
        { "text": "1 670", "isCorrect": False },
        { "text": "1 672", "isCorrect": False },
        { "text": "1 700", "isCorrect": False }
      ],
      "explanation": "Sending Ksh 1 500 falls in the 1 001 - 2 500 range, costing Ksh 30. Withdrawing Ksh 800 falls in the 501 - 1 000 range, costing Ksh 28. Total deductions = 1 500 (sent) + 30 (charge) + 800 (withdrawn) + 28 (charge) = Ksh 2 358. Remaining amount = 4 000 - 2 358 = Ksh 1 642."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "Salome estimated the height of a window to be 1.5 m. She measured it and found that the actual height was 1.2 m. Which of the following calculations gives the percentage error in her estimation?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(0.3 / 1.5) \u00d7 100%", "isCorrect": False },
        { "text": "(0.3 / 1.2) \u00d7 100%", "isCorrect": True },
        { "text": "(1.2 / 1.5) \u00d7 100%", "isCorrect": False },
        { "text": "(1.5 / 1.2) \u00d7 100%", "isCorrect": False }
      ],
      "explanation": "Percentage error is calculated as (Absolute Error / Actual Value) \u00d7 100%. The absolute error is |1.5 - 1.2| = 0.3 m. The actual value is 1.2 m. Therefore, the calculation is (0.3 / 1.2) \u00d7 100%."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "The following are properties of a quadrilateral.\n(i) Opposite sides are equal and parallel\n(ii) Diagonal bisect at 90\u00b0\n(iii) Opposite angles are equal\nWhat is the name of the quadrilateral?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Trapezium", "isCorrect": False },
        { "text": "Parallelogram", "isCorrect": False },
        { "text": "Rectangle", "isCorrect": False },
        { "text": "Rhombus", "isCorrect": True }
      ],
      "explanation": "A rhombus is a quadrilateral with opposite sides parallel and equal, opposite angles equal, and its diagonals bisect each other at 90 degrees."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "The scale on an architectural drawing was 1:100. A wall constructed using the drawing was 3 m long. What was the length of the wall on the drawing ?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "0.3 cm", "isCorrect": False },
        { "text": "3 cm", "isCorrect": True },
        { "text": "30 cm", "isCorrect": False },
        { "text": "300 cm", "isCorrect": False }
      ],
      "explanation": "The scale 1:100 means 1 cm on the drawing represents 100 cm in reality. Actual length = 3 m = 300 cm. Drawing length = 300 cm / 100 = 3 cm."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Owino drew a straight line L\u2081. The equation of line L\u2081 is 2y = x + 3. A line L\u2082 is perpendicular to L\u2081. What is the gradient of L\u2082?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "\u22121/2", "isCorrect": False },
        { "text": "1/2", "isCorrect": False },
        { "text": "\u22122", "isCorrect": True },
        { "text": "2", "isCorrect": False }
      ],
      "explanation": "First, find the gradient (m\u2081) of L\u2081 by rewriting it in the form y = mx + c. 2y = x + 3 implies y = (1/2)x + 3/2, so m\u2081 = 1/2. For a perpendicular line L\u2082, the product of their gradients is -1 (m\u2081 \u00d7 m\u2082 = -1). Therefore, m\u2082 = -1 / (1/2) = -2."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "A photograph was enlarged to twice its original size. The original photograph had a length of 16 cm. What was the new length of the photograph?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "32 cm", "isCorrect": True },
        { "text": "18 cm", "isCorrect": False },
        { "text": "14 cm", "isCorrect": False },
        { "text": "8 cm", "isCorrect": False }
      ],
      "explanation": "If the photograph is enlarged by a linear scale factor of 2, all its lengths are multiplied by 2. New length = 16 cm \u00d7 2 = 32 cm."
    }
]

file_path = 'src/data/kjsea-math-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = content[:content.rfind(']')]
suffix = content[content.rfind(']'):]

new_json = json.dumps(new_questions, indent=2)
# Remove opening bracket and closing bracket of the list
new_json = new_json[new_json.find('{'):new_json.rfind('}')+1]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(prefix + ',\n  ' + new_json + '\n' + suffix)

print("Batch 2 for KJSEA Math 2025 appended!")
