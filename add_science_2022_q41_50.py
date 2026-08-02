import json

questions = [
    {
        "id": "kpsea-science-2022-q41",
        "questionNumber": 41,
        "questionText": "You have been asked to select players for your school's volleyball team. How many players will you identify to be in the court at the start of a volleyball game?",
        "questionType": "mcq",
        "options": [
            {"text": "6", "isCorrect": True},
            {"text": "12", "isCorrect": False},
            {"text": "11", "isCorrect": False},
            {"text": "7", "isCorrect": False}
        ],
        "explanation": "In a standard game of volleyball, each team has 6 players on the court at the start of the game."
    },
    {
        "id": "kpsea-science-2022-q42",
        "questionNumber": 42,
        "questionText": "Grade six learners were planning for movement sequences in gymnastics. Which of the categories provided is an **appropriate** two-action sequence?",
        "questionType": "mcq",
        "options": [
            {"text": "Side vault to Backward roll.", "isCorrect": False},
            {"text": "Backward roll to fence vault.", "isCorrect": False},
            {"text": "Cartwheel to Headstand.", "isCorrect": False},
            {"text": "Astride Vault to Forward roll.", "isCorrect": True}
        ],
        "explanation": "In gymnastics, an astride vault (jumping over an apparatus with legs apart) smoothly transitions into a forward roll upon landing, making it a very common and appropriate two-action sequence."
    },
    {
        "id": "kpsea-science-2022-q43",
        "questionNumber": 43,
        "questionText": "Your group is preparing to demonstrate flexibility testing to other class members. Which of the following equipment should your group use?",
        "questionType": "mcq",
        "options": [
            {"text": "Sit and reach box.", "isCorrect": True},
            {"text": "Tape measure.", "isCorrect": False},
            {"text": "Weighing scale.", "isCorrect": False},
            {"text": "Measuring string.", "isCorrect": False}
        ],
        "explanation": "The \"sit and reach\" box is a standardized piece of equipment used specifically to measure the flexibility of the lower back and hamstring muscles."
    },
    {
        "id": "kpsea-science-2022-q44",
        "questionNumber": 44,
        "questionText": "An athlete from your school finished first in a marathon race. Which was the most important physical fitness component the athlete used?",
        "questionType": "mcq",
        "options": [
            {"text": "Power.", "isCorrect": False},
            {"text": "Speed.", "isCorrect": False},
            {"text": "Endurance.", "isCorrect": True},
            {"text": "Coordination.", "isCorrect": False}
        ],
        "explanation": "A marathon is a long-distance running race. The most critical fitness component for such an event is cardiovascular endurance (stamina), which allows the athlete to sustain prolonged physical activity."
    },
    {
        "id": "kpsea-science-2022-q45",
        "questionNumber": 45,
        "questionText": "A group of learners preserved food appropriately when going out for an excursion. Why was the food preserved?",
        "questionType": "mcq",
        "options": [
            {"text": "To add taste before eating.", "isCorrect": False},
            {"text": "To keep warm and dry.", "isCorrect": False},
            {"text": "To stay long before spoiling.", "isCorrect": True},
            {"text": "For ease of carrying.", "isCorrect": False}
        ],
        "explanation": "The primary purpose of food preservation (e.g., drying, canning, or salting) is to prevent the growth of microorganisms, allowing the food to last a long time without spoiling."
    },
    {
        "id": "kpsea-science-2022-q46",
        "questionNumber": 46,
        "questionText": "Four learners gave the meaning of ABC in first aid. Which of the responses given was the correct meaning?",
        "questionType": "mcq",
        "options": [
            {"text": "Awake Breathing and Circulation.", "isCorrect": False},
            {"text": "Assess Breathing and Circulation.", "isCorrect": False},
            {"text": "Airways Breathing and Circulation.", "isCorrect": True},
            {"text": "Airways Bleeding and Circulation.", "isCorrect": False}
        ],
        "explanation": "In first aid, the primary survey is known as ABC, which stands for Airway (checking if the airway is clear), Breathing (checking if the casualty is breathing), and Circulation (checking for pulse/blood flow)."
    },
    {
        "id": "kpsea-science-2022-q47",
        "questionNumber": 47,
        "questionText": "A learner was stung by a bee during an outdoor activity in the school farm. What did the teacher advice the learner to do?",
        "questionType": "mcq",
        "options": [
            {"text": "Immediately go home and sleep.", "isCorrect": False},
            {"text": "Place hot water in the stung area.", "isCorrect": False},
            {"text": "Pull the sting out immediately.", "isCorrect": True},
            {"text": "Kill the bees and continue.", "isCorrect": False}
        ],
        "explanation": "When a bee stings, it leaves its stinger and a venom sac behind. It is crucial to remove (pull or scrape out) the stinger immediately to prevent more venom from being pumped into the skin."
    },
    {
        "id": "kpsea-science-2022-q48",
        "questionNumber": 48,
        "questionText": "The images below show various skills used when playing volleyball game.\n\nWhich one shows an over arm serve technique?",
        "questionType": "mcq",
        "contextRef": "ctx-science-2022-q48",
        "options": [
            {"text": "A", "isCorrect": False},
            {"text": "B", "isCorrect": False},
            {"text": "C", "isCorrect": False},
            {"text": "D", "isCorrect": True}
        ],
        "explanation": "Image D demonstrates a sequence of throwing the ball into the air and striking it with an overarm swinging motion, which is the overarm serve technique in volleyball."
    },
    {
        "id": "kpsea-science-2022-q49",
        "questionNumber": 49,
        "questionText": "When playing a game, players aim at scoring. Which of the following games is correctly matched with the method of scoring?",
        "questionType": "mcq",
        "options": [
            {"text": "Tag rugby – Shot", "isCorrect": False},
            {"text": "Volleyball – Try", "isCorrect": False},
            {"text": "Soccer – Goal", "isCorrect": True},
            {"text": "Handball – Gun", "isCorrect": False}
        ],
        "explanation": "In soccer (football), the method of scoring is known as a \"Goal\". In tag rugby it is a \"Try\". Volleyball uses points/sets. The others are incorrectly matched."
    },
    {
        "id": "kpsea-science-2022-q50",
        "questionNumber": 50,
        "questionText": "During a netball competition, one player used a shoulder pass to pass the ball to a team mate. Why did this player choose to use the shoulder pass?",
        "questionType": "mcq",
        "options": [
            {"text": "Team mate was close.", "isCorrect": False},
            {"text": "Team mate was running.", "isCorrect": False},
            {"text": "Team mate was marked.", "isCorrect": False},
            {"text": "Team mate was far.", "isCorrect": True}
        ],
        "explanation": "The shoulder pass in netball is a powerful, one-handed pass used to throw the ball quickly over long distances to a teammate who is far away."
    }
]

file_path = 'src/data/kpsea-science-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the trailing "]\n}\n"
content = content.rstrip()
if content.endswith('}'):
    content = content[:-1].rstrip()
if content.endswith(']'):
    content = content[:-1].rstrip()
    
# If the last character was a '}', we also need to append a comma if it wasn't the first item
if content.endswith('}'):
    content += ',\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
    
    for i, q in enumerate(questions):
        json_str = json.dumps(q, indent=6)
        json_str = "    " + json_str.replace('\n', '\n    ')
        if i == len(questions) - 1:
            f.write(json_str + "\n")
        else:
            f.write(json_str + ",\n")
            
    f.write("  ]\n}\n")

print("Questions 41-50 appended successfully. File finalized.")
