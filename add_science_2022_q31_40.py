import json

questions = [
    {
        "id": "kpsea-science-2022-q31",
        "questionNumber": 31,
        "questionText": "Grade 6 learners used their digital devices to get information on cleaning a charcoal *jiko* that was used for cooking. The following is the information:\n\n* (i) Empty the *jiko*.\n* (ii) Let the *jiko* cool.\n* (iii) Leave it in an airy place to dry.\n* (iv) Wipe the metal parts with a cloth wrung out of warm soapy water.\n\nWhich of the following shows the correct order the learners can follow when cleaning the *jiko*?",
        "questionType": "mcq",
        "options": [
            {"text": "(ii), (i), (iv), (iii)", "isCorrect": True},
            {"text": "(i), (ii), (iv), (iii)", "isCorrect": False},
            {"text": "(i), (iii), (ii), (iv)", "isCorrect": False},
            {"text": "(ii), (i), (iii), (iv)", "isCorrect": False}
        ],
        "explanation": "Safety comes first. The *jiko* must be allowed to cool (ii) before doing anything else. Then, empty the ashes (i), wipe the metal parts (iv), and finally leave it to dry (iii)."
    },
    {
        "id": "kpsea-science-2022-q32",
        "questionNumber": 32,
        "questionText": "Wanjala was told by her parents to be cleaning utensils immediately after use. Why do you think this is important?",
        "questionType": "mcq",
        "options": [
            {"text": "To make the utensil last long.", "isCorrect": False},
            {"text": "To prevent them from staining.", "isCorrect": True},
            {"text": "To prevent them from cracking.", "isCorrect": False},
            {"text": "To make them shine after washing.", "isCorrect": False}
        ],
        "explanation": "Cleaning utensils immediately after use prevents food remnants from drying, hardening, or permanently staining the utensils."
    },
    {
        "id": "kpsea-science-2022-q33",
        "questionNumber": 33,
        "questionText": "Loima and Ole-Kina are talking about the importance of mending clothes before washing. Loima tells Ole-Kina that we mend clothes before washing to",
        "questionType": "mcq",
        "options": [
            {"text": "prevent the clothes from getting creased", "isCorrect": False},
            {"text": "make the clothes look new after washing", "isCorrect": False},
            {"text": "prevent further damage to the clothes", "isCorrect": True},
            {"text": "retain the original colour of the clothes.", "isCorrect": False}
        ],
        "explanation": "Washing involves agitation and rubbing, which can easily enlarge small tears or loose seams. Mending clothes before washing prevents further damage."
    },
    {
        "id": "kpsea-science-2022-q34",
        "questionNumber": 34,
        "questionText": "The diagram below shows a symbol found on a care label attached on a shirt.\n\nWhat is the meaning of the symbol?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q34",
        "options": [
            {"text": "Wash by hand.", "isCorrect": False},
            {"text": "Do not bleach.", "isCorrect": True},
            {"text": "Do not dry clean.", "isCorrect": False},
            {"text": "Dry on a clothes line.", "isCorrect": False}
        ],
        "explanation": "A triangle on a laundry care label represents bleaching. A triangle with a cross (X) through it means \"Do not bleach\"."
    },
    {
        "id": "kpsea-science-2022-q35",
        "questionNumber": 35,
        "questionText": "Kola wants to make a neck scarf to give his grandfather as a gift. Which one of the following is not a method he can use to make the neck scarf?",
        "questionType": "mcq",
        "options": [
            {"text": "Sewing.", "isCorrect": True},
            {"text": "Knitting.", "isCorrect": False},
            {"text": "Weaving.", "isCorrect": False},
            {"text": "Crotcheting.", "isCorrect": False}
        ],
        "explanation": "Knitting, weaving, and crocheting are methods of creating fabric or garments from yarn. Sewing is a method of joining existing pieces of fabric together, so it is not a primary method to \"make\" the scarf fabric from scratch."
    },
    {
        "id": "kpsea-science-2022-q36",
        "questionNumber": 36,
        "questionText": "Learners were asked to outline the process of performing long jump. Which of the following is the correct process?",
        "questionType": "mcq",
        "options": [
            {"text": "Flight, take-off, approach, landing.", "isCorrect": False},
            {"text": "Approach, take-off, flight, landing.", "isCorrect": True},
            {"text": "Take-off, landing, approach, flight.", "isCorrect": False},
            {"text": "Landing, approach, take-off, flight.", "isCorrect": False}
        ],
        "explanation": "The correct sequence for the long jump is: Approach (running to gain speed), Take-off (jumping from the board), Flight (movement through the air), and Landing (touching down in the sandpit)."
    },
    {
        "id": "kpsea-science-2022-q37",
        "questionNumber": 37,
        "questionText": "Which of the following statements is true about safety when throwing javelin in the field?",
        "questionType": "mcq",
        "options": [
            {"text": "Only the thrower and the one to collect the thrown javelin should be in the throwing area.", "isCorrect": False},
            {"text": "The javelin may be thrown back to the throwing area after landing.", "isCorrect": False},
            {"text": "The thrown javelin should be caught while in the air to avoid breaking.", "isCorrect": False},
            {"text": "The thrower is the only player who is supposed to be in the throwing area.", "isCorrect": True}
        ],
        "explanation": "Javelins are dangerous projectiles. For safety, absolutely no one except the thrower should be in the throwing or landing area during a throw."
    },
    {
        "id": "kpsea-science-2022-q38",
        "questionNumber": 38,
        "questionText": "A soccer goalkeeper strained a thigh muscle during a football match. A first aider applied a bandage on the injured part. Why was the bandage applied?",
        "questionType": "mcq",
        "options": [
            {"text": "To stop bleeding.", "isCorrect": False},
            {"text": "To reduce swelling.", "isCorrect": True},
            {"text": "To immobilise the leg.", "isCorrect": False},
            {"text": "To use the first aid materials.", "isCorrect": False}
        ],
        "explanation": "In the case of a strain or sprain, a bandage (compression) is applied to limit blood flow to the injured area, which helps to reduce swelling."
    },
    {
        "id": "kpsea-science-2022-q39",
        "questionNumber": 39,
        "questionText": "Four athletes consumed different types of drinks before the race. Who among the four consumed the most appropriate drink for hydration?",
        "questionType": "mcq",
        "options": [
            {"text": "Peter drunk water.", "isCorrect": True},
            {"text": "James drunk porridge.", "isCorrect": False},
            {"text": "Sophia drunk milk.", "isCorrect": False},
            {"text": "Daisy drunk coffee.", "isCorrect": False}
        ],
        "explanation": "Water is the best and most appropriate drink for simple hydration. Coffee can act as a diuretic, and milk or porridge are heavier and slower to digest before a race."
    },
    {
        "id": "kpsea-science-2022-q40",
        "questionNumber": 40,
        "questionText": "Which of the following activities would you and your friends engage in to enhance physical fitness?",
        "questionType": "mcq",
        "options": [
            {"text": "Sleeping for long hours so as to rest.", "isCorrect": False},
            {"text": "Swimming regulary with friends.", "isCorrect": True},
            {"text": "Eating balanced diet at all times.", "isCorrect": False},
            {"text": "Watching soccer games to learn the skills.", "isCorrect": False}
        ],
        "explanation": "Physical fitness is enhanced through regular physical exercise and activity, such as swimming regularly."
    }
]

with open('src/data/kpsea-science-2022.js', 'a', encoding='utf-8') as f:
    f.write(",\n")
    for i, q in enumerate(questions):
        json_str = json.dumps(q, indent=6)
        json_str = "    " + json_str.replace('\n', '\n    ')
        if i == len(questions) - 1:
            f.write(json_str + "\n")
        else:
            f.write(json_str + ",\n")
    f.write("  ]\n}\n")

print("Questions 31-40 appended successfully. File finalized.")
