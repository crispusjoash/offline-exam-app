import json
import os

new_questions = [
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Learners are preparing to transplant their vegetable seedlings. Which one of the following garden tools will they require?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Fork jembe.", "isCorrect": False },
        { "text": "Trowel.", "isCorrect": True },
        { "text": "Panga.", "isCorrect": False },
        { "text": "Spade.", "isCorrect": False }
      ],
      "explanation": "A garden trowel is a small hand tool with a pointed, scoop-shaped metal blade, ideal for digging small holes and moving small amounts of soil when transplanting seedlings."
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "Crops require suitable seedbeds for planting. Which one of the following crops requires a fine seedbed?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Beans.", "isCorrect": False },
        { "text": "Maize.", "isCorrect": False },
        { "text": "Millet.", "isCorrect": True },
        { "text": "Pumpkin.", "isCorrect": False }
      ],
      "explanation": "Millet seeds are very tiny. Tiny seeds require a fine seedbed (soil broken down into very small, fine particles) to ensure good soil-to-seed contact for germination. Beans, maize, and pumpkins have large seeds and can be planted in a rougher seedbed."
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "Teacher Juliani asked his learners to write how different methods of cooking are carried out. Which one of the following statements they wrote is **true** about baking?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Food is cooked using dry heat.", "isCorrect": True },
        { "text": "Cooking food immersed in water at high temperatures.", "isCorrect": False },
        { "text": "Melted fat from the foods is used to cook the same food.", "isCorrect": False },
        { "text": "Cooking food while immersed in oil.", "isCorrect": False }
      ],
      "explanation": "Baking is a method of cooking food that uses prolonged dry heat, normally in an oven. (Option B is boiling, C describes roasting, and D is deep-frying)."
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "Jim always gets tired quickly whenever he is playing football with his friends. Which of the following **groups** of food should he increase in his diet?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Carbohydrates.", "isCorrect": True },
        { "text": "Proteins.", "isCorrect": False },
        { "text": "Minerals.", "isCorrect": False },
        { "text": "Vitamins.", "isCorrect": False }
      ],
      "explanation": "Carbohydrates are energy-giving foods. If Jim gets tired quickly, he lacks energy and needs to consume more carbohydrates to fuel his physical activities."
    },
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Puma, Suma, Lama and Rama prepared lunch for their families. Who among them prepared a **healthy** meal?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "**Puma** - rice, chapati, potato stew and juice.", "isCorrect": False },
        { "text": "**Suma** - ugali, beef stew, steamed spinach and mangoes.", "isCorrect": True },
        { "text": "**Lama** - cake, mandazi, fried eggs and soda.", "isCorrect": False },
        { "text": "**Rama** - fried chips, deep fried chicken, sausage and soda.", "isCorrect": False }
      ],
      "explanation": "A healthy, balanced meal must contain carbohydrates (ugali), proteins (beef stew), and vitamins/minerals (spinach and mangoes). Suma's meal perfectly represents a balanced diet, unlike the others which are overloaded with carbohydrates or junk food."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Emily wants to stew meat for her family. Which of the following is one of the **correct** steps she will follow.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ensure water covers the meat being stewed.", "isCorrect": False },
        { "text": "Stir the meat well and serve when cold.", "isCorrect": False },
        { "text": "Add salt to taste when serving the meat.", "isCorrect": False },
        { "text": "Reduce heat and allow the meat to cook.", "isCorrect": True }
      ],
      "explanation": "Stewing is a slow cooking method where food is cooked in a small amount of liquid over low heat (simmering). Therefore, reducing the heat and allowing the meat to cook slowly is the correct step."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "Grade 6 learners were searching on the internet for the reasons for preserving vegetables. Which of the following is one of the **correct** reasons they found?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "To make them easy to cook.", "isCorrect": False },
        { "text": "To ensure they are hygienic before use.", "isCorrect": False },
        { "text": "To be available at a cheap price.", "isCorrect": False },
        { "text": "To be available when out of season.", "isCorrect": True }
      ],
      "explanation": "Preservation prevents food from spoiling, allowing it to be stored for a long time so that it can be consumed when it is naturally out of season."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Grade 6 learners normally carry out the following activities when cleaning their classroom.\n\n(i) dust windows, chairs, tables and desks\n(ii) sweep the class, dispose of waste in a dust bin and take it to the rubbish pit\n(iii) arrange the furniture after cleaning\n(iv) mop the class and allow to dry\n(v) clean and store the cleaning materials and tools properly\n\nWhich of the following shows the **correct order** of activities?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i), (ii), (iii), (iv), (v).", "isCorrect": False },
        { "text": "(ii), (iv), (i), (iii), (v).", "isCorrect": False },
        { "text": "(i), (ii), (iv), (iii), (v).", "isCorrect": True },
        { "text": "(ii), (i), (iv), (iii), (v).", "isCorrect": False }
      ],
      "explanation": "The correct sequence for cleaning a room is: first dust from top to bottom (i), then sweep the floor (ii), then mop (iv), then arrange the furniture back in place (iii), and finally clean and store the cleaning equipment (v)."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "Peter was asked to write how his family conserves cooking gas at home. One of the **correct** ways he wrote is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "light the match stick before turning on the gas", "isCorrect": True },
        { "text": "cut foods in large chunks before cooking", "isCorrect": False },
        { "text": "avoiding touching gas cylinders with wet hands", "isCorrect": False },
        { "text": "refill gas cylinder occasionally.", "isCorrect": False }
      ],
      "explanation": "Lighting the matchstick before turning on the gas ensures that gas is ignited immediately, preventing unburned gas from escaping and wasting fuel. (Cutting food into smaller chunks, not larger ones, conserves fuel by cooking faster)."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Sela's house has an earthen floor. She wants to sweep it. Which one of the following is the reason why Sela should close all the windows and doors before sweeping?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "To keep off dirt when sweeping the house.", "isCorrect": False },
        { "text": "To make her sweep the whole house faster.", "isCorrect": False },
        { "text": "To prevent dirt from being blown about by the wind.", "isCorrect": True },
        { "text": "To avoid interference from the other family members.", "isCorrect": False }
      ],
      "explanation": "Closing windows and doors prevents wind/drafts from blowing the dust and dirt around the house while sweeping an earthen floor."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Mkubwa always wears clean school uniform. Which one of the following is a reason for wearing clean uniform?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "To feel good about himself.", "isCorrect": True },
        { "text": "To do all his class work well.", "isCorrect": False },
        { "text": "To make his classmates happy.", "isCorrect": False },
        { "text": "To be liked by others.", "isCorrect": False }
      ],
      "explanation": "Wearing clean clothes promotes good personal hygiene, prevents diseases, and boosts self-esteem, making one feel good and confident about themselves."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "Grade 6 learners were talking about the process of soaking in laundry work. Which of the following **correctly** describes what they said about soaking? Soaking is done in",
      "questionType": "multiple-choice",
      "options": [
        { "text": "clean warm water for some time before washing", "isCorrect": False },
        { "text": "clean cold water for some time before washing", "isCorrect": False },
        { "text": "warm soapy water for some time before washing", "isCorrect": False },
        { "text": "cold soapy water for some time before washing.", "isCorrect": True }
      ],
      "explanation": "Soaking heavily soiled clothes in cold soapy water before washing helps loosen the dirt effectively without setting protein-based stains (which warm water would do)."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "Jenny wants to make a scarf for her grandson. Which of the following **stitches** would you advise her to use?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Stem stitch.", "isCorrect": False },
        { "text": "Chain stitch.", "isCorrect": False },
        { "text": "Single crotchet.", "isCorrect": True },
        { "text": "Satin stitch.", "isCorrect": False }
      ],
      "explanation": "Single crochet is a foundational crochet stitch used to create entire articles of clothing, such as a scarf. Stem, chain, and satin stitches are embroidery stitches used for decorating existing fabrics."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "The head teacher of Bidii primary school advised the learners to always repair their uniform when torn. Why is this important?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "For the uniform not to have creases.", "isCorrect": False },
        { "text": "For the uniform to look neat.", "isCorrect": True },
        { "text": "For the uniform to fit well.", "isCorrect": False },
        { "text": "For the uniform to be clean.", "isCorrect": False }
      ],
      "explanation": "Repairing torn clothes (like mending or darning) ensures they look neat and presentable, and prevents the tear from getting worse."
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

print("Batch 4 questions inserted successfully!")
