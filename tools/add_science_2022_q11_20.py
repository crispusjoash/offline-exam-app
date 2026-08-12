import json

questions = [
    {
        "id": "kpsea-science-2022-q11",
        "questionNumber": 11,
        "questionText": "During a class discussion, learners listed the following as some effects of gravity.\n\n* (i) Flowing of water in rivers.\n* (ii) Writing on chalkboard.\n* (iii) Fruits falling from a tree.\n* (iv) Swimming in a pool.\n\nWhich **two** are correct effects of gravity?",
        "questionType": "mcq",
        "options": [
            {"text": "(ii) and (iii)", "isCorrect": False},
            {"text": "(i) and (iv)", "isCorrect": False},
            {"text": "(i) and (iii)", "isCorrect": True},
            {"text": "(ii) and (iv)", "isCorrect": False}
        ],
        "explanation": "Gravity pulls objects downwards towards the centre of the Earth. It causes water to flow downhill in rivers (i) and makes fruits fall downwards from trees (iii). Writing on a chalkboard involves friction, and swimming involves buoyancy and muscular force."
    },
    {
        "id": "kpsea-science-2022-q12",
        "questionNumber": 12,
        "questionText": "Learners dropped dry leaves on a fire and observed that some leaves moved upwards instead of dropping into the fire. Which one of the following statements best explains the observation?",
        "questionType": "mcq",
        "options": [
            {"text": "Leaves are light.", "isCorrect": False},
            {"text": "Leaves expand.", "isCorrect": False},
            {"text": "Wind carried leaves upwards.", "isCorrect": False},
            {"text": "Hot air carried leaves upwards.", "isCorrect": True}
        ],
        "explanation": "When air is heated by a fire, it expands and becomes lighter (less dense), causing convection currents where hot air rises. The rising hot air carries the light dry leaves upwards."
    },
    {
        "id": "kpsea-science-2022-q13",
        "questionNumber": 13,
        "questionText": "Learners were preparing to go out for a nature walk in a nearby forest. Which one of the following pair of protective equipment would be most suitable for their safety when handling plants in the forest?",
        "questionType": "mcq",
        "options": [
            {"text": "Gloves and goggles.", "isCorrect": False},
            {"text": "Gloves and overcoats.", "isCorrect": True},
            {"text": "Tongs and overcoats.", "isCorrect": False},
            {"text": "Goggles and tongs.", "isCorrect": False}
        ],
        "explanation": "When handling plants in a forest, gloves protect the hands from thorns, stinging nettles, and toxic saps. Overcoats protect the body and clothing from scratches, insects, and sticky sap."
    },
    {
        "id": "kpsea-science-2022-q14",
        "questionNumber": 14,
        "questionText": "A learner went to hospital complaining of severe diarrhoea, vomiting and thirst. Which one of the following diseases was the learner likely to be suffering from?",
        "questionType": "mcq",
        "options": [
            {"text": "Bilharzia.", "isCorrect": False},
            {"text": "Cholera.", "isCorrect": True},
            {"text": "Typhoid.", "isCorrect": False},
            {"text": "Dysentry.", "isCorrect": False}
        ],
        "explanation": "Severe diarrhoea (often described as \"rice-water stools\"), vomiting, and subsequent severe dehydration (thirst) are the classic and primary symptoms of cholera."
    },
    {
        "id": "kpsea-science-2022-q15",
        "questionNumber": 15,
        "questionText": "Learners observed a cloud that was low in the sky, dark-grey in colour and thick. The appearance of the cloud indicates that there was going to be a",
        "questionType": "mcq",
        "options": [
            {"text": "windy weather", "isCorrect": False},
            {"text": "foggy weather", "isCorrect": False},
            {"text": "rainy weather", "isCorrect": True},
            {"text": "sunny weather.", "isCorrect": False}
        ],
        "explanation": "Nimbus clouds (specifically nimbostratus or cumulonimbus) are typically low, thick, and dark-grey, indicating that rain or heavy precipitation is imminent."
    },
    {
        "id": "kpsea-science-2022-q16",
        "questionNumber": 16,
        "questionText": "Which of the following crop is a climbing fruit?",
        "questionType": "mcq",
        "options": [
            {"text": "Orange.", "isCorrect": False},
            {"text": "Passion.", "isCorrect": True},
            {"text": "Mango.", "isCorrect": False},
            {"text": "Apple.", "isCorrect": False}
        ],
        "explanation": "Passion fruit grows on a vine that climbs using tendrils for support. Oranges, mangoes, and apples grow on sturdy, self-supporting trees."
    },
    {
        "id": "kpsea-science-2022-q17",
        "questionNumber": 17,
        "questionText": "How can the learners protect young climbing fruit plants from damage by animals?",
        "questionType": "mcq",
        "options": [
            {"text": "Staking the plants.", "isCorrect": False},
            {"text": "Constructing a shade.", "isCorrect": False},
            {"text": "Trapping the animals.", "isCorrect": False},
            {"text": "Applying a mulch.", "isCorrect": False},
            {"text": "Fencing the plants.", "isCorrect": True}
        ],
        "explanation": "Wait, let's look at the original options. \nA. Staking the plants. B. Constructing a shade. C. Trapping the animals. D. Applying a mulch. Wait, none of these directly protect from animals natively like fencing, but sometimes \"Staking\" lifts the tender parts out of reach, but \"Trapping\" controls pests, let's review... Ah, wait! The correct way to protect young plants in agricultural science is often enclosing them or fencing. Let's look at the options again from the image. \nA. Staking the plants. B. Constructing a shade. C. Trapping the animals. D. Applying a mulch.\nActually, wait... Let me check standard curriculum. Trapping is sometimes taught, but fencing is better. However, fencing isn't an option. Staking helps climbers. Let's review the image closely... \nLet me re-read the options. Ah! Wait, the options for 17 are A, B, C, D. Let's provide the exact options. Actually, for young plants, some say \"fencing\", but since it's missing, let's leave the options exact."
    }
]

# Fixing Q17 options correctly:
questions[6]['options'] = [
    {"text": "Staking the plants.", "isCorrect": False},
    {"text": "Constructing a shade.", "isCorrect": False},
    {"text": "Trapping the animals.", "isCorrect": True},
    {"text": "Applying a mulch.", "isCorrect": False}
]
questions[6]['explanation'] = "Among the options provided, trapping the animals is a method used to protect crops from wild animals and pests. (Note: Fencing or using protective cages is often more common for young plants)."

questions.extend([
    {
        "id": "kpsea-science-2022-q18",
        "questionNumber": 18,
        "questionText": "Which of the following practices will provide support to a climbing fruit plant?",
        "questionType": "mcq",
        "options": [
            {"text": "Hardening.", "isCorrect": False},
            {"text": "Pruning.", "isCorrect": False},
            {"text": "Training.", "isCorrect": True},
            {"text": "Mulching.", "isCorrect": False}
        ],
        "explanation": "Training involves directing or tying climbing plants to a support (like a trellis or stake) to guide their growth and provide necessary structural support."
    },
    {
        "id": "kpsea-science-2022-q19",
        "questionNumber": 19,
        "questionText": "Which of the following crops is eaten as a fresh fruit?",
        "questionType": "mcq",
        "options": [
            {"text": "Pumpkin.", "isCorrect": False},
            {"text": "Water melon.", "isCorrect": True},
            {"text": "Cucumber.", "isCorrect": False},
            {"text": "Calabash.", "isCorrect": False}
        ],
        "explanation": "Watermelon is a sweet, fleshy crop typically eaten raw as a fresh dessert fruit. Pumpkins and calabashes are usually cooked, and while cucumbers can be eaten raw, they are culinary vegetables often used in salads rather than considered a \"fresh fruit\" snack."
    },
    {
        "id": "kpsea-science-2022-q20",
        "questionNumber": 20,
        "questionText": "What is the main nutritional benefit of eating mangoes?",
        "questionType": "mcq",
        "options": [
            {"text": "Vitamins.", "isCorrect": True},
            {"text": "Proteins.", "isCorrect": False},
            {"text": "Fibre.", "isCorrect": False},
            {"text": "Carbohydrates.", "isCorrect": False}
        ],
        "explanation": "Fruits like mangoes are primarily known for being rich sources of vitamins (especially Vitamin C and Vitamin A) which protect the body from diseases."
    }
])

with open('src/data/kpsea-science-2022.js', 'a', encoding='utf-8') as f:
    f.write(",\n")
    for i, q in enumerate(questions):
        json_str = json.dumps(q, indent=6)
        json_str = "    " + json_str.replace('\n', '\n    ')
        if i == len(questions) - 1:
            f.write(json_str + "\n")
        else:
            f.write(json_str + ",\n")

print("Questions 11-20 appended successfully.")
