import json

new_questions = [
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Juma sang a song with the phrase 'Kenya nchi yangu, naipenda daima'. What type of song did Juma sing?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Folk song.", "isCorrect": False },
        { "text": "Patriotic song.", "isCorrect": True },
        { "text": "Religious song.", "isCorrect": False },
        { "text": "Topical song.", "isCorrect": False }
      ],
      "explanation": "The phrase translates to 'Kenya my country, I will love it forever'. Songs that express love, loyalty, and praise for one's country are patriotic songs."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "The following picture shows a high jump technique.\n\n[Image: A person clearing a bar in high jump. Their legs are thrown forward in a scissoring motion.]\n\nWhat is the name of the technique?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Scissor style.", "isCorrect": True },
        { "text": "Vaulting style.", "isCorrect": False },
        { "text": "Straddle style.", "isCorrect": False },
        { "text": "One leg style.", "isCorrect": False }
      ],
      "explanation": "The image shows the scissor technique, where the athlete throws one leg over the bar followed by the other in a scissoring motion."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "How can the value of a colour be made lighter when painting using wash technique?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Reduce the amount of water mixed into the paint.", "isCorrect": False },
        { "text": "Paint a dark color in an adjacent area.", "isCorrect": False },
        { "text": "Thin the paint with water.", "isCorrect": True },
        { "text": "Mix the colour with its complement.", "isCorrect": False }
      ],
      "explanation": "In watercolour wash techniques, adding more water thins the paint and allows more of the white paper to show through, thereby making the colour value lighter."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "Tempo in music refers to the",
      "questionType": "multiple-choice",
      "options": [
        { "text": "fastness or slowness of music", "isCorrect": True },
        { "text": "highness or lowness of sound", "isCorrect": False },
        { "text": "loudness or softness of sound", "isCorrect": False },
        { "text": "simultaneous sounding of notes.", "isCorrect": False }
      ],
      "explanation": "Tempo refers to the speed or pace of a given piece of music, which indicates how fast or slow it should be played."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "During a class discussion, four learners gave the following descriptions of the sail technique in long jump. Which learner gave the correct description?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Learner 1: Cycling of arms and legs while in flight phase of long jump.", "isCorrect": False },
        { "text": "Learner 2: Stretching and lengthening of the body while in the air in preparation for landing.", "isCorrect": False },
        { "text": "Learner 3: Lifting the legs and stretching hands into a toe touching position after taking off.", "isCorrect": True },
        { "text": "Learner 4: Gaining speed and taking off from one foot at the take-off board.", "isCorrect": False }
      ],
      "explanation": "In the sail technique, the jumper takes off and brings both legs forward while stretching the arms towards the toes, resembling a seated or 'V' position in the air."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Which of the following statements is not true about indigenous Kenyan crafts? They",
      "questionType": "multiple-choice",
      "options": [
        { "text": "are source of income", "isCorrect": False },
        { "text": "represent different cultures", "isCorrect": False },
        { "text": "cause differences in society", "isCorrect": True },
        { "text": "are used for decoration.", "isCorrect": False }
      ],
      "explanation": "Indigenous crafts celebrate culture, provide income, and are used for decoration. They do not cause differences or conflicts in society."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Which French rhythm names correspond with the following rhythmic pattern?\n\n[Image: A minim, followed by two joined quavers, followed by a crotchet]",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ta-te Taa Taa Taa-aa", "isCorrect": False },
        { "text": "Taa-aa ta-te Taa", "isCorrect": True },
        { "text": "Taa-aa Taa Taa ta-te", "isCorrect": False },
        { "text": "Ta-te ta-te Taa Taa", "isCorrect": False }
      ],
      "explanation": "A minim corresponds to 'Taa-aa'. Two joined quavers correspond to 'ta-te'. A crotchet corresponds to 'Taa'. Therefore, the pattern is 'Taa-aa ta-te Taa'."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "Four members of a discussion group gave various statements about crab balance in gymnastics. Which member gave the correct answer?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Member 1: The body of the performer is supported by the legs only.", "isCorrect": False },
        { "text": "Member 2: The stomach faces down during the performance.", "isCorrect": False },
        { "text": "Member 3: The performer lies flat on the ground while facing up.", "isCorrect": False },
        { "text": "Member 4: The performer is supported by both hands and feet.", "isCorrect": True }
      ],
      "explanation": "In a crab balance, the performer faces upwards with their stomach facing the sky, supporting their body weight on both their hands and feet, with hips lifted off the ground."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "Which of the following is a safety measure that should be observed when handling dye?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Wear warm clothes.", "isCorrect": False },
        { "text": "Work in an open space.", "isCorrect": True },
        { "text": "Use double containers.", "isCorrect": False },
        { "text": "Work in a closed room.", "isCorrect": False }
      ],
      "explanation": "Dyes often contain chemicals that emit toxic fumes. Working in an open, well-ventilated space is a crucial safety measure to avoid inhaling these fumes."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "Which of the following is not a way of tuning Kenyan indigenous string instruments?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Adjusting the position of the bridge.", "isCorrect": False },
        { "text": "Tightening and loosening of knobs.", "isCorrect": True },
        { "text": "Tightening and loosening of laces.", "isCorrect": False },
        { "text": "Tightening and loosening of pegs.", "isCorrect": False }
      ],
      "explanation": "Indigenous string instruments are typically tuned using traditional methods like tightening pegs, adjusting laces/thongs, or moving the bridge. Knobs (machine heads) are found on modern instruments like guitars."
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

print("Batch 2 for KPSEA SST Part A 2025 appended!")
