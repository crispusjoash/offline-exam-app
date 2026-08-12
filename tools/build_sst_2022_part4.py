import json
import os

filepath = "src/data/kpsea-sst-parta-2022.js"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kpseaSstParta2022 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

q30_to_35 = [
  {
    "id": "q30",
    "questionNumber": 30,
    "questionText": "Peter was asked by the class teacher to give qualities of a good leader. He made the table below. Choose the option that has the correct qualities.",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Selfish, Cruel", "isCorrect": False},
      {"text": "Unjust, Arrogant", "isCorrect": False},
      {"text": "Dishonest, Cruel", "isCorrect": False},
      {"text": "Caring, Kind", "isCorrect": True}
    ],
    "explanation": "The correct answer is **Caring, Kind.**\n\n**Analysis of the Correct Answer:**\nA good leader is someone who considers the needs of their followers, shows empathy, and acts with fairness and compassion. Caring and kind are positive attributes essential for good leadership.\n\n**Why Other Options Are Incorrect:**\n- **Selfish, Cruel, Unjust, Arrogant, Dishonest:** These are all negative traits that describe bad leadership or dictatorship, not a good leader."
  },
  {
    "id": "q31",
    "questionNumber": 31,
    "questionText": "Ali has been asked by his parent to sell sweets in the streets in order to get money to buy food. Ali's parent can be accused of",
    "questionType": "multiple-choice",
    "options": [
      {"text": "promoting early marriage", "isCorrect": False},
      {"text": "promoting child labour", "isCorrect": True},
      {"text": "causing physical harm", "isCorrect": False},
      {"text": "denial of shelter.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **promoting child labour.**\n\n**Analysis of the Correct Answer:**\nChild labour refers to the exploitation of children through any form of work that deprives them of their childhood, interferes with their ability to attend regular school, and is mentally, physically, socially or morally dangerous. Forcing a child to sell sweets on the streets instead of being in school or playing is a classic example of child labour.\n\n**Why Other Options Are Incorrect:**\n- **early marriage:** Unrelated to working on the streets.\n- **physical harm / denial of shelter:** While street work is dangerous and might expose him to harm, the specific act of making a child work for income is legally defined as child labour."
  },
  {
    "id": "q32",
    "questionNumber": 32,
    "questionText": "Which one of the following traditional leaders practised long distance trade?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Mekatilili wa Menza.", "isCorrect": False},
      {"text": "Chief Kivoi Mwendwa.", "isCorrect": True},
      {"text": "Kabaka Mwanga.", "isCorrect": False},
      {"text": "Chief Mirambo.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Chief Kivoi Mwendwa.**\n\n**Analysis of the Correct Answer:**\nChief Kivoi Mwendwa was a famous Akamba leader and long-distance trader in Kenya during the 19th century. He organized large caravans that traded ivory and other goods between the interior (Kitui) and the Kenyan coast (Mombasa).\n\n**Why Other Options Are Incorrect:**\n- **Mekatilili wa Menza:** A Giriama leader famous for resisting British colonial rule, not for long-distance trade.\n- **Kabaka Mwanga / Chief Mirambo:** While Mirambo (Nyamwezi) was involved in trade, Kivoi is the prominent Kenyan curriculum example for local long-distance traders."
  },
  {
    "id": "q33",
    "questionNumber": 33,
    "questionText": "Which of the following factors promote peace in school.",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Obedience, Respect", "isCorrect": True},
      {"text": "Conflict, Selfishness", "isCorrect": False},
      {"text": "Love, Jealousy", "isCorrect": False},
      {"text": "Dishonesty, Respect", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Obedience, Respect.**\n\n**Analysis of the Correct Answer:**\nPeace is fostered in an environment where people follow rules (obedience) and treat each other with dignity and consideration (respect). When students and teachers exhibit these traits, the school environment remains calm and harmonious.\n\n**Why Other Options Are Incorrect:**\n- **Conflict, Selfishness, Jealousy, Dishonesty:** These are all negative traits that create division, misunderstandings, and violence, thereby destroying peace."
  },
  {
    "id": "q34",
    "questionNumber": 34,
    "questionText": "Your class is planning to start an enterprise project in the school. The first activity the class should do is to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "share the profits from the project", "isCorrect": False},
      {"text": "agree on roles during the project", "isCorrect": False},
      {"text": "discuss where to sell the products", "isCorrect": False},
      {"text": "discuss the type of project to start.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **discuss the type of project to start.**\n\n**Analysis of the Correct Answer:**\nBefore any business or enterprise can begin, the very first step in the planning phase is ideation—deciding exactly what the project will be. You cannot assign roles, find a market, or share profits for a project that hasn't been chosen yet.\n\n**Why Other Options Are Incorrect:**\n- **share profits:** This is the absolute last step after the project has succeeded.\n- **agree on roles / where to sell:** These are secondary steps that happen after the group has decided what they are actually producing."
  },
  {
    "id": "q35",
    "questionNumber": 35,
    "questionText": "Mohammed has been asked to write one duty of a judge. The correct duty will be to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "listen to evidence and make decisions", "isCorrect": True},
      {"text": "listen to people's problems", "isCorrect": False},
      {"text": "maintain law and order", "isCorrect": False},
      {"text": "make laws and policies.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **listen to evidence and make decisions.**\n\n**Analysis of the Correct Answer:**\nThe primary role of a judge in the judiciary system is to preside over court proceedings, listen objectively to the evidence and arguments presented by both sides, and make a legal decision or ruling based on the law.\n\n**Why Other Options Are Incorrect:**\n- **listen to people's problems:** While they hear cases, this describes a counselor or social worker.\n- **maintain law and order:** This is the duty of the police (executive branch).\n- **make laws and policies:** This is the duty of the legislature/parliament."
  }
]

data["sectionA"].extend(q30_to_35)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstParta2022 = {json.dumps(data, indent=2)};\n")

print("Updated kpsea-sst-parta-2022.js with Q30-Q35 successfully.")
