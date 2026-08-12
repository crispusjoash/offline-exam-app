import json

new_questions = [
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Learners watched a video of a gymnast performing a side roll technique. Which part of the body touched the ground during the performance?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Head", "isCorrect": False },
        { "text": "Shoulder", "isCorrect": True },
        { "text": "Neck", "isCorrect": False },
        { "text": "Stomach", "isCorrect": False }
      ],
      "explanation": "In a side roll, the side of the body, particularly the shoulders and the hips, make contact with the ground as the performer rolls sideways."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "The purpose of a theatre in a puppet show is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "display the puppeteer", "isCorrect": False },
        { "text": "record a video", "isCorrect": False },
        { "text": "increase puppeteer's voice", "isCorrect": False },
        { "text": "create scenery.", "isCorrect": True }
      ],
      "explanation": "A puppet theatre provides a stage frame and scenery or background for the puppets to perform in, while hiding the puppeteer from the audience."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "Which letter names are represented by the following fingering of a descant recorder?\n\n[Image: Three descant recorders showing different fingerings. Recorder (i) has thumb and top 5 holes covered. Recorder (ii) has thumb and top 3 holes covered. Recorder (iii) has thumb and all 7 top holes covered.]",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) C (ii) G (iii) E", "isCorrect": False },
        { "text": "(i) E (ii) C (iii) G", "isCorrect": False },
        { "text": "(i) E (ii) G (iii) C", "isCorrect": True },
        { "text": "(i) G (ii) E (iii) C", "isCorrect": False }
      ],
      "explanation": "Recorder (i) with thumb and 5 holes covered plays E. Recorder (ii) with thumb and 3 holes covered plays G. Recorder (iii) with thumb and all 7 holes covered plays C."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "There are various equipment used in a game of volleyball. Which of the following equipment is matched with its correct use?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Net \u2013 To keep spectators away.", "isCorrect": False },
        { "text": "Whistle \u2013 To start and stop the game.", "isCorrect": True },
        { "text": "Antenna \u2013 To show where the service takes place.", "isCorrect": False },
        { "text": "The ball \u2013 To determine the period of play.", "isCorrect": False }
      ],
      "explanation": "The referee uses a whistle to signal the start and stop of play in volleyball. The net divides the court, and the antennae mark the vertical boundaries over the net."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "Why is focus an important element in photography? It",
      "questionType": "multiple-choice",
      "options": [
        { "text": "makes images sharp", "isCorrect": True },
        { "text": "reduces light", "isCorrect": False },
        { "text": "reduces the colour", "isCorrect": False },
        { "text": "makes images blurred.", "isCorrect": False }
      ],
      "explanation": "Focusing the camera lens ensures that the main subject of the photograph is sharp, clear, and well-defined rather than blurry."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "Which of the following sounds does not maintain a steady beat? Sound from",
      "questionType": "multiple-choice",
      "options": [
        { "text": "a clock", "isCorrect": False },
        { "text": "an ambulance siren", "isCorrect": False },
        { "text": "a posho mill", "isCorrect": False },
        { "text": "a crowing cock.", "isCorrect": True }
      ],
      "explanation": "A clock, a posho mill, and a siren produce rhythmic, continuous, and steady beats/sounds. A crowing cock produces an irregular, isolated burst of sound without a steady continuous beat."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "During a game of rounders, John was eliminated from the game while running from one base to the other. John was eliminated because he",
      "questionType": "multiple-choice",
      "options": [
        { "text": "ran back to a base", "isCorrect": False },
        { "text": "was tagged with a ball", "isCorrect": True },
        { "text": "ran too fast to the base", "isCorrect": False },
        { "text": "ran past home plate.", "isCorrect": False }
      ],
      "explanation": "In games like rounders, a runner can be eliminated (put out) if they are tagged with the ball by a fielder while they are running between bases."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "A learner wants to make a mitre joint using the following pieces of wood.\n\n[Image: Two pieces of wood with 45-degree angled cuts at their ends.]\n\nWhich two materials should the learner use to make the joint strong?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Glue and strings.", "isCorrect": False },
        { "text": "Glue and nails.", "isCorrect": True },
        { "text": "Strings and nails.", "isCorrect": False },
        { "text": "Metal and strings.", "isCorrect": False }
      ],
      "explanation": "A mitre joint is commonly made strong and secure by applying wood glue to the angled faces and then reinforcing the joint with nails."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "Which of the following elements of music is not correctly matched with the given description?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Dynamics - loud and soft", "isCorrect": False },
        { "text": "Melody - pitch and rhythm", "isCorrect": False },
        { "text": "Form - order and arrangement", "isCorrect": False },
        { "text": "Texture - pulse and speed", "isCorrect": True }
      ],
      "explanation": "Texture in music refers to how different layers of sound (melody, harmony, rhythm) interact. Pulse and speed refer to Tempo. Thus, Texture is incorrectly matched."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "Your team has been advised to observe safety measures when playing a volleyball match to avoid injuries. Which of the following is a safety measure that the team should observe?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Use a new brightly coloured ball for visibility.", "isCorrect": False },
        { "text": "Wear clean uniform and wash hands after the match.", "isCorrect": False },
        { "text": "Ensure that the playing field is flat and free of objects.", "isCorrect": True },
        { "text": "Lower the net so that players can pass the ball over it easily.", "isCorrect": False }
      ],
      "explanation": "Ensuring the playing surface is flat and clear of any hazardous objects is a critical safety measure to prevent tripping and falling injuries during a match."
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

print("Batch 3 for KPSEA SST Part A 2025 appended!")
