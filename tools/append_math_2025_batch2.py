import json
import re

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = re.sub(r'^export const [a-zA-Z0-9_]+ = ', '', content)
json_str = re.sub(r';\s*$', '', json_str)
data = json.loads(json_str)

new_questions = [
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "Atieno arrived in school at a quarter past seven in the morning.\nWhat was the time in 12 hour system?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "6.45 a.m.", "isCorrect": False },
        { "text": "7.15 p.m.", "isCorrect": False },
        { "text": "7.15 a.m.", "isCorrect": True },
        { "text": "7.45 a.m.", "isCorrect": False }
      ],
      "explanation": "A quarter past seven in the morning is 7:15 a.m."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "Ahmed bought 2 dresses at sh 900 each. He later sold each dress for sh 1 150. How much profit did he make altogether?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "sh 1 300", "isCorrect": False },
        { "text": "sh 500", "isCorrect": True },
        { "text": "sh 650", "isCorrect": False },
        { "text": "sh 250", "isCorrect": False }
      ],
      "explanation": "Profit per dress = 1 150 - 900 = 250. For 2 dresses, 250 \u00d7 2 = 500 shillings."
    },
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Peter bought the following items from a shop.\nMathematical set: 250\nPen: 45\nPencil: 25\n\nHe paid for all the items using a one-thousand shilling note.\nHow much balance did he receive?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "sh 320", "isCorrect": False },
        { "text": "sh 680", "isCorrect": True },
        { "text": "sh 780", "isCorrect": False },
        { "text": "sh 1 320", "isCorrect": False }
      ],
      "explanation": "Total cost = 250 + 45 + 25 = 320. Balance = 1 000 - 320 = 680 shillings."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "The following figure shows a triangle drawn accurately. A learner used a protractor to measure the angle marked r.\n\nWhat is the size of angle r?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "40\u00b0", "isCorrect": False },
        { "text": "60\u00b0", "isCorrect": True },
        { "text": "80\u00b0", "isCorrect": False },
        { "text": "120\u00b0", "isCorrect": False }
      ],
      "explanation": "By visual estimation of the accurately drawn acute angle (it is noticeably larger than 45\u00b0 but smaller than 90\u00b0), it measures 60\u00b0."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "A Grade 6 learner carried the following 3-D object to use for collecting garbage in the school compound.\n(The object is an open cuboid box with no top face)\n\nHow many vertices and faces does the object have?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "7 vertices 2 faces", "isCorrect": False },
        { "text": "8 vertices 5 faces", "isCorrect": True },
        { "text": "8 vertices 6 faces", "isCorrect": False },
        { "text": "12 vertices 6 faces", "isCorrect": False }
      ],
      "explanation": "A cuboid has 8 vertices. Since the top is open for collecting garbage, it has only 5 faces instead of 6."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "Learners were asked to construct a rabbit hutch. They joined pieces of timber and made one side of the hutch as shown.\n(Timbers h and i are vertical supports on the left and right sides)\n\nWhich of the following pieces of timber are parallel?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "h and i", "isCorrect": True },
        { "text": "e and h", "isCorrect": False },
        { "text": "f and i", "isCorrect": False },
        { "text": "e and f", "isCorrect": False }
      ],
      "explanation": "Pieces h and i are the two vertical posts, which are parallel to each other."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "The following bar graph shows favourite games as chosen by learners in a certain school.\nFootball: 120, Handball: 80, Netball: 100, Volleyball: 60\n\nWhat is the number of learners who chose netball and volleyball altogether?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "200", "isCorrect": False },
        { "text": "180", "isCorrect": False },
        { "text": "160", "isCorrect": True },
        { "text": "140", "isCorrect": False }
      ],
      "explanation": "Netball = 100, Volleyball = 60. Total = 100 + 60 = 160."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "A hospital received 101 patients between Tuesday and Friday. The number of patients received each day was recorded in the following table except for Wednesday.\nTuesday: 23\nWednesday: \u2014\nThursday: 18\nFriday: 26\n\nHow many patients were received on Wednesday?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "34", "isCorrect": True },
        { "text": "44", "isCorrect": False },
        { "text": "67", "isCorrect": False },
        { "text": "168", "isCorrect": False }
      ],
      "explanation": "Total known patients = 23 + 18 + 26 = 67. Wednesday's patients = 101 - 67 = 34."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "During a class visit to a construction site, learners observed a stone in the shape of a cube.\nWhich of the following 2-D shapes did they see on the face of the stone?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Rectangle", "isCorrect": False },
        { "text": "Circle", "isCorrect": False },
        { "text": "Square", "isCorrect": True },
        { "text": "Triangle", "isCorrect": False }
      ],
      "explanation": "All faces of a cube are squares."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "Fatuma left home at 11.20 a.m. and drove to town. She arrived in town at 2.30 p.m.\nHow long was her journey from home to town?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "4 hours 10 minutes", "isCorrect": False },
        { "text": "3 hours 10 minutes", "isCorrect": True },
        { "text": "8 hours 50 minutes", "isCorrect": False },
        { "text": "13 hours 50 minutes", "isCorrect": False }
      ],
      "explanation": "From 11:20 a.m. to 12:00 noon is 40 minutes. From 12:00 noon to 2:30 p.m. is 2 hours 30 minutes. Total time = 2 hr 30 min + 40 min = 3 hours 10 minutes."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "Kantet bought 6 pineapples and some oranges from a market. The total number of pineapples and oranges bought were less than 25. Let the number of oranges bought be represented by letter x.\nWhich of the following inequalities correctly represents the information?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "6 + x > 25", "isCorrect": False },
        { "text": "6 - x > 25", "isCorrect": False },
        { "text": "6 - x < 25", "isCorrect": False },
        { "text": "6 + x < 25", "isCorrect": True }
      ],
      "explanation": "The sum of pineapples (6) and oranges (x) is less than 25, which translates to 6 + x < 25."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "A school bought 56 pairs of games uniform for handball and netball teams. The handball team received 18 pairs.\nLet the number of pairs of uniform received by the netball team be represented by letter y.\nWhich of the following equations correctly represents the information?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "y - 18 = 56", "isCorrect": False },
        { "text": "18 - y = 56", "isCorrect": False },
        { "text": "18y = 56", "isCorrect": False },
        { "text": "y + 18 = 56", "isCorrect": True }
      ],
      "explanation": "The total uniforms equals the sum of netball and handball pairs: y + 18 = 56."
    }
]

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaMath2025 = ' + json.dumps(data, indent=2) + ';\n')

print('Questions 19-30 successfully appended to KPSEA Math 2025!')
