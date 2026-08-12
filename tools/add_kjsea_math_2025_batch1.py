import json
import os

paper_structure = {
  "id": "kjsea-math-2025",
  "title": "KJSEA 2025 Mathematics",
  "subject": "Mathematics",
  "year": "2025",
  "isParentPaper": False,
  "durationMinutes": 120,
  "timeAllowed": 120,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "A packet contains number cards. Sally picked cards with numbers 2, 4, 5 and 9 from the packet. Which of the following sets has prime numbers only?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "2 and 4", "isCorrect": False },
        { "text": "2 and 5", "isCorrect": True },
        { "text": "4 and 9", "isCorrect": False },
        { "text": "5 and 9", "isCorrect": False }
      ],
      "explanation": "A prime number is a number greater than 1 that has only two factors: 1 and itself. In the given set (2, 4, 5, 9), 2 and 5 are prime numbers. 4 is divisible by 2, and 9 is divisible by 3, so they are composite numbers."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "There are 120 boys, 180 girls and 24 teachers in a school. The school formed groups with equal numbers of boys, girls and teachers. What is the largest number of groups formed?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "12", "isCorrect": True },
        { "text": "60", "isCorrect": False },
        { "text": "324", "isCorrect": False },
        { "text": "360", "isCorrect": False }
      ],
      "explanation": "To find the largest number of groups where each group has an equal number of boys, girls, and teachers, we need to find the Greatest Common Divisor (GCD) of 120, 180, and 24. The GCD of 120, 180, and 24 is 12."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "The temperature of a deep freezer was \u22128\u00b0C. The deep freezer was adjusted and the temperature was increased by 15\u00b0C. What was the temperature of the deep freezer after it was adjusted?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "\u221223\u00b0C", "isCorrect": False },
        { "text": "\u22127\u00b0C", "isCorrect": False },
        { "text": "7\u00b0C", "isCorrect": True },
        { "text": "23\u00b0C", "isCorrect": False }
      ],
      "explanation": "The initial temperature was \u22128\u00b0C. An increase means adding to the initial temperature. So, \u22128 + 15 = 7. The new temperature is 7\u00b0C."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "Kamau intended to plant 70 seedlings. He allocated 1/5 of an hour to plant each seedling. During the planting, he took 1/4 of an hour to plant each seedling. Which of the following calculations will give the extra time Kamau used to plant all the seedlings?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(1/5 + 1/4) \u00d7 70", "isCorrect": False },
        { "text": "(1/4 \u00f7 1/5) \u00d7 70", "isCorrect": False },
        { "text": "(1/5 \u2212 1/4) \u00d7 70", "isCorrect": False },
        { "text": "(1/4 \u2212 1/5) \u00d7 70", "isCorrect": True }
      ],
      "explanation": "The extra time taken to plant ONE seedling is the difference between the actual time taken and the allocated time: (1/4 - 1/5) hours. For 70 seedlings, the total extra time is the extra time for one seedling multiplied by 70, which is (1/4 - 1/5) \u00d7 70."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "A Grade 9 teacher had flash cards containing questions on indices. Kirui picked a flash card containing the question 2\u02e3 \u00d7 2\u00b3 = 32. What is the value of x in the equation?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "16", "isCorrect": False },
        { "text": "8", "isCorrect": False },
        { "text": "2", "isCorrect": True },
        { "text": "1 2/3", "isCorrect": False }
      ],
      "explanation": "Using the laws of indices for multiplication with the same base: 2\u02e3 \u00d7 2\u00b3 = 2\u1d41\u207a\u00b3. We know that 32 can be written as 2\u2075. Therefore, 2\u1d41\u207a\u00b3 = 2\u2075. Equating the powers gives x + 3 = 5, which means x = 2."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "The total number of animals in Kiyapi's farm is 26. There are x donkeys in the farm. The number of goats in the farm is twice the number of donkeys. The remaining animals are sheep. Which of the following represents the number of sheep in the farm?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "26 \u2212 3x", "isCorrect": True },
        { "text": "26 \u2212 2x", "isCorrect": False },
        { "text": "26 \u2212 x", "isCorrect": False },
        { "text": "26 + 3x", "isCorrect": False }
      ],
      "explanation": "Number of donkeys = x. Number of goats = 2x. Total number of donkeys and goats = x + 2x = 3x. Since the total number of animals is 26, the number of sheep is the total minus the donkeys and goats: 26 \u2212 3x."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "A school is planning to transport x number of learners for drama festivals. For cost efficiency, the school has to transport at least 30 learners but less than 50 learners. Which of the following inequalities represents the above information?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "30 < x < 50", "isCorrect": False },
        { "text": "30 < x \u2264 50", "isCorrect": False },
        { "text": "30 \u2264 x \u2264 50", "isCorrect": False },
        { "text": "30 \u2264 x < 50", "isCorrect": True }
      ],
      "explanation": "'At least 30' means greater than or equal to 30 (x \u2265 30). 'Less than 50' means strictly less than 50 (x < 50). Combining these gives 30 \u2264 x < 50."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Learners presented the results of two teams in a football league using the matrix:\n( 3  2  1  0  7 )\n( 4  1  2  1  5 )\nWhat is the order of the matrix?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "10 \u00d7 1", "isCorrect": False },
        { "text": "1 \u00d7 10", "isCorrect": False },
        { "text": "5 \u00d7 2", "isCorrect": False },
        { "text": "2 \u00d7 5", "isCorrect": True }
      ],
      "explanation": "The order of a matrix is given as 'rows \u00d7 columns'. The given matrix has 2 rows and 5 columns, so its order is 2 \u00d7 5."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "The width of a door is 0.91 m. The door is opened through an angle of 72\u00b0. What is the length which the tip of the door sweeps through?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "5.72 m", "isCorrect": False },
        { "text": "1.14 m", "isCorrect": True },
        { "text": "0.57 m", "isCorrect": False },
        { "text": "0.52 m", "isCorrect": False }
      ],
      "explanation": "The tip of the door forms an arc of a circle. The radius (r) is the width of the door, 0.91 m. The angle (\u03b8) is 72\u00b0. Arc length = (\u03b8/360) \u00d7 2\u03c0r. Using \u03c0 \u2248 22/7: Arc length = (72/360) \u00d7 2 \u00d7 (22/7) \u00d7 0.91 = (1/5) \u00d7 2 \u00d7 22 \u00d7 0.13 = 1.144 m. The closest option is 1.14 m."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "A water bucket is cylindrical in shape. The diameter of the bucket is 40 cm. The bucket is filled with water up to a height of 42 cm. What is the surface area of the bucket in contact with water?\n(Use calculator value for \u03c0)",
      "questionType": "multiple-choice",
      "options": [
        { "text": "1256.64", "isCorrect": False },
        { "text": "5277.87", "isCorrect": False },
        { "text": "6534.51", "isCorrect": True },
        { "text": "7791.15", "isCorrect": False }
      ],
      "explanation": "The surface area in contact with water is the curved surface area plus the area of the circular base. Radius (r) = 40/2 = 20 cm. Height (h) = 42 cm. \nArea of base = \u03c0r\u00b2 = \u03c0 \u00d7 20\u00b2 = 400\u03c0. \nCurved surface area = 2\u03c0rh = 2 \u00d7 \u03c0 \u00d7 20 \u00d7 42 = 1680\u03c0.\nTotal area = 400\u03c0 + 1680\u03c0 = 2080\u03c0.\nUsing a calculator: 2080 \u00d7 3.14159... \u2248 6534.51."
    }
  ]
}

file_path = 'src/data/kjsea-math-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kjseaMath2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("Batch 1 for KJSEA Math 2025 generated!")
