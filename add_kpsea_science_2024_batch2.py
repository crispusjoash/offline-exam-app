import json
import os

new_questions = [
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "A patient complained of having pain in the lower abdomen and passing urine containing blood.\n\nThe patient was showing signs and symptoms of",
      "questionType": "multiple-choice",
      "options": [
        { "text": "typhoid", "isCorrect": False },
        { "text": "dysentery", "isCorrect": False },
        { "text": "cholera", "isCorrect": False },
        { "text": "bilharzia.", "isCorrect": True }
      ],
      "explanation": "Blood in urine and lower abdominal pain are classic symptoms of urinary bilharzia (schistosomiasis), which is caused by parasitic worms found in contaminated fresh water."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Grade 5 learners used the internet to search for health measures that prevent common communicable diseases. Some of the information they found included:\n\n(i) using a handkerchief always.\n(ii) proper use of latrines.\n(iii) washing hands after visiting the toilet.\n(iv) not sharing personal items.\n(v) observing personal hygiene.\n\nWhich one of the following common communicable diseases may **not** be prevented by observing all the above health measures?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ringworm.", "isCorrect": False },
        { "text": "Coughs.", "isCorrect": False },
        { "text": "Measles.", "isCorrect": True },
        { "text": "Typhoid.", "isCorrect": False }
      ],
      "explanation": "Measles is a highly contagious airborne viral disease. Standard hygiene practices like handwashing and using latrines are not the primary prevention methods; it is primarily prevented through vaccination."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "A learner classified substances as either acids or bases as shown in the following table.\n\n| Acids | Base |\n| :--- | :--- |\n| Ash solution | Soap solution |\n| Sour milk | Baking powder |\n\nWhich substance was **wrongly** classified?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Soap solution.", "isCorrect": False },
        { "text": "Sour milk.", "isCorrect": False },
        { "text": "Baking powder.", "isCorrect": False },
        { "text": "Ash solution.", "isCorrect": True }
      ],
      "explanation": "Ash solution is alkaline (a base). However, it has been wrongly placed under the \"Acids\" column in the table."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "Learners left ice cubes in the open for some time and observed that the ice cubes had changed as shown in the following picture.\n\n[Image: A beaker with solid ice cubes changes to a beaker with liquid water]\n\nWhich one of the following is the process that caused the change?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Evaporation.", "isCorrect": False },
        { "text": "Freezing.", "isCorrect": False },
        { "text": "Boiling.", "isCorrect": False },
        { "text": "Melting.", "isCorrect": True }
      ],
      "explanation": "The change of state from a solid (ice cubes) to a liquid (water) is called melting, and it happens when the ice absorbs heat from the open environment."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "A bell was rung for lunch and everyone in the school heard it. Which one of the following statements **best** explains why everyone heard the bell? Sound",
      "questionType": "multiple-choice",
      "options": [
        { "text": "travels in all directions", "isCorrect": True },
        { "text": "is reflected", "isCorrect": False },
        { "text": "was loud enough", "isCorrect": False },
        { "text": "travels fast in the afternoon.", "isCorrect": False }
      ],
      "explanation": "Sound waves propagate outwards in all directions from the source, allowing people located in different parts of the school to hear the bell."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "A learner classified materials as either translucent or transparent as shown in the table.\n\n| Transparent | Translucent |\n| :--- | :--- |\n| Frosted glass | Car windscreen |\n| Clear water | Air |\n\nWhich material is **correctly** classified?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Air.", "isCorrect": False },
        { "text": "Clear water.", "isCorrect": True },
        { "text": "Frosted glass.", "isCorrect": False },
        { "text": "Car windscreen.", "isCorrect": False }
      ],
      "explanation": "Clear water allows light to pass through it so that objects behind can be distinctly seen, which means it is transparent. It is placed correctly in the \"Transparent\" column. (The other items are swapped in the table: Frosted glass is translucent, Car windscreen and air are transparent)."
    },
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Learners carried out activities to demonstrate effects of force on objects.\n\nWhich of the activities shows that force can stop movement?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Holding a ball in the hand.", "isCorrect": True },
        { "text": "Squeezing a sponge.", "isCorrect": False },
        { "text": "Turning a water tap.", "isCorrect": False },
        { "text": "Breaking a stick.", "isCorrect": False }
      ],
      "explanation": "Catching and holding a ball in the hand stops it from moving. Squeezing a sponge and breaking a stick show a change in shape. Turning a tap shows force causing a turning effect."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "The following picture represents a set-up used by learners to demonstrate transfer of heat. Learners observed that the cooking fat melted after sometime.\n\n[Image: A candle heating a beaker of water. Inside the beaker, a piece of cooking fat is floating on the water.]\n\nThe heat was transferred to the cooking fat **mainly** by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "convection", "isCorrect": True },
        { "text": "radiation", "isCorrect": False },
        { "text": "conduction", "isCorrect": False },
        { "text": "evaporation.", "isCorrect": False }
      ],
      "explanation": "The candle heats the water at the bottom. Heat travels through the water via convection currents, carrying warmth to the surface where the cooking fat is floating, causing it to melt."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "During a class discussion on force of gravity, learners listed activities that oppose gravity. Which of the following activities they listed is **correct**?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "A fruit falling from a tree.", "isCorrect": False },
        { "text": "Pouring water into a trough.", "isCorrect": False },
        { "text": "A rock rolling downhill.", "isCorrect": False },
        { "text": "Picking iron pins using magnet.", "isCorrect": True }
      ],
      "explanation": "Gravity is the force that pulls objects downwards towards the earth. Picking up iron pins using a magnet moves them upwards, effectively opposing gravity."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "A learner observed a phase of the moon and drew it as shown.\n\n[Image: A moon phase showing a sliver illuminated on the left side, with the majority of the right side dark]\n\nThe phase of the moon drawn by the learner is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "waning gibbous", "isCorrect": False },
        { "text": "waxing crescent", "isCorrect": False },
        { "text": "waning crescent", "isCorrect": True },
        { "text": "waxing gibbous.", "isCorrect": False }
      ],
      "explanation": "The illuminated portion is shaped like a crescent and appears on the left side. As the illuminated part shrinks (wanes) from a full moon back to a new moon, the last sliver is the waning crescent."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "The **best** weather condition for harvesting maize for grinding into flour is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "cold and calm", "isCorrect": False },
        { "text": "cold and sunny", "isCorrect": False },
        { "text": "calm and dry", "isCorrect": False },
        { "text": "sunny and dry.", "isCorrect": True }
      ],
      "explanation": "Sunny and dry weather provides the heat and lack of moisture necessary for maize to dry thoroughly. This prevents the grains from rotting or developing aflatoxin before grinding."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "The following picture shows vegetables established on a special seedbed that conserves water.\n\n[Image: A raised seedbed inside a structure lined with a black polythene sheet]\n\nThe seedbed conserves water because it",
      "questionType": "multiple-choice",
      "options": [
        { "text": "has compost manure", "isCorrect": False },
        { "text": "is a deep seedbed", "isCorrect": False },
        { "text": "has a polythene sheet lining", "isCorrect": True },
        { "text": "is raised above the ground level.", "isCorrect": False }
      ],
      "explanation": "The black polythene sheet lining at the bottom and sides prevents water from seeping away deep into the ground, thus conserving moisture for the vegetables."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "The following picture shows land destroyed by soil erosion. Use it to answer questions **27** and **28**.\n\n[Image: Land with deep, wide channels and ravines cut into the soil]\n\nIdentify the type of soil erosion.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Gulley.", "isCorrect": True },
        { "text": "Rill.", "isCorrect": False },
        { "text": "Sheet.", "isCorrect": False },
        { "text": "Splash.", "isCorrect": False }
      ],
      "explanation": "The image shows deep, V-shaped channels and trenches carved into the landscape, which is the defining characteristic of gulley erosion."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "The **best** way of improving the above land for crop production is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "apply manure", "isCorrect": False },
        { "text": "construct gabions", "isCorrect": True },
        { "text": "mulch the land", "isCorrect": False },
        { "text": "plant cover crops.", "isCorrect": False }
      ],
      "explanation": "For deep gullies, the most effective method of control and repair is constructing gabions (wire mesh boxes filled with stones) across the gully to trap soil and slow down water."
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

print("Batch 2 questions inserted successfully!")
