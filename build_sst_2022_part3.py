import json
import os

filepath = "src/data/kpsea-sst-parta-2022.js"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kpseaSstParta2022 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

q21_to_29 = [
  {
    "id": "q21",
    "questionNumber": 21,
    "questionText": "A grade six teacher has asked the learners to identify the country that borders Kenya to the North West. The country is",
    "questionType": "multiple-choice",
    "options": [
      {"text": "South Sudan", "isCorrect": True},
      {"text": "Ethiopia", "isCorrect": False},
      {"text": "Somalia", "isCorrect": False},
      {"text": "Uganda.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **South Sudan.**\n\n**Analysis of the Correct Answer:**\nKenya is bordered by several countries: South Sudan lies to the North West, Ethiopia is to the North, Somalia is to the East, Tanzania is to the South, and Uganda is to the West. Therefore, the country to the North West is South Sudan.\n\n**Why Other Options Are Incorrect:**\n- **Ethiopia:** Borders Kenya to the North.\n- **Somalia:** Borders Kenya to the East.\n- **Uganda:** Borders Kenya to the West."
  },
  {
    "id": "q22",
    "questionNumber": 22,
    "questionText": "During a visit to the museum, grade five learners asked an officer why they take care of historical built environments? The correct response was, to protect",
    "questionType": "multiple-choice",
    "options": [
      {"text": "them from visitors", "isCorrect": False},
      {"text": "them from destruction", "isCorrect": True},
      {"text": "our natural environment", "isCorrect": False},
      {"text": "our beautiful country.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **them from destruction.**\n\n**Analysis of the Correct Answer:**\nHistorical built environments (like monuments, old forts, and museums) are preserved and cared for to protect them from physical destruction, weathering, and vandalism so that future generations can learn about history and heritage.\n\n**Why Other Options Are Incorrect:**\n- **them from visitors:** The goal is actually to *allow* visitors to see them, safely.\n- **our natural environment:** Built environments are man-made, not natural.\n- **our beautiful country:** Too general; specific conservation efforts on built sites are about preventing their direct destruction."
  },
  {
    "id": "q23",
    "questionNumber": 23,
    "questionText": "Grade six learners went for a field trip and saw an ox bow lake. After the trip, the teacher told them to draw the feature they saw. Which of the following diagrams is correct?\n\n[Diagram A: A meandering river with a separate U-shaped lake next to it]\n[Diagram B: A meandering river only]\n[Diagram C: A sharp river bend]\n[Diagram D: A solid irregular shape]",
    "questionType": "multiple-choice",
    "options": [
      {"text": "A", "isCorrect": True},
      {"text": "B", "isCorrect": False},
      {"text": "C", "isCorrect": False},
      {"text": "D", "isCorrect": False}
    ],
    "explanation": "The correct answer is **A.**\n\n**Analysis of the Correct Answer:**\nAn oxbow lake is a U-shaped body of water that forms when a wide meander from the main stem of a river is cut off, creating a free-standing body of water. Diagram A shows exactly this: the main river channel flowing straight, leaving a detached, curved (U-shaped) lake beside it.\n\n**Why Other Options Are Incorrect:**\n- **B, C:** Show meanders that are still connected to the river, not fully formed oxbow lakes.\n- **D:** Represents a generic lake or landmass, not specifically an oxbow."
  },
  {
    "id": "q24",
    "questionNumber": 24,
    "questionText": "The following are characteristics of a type of vegetation:\n\ni. tall trees.\nii. trees close together.\niii. huge roots.\niv. climbing plants.\n\nThis type of vegetation is called",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Savanna", "isCorrect": False},
      {"text": "Semi-desert", "isCorrect": False},
      {"text": "Mangrove", "isCorrect": False},
      {"text": "Equatorial.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **Equatorial.**\n\n**Analysis of the Correct Answer:**\nEquatorial rainforests are known for their dense canopy (trees close together), very tall emergent trees, buttress roots (huge roots that support the tall trees), and lianas or creepers (climbing plants trying to reach sunlight). \n\n**Why Other Options Are Incorrect:**\n- **Savanna:** Characterized by tall grasses and scattered trees.\n- **Semi-desert:** Sparse vegetation, thorny bushes, and drought-resistant plants.\n- **Mangrove:** Found along muddy coastlines with aerial breathing roots, but not typically characterized by a very tall, dense multi-canopy forest with lianas."
  },
  {
    "id": "q25",
    "questionNumber": 25,
    "questionText": "You were asked to identify a historic built environment in Kenya.\nWhich one is correct?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Mount Kenya.", "isCorrect": False},
      {"text": "Fort Jesus.", "isCorrect": True},
      {"text": "Tana River.", "isCorrect": False},
      {"text": "Hilton Hotel.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Fort Jesus.**\n\n**Analysis of the Correct Answer:**\nA \"historic built environment\" refers to a man-made structure of significant historical value. Fort Jesus in Mombasa was built in the 16th century by the Portuguese and is a famous historical monument and UNESCO World Heritage site in Kenya.\n\n**Why Other Options Are Incorrect:**\n- **Mount Kenya / Tana River:** These are physical/natural environments, not built by humans.\n- **Hilton Hotel:** While built, it does not carry the deep, ancient historical heritage associated with \"historic built environments\" in the curriculum context."
  },
  {
    "id": "q26",
    "questionNumber": 26,
    "questionText": "Grade six learners were asked to write short messages to help in caring for plants within the school compound. Three of the messages will help to care for the plants **except**",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Do not step on grass", "isCorrect": False},
      {"text": "Do not use tree branches to sweep", "isCorrect": False},
      {"text": "Do not water the grass frequently", "isCorrect": True},
      {"text": "Weed the trees regularly.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Do not water the grass frequently.**\n\n**Analysis of the Correct Answer:**\nPlants require adequate water to survive and thrive. Advising people *not* to water the grass frequently would lead to the grass drying up and dying, making it terrible advice for caring for plants. Therefore, it is the exception.\n\n**Why Other Options Are Incorrect:**\n- **Do not step on grass:** Helps protect the grass from damage.\n- **Do not use tree branches to sweep:** Prevents people from breaking branches and damaging trees.\n- **Weed the trees regularly:** Removes competing plants, helping the trees grow healthier."
  },
  {
    "id": "q27",
    "questionNumber": 27,
    "questionText": "Jane is walking to school and wants to cross the road. Which of the following road signs indicates that she may cross the road?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "A (No entry sign)", "isCorrect": False},
      {"text": "B (Stop sign)", "isCorrect": False},
      {"text": "C (Pedestrian crossing sign)", "isCorrect": True},
      {"text": "D (Roundabout ahead sign)", "isCorrect": False}
    ],
    "explanation": "The correct answer is **C (Pedestrian crossing sign).**\n\n**Analysis of the Correct Answer:**\nSign C (a triangle showing figures walking) is a warning sign that indicates a pedestrian crossing ahead. This is the designated and safe place for people like Jane to cross the road.\n\n**Why Other Options Are Incorrect:**\n- **A:** \"No entry\" is for vehicles.\n- **B:** \"Stop\" commands vehicles to halt at an intersection.\n- **D:** Alerts drivers of a roundabout ahead."
  },
  {
    "id": "q28",
    "questionNumber": 28,
    "questionText": "Which one of the following minerals is **correctly** matched with the area where it is mined?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Diatomite – Athi River", "isCorrect": False},
      {"text": "Soda Ash – Kariandusi", "isCorrect": False},
      {"text": "Salt – Malindi", "isCorrect": True},
      {"text": "Petroleum – Magadi.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Salt – Malindi.**\n\n**Analysis of the Correct Answer:**\nIn Kenya, salt is heavily mined along the coastal areas, specifically at Ngomeni near Malindi, where seawater is evaporated in large pans to produce salt.\n\n**Why Other Options Are Incorrect:**\n- **Diatomite:** Mined in Kariandusi, not Athi River (which is known for limestone/cement).\n- **Soda Ash:** Mined at Lake Magadi, not Kariandusi.\n- **Petroleum:** Extracted in Turkana County (Ngamia), not Magadi."
  },
  {
    "id": "q29",
    "questionNumber": 29,
    "questionText": "Which of the following factors does **not** influence dense population?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Presence of minerals", "isCorrect": False},
      {"text": "Hilly places", "isCorrect": True},
      {"text": "Government policy", "isCorrect": False},
      {"text": "Presence of towns", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Hilly places.**\n\n**Analysis of the Correct Answer:**\nDense populations are usually found in areas that are easy to settle and develop. Hilly, rugged, or steep terrain is difficult to build on, lacks good transport networks, and is hard to farm, making it a factor that typically discourages (rather than influences) dense population.\n\n**Why Other Options Are Incorrect:**\n- **Presence of minerals, Presence of towns, Government policy:** These factors attract people for jobs, amenities, and security, thereby strongly influencing high/dense population."
  }
]

data["sectionA"].extend(q21_to_29)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstParta2022 = {json.dumps(data, indent=2)};\n")

print("Updated kpsea-sst-parta-2022.js with Q21-Q29 successfully.")
