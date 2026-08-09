import json

new_sectionA_questions = [
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "The following figure shows an object in the shape of a triangle ABC. Use a protractor to determine the size of angle ABC.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "60\u00b0", "isCorrect": False },
        { "text": "85\u00b0", "isCorrect": False },
        { "text": "95\u00b0", "isCorrect": True },
        { "text": "105\u00b0", "isCorrect": False }
      ],
      "explanation": "Using a protractor on the physical paper to measure angle ABC reveals it is slightly obtuse, measuring 95\u00b0."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "The letters of the word ELEMENTAITA were written on cards. Each letter was on its own card. The cards were placed in a bucket. Asha picked a card from the bucket at random. What is the probability that Asha picked a card with letter E?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "1/11", "isCorrect": False },
        { "text": "2/11", "isCorrect": False },
        { "text": "3/11", "isCorrect": True },
        { "text": "8/11", "isCorrect": False }
      ],
      "explanation": "The word ELEMENTAITA has a total of 11 letters. The letter 'E' appears 3 times. Therefore, the probability of picking the letter 'E' is the number of favorable outcomes (3) divided by the total possible outcomes (11), which is 3/11."
    }
]

sectionB_questions = [
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Anita, a Grade 7 learner participated in a 10000 m race. She ran 6784 m and walked the remaining distance.\n(a) Work out the distance that Anita walked.\n(b) Write the distance that Anita ran in words.\n(c) Write the distance that Anita ran rounded off to the nearest hundreds.",
      "maxScore": 3,
      "modelAnswer": "(a) Distance walked = Total distance - Distance ran\nDistance walked = 10000 m - 6784 m = 3216 m.\n\n(b) 6784 in words is: Six thousand, seven hundred and eighty-four.\n\n(c) 6784 rounded to the nearest hundreds is 6800. (The tens digit is 8, which is 5 or more, so we round up the hundreds digit from 7 to 8).",
      "rubric": "Award 1 mark for each correct part:\n(a) 3216 m (1 mark)\n(b) Six thousand, seven hundred and eighty-four (1 mark)\n(c) 6800 (1 mark)",
      "questionType": "structured"
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "A metallic container is in the shape of a cube. The length of the container is 2.4 m.\n(a) Determine the volume of the container.\n(b) Smaller cubes of side 50 cm were packed in the container. Determine the number of smaller cubes that were packed.",
      "maxScore": 4,
      "modelAnswer": "(a) Volume of a cube = length \u00d7 length \u00d7 length.\nVolume = 2.4 m \u00d7 2.4 m \u00d7 2.4 m = 13.824 m\u00b3.\n\n(b) Side of the smaller cube = 50 cm = 0.5 m.\nNumber of smaller cubes that can fit along the length = 2.4 m / 0.5 m = 4.8. \nSince only whole cubes can be packed without cutting them, 4 cubes fit along each edge.\nTotal number of smaller cubes = 4 \u00d7 4 \u00d7 4 = 64 cubes.\n(Note: If the question intended simple volume division without considering physical fitting: 13.824 / (0.5\u00b3) = 13.824 / 0.125 = 110.592. However, practically, 64 is the correct number of whole cubes packed).",
      "rubric": "Award marks as follows:\n(a) 13.824 m\u00b3 (2 marks - 1 for method, 1 for correct answer).\n(b) 64 cubes (2 marks - 1 for dividing side lengths, 1 for final number). Accept 110 cubes if solved using volume division.",
      "questionType": "structured"
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "A thanksgiving ceremony was attended by men, women and children. The ratio of men to women to children was 5:7:3. There were 60 children in the ceremony. Determine:\n(a) the number of men who attended the ceremony;\n(b) how many more women than men attended the ceremony.",
      "maxScore": 5,
      "modelAnswer": "The ratio is Men : Women : Children = 5 : 7 : 3.\n\n(a) Children represent 3 parts of the ratio, and there are 60 children.\n3 parts = 60\n1 part = 60 / 3 = 20\nNumber of men = 5 parts = 5 \u00d7 20 = 100 men.\n\n(b) Number of women = 7 parts = 7 \u00d7 20 = 140 women.\nNumber of men = 100 men.\nDifference (how many more women) = 140 - 100 = 40 more women.",
      "rubric": "Award marks as follows:\n(a) 100 men (3 marks: 1 for finding value of 1 part, 1 for method, 1 for answer)\n(b) 40 (2 marks: 1 for finding number of women, 1 for final difference)",
      "questionType": "structured"
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "A factory employed 5 men working 6 hours per day to pack flour in packets. The men worked for 12 days. Determine how many more days 3 men working for 8 hours per day will take to pack the same amount of flour.",
      "maxScore": 4,
      "modelAnswer": "Total man-hours required to pack the flour = 5 men \u00d7 6 hours/day \u00d7 12 days = 360 man-hours.\nFor the new scenario, let the number of days be D.\n3 men \u00d7 8 hours/day \u00d7 D days = 360 man-hours\n24 \u00d7 D = 360\nD = 360 / 24 = 15 days.\nThe new team takes 15 days to complete the work.\nThe original team took 12 days.\nNumber of MORE days = 15 days - 12 days = 3 days.",
      "rubric": "Award 4 marks in total:\n- 1 mark for total man-hours (360) or setting up the inverse proportion.\n- 1 mark for setting up the equation for the new group (24 \u00d7 D = 360).\n- 1 mark for finding the total days for the new group (15 days).\n- 1 mark for finding the difference (3 days).",
      "questionType": "structured"
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "The number of malaria patients admitted in a hospital was expressed as a fraction of the total number of patients admitted. The fraction was written in decimal form as 0.17 (with a dot on 7). Express the decimal in fraction form.",
      "maxScore": 4,
      "modelAnswer": "Let the recurring decimal be x = 0.1777...\nMultiply by 10 to move the decimal past the non-recurring part:\n10x = 1.777... (Equation 1)\nMultiply by 100 to move the decimal past the first recurring digit:\n100x = 17.777... (Equation 2)\n\nSubtract Equation 1 from Equation 2:\n100x - 10x = 17.777... - 1.777...\n90x = 16\nx = 16 / 90\n\nSimplify the fraction by dividing by the common factor 2:\nx = 8 / 45.\nThe decimal in fraction form is 8/45.",
      "rubric": "Award 4 marks in total:\n- 1 mark for correctly formulating equations (e.g. 10x = 1.777... and 100x = 17.777...)\n- 1 mark for subtracting correctly to eliminate the recurring decimal (90x = 16)\n- 1 mark for isolating x (x = 16/90)\n- 1 mark for the simplified fraction (8/45)",
      "questionType": "structured"
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "Regina bought 4 books and 3 pens from a shop and paid Ksh 315. Hamisi bought 8 books and 2 pens of the same type from the same shop. He paid Ksh 530. Determine the cost of one book and one pen.",
      "maxScore": 4,
      "modelAnswer": "Let the cost of one book be b and the cost of one pen be p.\nFrom Regina's purchase: 4b + 3p = 315  (Equation 1)\nFrom Hamisi's purchase: 8b + 2p = 530  (Equation 2)\n\nUsing elimination method, multiply Equation 1 by 2 to equate the coefficients of b:\n8b + 6p = 630  (Equation 3)\n\nSubtract Equation 2 from Equation 3:\n(8b + 6p) - (8b + 2p) = 630 - 530\n4p = 100\np = 25.\nThe cost of one pen is Ksh 25.\n\nSubstitute p = 25 into Equation 1:\n4b + 3(25) = 315\n4b + 75 = 315\n4b = 315 - 75\n4b = 240\nb = 60.\nThe cost of one book is Ksh 60.",
      "rubric": "Award 4 marks in total:\n- 1 mark for forming the two simultaneous equations.\n- 1 mark for a correct method to solve (elimination or substitution).\n- 1 mark for finding the cost of a pen (Ksh 25).\n- 1 mark for finding the cost of a book (Ksh 60).",
      "questionType": "structured"
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "Two families, A and B bought oranges, mangoes and bananas in two weeks as shown in the following tables.\n\nWeek 1\nFamily | Oranges | Mangoes | Bananas\nA      | 7       | 15      | 5\nB      | 9       | 20      | 3\n\nWeek 2\nFamily | Oranges | Mangoes | Bananas\nA      | 6       | 10      | 4\nB      | 14      | 15      | 8\n\n(a) Form matrices to represent the information provided.\n(b) Determine the total number of fruits of each type bought by each family.",
      "maxScore": 2,
      "modelAnswer": "(a) Matrix for Week 1 (W1):\n( 7   15   5 )\n( 9   20   3 )\nMatrix for Week 2 (W2):\n(  6   10   4 )\n( 14   15   8 )\n\n(b) Add the two matrices W1 + W2 to get the total fruits:\n( 7+6    15+10   5+4 )\n( 9+14   20+15   3+8 )\n=\n( 13   25    9 )\n( 23   35   11 )\nFamily A bought 13 oranges, 25 mangoes, and 9 bananas.\nFamily B bought 23 oranges, 35 mangoes, and 11 bananas.",
      "rubric": "Award 2 marks:\n(a) 1 mark for correctly forming the two 2x3 matrices.\n(b) 1 mark for correctly adding the matrices and stating the totals.",
      "questionType": "structured"
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "Mary drew a parallelogram on a grid. One side of the parallelogram passed through point (1,4) with a gradient of 1/2. Determine:\n(a) the equation of the line;\n(b) the co-ordinates of the x-intercept of the line.",
      "maxScore": 4,
      "modelAnswer": "(a) The equation of a straight line is y = mx + c.\nThe gradient m = 1/2. The line passes through (x,y) = (1,4).\nSubstitute to find c:\n4 = (1/2)(1) + c\n4 = 0.5 + c\nc = 3.5 = 7/2.\nThe equation of the line is y = (1/2)x + 7/2, which can also be written as 2y = x + 7.\n\n(b) The x-intercept occurs where y = 0.\nSubstitute y = 0 into the equation:\n0 = (1/2)x + 7/2\n-7/2 = (1/2)x\nx = -7.\nThe coordinates of the x-intercept are (-7, 0).",
      "rubric": "Award 4 marks:\n(a) 1 mark for substitution into y=mx+c, 1 mark for correct equation (y = 1/2 x + 7/2 or 2y = x + 7).\n(b) 1 mark for setting y=0, 1 mark for correct coordinates (-7, 0).",
      "questionType": "structured"
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "A Grade 8 learner moulded a solid in the shape of a cone. The slant height of the cone was 20 cm. The base radius of the cone was 4.2 cm. Calculate the total surface area of the solid, correct to 2 decimal places.",
      "maxScore": 5,
      "modelAnswer": "Total surface area (TSA) of a solid cone = Area of base + Curved surface area\nTSA = \u03c0r\u00b2 + \u03c0rl = \u03c0r(r + l)\nGiven:\nRadius, r = 4.2 cm\nSlant height, l = 20 cm\nUsing \u03c0 \u2248 22/7 (or 3.14159):\nTSA = (22/7) \u00d7 4.2 \u00d7 (4.2 + 20)\nTSA = (22/7) \u00d7 4.2 \u00d7 24.2\nSince 4.2 / 7 = 0.6:\nTSA = 22 \u00d7 0.6 \u00d7 24.2\nTSA = 13.2 \u00d7 24.2 = 319.44 cm\u00b2.\nThe total surface area is 319.44 cm\u00b2.",
      "rubric": "Award 5 marks:\n- 1 mark for the correct formula (\u03c0r\u00b2 + \u03c0rl).\n- 1 mark for correct substitution of values.\n- 2 marks for correct calculation steps.\n- 1 mark for final answer correct to 2 decimal places (319.44).",
      "questionType": "structured"
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "A cylindrical tin of radius 1.8 cm contains some water. A spherical ball bearing of radius 1.5 cm is immersed in water in the tin. Determine the rise in the water level in the tin, correct to one decimal place.",
      "maxScore": 4,
      "modelAnswer": "When the spherical ball is completely immersed, the volume of water displaced is equal to the volume of the ball.\nVolume of spherical ball = (4/3)\u03c0r\u00b3\nRadius of ball = 1.5 cm.\nVolume of ball = (4/3) \u00d7 \u03c0 \u00d7 (1.5)\u00b3 = (4/3) \u00d7 \u03c0 \u00d7 3.375 = 4.5\u03c0 cm\u00b3.\n\nThe displaced water takes the shape of a cylinder with the same radius as the tin (1.8 cm) and a height h (which is the rise in water level).\nVolume of displaced water = \u03c0r\u00b2h = \u03c0 \u00d7 (1.8)\u00b2 \u00d7 h = 3.24\u03c0 \u00d7 h.\n\nEquating the two volumes:\n3.24\u03c0 \u00d7 h = 4.5\u03c0\n3.24h = 4.5\nh = 4.5 / 3.24 = 450 / 324 = 50 / 36 = 25 / 18 \u2248 1.3888... cm.\nCorrect to one decimal place, the rise is 1.4 cm.",
      "rubric": "Award 4 marks:\n- 1 mark for finding the volume of the sphere in terms of \u03c0 (4.5\u03c0).\n- 1 mark for formulating the volume of the displaced water cylinder (3.24\u03c0h).\n- 1 mark for equating the volumes.\n- 1 mark for the correct final answer rounded to 1 decimal place (1.4 cm).",
      "questionType": "structured"
    }
]

file_path = 'src/data/kjsea-math-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert new_sectionA_questions into sectionA, and add sectionB.
# Find the end of sectionA array:
sectionA_end = content.rfind(']')

# Generate JSON for new A questions (strip outer brackets)
new_A_json = json.dumps(new_sectionA_questions, indent=2)
new_A_json = new_A_json[new_A_json.find('{'):new_A_json.rfind('}')+1]

# Generate JSON for sectionB
sectionB_json = json.dumps(sectionB_questions, indent=2)

prefix = content[:sectionA_end]
suffix = content[sectionA_end+1:] # this is just '\n};\n'

new_content = prefix + ',\n  ' + new_A_json + '\n  ],\n  "sectionB": ' + sectionB_json + suffix

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 3 (Q19-Q30) for KJSEA Math 2025 appended and Section B created!")
