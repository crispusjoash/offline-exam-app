import json

new_questions = [
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "Study the following map of Eastern Africa and use it to answer questions 31 to 33.\n\n[Image: Map of Eastern Africa. K is a shaded region along the eastern coast. L shows migration arrows from the Horn of Africa. M points to a National Park in Western Uganda.]\n\nIdentify the shaded climatic region marked K.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Desert", "isCorrect": False },
        { "text": "Maritime", "isCorrect": True },
        { "text": "Sub-tropical", "isCorrect": False },
        { "text": "Modified equatorial", "isCorrect": False }
      ],
      "explanation": "The shaded region K lies along the coast of the Indian Ocean (coast of Somalia and Kenya), which experiences a Maritime (or Coastal Tropical) climate."
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "Which language group migrated to Eastern Africa through the route marked L?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Nilotes", "isCorrect": False },
        { "text": "Semites", "isCorrect": False },
        { "text": "Bantus", "isCorrect": False },
        { "text": "Cushites", "isCorrect": True }
      ],
      "explanation": "The arrows for route L originate from the Horn of Africa, which is the original homeland of the Cushites before they migrated into East Africa."
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "Identify the national park marked M.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ruwenzori", "isCorrect": False },
        { "text": "Kibale", "isCorrect": False },
        { "text": "Queen Elizabeth", "isCorrect": True },
        { "text": "Murchison falls", "isCorrect": False }
      ],
      "explanation": "National Park M is located in south-western Uganda around Lakes Edward and George, which corresponds to Queen Elizabeth National Park."
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "The following diagram shows an instrument used to measure an element of weather.\n\n[Image: A simple barometer with an inverted glass tube in a trough containing liquid X.]\n\nThe substance marked X is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "water", "isCorrect": False },
        { "text": "alcohol", "isCorrect": False },
        { "text": "spirit", "isCorrect": False },
        { "text": "mercury.", "isCorrect": True }
      ],
      "explanation": "The instrument shown is a simple mercury barometer, which is used to measure atmospheric pressure. The liquid X in the trough and tube is mercury."
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "The highlands of Eastern Africa have high population density. The high population density in these areas is likely to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "improve standards of living", "isCorrect": False },
        { "text": "increase agricultural production", "isCorrect": False },
        { "text": "increase urban to rural migration", "isCorrect": False },
        { "text": "increase labour supply.", "isCorrect": True }
      ],
      "explanation": "A high population density means there are many people living in the area, which directly leads to an increase in the available labour supply."
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "Grade 6 learners visited a horticultural farm near their school. Which of the following group of crops are they likely to find?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Cabbages, roses, pineapples.", "isCorrect": True },
        { "text": "Maize, oranges, carrots.", "isCorrect": False },
        { "text": "Tomatoes, grapes, wheat.", "isCorrect": False },
        { "text": "Onions, kales, cotton.", "isCorrect": False }
      ],
      "explanation": "Horticulture involves the growing of vegetables, fruits, and flowers. Cabbages (vegetables), roses (flowers), and pineapples (fruits) are all horticultural crops. Maize, wheat, and cotton are not."
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "While reading about tourism, a learner found out that the number of tourists who visited Eastern Africa in 2020 and 2021 reduced drastically. What was the likely cause of the decline?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Threat of terrorism.", "isCorrect": False },
        { "text": "Prolonged drought.", "isCorrect": False },
        { "text": "COVID-19 pandemic.", "isCorrect": True },
        { "text": "Tribal clashes.", "isCorrect": False }
      ],
      "explanation": "The global COVID-19 pandemic severely restricted international travel and caused a drastic reduction in tourism worldwide during 2020 and 2021."
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "Rashid was taken to the Chief Magistrate's court by a neighbour over a disagreement on land boundary.\n\nWhich type of conflict resolution was applied in this case?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Arbitration", "isCorrect": False },
        { "text": "Reconciliation", "isCorrect": False },
        { "text": "Litigation", "isCorrect": True },
        { "text": "Mediation", "isCorrect": False }
      ],
      "explanation": "Litigation is the process of resolving disputes by taking the matter to a court of law, as was done in this case (Chief Magistrate's court)."
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "The county governments in Kenya should mainly spend their revenue on",
      "questionType": "multiple-choice",
      "options": [
        { "text": "paying water bills", "isCorrect": False },
        { "text": "paying salaries for county workers", "isCorrect": False },
        { "text": "meeting workers' transport costs", "isCorrect": False },
        { "text": "implementing development projects.", "isCorrect": True }
      ],
      "explanation": "While revenue is used to pay salaries and run the government, the primary and main purpose of government revenue is to implement development projects and provide services to the public."
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "You interacted with an audio-visual clip on the Preamble of the Kenyan Constitution. Which of the following is a key word in the preamble?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Honesty", "isCorrect": False },
        { "text": "Courage", "isCorrect": False },
        { "text": "Honouring", "isCorrect": True },
        { "text": "Responsibility", "isCorrect": False }
      ],
      "explanation": "The Preamble of the Kenyan Constitution includes the phrase: 'HONOURING those who heroically struggled to bring freedom and justice to our land'. Therefore, 'Honouring' is a key word found in the preamble."
    }
]

file_path = 'src/data/kpsea-sst-parta-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('{'):content.rfind('}')+1]
data = json.loads(json_str)

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2025 = ' + json.dumps(data, indent=2) + ';\n')

print("Batch 4 for KPSEA SST Part A 2025 appended!")
