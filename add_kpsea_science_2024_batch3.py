import json
import os

new_questions = [
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "A monkey was observed damaging a creeping fruit crop by feeding on mature fruits. Use this information to answer questions **29** to **31**.\n\nThe fruit crop is **more** likely to be",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Pawpaw", "isCorrect": False },
        { "text": "Guava", "isCorrect": False },
        { "text": "Mango", "isCorrect": False },
        { "text": "Watermelon.", "isCorrect": True }
      ],
      "explanation": "Pawpaw, guava, and mango are fruits that grow on trees. Watermelon is a fruit that grows on a creeping vine along the ground."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "The crop can be protected from the monkey by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "poisoning the animal", "isCorrect": False },
        { "text": "trapping and killing the animal", "isCorrect": False },
        { "text": "use of dogs to attack and kill it", "isCorrect": False },
        { "text": "use of scare crows.", "isCorrect": True }
      ],
      "explanation": "Killing wild animals (via poison, traps, or dogs) is illegal and discouraged for wildlife conservation. Using scarecrows is a safe, non-lethal method of deterring wild animals from crops."
    },
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "Which other creeping crop provides vitamins?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Tree tomato.", "isCorrect": False },
        { "text": "Orange.", "isCorrect": False },
        { "text": "Avocado.", "isCorrect": False },
        { "text": "Strawberry.", "isCorrect": True }
      ],
      "explanation": "Tree tomato, orange, and avocado grow on trees. Strawberries grow on small creeping plants (runners) and are a rich source of vitamins."
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "The following pictures show cabbage at different stages of growth. Use them to answer questions **32** and **33**.\n\n[Image: 4 stages of cabbage growth labelled E, F, G, H. Picture F shows a firm, compact head.]\n\nWhich picture shows the **correct** stage of harvesting?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "E", "isCorrect": False },
        { "text": "F", "isCorrect": True },
        { "text": "G", "isCorrect": False },
        { "text": "H", "isCorrect": False }
      ],
      "explanation": "Cabbages are ready for harvesting when the head is fully formed, firm, and compact, which is depicted in picture F."
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "The cabbage is harvested by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "cutting the head", "isCorrect": False },
        { "text": "cutting the stem", "isCorrect": True },
        { "text": "uprooting the crop", "isCorrect": False },
        { "text": "plucking the leaves.", "isCorrect": False }
      ],
      "explanation": "The proper way to harvest a cabbage is by cutting the stem at the base of the head using a sharp knife or panga."
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "A Grade 4 learner classified black night shade, lettuce, spider weed, cabbage, kales and coriander into the same group. Which one of the following features did the learner use to classify the vegetables?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Leaves.", "isCorrect": True },
        { "text": "Flowers.", "isCorrect": False },
        { "text": "Fruits.", "isCorrect": False },
        { "text": "Pods.", "isCorrect": False }
      ],
      "explanation": "All the listed plants (lettuce, cabbage, kales, etc.) are leafy vegetables. The leaves are the primary part harvested and consumed."
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "The following picture shows an innovative garden used by learners to grow indigenous vegetables. Use the picture to answer questions **35** and **36**.\n\n[Image: A hanging garden with potted plants suspended in the air.]\n\nThe **main** reason for growing vegetables using this type of garden is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "conserve moisture", "isCorrect": False },
        { "text": "reuse containers", "isCorrect": False },
        { "text": "use limited space", "isCorrect": True },
        { "text": "control crop diseases.", "isCorrect": False }
      ],
      "explanation": "Hanging gardens or vertical gardens are innovative farming methods designed to maximize crop production in areas where ground space is very limited."
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "The **best** way learners can improve the growth rate of their vegetables is by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "applying manure on the garden", "isCorrect": True },
        { "text": "spraying chemicals to kill weeds", "isCorrect": False },
        { "text": "mulching the crop to cover weeds", "isCorrect": False },
        { "text": "irrigating the crop.", "isCorrect": False }
      ],
      "explanation": "While watering is essential for survival, applying manure directly adds essential nutrients to the soil, which significantly improves the growth rate and health of the vegetables."
    }
]

file_path = 'src/data/kpsea-science-2024.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('export const kpseaScience2024 = ', '').rstrip(';\n')
data = json.loads(json_str)

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaScience2024 = ' + json.dumps(data, indent=2) + ';\n')

print("Batch 3 questions inserted successfully!")
