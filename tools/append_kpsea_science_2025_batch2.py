import json

new_questions = [
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Which of the following statements describes the functions of a trachea?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Allows the lungs to expand and cleans air.", "isCorrect": False },
        { "text": "Traps dust and allows air to pass.", "isCorrect": True },
        { "text": "Allows the lungs to expand and traps dust.", "isCorrect": False },
        { "text": "Cleans and absorbs air.", "isCorrect": False }
      ],
      "explanation": "The trachea (windpipe) has rings of cartilage that keep it open to allow air to pass, and is lined with mucus and cilia to trap dust and clean the air."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "In an investigation on the different components of air, learners used blocks of different sizes to represent gases that make up air as shown.\n\n[Image: Blocks F (largest), G, H, J (smallest)]\n\nWhich of the blocks represents carbon dioxide gas?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "F", "isCorrect": False },
        { "text": "G", "isCorrect": False },
        { "text": "H", "isCorrect": False },
        { "text": "J", "isCorrect": True }
      ],
      "explanation": "Air consists of Nitrogen (78%), Oxygen (21%), inert gases (0.97%), and Carbon dioxide (0.03%). Carbon dioxide takes up the smallest percentage, so it is represented by the smallest block (J)."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "A learner placed objects into an empty trough, filled it with water and observed what happened to the objects.\n\n[Image: A trough with water. Inside, a Wooden plank floats, a Plastic ruler floats, a Pencil floats, and a Coin is at the bottom]\n\nWhich object remained at the bottom of the trough?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Plastic ruler.", "isCorrect": False },
        { "text": "Pencil.", "isCorrect": False },
        { "text": "Coin.", "isCorrect": True },
        { "text": "Wooden plank.", "isCorrect": False }
      ],
      "explanation": "The coin sank to the bottom of the trough because it is made of metal, which is denser than water."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "During a lesson on properties of matter, learners listed the properties of solids and gases as shown in the table.\n\nWhich property was correctly summarised for both solids and gases?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "has weight: Solids (Yes), Gases (No)", "isCorrect": False },
        { "text": "has definite mass: Solids (Yes), Gases (Yes)", "isCorrect": True },
        { "text": "has definite shape: Solids (No), Gases (Yes)", "isCorrect": False },
        { "text": "has definite volume: Solids (Yes), Gases (Yes)", "isCorrect": False }
      ],
      "explanation": "All matter, including solids and gases, has a definite mass. Solids have definite shape and volume, while gases do not have definite shape or volume. Both solids and gases have weight."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "The following picture shows a set-up used by a learner to demonstrate a certain property of light.\n\n[Image: A hollow curved pipe. One end has a candle flame, the other end has the learner's eye. The pipe is curved.]\n\nThe learner could not see the flame. What should the learner do in order to see the flame?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Move the pipe closer to the flame.", "isCorrect": False },
        { "text": "Bend the pipe more.", "isCorrect": False },
        { "text": "Make the pipe straight.", "isCorrect": True },
        { "text": "Move the pipe closer to the eye.", "isCorrect": False }
      ],
      "explanation": "Light travels in a straight line. The learner cannot see the flame through a curved pipe and needs to make the pipe straight to see it."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Workers at a construction site want to lift a load. Which of the following pictures shows the easiest way they can use to lift the load?\n\n[Image: A: Man lifting block directly with a rope over a single fixed pulley. B: Man lifting block with a single movable pulley system. C: Man pushing a block up a short steep inclined plane. D: Man lifting the block directly on his head]",
      "questionType": "multiple-choice",
      "options": [
        { "text": "A", "isCorrect": False },
        { "text": "B", "isCorrect": True },
        { "text": "C", "isCorrect": False },
        { "text": "D", "isCorrect": False }
      ],
      "explanation": "System B shows a block and tackle (or a system with a movable pulley). A movable pulley provides a mechanical advantage, reducing the effort needed to lift the load, making it the easiest way."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "The following picture shows a learner playing with a ball.\n\n[Image: A learner hitting a volleyball upwards]\n\nWhich of the following statements describes the effect of gravity as the learner plays with the ball?\nGravity makes the",
      "questionType": "multiple-choice",
      "options": [
        { "text": "ball to rise up from the hands", "isCorrect": False },
        { "text": "ball to fall back to the hands", "isCorrect": True },
        { "text": "hands to hit the ball", "isCorrect": False },
        { "text": "hands to lift the ball.", "isCorrect": False }
      ],
      "explanation": "Gravity is the force that pulls objects towards the centre of the earth. When the ball is hit upwards, gravity pulls it back down to the hands."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "During a lesson on sources of sound, learners listed the following:\n(i) a mobile phone\n(ii) a siren of an ambulance\n(iii) a guitar\n(iv) a helicopter\n\nWhich pair of the sources produces sound that is more likely to harm the ears?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) and (ii)", "isCorrect": False },
        { "text": "(i) and (iii)", "isCorrect": False },
        { "text": "(ii) and (iv)", "isCorrect": True },
        { "text": "(iii) and (iv)", "isCorrect": False }
      ],
      "explanation": "Loud sounds cause noise pollution and can harm the ears. The siren of an ambulance and a helicopter produce very loud sounds."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "During a class discussion, learners gave the following as characteristics of an animal that they had observed in the school garden:\n(i) has four pairs of legs\n(ii) body is divided into two parts\n(iii) has no backbone\n\nThe animal they observed is likely to be a",
      "questionType": "multiple-choice",
      "options": [
        { "text": "spider", "isCorrect": True },
        { "text": "grasshopper", "isCorrect": False },
        { "text": "beetle", "isCorrect": False },
        { "text": "ladybird.", "isCorrect": False }
      ],
      "explanation": "A spider is an arachnid, characterized by having 8 legs (four pairs) and a body divided into two parts (cephalothorax and abdomen). The others are insects with 6 legs and three body parts."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "The following picture shows the sole of a learner's shoe.\n\n[Image: The sole of a shoe, completely worn out and smooth]\n\nThe learner finds it difficult to walk in the shoe because the sole is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "heavy", "isCorrect": False },
        { "text": "smooth", "isCorrect": True },
        { "text": "curved", "isCorrect": False },
        { "text": "hard.", "isCorrect": False }
      ],
      "explanation": "A smooth, worn-out sole reduces friction between the shoe and the ground, making it slippery and difficult to walk."
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

print("Batch 2 for KPSEA Science 2025 appended!")
