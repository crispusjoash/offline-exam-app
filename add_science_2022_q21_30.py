import json

questions = [
    {
        "id": "kpsea-science-2022-q21",
        "questionNumber": 21,
        "questionText": "The picture below shows a farm produce after harvesting.\n\nWhy is the part labelled **G** left attached on the produce during harvesting?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q21",
        "options": [
            {"text": "For hanging during storage.", "isCorrect": False},
            {"text": "For holding during slicing.", "isCorrect": False},
            {"text": "To prevent spoilage.", "isCorrect": True},
            {"text": "To hold when carrying.", "isCorrect": False}
        ],
        "explanation": "The stalk (labelled G) on fruits like pumpkins, squashes, and watermelons is left attached after harvesting to seal the fruit. This prevents bacteria and fungi from entering the fruit, thereby preventing rapid spoilage."
    },
    {
        "id": "kpsea-science-2022-q22",
        "questionNumber": 22,
        "questionText": "A farmer planted maize as shown in the picture below to conserve soil water. Study the picture and answer questions 22 to 23.\n\nThe type of seedbed shown in the picture to grow maize is a",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q22-23",
        "options": [
            {"text": "container", "isCorrect": False},
            {"text": "shallow pit", "isCorrect": False},
            {"text": "sunken bed", "isCorrect": True},
            {"text": "moisture bed.", "isCorrect": False}
        ],
        "explanation": "The picture shows crops planted in a depression or trench lower than the surrounding ground level, which is characteristic of a sunken bed."
    },
    {
        "id": "kpsea-science-2022-q23",
        "questionNumber": 23,
        "questionText": "How does the seedbed in the picture help to conserve water?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q22-23",
        "options": [
            {"text": "Reduces evaporation.", "isCorrect": False},
            {"text": "Collects surface run-off.", "isCorrect": True},
            {"text": "Prevents effects of strong wind.", "isCorrect": False},
            {"text": "Protects soil from strong sun.", "isCorrect": False}
        ],
        "explanation": "Sunken beds are designed with a depression that traps and collects surface water run-off, directing it straight to the roots of the crops and preventing water from flowing away."
    },
    {
        "id": "kpsea-science-2022-q24",
        "questionNumber": 24,
        "questionText": "In the preparation of a nursery bed, Grade five learners used the garden tool shown below. Study the picture and answer questions 24 to 25.\n\nThe learners used the garden tool",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q24-25",
        "options": [
            {"text": "to lift seedlings from the nursery bed", "isCorrect": False},
            {"text": "for weeding the nursery bed", "isCorrect": False},
            {"text": "to measure the spacing for the crop", "isCorrect": False},
            {"text": "to level the nursery bed.", "isCorrect": True}
        ],
        "explanation": "The tool shown is a rake. In nursery bed preparation, a rake is primarily used to break down large soil clods, remove stones, and level the surface of the soil."
    },
    {
        "id": "kpsea-science-2022-q25",
        "questionNumber": 25,
        "questionText": "Which of the following caring practices should be carried out on the tool after use?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q24-25",
        "options": [
            {"text": "Oiling.", "isCorrect": False},
            {"text": "Painting.", "isCorrect": False},
            {"text": "Cleaning.", "isCorrect": True},
            {"text": "Sharpening.", "isCorrect": False}
        ],
        "explanation": "The most immediate and fundamental care practice after using any garden tool in the soil (like a rake) is to clean off the mud and dirt before storing it."
    },
    {
        "id": "kpsea-science-2022-q26",
        "questionNumber": 26,
        "questionText": "Mrs. Chacha always stuffs her leather shoes with old newspapers before storing. Which of the following is the reason for stuffing old newspapers? To",
        "questionType": "mcq",
        "options": [
            {"text": "prevent her shoes from becoming small", "isCorrect": False},
            {"text": "prevent her shoes from getting dirty", "isCorrect": False},
            {"text": "make her shoes dry completely", "isCorrect": False},
            {"text": "prevent her shoes from losing shape.", "isCorrect": True}
        ],
        "explanation": "Stuffing leather shoes with old newspapers helps to maintain their original shape and prevents them from creasing or collapsing while in storage."
    },
    {
        "id": "kpsea-science-2022-q27",
        "questionNumber": 27,
        "questionText": "Kwamboka is feeling unwell. She is showing the following symptoms: Fever, pain in the joints, headache and vomiting. Which of the following diseases is she suffering from?",
        "questionType": "mcq",
        "options": [
            {"text": "Malaria.", "isCorrect": True},
            {"text": "Cough.", "isCorrect": False},
            {"text": "Measles.", "isCorrect": False},
            {"text": "Chicken pox.", "isCorrect": False}
        ],
        "explanation": "Fever, joint pains, severe headache, and vomiting are the classic symptoms of malaria."
    },
    {
        "id": "kpsea-science-2022-q28",
        "questionNumber": 28,
        "questionText": "Kangu and Yala are helping to make a family budget. Which of the following is the reason why they are making a family budget? To",
        "questionType": "mcq",
        "options": [
            {"text": "make their family happy", "isCorrect": False},
            {"text": "buy expensive items", "isCorrect": False},
            {"text": "make good use of money", "isCorrect": True},
            {"text": "buy all the items in fashion.", "isCorrect": False}
        ],
        "explanation": "A family budget is a plan that helps a family allocate their income wisely to cover needs and savings, thereby making good use of money."
    },
    {
        "id": "kpsea-science-2022-q29",
        "questionNumber": 29,
        "questionText": "Grade 4 learners were asked by their Home Science teacher to make posters on the foods that make us healthy. Read what they wrote on the posters.\n\n* **Poster 1:** Beans, Meat, Eggs, Fish\n* **Poster 2:** Cassava, Rice, Bread, Ugali\n* **Poster 3:** Oranges, Spinach, Pineapples, Cabbages\n\nWhich of the posters contain foods that provide our body with energy?",
        "questionType": "mcq",
        "options": [
            {"text": "Poster 1", "isCorrect": False},
            {"text": "Poster 2", "isCorrect": True},
            {"text": "Poster 3", "isCorrect": False},
            {"text": "Posters 1 and 3.", "isCorrect": False}
        ],
        "explanation": "Foods that provide the body with energy are carbohydrates. Cassava, rice, bread, and ugali (in Poster 2) are all carbohydrate-rich energy-giving foods. Poster 1 lists proteins, and Poster 3 lists vitamins."
    },
    {
        "id": "kpsea-science-2022-q30",
        "questionNumber": 30,
        "questionText": "Joan wants to help her mother preserve cereals by drying in the sun. Which of the following shows the correct steps?",
        "questionType": "mcq",
        "options": [
            {"text": "Wash, dry completely and put in the sun.", "isCorrect": False},
            {"text": "Dry completely, pack in airtight bags", "isCorrect": False},
            {"text": "Dry completely, pack in bags and store.", "isCorrect": False},
            {"text": "Dry completely, pack in airtight bags, store in a dry place.", "isCorrect": True}
        ],
        "explanation": "For effective preservation, cereals must be dried completely in the sun to remove moisture, packed in airtight bags to prevent pests and moisture from entering, and finally stored in a dry place."
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

print("Questions 21-30 appended successfully.")
