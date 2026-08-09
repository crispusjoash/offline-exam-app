import json

new_questions = [
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "Which of the following is not one of the safety measures Kevin should observe?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Putting the egg into the hot pan.", "isCorrect": True },
        { "text": "Do not splash water into the pan.", "isCorrect": False },
        { "text": "Keep flammable materials away.", "isCorrect": False },
        { "text": "Do not add oil to a wet pan.", "isCorrect": False }
      ],
      "explanation": "Putting the egg into the hot pan is a step in the cooking process, not a safety measure. The other three options are actual safety precautions to prevent accidents like fires or hot oil splashing."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Katana wants to buy a suit for his birthday. Which of the following is the main factor he should consider?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "The colour should match that of his other suits.", "isCorrect": False },
        { "text": "The colour should match that of his friend's suit.", "isCorrect": False },
        { "text": "The suit should have bright colours.", "isCorrect": False },
        { "text": "The suit should be well fitting.", "isCorrect": True }
      ],
      "explanation": "When buying clothes, the most important factor to consider is that the clothes fit the wearer properly."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "A nurse was invited to talk to Grade 6 learners on menstrual hygiene. Which of the following is a way of promoting menstrual hygiene that the nurse could have talked about?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Bathing every day.", "isCorrect": True },
        { "text": "Eating a balanced diet.", "isCorrect": False },
        { "text": "Applying body sprays.", "isCorrect": False },
        { "text": "Drinking plenty of water.", "isCorrect": False }
      ],
      "explanation": "Bathing every day is a key practice for promoting personal and menstrual hygiene to prevent infections and keep the body clean."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Your uncle wants to buy a household item after seeing advertisements. Which of the following would be an important point to consider before buying the item?\n\nChoose the item",
      "questionType": "multiple-choice",
      "options": [
        { "text": "with attractive advertisements", "isCorrect": False },
        { "text": "that is rare and imported", "isCorrect": False },
        { "text": "advertised by popular people", "isCorrect": False },
        { "text": "where all information is provided.", "isCorrect": True }
      ],
      "explanation": "Before buying an item, it is important to be a wise consumer by checking that all necessary information (like instructions, expiry dates, and ingredients) is provided, rather than just being persuaded by advertisements."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Musa cleaned a certain surface using the following procedure:\n(i) removing loose dust from the surface using a soft dry cloth\n(ii) cleaning the surface using a soft cloth wrung out of warm soapy water\n(iii) rinsing using a soft cloth wrung out of warm water\n(iv) drying the surface using a dry cloth\n(v) shining the surface using an old newspaper.\n\nWhich of the following surfaces did Musa clean?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Wooden surface.", "isCorrect": False },
        { "text": "Glass surface.", "isCorrect": True },
        { "text": "Cemented surface.", "isCorrect": False },
        { "text": "Earthen surface.", "isCorrect": False }
      ],
      "explanation": "The procedure of cleaning and then shining the surface using an old newspaper is specific to glass surfaces, such as windows, to remove streaks."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "Ada soaked her stained blouse in cold water until the stain dissolved.\nWhich stain did Ada's blouse have?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Chewing gum stain.", "isCorrect": False },
        { "text": "Rust stain.", "isCorrect": False },
        { "text": "Grass stain.", "isCorrect": False },
        { "text": "Blood stain.", "isCorrect": True }
      ],
      "explanation": "Blood is a protein stain. Protein stains should be soaked in cold water to dissolve them. Using hot water would 'cook' the protein and set the stain into the fabric."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "Karen was happy to learn about stitches in school. Below is a diagram showing one of the stitches she made.\n\n[Image: A diagram showing vertical stitches connected along the top edge]\n\nWhich stitch did Karen make?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Back stitch.", "isCorrect": False },
        { "text": "Loop stitch.", "isCorrect": True },
        { "text": "Hemming stitch.", "isCorrect": False },
        { "text": "Chain stitch.", "isCorrect": False }
      ],
      "explanation": "The diagram shows a loop stitch (also known as a blanket stitch), which is used along the edges of fabric to prevent fraying or for decoration."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "Michael's shirt has a damaged pocket and some loose stitches. Which of the following is a factor he will consider when repairing the damaged pocket? The",
      "questionType": "multiple-choice",
      "options": [
        { "text": "size of his shirt", "isCorrect": False },
        { "text": "size of the pocket", "isCorrect": False },
        { "text": "type of the needle", "isCorrect": False },
        { "text": "colour of the thread.", "isCorrect": True }
      ],
      "explanation": "When repairing torn clothes or loose stitches, it is important to consider the colour of the thread and ensure it matches the colour of the garment so that the repair looks neat."
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

print("Batch 6 for KPSEA Science 2025 appended!")
