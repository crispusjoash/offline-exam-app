import json

questions = [
    {
        "id": "kpsea-science-2022-q1",
        "questionNumber": 1,
        "questionText": "Learners went for a nature walk to study the importance of plants. They listed the following as the importance of plants.\nThey\n* (i) produce fruits\n* (ii) attract rain\n* (iii) beautify environment\n* (iv) protect soil\n* (v) produce nectar\n\nWhich **two** are true for flowering plants?",
        "questionType": "mcq",
        "options": [
            {"text": "(i) and (iii)", "isCorrect": False},
            {"text": "(i) and (v)", "isCorrect": True},
            {"text": "(ii) and (iv)", "isCorrect": False},
            {"text": "(iii) and (v)", "isCorrect": False}
        ],
        "explanation": "Flowering plants are uniquely characterised by the production of flowers, which contain nectar to attract pollinators, and eventually develop into fruits."
    },
    {
        "id": "kpsea-science-2022-q2",
        "questionNumber": 2,
        "questionText": "Grade 5 learners in a certain primary school grouped fungi with their use. Which of the following fungi was correctly matched to its use?\n\n| Fungi | Use |\n| :--- | :--- |\n| A. Yeast | preservation of beverages |\n| B. Toadstool | food for animals |\n| C. Mushroom | beauty of environment |\n| D. Penicillium | source of medicine |",
        "questionType": "mcq",
        "options": [
            {"text": "Yeast - preservation of beverages", "isCorrect": False},
            {"text": "Toadstool - food for animals", "isCorrect": False},
            {"text": "Mushroom - beauty of environment", "isCorrect": False},
            {"text": "Penicillium - source of medicine", "isCorrect": True}
        ],
        "explanation": "Penicillium is a type of fungus used to produce the antibiotic medicine penicillin. Yeast is used in baking and brewing, toadstools are often poisonous, and while mushrooms can be beautiful, their primary human use is often as food (for edible varieties)."
    },
    {
        "id": "kpsea-science-2022-q3",
        "questionNumber": 3,
        "questionText": "A learner observed that when food remains fell on the floor, the food was quickly covered by small ants which ate all of it.\n\nThis behaviour by the ants demonstrated that living things",
        "questionType": "mcq",
        "options": [
            {"text": "respond to changes in their environment", "isCorrect": True},
            {"text": "love eating food", "isCorrect": False},
            {"text": "hunt for food in their environment", "isCorrect": False},
            {"text": "hide after feeding.", "isCorrect": False}
        ],
        "explanation": "The ants detecting the food and moving towards it is a clear example of living things responding to stimuli (changes) in their environment."
    },
    {
        "id": "kpsea-science-2022-q4",
        "questionNumber": 4,
        "questionText": "In a certain family the water used for washing clothes is then used to clean the house. Water taps are also turned off when not in use. Which one of the following is true about the family? It conserves water by",
        "questionType": "mcq",
        "options": [
            {"text": "recycling and re-using", "isCorrect": False},
            {"text": "reducing only", "isCorrect": False},
            {"text": "re-using and reducing", "isCorrect": True},
            {"text": "recycling only.", "isCorrect": False}
        ],
        "explanation": "Using water meant for clothes to clean the house is **re-using**. Turning off taps when not in use is **reducing** water wastage."
    },
    {
        "id": "kpsea-science-2022-q5",
        "questionNumber": 5,
        "questionText": "While sweeping the classroom, Jane started sneezing and found it difficult to continue sweeping. What could Jane do to prevent sneezing and continue sweeping?",
        "questionType": "mcq",
        "options": [
            {"text": "Put on an overcoat.", "isCorrect": False},
            {"text": "Sprinkle water on the floor.", "isCorrect": True},
            {"text": "Wear gloves.", "isCorrect": False},
            {"text": "Change the broom she is using.", "isCorrect": False}
        ],
        "explanation": "Sprinkling water on the floor settles the dust, preventing it from rising into the air and causing sneezing."
    },
    {
        "id": "kpsea-science-2022-q6",
        "questionNumber": 6,
        "questionText": "During a lesson on fungi, the teacher warned learners not to pick mushrooms on their own for cooking. The reason why learners should follow their teacher's advice is that",
        "questionType": "mcq",
        "options": [
            {"text": "mushrooms have no nutrients", "isCorrect": False},
            {"text": "some mushrooms have worms", "isCorrect": False},
            {"text": "mushrooms are difficult to cook", "isCorrect": False},
            {"text": "some mushrooms are poisonous.", "isCorrect": True}
        ],
        "explanation": "Many species of wild mushrooms are highly poisonous and can be fatal if eaten. It is dangerous to pick them without expert knowledge."
    },
    {
        "id": "kpsea-science-2022-q7",
        "questionNumber": 7,
        "questionText": "The picture below shows a kettle with parts labelled L, M, N and P.\n\nWhich two parts are likely to be made of poor conductors of heat?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q7",
        "options": [
            {"text": "L and P", "isCorrect": False},
            {"text": "L and N", "isCorrect": False},
            {"text": "M and N", "isCorrect": False},
            {"text": "M and P", "isCorrect": True}
        ],
        "explanation": "Part **M** (the handle) and Part **P** (the lid knob) are handled by users, so they are made of poor conductors (insulators) like plastic or wood to prevent burns."
    },
    {
        "id": "kpsea-science-2022-q8",
        "questionNumber": 8,
        "questionText": "To control the COVID-19 pandemic, one of the measures taken is to clean hands. A learner noted that after using a sanitiser, hands dry up faster than when washed with water. This is because the sanitiser",
        "questionType": "mcq",
        "options": [
            {"text": "freezes quickly", "isCorrect": False},
            {"text": "is absorbed by the skin", "isCorrect": False},
            {"text": "condenses easily", "isCorrect": False},
            {"text": "evaporates easily.", "isCorrect": True}
        ],
        "explanation": "Sanitisers contain a high percentage of alcohol, which is highly volatile and evaporates much faster than water at room temperature."
    },
    {
        "id": "kpsea-science-2022-q9",
        "questionNumber": 9,
        "questionText": "After a discussion on composition of air, learners presented the information in a pie chart as shown below.\n\nWhich one of the following letters represents a gas that supports burning?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q9",
        "options": [
            {"text": "M", "isCorrect": False},
            {"text": "K", "isCorrect": True},
            {"text": "L", "isCorrect": False},
            {"text": "J", "isCorrect": False}
        ],
        "explanation": "The gas that supports burning is Oxygen, which makes up 21% of the air. In the standard pie chart, this is the second-largest portion (represented by letter K)."
    },
    {
        "id": "kpsea-science-2022-q10",
        "questionNumber": 10,
        "questionText": "The diagram below represents a beam balance that was constructed by learners to be used for comparing masses of objects.\n\nThe beam balance could not compare masses of objects because",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q10",
        "options": [
            {"text": "the arm was fixed", "isCorrect": True},
            {"text": "a wooden arm was used", "isCorrect": False},
            {"text": "wires were used instead of thread", "isCorrect": False},
            {"text": "similar tins were used.", "isCorrect": False}
        ],
        "explanation": "In the diagram, the beam (wooden arm) is shown nailed tightly with two nails at the pivot. A beam balance requires a free-swinging pivot to tip and compare masses. If the arm is fixed, it cannot swing."
    }
]

with open('src/data/kpsea-science-2022.js', 'a', encoding='utf-8') as f:
    for i, q in enumerate(questions):
        json_str = json.dumps(q, indent=6)
        # Fix indentation for neatness
        json_str = "    " + json_str.replace('\n', '\n    ')
        if i == len(questions) - 1:
            f.write(json_str + "\n")
        else:
            f.write(json_str + ",\n")

print("Questions 1-10 appended successfully.")
