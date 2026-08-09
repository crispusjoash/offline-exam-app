import json

new_questions = [
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "The following are some of the reasons for rearing domestic animals:\n(i) alert on presence of strangers\n(ii) provide fur and skins\n(iii) provide manure\n(iv) provide meat\n(v) scare away, catch and eat rats.\n\nWhich of the following domestic animals is reared for most of the listed reasons?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Cat.", "isCorrect": False },
        { "text": "Chicken.", "isCorrect": False },
        { "text": "Dog.", "isCorrect": False },
        { "text": "Rabbit.", "isCorrect": True }
      ],
      "explanation": "Rabbits provide fur/skins, manure, and meat (3 reasons). Dogs mainly alert on strangers, and cats catch rats. Therefore, the rabbit is reared for most of the listed reasons."
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "Which of the following planting materials is used to establish kales from a nursery bed?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Seeds.", "isCorrect": True },
        { "text": "Vines.", "isCorrect": False },
        { "text": "Splits.", "isCorrect": False },
        { "text": "Stem cuttings.", "isCorrect": False }
      ],
      "explanation": "Kales (sukuma wiki) are propagated by planting their seeds in a nursery bed before transplanting the seedlings to the main field."
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Grade 5 learners used the garden tool shown in the picture on a tree nursery. Use the picture to answer questions 37 and 38.\n\n[Image: A panga or machete]\n\nWhat was the appropriate use of the tool on the tree nursery?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Applying fertilizer during transplanting.", "isCorrect": False },
        { "text": "Lifting seedlings during transplanting.", "isCorrect": False },
        { "text": "Pruning roots of seedlings.", "isCorrect": True },
        { "text": "Carrying manure.", "isCorrect": False }
      ],
      "explanation": "A panga is a cutting tool used in a nursery for activities like pruning roots of seedlings during transplanting."
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "For the tool to function well, it should be",
      "questionType": "multiple-choice",
      "options": [
        { "text": "cleaned", "isCorrect": False },
        { "text": "sharpened", "isCorrect": True },
        { "text": "oiled", "isCorrect": False },
        { "text": "painted.", "isCorrect": False }
      ],
      "explanation": "For a cutting tool like a panga to function effectively (cut well), its cutting edge needs to be sharpened."
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "Jay wants to build strong muscles in order to play in the school football team.\n\nWhich food group should he increase in his diet?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Carbohydrates.", "isCorrect": False },
        { "text": "Vitamins.", "isCorrect": False },
        { "text": "Proteins.", "isCorrect": True },
        { "text": "Fats.", "isCorrect": False }
      ],
      "explanation": "Proteins are body-building foods. They are necessary for the growth and repair of body tissues and for building strong muscles."
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "Kalu wants to bake a cake. Which of the following can he use as an improvised baking tin?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Melamine bowl.", "isCorrect": False },
        { "text": "Hot sand.", "isCorrect": False },
        { "text": "Plastic bowl.", "isCorrect": False },
        { "text": "Sufuria.", "isCorrect": True }
      ],
      "explanation": "A sufuria (a metal cooking pot) can withstand high baking temperatures without melting, making it suitable as an improvised baking tin. Plastic or melamine would melt or get damaged."
    },
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "A Grade 6 learner was asked by his teacher to explain the meaning of stewing food.\n\nWhich of the following would the learner give as the correct meaning?\n\nStewing food is cooking food",
      "questionType": "multiple-choice",
      "options": [
        { "text": "using steam", "isCorrect": False },
        { "text": "using dry heat", "isCorrect": False },
        { "text": "in water under low heat", "isCorrect": True },
        { "text": "in water under high heat.", "isCorrect": False }
      ],
      "explanation": "Stewing is a slow method of cooking where food is cooked in a small amount of liquid (like water) over low heat for a long time."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Use the following statement to answer questions 42 and 43.\nKevin wants to shallow fry an egg for breakfast using the following steps:\n(i) pour the beaten egg into the pan\n(ii) heat a little oil in a frying pan\n(iii) beat the egg in a bowl using a fork\n(iv) fry the egg and turn using a flat spoon and fry the other side.\n\nWhich is the correct order of steps Kevin should follow?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(iii), (iv), (i), (ii)", "isCorrect": False },
        { "text": "(iii), (ii), (i), (iv)", "isCorrect": True },
        { "text": "(iv), (i), (ii), (iii)", "isCorrect": False },
        { "text": "(iv), (i), (iii), (ii)", "isCorrect": False }
      ],
      "explanation": "First, beat the egg in a bowl (iii). Second, heat a little oil in a pan (ii). Third, pour the beaten egg into the pan (i). Finally, fry and turn to fry the other side (iv)."
    }
]

file_path = 'src/data/kpsea-science-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('{'):content.rfind('}')+1]
data = json.loads(json_str)

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaScience2025 = ' + json.dumps(data, indent=2) + ';\\n')

print("Batch 5 for KPSEA Science 2025 appended!")
