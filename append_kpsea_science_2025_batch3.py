import json

new_questions = [
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "The following diagram represents a human circulatory system labelled K, L, M and N.\n\n[Image: Diagram of circulatory system with Lungs, Heart, and Body Organs. L connects lungs to the left side of heart. M is the left auricle. N connects the left ventricle to Body Organs. K connects Body Organs to the right side of the heart.]\n\nWhich one of the following correctly represents the parts labelled K, L, M and N?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "K: Vena cava, L: Pulmonary vein, M: Left auricle, N: Aorta", "isCorrect": True },
        { "text": "K: Aorta, L: Pulmonary artery, M: Right auricle, N: Vena cava", "isCorrect": False },
        { "text": "K: Aorta, L: Pulmonary vein, M: Right auricle, N: Vena cava", "isCorrect": False },
        { "text": "K: Vena cava, L: Pulmonary artery, M: Left auricle, N: Aorta", "isCorrect": False }
      ],
      "explanation": "L carries oxygenated blood from lungs to the heart (Pulmonary vein). M is the upper left chamber of the heart (Left auricle). N carries oxygenated blood from the heart to body organs (Aorta). K carries deoxygenated blood from body organs back to the heart (Vena cava)."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "The following diagram shows how a carpenter used a hammer as a lever.\n\n[Image: A hand holding a hammer handle at M, pulling a nail at P out of wood Q. N is the neck of the hammer resting on the wood.]\n\nWhich letter represents the pivot?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "M", "isCorrect": False },
        { "text": "N", "isCorrect": True },
        { "text": "P", "isCorrect": False },
        { "text": "Q", "isCorrect": False }
      ],
      "explanation": "In a lever, the pivot (or fulcrum) is the turning point. N is the point where the hammer rests on the wood and turns to pull out the nail, so it represents the pivot."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "A learner demonstrated heat transfer as shown in the following picture.\n\n[Image: A hand holding a wooden rod, the other end of the rod is in a candle flame.]\n\nThe heat did not reach the hand because",
      "questionType": "multiple-choice",
      "options": [
        { "text": "candle is a poor conductor of heat", "isCorrect": False },
        { "text": "heat was transferred upwards", "isCorrect": False },
        { "text": "heat from the candle was not enough", "isCorrect": False },
        { "text": "wood is a poor conductor of heat.", "isCorrect": True }
      ],
      "explanation": "Wood is a non-metal and an insulator, meaning it is a poor conductor of heat. Therefore, heat from the flame did not travel along the wooden rod to the hand."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "While searching for information on the uses of heat, a learner came across the following picture.\n\n[Image: A person cooking using a frying pan over a gas flame]\n\nWhat safety measure should have been observed by the person cooking?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Wearing gloves.", "isCorrect": True },
        { "text": "Using one hand.", "isCorrect": False },
        { "text": "Using a bigger pan.", "isCorrect": False },
        { "text": "Putting hands in cold water.", "isCorrect": False }
      ],
      "explanation": "When cooking or handling hot items, it is important to wear protective gloves (like oven gloves) to prevent burns from heat transfer."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "During a lesson, learners listed the following as characteristics of vertebrates:\n(i) have fins\n(ii) body covered with scales\n(iii) body temperature varies with the surrounding\n(iv) breathe using gills\n\nWhich two characteristics are only found in fish?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) and (ii)", "isCorrect": False },
        { "text": "(i) and (iv)", "isCorrect": True },
        { "text": "(ii) and (iii)", "isCorrect": False },
        { "text": "(iii) and (iv)", "isCorrect": False }
      ],
      "explanation": "Reptiles also have scales (ii), and amphibians/reptiles also have varying body temperatures (iii). Having fins (i) and breathing using gills (iv) are characteristics unique to fish among adult vertebrates."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "The following picture shows a crop established on a special seedbed.\n\n[Image: A crop grown in sunken beds dug below the ground level.]\n\nWhy was the special seedbed used to establish the crop? To",
      "questionType": "multiple-choice",
      "options": [
        { "text": "conserve water", "isCorrect": True },
        { "text": "control soil erosion", "isCorrect": False },
        { "text": "protect the crop from pests", "isCorrect": False },
        { "text": "control weeds.", "isCorrect": False }
      ],
      "explanation": "The image shows sunken seedbeds, which are dug below the surrounding ground level. They are used primarily in dry areas to collect and conserve water for the crop."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "While walking to school, a Grade 6 learner observed a piece of land affected by rill erosion.\n\nWhich of the following statements describes what the learner observed?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Deep U-shaped trenches.", "isCorrect": False },
        { "text": "Small V-shaped trenches.", "isCorrect": True },
        { "text": "Small holes left by detached soil.", "isCorrect": False },
        { "text": "Stones left after removal of soil.", "isCorrect": False }
      ],
      "explanation": "Rill erosion is characterized by the formation of small, shallow V-shaped trenches or channels on the ground surface."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "The type of soil erosion observed by the learner was most likely caused by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "strong wind", "isCorrect": False },
        { "text": "moving water", "isCorrect": True },
        { "text": "moving animals", "isCorrect": False },
        { "text": "road construction.", "isCorrect": False }
      ],
      "explanation": "Rill erosion is caused by moving water (surface runoff) that cuts small channels into the soil."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "Bright lights that blink at night were installed on a cattle shed.\n\nWhat was the purpose of the blinking lights? To",
      "questionType": "multiple-choice",
      "options": [
        { "text": "attract cattle to the shed", "isCorrect": False },
        { "text": "guide the milkman", "isCorrect": False },
        { "text": "keep off wild animals", "isCorrect": True },
        { "text": "make the cattle sleep.", "isCorrect": False }
      ],
      "explanation": "Blinking lights (such as 'lion lights') are an innovation used at night to scare away and keep off wild animals like predators from attacking livestock."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "Which other device can be used instead of the blinking lights?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Hole trap.", "isCorrect": False },
        { "text": "Innovative sound.", "isCorrect": True },
        { "text": "Insect catcher.", "isCorrect": False },
        { "text": "Rat trap.", "isCorrect": False }
      ],
      "explanation": "Innovative sound devices or noise makers can also be used as a deterrent to scare away wild animals from the cattle shed."
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

print("Batch 3 for KPSEA Science 2025 appended!")
