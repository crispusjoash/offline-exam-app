import json

new_questions = [
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "The best way of controlling weeds in a container garden is by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "spraying with chemicals", "isCorrect": False },
        { "text": "cultivating using a jembe", "isCorrect": False },
        { "text": "mulching with dry grass", "isCorrect": False },
        { "text": "uprooting the weeds.", "isCorrect": True }
      ],
      "explanation": "A container garden has limited space, making large tools like a jembe impractical. The easiest and best way to control weeds is by uprooting them directly using hands."
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "The following picture shows a farmer carrying out a caring practice on an innovative garden. Use it to answer questions 32 to 34.\n\n[Image: A farmer watering a garden constructed from stacked tyres]\n\nIdentify the innovative garden.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Container garden.", "isCorrect": False },
        { "text": "Horizontal garden.", "isCorrect": False },
        { "text": "Sunken bed.", "isCorrect": False },
        { "text": "Vertical garden.", "isCorrect": True }
      ],
      "explanation": "The image shows a vertical garden where crops are grown upwards in stacked layers of tyres to maximize space."
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "The main reason for using innovative gardening is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "prevent the spread of pests", "isCorrect": False },
        { "text": "control crop diseases", "isCorrect": False },
        { "text": "utilize limited space", "isCorrect": True },
        { "text": "prevent germination of weeds.", "isCorrect": False }
      ],
      "explanation": "Innovative gardening methods, such as vertical gardening and multi-storey gardens, are mainly designed to allow crop growing in urban areas or places with limited space."
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "What is the best time to carry out the practice shown in the picture?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "At midday.", "isCorrect": False },
        { "text": "Early in the morning.", "isCorrect": True },
        { "text": "When the sun is too hot.", "isCorrect": False },
        { "text": "When plants start to dry.", "isCorrect": False }
      ],
      "explanation": "The practice shown is watering crops. Watering should be done early in the morning or late in the evening when temperatures are lower to reduce the rate of evaporation."
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

print("Batch 4 for KPSEA Science 2025 appended!")
