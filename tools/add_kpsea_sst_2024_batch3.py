import json
import os

new_questions = [
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "Study the following map of Eastern Africa and use it to answer questions 31 and 32.\n\n[Image: Map of Eastern Africa indicating region F in the far north and route G showing migration from the northwest towards the south/southeast.]\n\nThe climatic region marked F is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "modified equatorial", "isCorrect": False },
        { "text": "modified tropical", "isCorrect": False },
        { "text": "desert", "isCorrect": True },
        { "text": "mountain.", "isCorrect": False }
      ],
      "explanation": "Region F is located in the northernmost part of Eastern Africa (Sudan), which falls under the desert climate zone, specifically part of the Sahara Desert."
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "Which language group migrated into Eastern Africa using the route marked G?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Nilotes.", "isCorrect": True },
        { "text": "Bantus.", "isCorrect": False },
        { "text": "Semites.", "isCorrect": False },
        { "text": "Cushites.", "isCorrect": False }
      ],
      "explanation": "Route G shows a migration pattern originating from the Nile Valley/Bahr el Ghazal area in modern-day South Sudan, moving southwards into East Africa. This is the historical migration route of the Nilotes."
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "Grade 6 learners are planning to harvest the beans they had planted. Which weather season is suitable for the activity?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Dry.", "isCorrect": True },
        { "text": "Cold.", "isCorrect": False },
        { "text": "Windy.", "isCorrect": False },
        { "text": "Rainy.", "isCorrect": False }
      ],
      "explanation": "Harvesting crops like beans is best done during the dry season to ensure the crops are properly dried, preventing them from rotting or germinating during storage."
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "Grade 4 learners created a corner in their class to showcase cultural items during a school cultural day. Which one of the following consists of cultural items only?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Baskets, beads, sufurias.", "isCorrect": False },
        { "text": "Calabash, arrows, carvings.", "isCorrect": True },
        { "text": "Gourds, drums, plates.", "isCorrect": False },
        { "text": "Stove, bows, pots.", "isCorrect": False }
      ],
      "explanation": "Calabashes, arrows, and carvings are purely traditional cultural artifacts. Items like sufurias (metal cooking pots), modern plates, and stoves are typically modern utilitarian items rather than traditional cultural artifacts."
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "Soil is one of the natural resources found in Hema school. The best way of taking care of this resource is by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "ploughing the soil repeatedly", "isCorrect": False },
        { "text": "starting a nature corner", "isCorrect": False },
        { "text": "treating the soil with chemicals", "isCorrect": False },
        { "text": "planting cover crops.", "isCorrect": True }
      ],
      "explanation": "Planting cover crops is an effective soil conservation method. It protects the soil from erosion by wind and water, helps retain moisture, and improves soil fertility."
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "During a radio lesson on 'beef farming in Kenya', a learner noted that imported beef products affect beef farming. This is because it may lead to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "increased prices of beef products", "isCorrect": False },
        { "text": "reduced market for local beef products", "isCorrect": True },
        { "text": "increased foreign exchange earnings", "isCorrect": False },
        { "text": "reduced import trade.", "isCorrect": False }
      ],
      "explanation": "Imported beef products compete directly with local beef. If imports are cheaper or readily available, they reduce the market share and demand for locally produced beef, hurting local farmers."
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Learners at Masomo school watched a video clip on the effects of mining on the environment. Which of the following is an effect they are likely to have observed? It",
      "questionType": "multiple-choice",
      "options": [
        { "text": "creates many sceneries", "isCorrect": False },
        { "text": "creates land for farming", "isCorrect": False },
        { "text": "leads to ugly landscape", "isCorrect": True },
        { "text": "leads to growth of dense vegetation.", "isCorrect": False }
      ],
      "explanation": "Mining, especially open-cast mining, often degrades the environment by leaving behind open pits, heaps of waste rock, and barren land, resulting in an ugly or degraded landscape."
    }
]

file_path = 'src/data/kpsea-sst-parta-2024.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('export const kpseaSstParta2024 = ', '').rstrip(';\n')
data = json.loads(json_str)

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2024 = ' + json.dumps(data, indent=2) + ';\n')

print("Batch 3 questions inserted successfully!")
