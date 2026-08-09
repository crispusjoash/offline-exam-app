import json
import os

paper_structure = {
  "id": "kpsea-science-2024",
  "title": "KPSEA 2024 Integrated Science",
  "subject": "Integrated Science",
  "year": "2024",
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "The following picture was taken by a learner during a study on characteristics of plants.\n\n[Image: Plant before touch, Plant being touched, Plant after touch. The leaves fold up after being touched.]\n\nThe picture shows that plants",
      "questionType": "multiple-choice",
      "options": [
        { "text": "grow", "isCorrect": False },
        { "text": "respond to environmental changes", "isCorrect": True },
        { "text": "reproduce", "isCorrect": False },
        { "text": "carry out a gaseous exchange to survive.", "isCorrect": False }
      ],
      "explanation": "The plant depicted is folding its leaves when touched (a stimulus). This demonstrates that plants respond to changes in their environment."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "The following chart was drawn by a learner to show classification of plants.\n\nPlants \u2192 Flowering Plants (**E**) and Non-Flowering Plants (**F**)\n\nWhich of the following plants should the learner use to **correctly** represent **E** and **F**?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "E: Maize, F: Onion", "isCorrect": False },
        { "text": "E: Bean, F: Moss", "isCorrect": True },
        { "text": "E: Fern, F: Sugarcane", "isCorrect": False },
        { "text": "E: Cypress, F: Napier", "isCorrect": False }
      ],
      "explanation": "E represents flowering plants, and a bean plant produces flowers. F represents non-flowering plants, and moss is a non-flowering plant that reproduces via spores."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "Learners listed the following as functions of the human skeleton:\n\n(i) protection of organs\n(ii) maintenance of body posture\n(iii) manufacture of red blood cells\n(iv) movement of the body\n\nWhich of the listed functions are for limb bones of the human skeleton?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) and (ii)", "isCorrect": False },
        { "text": "(i) and (iii)", "isCorrect": False },
        { "text": "(ii) and (iv)", "isCorrect": False },
        { "text": "(iii) and (iv)", "isCorrect": True }
      ],
      "explanation": "Limb bones (such as the femur and humerus) are long bones. Their bone marrow manufactures red blood cells, and they act as levers with muscles to facilitate movement of the body."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "During a class discussion on signs and symptoms of diseases of the human breathing system, learners identified the following:\n\n(i) coughing up blood\n(ii) blocked nostrils\n(iii) pain in the chest\n(iv) vomiting\n(v) difficulties in breathing\n\nWhich of the following consists **only** of signs and symptoms of tuberculosis?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i), (ii) and (iii).", "isCorrect": False },
        { "text": "(i), (iii) and (v).", "isCorrect": True },
        { "text": "(ii), (iv) and (v).", "isCorrect": False },
        { "text": "(iii), (iv) and (v).", "isCorrect": False }
      ],
      "explanation": "Tuberculosis (TB) primarily affects the lungs. Common symptoms include a persistent cough (sometimes coughing up blood), chest pain, and breathing difficulties."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "During a lesson on classification of invertebrates, learners observed the characteristics of the invertebrate animal shown in the following picture.\n\n[Image: A spider with 8 legs]\n\nWhich of the following animals has the **same** characteristics as the animal in the picture?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Butterfly.", "isCorrect": False },
        { "text": "Millipede.", "isCorrect": False },
        { "text": "Tick.", "isCorrect": True },
        { "text": "Snail.", "isCorrect": False }
      ],
      "explanation": "The animal in the picture is a spider, which belongs to the class Arachnida (having 8 legs and two body parts). A tick is also an arachnid and shares these characteristics."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "During a class discussion, learners listed some characteristics of vertebrates. The following characteristics they listed apply to amphibians, **except**",
      "questionType": "multiple-choice",
      "options": [
        { "text": "live on both land and water.", "isCorrect": False },
        { "text": "have a moist skin.", "isCorrect": False },
        { "text": "the body is covered by scales.", "isCorrect": True },
        { "text": "body temperature controlled by the surrounding.", "isCorrect": False }
      ],
      "explanation": "Amphibians have a smooth, moist skin without scales. Animals with bodies covered by scales include fish and reptiles."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "While at home, a learner found some fungi growing on bread that had been poorly stored. This type of fungi is a",
      "questionType": "multiple-choice",
      "options": [
        { "text": "mould", "isCorrect": True },
        { "text": "mushroom", "isCorrect": False },
        { "text": "puffball", "isCorrect": False },
        { "text": "yeast.", "isCorrect": False }
      ],
      "explanation": "The fuzzy fungi that commonly grow on poorly stored, stale bread are called bread moulds."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Learners visited a certain factory and were each given ear muffs to put on. The purpose of the ear muffs was to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "protect them against loud sound.", "isCorrect": True },
        { "text": "avoid ear infections.", "isCorrect": False },
        { "text": "protect them against dust particles.", "isCorrect": False },
        { "text": "enable them hear properly.", "isCorrect": False }
      ],
      "explanation": "Ear muffs are safety devices worn over the ears to block out loud noises, protecting the eardrums from damage."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "During a class discussion, learners listed the following as causes of air pollution.\n\n(i) Smoke from burning farm waste\n(ii) Smell from waste in a pit latrine\n(iii) Waste from a construction site\n(iv) Smell from kitchen waste\n\nWhich one of the following pairs consists only of causes that can be controlled by changing waste into manure?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) and (ii).", "isCorrect": False },
        { "text": "(ii) and (iii).", "isCorrect": False },
        { "text": "(iii) and (iv).", "isCorrect": False },
        { "text": "(i) and (iv).", "isCorrect": True }
      ],
      "explanation": "Farm waste (like crop residue) and kitchen waste (like vegetable peelings) are biodegradable. Instead of burning farm waste (which causes smoke) or letting kitchen waste rot (which causes bad smell), they can be composted into manure."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "During a class discussion, learners stated ways of conserving water at home. Which of the following ways stated by the learners conserves water by re-using?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Harvesting rain water.", "isCorrect": False },
        { "text": "Boiling water for drinking.", "isCorrect": False },
        { "text": "Treating polluted water with chemicals.", "isCorrect": False },
        { "text": "Cleaning floor with laundry water.", "isCorrect": True }
      ],
      "explanation": "Re-using water involves taking water that has already been used for one purpose and using it for another purpose without undergoing a purification process, such as using laundry rinse water to clean the floor."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Learners collected different types of waste paper in the school compound and used them to make footballs. This is managing solid waste by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "recycling and re-using.", "isCorrect": True },
        { "text": "recycling only.", "isCorrect": False },
        { "text": "reducing and re-using.", "isCorrect": False },
        { "text": "re-using only.", "isCorrect": False }
      ],
      "explanation": "Making an entirely new item (football) out of waste materials (paper) involves a creative form of recycling and puts the waste to a new use."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "Grade 6 learners were asked to list various ways of managing solid waste.\nWhich of the following ways they listed involves recycling?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Giving out old clothes to the needy.", "isCorrect": False },
        { "text": "Feeding animals on potato peelings.", "isCorrect": False },
        { "text": "Making toilet paper from old newspapers.", "isCorrect": True },
        { "text": "Using old parts from a computer to repair other computers.", "isCorrect": False }
      ],
      "explanation": "Recycling involves processing waste materials at an industrial level into new products. Making toilet paper from old newspapers is an example of recycling."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "In creating a puzzle game, learners coded letters of the alphabet using numbers as shown.\n\na - 1, e - 5, i - 9\nb - 2, f - 6, j - 01\nc - 3, g - 7, k - 02\nd - 4, h - 8, l - 03\n\nWhich one of the following codes represented the word 'clickfile'?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "303903269035", "isCorrect": False },
        { "text": "303903026935", "isCorrect": False },
        { "text": "303930269035", "isCorrect": True },
        { "text": "303930269305", "isCorrect": False }
      ],
      "explanation": "Substitute the letters with their codes: c=3, l=03, i=9, c=3, k=02, f=6, i=9, l=03, e=5. Combining them gives 3 03 9 3 02 6 9 03 5."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "The following picture shows a spreadsheet window used by a learner to carry out simple operations.\n\n[Image: A spreadsheet window highlighting the formula bar labelled J]\n\nWhich one of the following operations can be carried out in the part labelled J?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Type the formula in the spreadsheet.", "isCorrect": True },
        { "text": "Type the name of the spreadsheet.", "isCorrect": False },
        { "text": "Create the spreadsheet.", "isCorrect": False },
        { "text": "Retrieve the spreadsheet.", "isCorrect": False }
      ],
      "explanation": "The part labelled J points to the Formula Bar in a spreadsheet application, which is used to view, type, or edit formulas and data in the active cell."
    }
  ]
}

file_path = 'src/data/kpsea-science-2024.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaScience2024 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("Batch 1 for Science 2024 generated!")
