import json
import os

paper_structure = {
  "id": "kpsea-science-2025",
  "title": "KPSEA 2025 Integrated Science",
  "subject": "Integrated Science",
  "year": "2025",
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "During a nature walk, learners saw a lizard on a rock. When the weather became hot, the lizard was seen under a shade. The behaviour of the lizard shows that as a living thing, it",
      "questionType": "multiple-choice",
      "options": [
        { "text": "moves from place to place", "isCorrect": False },
        { "text": "breathes", "isCorrect": False },
        { "text": "responds to environmental changes", "isCorrect": True },
        { "text": "feeds.", "isCorrect": False }
      ],
      "explanation": "The lizard moving to a shade when the weather became hot is a response to the change in temperature (an environmental change)."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "During a class discussion, learners listed the following as the benefits of fungi to humans:\n(i) used as food\n(ii) used to make medicine\n(iii) used in baking\n(iv) used in brewing\n\nWhich two benefits apply to yeast?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(i) and (ii)", "isCorrect": False },
        { "text": "(ii) and (iii)", "isCorrect": False },
        { "text": "(iii) and (iv)", "isCorrect": True },
        { "text": "(i) and (iv)", "isCorrect": False }
      ],
      "explanation": "Yeast is a type of fungi commonly used in baking (to make dough rise) and in brewing (for fermentation)."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "The following diagram represents the human digestive system.\n\n[Image: Human digestive system diagram with part G pointing to the large intestines]\n\nIdentify the part labeled G.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Large intestines.", "isCorrect": True },
        { "text": "Rectum.", "isCorrect": False },
        { "text": "Small intestines.", "isCorrect": False },
        { "text": "Stomach.", "isCorrect": False }
      ],
      "explanation": "The part labeled G points to the large intestines (colon), which absorbs water from undigested food."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "A person felt cold and decided to move to a nearby fire place. The sense organs involved in the person's action are",
      "questionType": "multiple-choice",
      "options": [
        { "text": "eyes and nose", "isCorrect": False },
        { "text": "ears and skin", "isCorrect": False },
        { "text": "nose and ears", "isCorrect": False },
        { "text": "skin and eyes.", "isCorrect": True }
      ],
      "explanation": "The person felt cold using the skin (sense of touch/temperature) and located the nearby fireplace using the eyes (sense of sight)."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "Water cycle involves freezing, melting, evaporation and condensation processes.\n\nWhich of the following statements describes condensation?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ice changing to water.", "isCorrect": False },
        { "text": "Water vapour changing to water.", "isCorrect": True },
        { "text": "Water changing to ice.", "isCorrect": False },
        { "text": "Water changing to water vapour.", "isCorrect": False }
      ],
      "explanation": "Condensation is the process where a gas (water vapour) changes into a liquid (water) upon cooling."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "After rains, a learner observed water flowing from farms to a nearby river. The learner concluded that the main pollutant of the river was",
      "questionType": "multiple-choice",
      "options": [
        { "text": "animal feed remains", "isCorrect": False },
        { "text": "used polythene bags", "isCorrect": False },
        { "text": "farm chemicals", "isCorrect": True },
        { "text": "sewage waste.", "isCorrect": False }
      ],
      "explanation": "Water flowing from farms is likely to carry farm chemicals such as fertilizers and pesticides into the river, causing water pollution."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "The following picture shows a modified root observed by learners during a lesson on functions of roots.\n\n[Image: A carrot]\n\nWhat is the function of the modified root?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Breathing.", "isCorrect": False },
        { "text": "Storage.", "isCorrect": True },
        { "text": "Anchorage.", "isCorrect": False },
        { "text": "Absorption.", "isCorrect": False }
      ],
      "explanation": "The picture shows a carrot, which is a root modified to store manufactured food for the plant."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Which of the following pairs of liquids will give a homogenous mixture when put together?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Water and kerosene.", "isCorrect": False },
        { "text": "Cooking oil and water.", "isCorrect": False },
        { "text": "Kerosene and cooking oil.", "isCorrect": True },
        { "text": "Milk and kerosene.", "isCorrect": False }
      ],
      "explanation": "Kerosene and cooking oil are both miscible liquids that will mix uniformly to form a homogenous mixture. Water does not mix with kerosene or cooking oil."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "The following picture shows a composting practice used by learners to manage waste in their school.\n\n[Image: A compost pit with organic waste]\n\nThe practice manages waste by",
      "questionType": "multiple-choice",
      "options": [
        { "text": "recycling and reusing", "isCorrect": False },
        { "text": "reducing only", "isCorrect": False },
        { "text": "reusing and reducing", "isCorrect": False },
        { "text": "recycling only.", "isCorrect": True }
      ],
      "explanation": "Composting involves the breaking down of organic waste into manure. This is a form of recycling nutrients back into the soil."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "Ali, while standing outside the classroom, could clearly see other classmates through a glass window. When he smeared the window with petroleum jelly, he could no longer see the classmates. This is because the glass changed from",
      "questionType": "multiple-choice",
      "options": [
        { "text": "translucent to opaque", "isCorrect": False },
        { "text": "transparent to translucent", "isCorrect": True },
        { "text": "transparent to opaque", "isCorrect": False },
        { "text": "opaque to translucent.", "isCorrect": False }
      ],
      "explanation": "Glass is transparent (allows light to pass through clearly). Smearing it with petroleum jelly makes it translucent (allows some light to pass but scatters it, making objects on the other side unclear)."
    }
  ]
}

file_path = 'src/data/kpsea-science-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaScience2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("Batch 1 for KPSEA Science 2025 generated!")
