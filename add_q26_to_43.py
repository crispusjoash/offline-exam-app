import json
import shutil
import os

filepath = 'public/data/kjsea-creative-arts-sports-2025.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_sectionA = [
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "Mateka was asked by the teacher to perform a pass in rugby where he held the ball vertically at the lower part using both hands and threw it into the air towards the team-mate. Which of the following passes did Mateka perform?",
      "options": [
        "A. Flick pass",
        "B. Frisk pass",
        "C. Pop pass",
        "D. Spin pass"
      ],
      "correctAnswer": "C",
      "explanation": "A pop pass in rugby is executed by holding the ball vertically with both hands and 'popping' it up in the air for a teammate running in support."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "A Grade 9 learner performed passing skills used in a game of basketball. Identify the skill that is used to pass the ball accurately, at high speed over short distance.",
      "options": [
        "A. Chest pass",
        "B. Overhead pass",
        "C. Shoulder pass",
        "D. Side pass"
      ],
      "correctAnswer": "A",
      "explanation": "The chest pass is the most common basketball pass used for quick, accurate, high-speed passing over short distances."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "Mambo performed well during the inter-grade football game competition. What is the best thing Mambo's parents should do to make him excel in the game?",
      "options": [
        "A. Buy him a mountain bike.",
        "B. Buy him a snacks to celebrate.",
        "C. Enroll him in a sports academy.",
        "D. Ask his teacher to encourage him to do better."
      ],
      "correctAnswer": "C",
      "explanation": "Enrolling him in a sports academy provides specialized coaching and consistent training to help him develop and excel."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "A Junior School hosted a successful art exhibition. Which of the following describes the role Creative Arts achieved through the exhibition?",
      "options": [
        "A. Self-expression and personal fulfilment.",
        "B. Economic empowerment through art sales.",
        "C. Promoting social engagement Community service.",
        "D. Raising awareness on environmental issues through art."
      ],
      "correctAnswer": "B",
      "explanation": "A successful exhibition where artworks are displayed to the public and potentially sold primarily promotes economic empowerment for the artists, though it also fosters social engagement."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "During art lesson, learners applied a thin diluted layer of colour to cover the background in their landscape painting. Which painting technique did they use?",
      "options": [
        "A. Wash technique",
        "B. Sponge technique",
        "C. Brush stroke technique",
        "D. Finger painting technique"
      ],
      "correctAnswer": "A",
      "explanation": "A wash technique involves applying a thin, highly diluted, watery layer of paint to cover large areas like a background quickly and smoothly."
    },
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "The following motif illustrates a type of balance.\n\nThe type of balance illustrated is",
      "imagePath": "/assets/kjsea_cas_2025_q31.png",
      "options": [
        "A. linear",
        "B. radial",
        "C. symmetrical",
        "D. asymmetrical."
      ],
      "correctAnswer": "B",
      "explanation": "Radial balance occurs when elements radiate outward from a central point, as seen in the swirling dots."
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "Which two stages of drawing are shown in the following illustration?",
      "imagePath": "/assets/kjsea_cas_2025_q32.png",
      "options": [
        "A. Sketching and shading",
        "B. Sketching and drawing",
        "C. Observation and shading",
        "D. Drawing and photography"
      ],
      "correctAnswer": "A",
      "explanation": "The left side of the illustration shows basic line sketching and outlines, while the right side shows rendering and shading to add volume and texture."
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "The following reproduction of a still life painting was displayed for an art critique session.\n\nWhich of the following suggestions can improve the painting without changing the colour scheme?",
      "imagePath": "/assets/kjsea_cas_2025_q33.png",
      "options": [
        "A. Using more water.",
        "B. Adding bright colours.",
        "C. Darkening the background.",
        "D. Adding highlights with white."
      ],
      "correctAnswer": "D",
      "explanation": "Adding highlights with white enhances contrast, forms, and light reflections without introducing new colors to the established color scheme."
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "Patterns are used to enhance the beauty of traditional ornaments. What type of pattern was used in the following ornament?",
      "imagePath": "/assets/kjsea_cas_2025_q34.png",
      "options": [
        "A. Full repeat",
        "B. Regular repeat",
        "C. Alternate repeat",
        "D. Random repeat"
      ],
      "correctAnswer": "B",
      "explanation": "The pattern repeats the same geometric shape systematically, characteristic of a regular repeat pattern."
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "Zuka displayed a carving for sale but no buyer showed interest. What should Zuka do to make the carving more appealing?",
      "options": [
        "A. Improve on the finishing.",
        "B. Reduce the price to attract buyers.",
        "C. Transfer the carving to another shop.",
        "D. Change the labeling for better presentation."
      ],
      "correctAnswer": "A",
      "explanation": "Improving the finishing (sanding, polishing, varnishing) dramatically increases the aesthetic appeal and value of a carving."
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "To achieve strong contrast and create vibrant focal point an artist chooses to use complementary colours. Which of the following pairs of colours is considered complementary on the colour wheel?",
      "options": [
        "A. Red and blue",
        "B. Red and green",
        "C. Blue and violet",
        "D. Yellow and orange"
      ],
      "correctAnswer": "B",
      "explanation": "Complementary colors are located directly across from each other on the color wheel, such as red and green, blue and orange, or yellow and violet."
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Analyse the following picture of a gourd and answer the question that follows.\n\nWhich two techniques were used to decorate the gourd?",
      "imagePath": "/assets/kjsea_cas_2025_q37.png",
      "options": [
        "A. Burning and pasting",
        "B. Casting and painting",
        "C. Engraving and painting",
        "D. Engraving and pasting"
      ],
      "correctAnswer": "C",
      "explanation": "The gourd is decorated by engraving (carving lines into the surface) and painting (applying color to sections)."
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "Which of the following steps shows the correct order in the tie and dye fabric decoration process?",
      "options": [
        "A. Tie the fabric → Dip in dye → Dampen the fabric → Untie the fabric",
        "B. Dampen the fabric → Tie the fabric → Dip in dye → Untie the fabric",
        "C. Dip in dye → Tie the fabric → Dampen the fabric → Untie the fabric",
        "D. Tie the fabric → Dampen the fabric → Untie the fabric → Dip in dye"
      ],
      "correctAnswer": "B",
      "explanation": "The proper sequence is to first wash/dampen the fabric, fold and tie it tightly, dip it into the dye solution, and finally untie it after it sets."
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "Grade 8 learners selected blocks of soft wood and carved an animal in four steps as follows:\n(i) defining the features\n(ii) drawing outlines\n(iii) cutting away\n(iv) finishing\n\nWhich of the following shows the correct order they followed?",
      "options": [
        "A. (ii), (i), (iii), (iv)",
        "B. (iii), (i), (ii), (iv)",
        "C. (iii), (ii), (iv), (i)",
        "D. (ii), (iii), (i), (iv)"
      ],
      "correctAnswer": "D",
      "explanation": "The carving process starts with drawing outlines (ii), then cutting away excess material (iii), then defining detailed features (i), and concludes with finishing (iv)."
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "When choosing lettering for a logo design, several factors should be considered. Which of the following is least considered?",
      "options": [
        "A. Size of the letters.",
        "B. Shape of the letters.",
        "C. Typeface selection.",
        "D. Aesthetic appeal of the letters."
      ],
      "correctAnswer": "A",
      "explanation": "A well-designed logo must be scalable to any size (from a billboard to a business card). Therefore, absolute size is the least considered factor during the core design, whereas shape, typeface, and aesthetic appeal are permanent features."
    }
]

new_sectionB = [
    {
        "id": "q41",
        "questionNumber": 41,
        "parentQuestionText": "PART I: PERFORMING ARTS\n\nAnswer all questions in this part in the spaces provided.",
        "subQuestions": [
            {
                "id": "q41a",
                "questionText": "Using semi-breves, write the ascending scale of F major without key signature on treble staff.",
                "questionType": "drawing",
                "maxScore": 4,
                "modelAnswer": "Check student's drawing for the ascending scale of F major (F G A Bb C D E F). The notes must be semi-breves. Crucially, a flat symbol (b) must be placed immediately before the B note, since it's written without a key signature.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 4 marks for completely correct scale. Deduct marks for missing B flat, incorrect note positions, or wrong note types.",
                "subNumber": "(a)",
                "imagePath": "/assets/kjsea_cas_2025_q41.png"
            }
        ]
    },
    {
        "id": "q42",
        "questionNumber": 42,
        "subQuestions": [
            {
                "id": "q42a",
                "questionText": "Complete the following melody by adding an answering phrase to make a four-bar melody.",
                "questionType": "drawing",
                "maxScore": 4,
                "modelAnswer": "Check student's drawing. The answering phrase should match the rhythm and harmonic structure. For example, a common answering phrase to the given Twinkle Twinkle Little Star melody (G G D D E E D rest) would be (C C B B A A G rest).",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award up to 4 marks for a musically logical answering phrase that fits the time signature and resolves correctly.",
                "subNumber": "(a)",
                "imagePath": "/assets/kjsea_cas_2025_q42.png"
            }
        ]
    },
    {
        "id": "q43",
        "questionNumber": 43,
        "subQuestions": [
            {
                "id": "q43ai",
                "questionText": "What is the meaning of the following sign as used in the music?\n**mf**",
                "questionType": "structured",
                "maxScore": 1,
                "modelAnswer": "Here is a list of acceptable meanings:\n\n1. **Mezzo-forte:** Moderately loud.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for correct definition (Max 1 mark).",
                "subNumber": "(a)(i)",
                "imagePath": "/assets/kjsea_cas_2025_q43.png"
            },
            {
                "id": "q43aii",
                "questionText": "What is the meaning of the following sign as used in the music?\n**p**",
                "questionType": "structured",
                "maxScore": 1,
                "modelAnswer": "Here is a list of acceptable meanings:\n\n1. **Piano:** Soft.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for correct definition (Max 1 mark).",
                "subNumber": "(a)(ii)"
            },
            {
                "id": "q43aiii",
                "questionText": "What is the meaning of the following sign as used in the music?\n**||:  :||**",
                "questionType": "structured",
                "maxScore": 1,
                "modelAnswer": "Here is a list of acceptable meanings:\n\n1. **Repeat marks:** Indicates that the music enclosed within the signs is to be repeated.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for correct definition (Max 1 mark).",
                "subNumber": "(a)(iii)"
            }
        ],
        "parentQuestionText": "Study the music below and answer the questions that follow.\n*Bobby Shaftoe*"
    }
]

data['sectionA'].extend(new_sectionA)
data['sectionB'].extend(new_sectionB)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

dest_json = 'electron/app/data/kjsea-creative-arts-sports-2025.json'
shutil.copy(filepath, dest_json)

print(f"Added {len(new_sectionA)} Qs to Section A and {len(new_sectionB)} Qs to Section B.")
