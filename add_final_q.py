import json
import shutil

filepath = 'public/data/kjsea-creative-arts-sports-2025.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_q43_sub = [
    {
        "id": "q43a_ii",
        "questionText": "Identify two bars with exact repetition.",
        "questionType": "structured",
        "maxScore": 1,
        "modelAnswer": "Here is a list of acceptable answers:\n\n1. **Bars 1 and 2:** These two bars are typically identical in the song Bobby Shaftoe.\n2. **Bars 5 and 6** (if applicable based on the specific arrangement).",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for correctly identifying two bars with exact repetition (Max 1 mark).",
        "subNumber": "(a)(ii)"
    },
    {
        "id": "q43a_iii",
        "questionText": "What is the lowest pitch in the music?",
        "questionType": "structured",
        "maxScore": 1,
        "modelAnswer": "Here is a list of acceptable answers:\n\n1. **Middle C (C4):** Depending on the key signature, it is usually the lowest note written in the typical arrangement shown.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for correctly identifying the lowest pitch (Max 1 mark).",
        "subNumber": "(a)(iii)"
    },
    {
        "id": "q43b_i",
        "questionText": "Outline three roles of music during a football match.",
        "questionType": "structured",
        "maxScore": 3,
        "modelAnswer": "Here is a list of acceptable roles:\n\n1. **Motivation/Encouragement:** To boost the morale of the players.\n2. **Entertainment:** To keep fans and spectators entertained before the match or during half-time.\n3. **Identity/Unity:** Singing anthems (national or club anthems) brings unity and a sense of belonging.\n4. **Intimidation:** Fans sing loud chants to intimidate the opposing team.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid role outlined (Max 3 marks).",
        "subNumber": "(b)(i)"
    },
    {
        "id": "q43b_ii",
        "questionText": "A soloist enjoys freedom in a performance of a traditional dance. Identify two ways in which they exercise this freedom.",
        "questionType": "structured",
        "maxScore": 2,
        "modelAnswer": "Here is a list of acceptable ways:\n\n1. **Improvisation of lyrics/melody:** They can make up words or change the tune spontaneously.\n2. **Movement/Dancing:** They are free to move around the stage or dance freely compared to the choir.\n3. **Pitch/Tempo control:** They can alter the speed or pitch to express emotion.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid way identified (Max 2 marks).",
        "subNumber": "(b)(ii)"
    }
]

new_sectionB_rest = [
    {
        "id": "q44",
        "questionNumber": 44,
        "subQuestions": [
            {
                "id": "q44a",
                "questionText": "State three aspects that need to be brought out at the beginning of the plot in a story.",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable aspects:\n\n1. **Setting:** Time and place where the story happens.\n2. **Characters:** Introduction of the main characters (protagonist, etc.).\n3. **Conflict/Problem:** The inciting incident or the main problem the characters will face.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid aspect stated (Max 3 marks).",
                "subNumber": "(a)"
            },
            {
                "id": "q44b",
                "questionText": "Outline three reasons why it is important to engage in vocal and physical warm up activities before performing a play.",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable reasons:\n\n1. **Prevent injuries:** Physical warm-ups prepare muscles and prevent strains.\n2. **Vocal clarity/projection:** Vocal warm-ups clear the throat, improve articulation, and prevent voice cracking.\n3. **Relieve tension:** Helps actors relax, reduce stage fright, and focus mentally.\n4. **Flexibility:** Enhances body movement for expressive acting.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid reason outlined (Max 3 marks).",
                "subNumber": "(b)"
            }
        ]
    },
    {
        "id": "q45",
        "questionNumber": 45,
        "parentQuestionText": "PART II: SPORTS\nAnswer questions 45, 46, 47 and either question 48 or 49 in the spaces provided.\n\nGrade 7 learners discussed strength component of physical fitness. Identify four activities that can help to develop strength that they may have discussed.",
        "subQuestions": [
            {
                "id": "q45",
                "questionText": "",
                "questionType": "structured",
                "maxScore": 4,
                "modelAnswer": "Here is a list of acceptable activities:\n\n1. Push-ups\n2. Squats\n3. Weightlifting / carrying heavy objects\n4. Pull-ups\n5. Planks\n6. Sit-ups",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid activity identified (Max 4 marks)."
            }
        ]
    },
    {
        "id": "q46",
        "questionNumber": 46,
        "parentQuestionText": "Grade 7 learners were practising performance in triple jump. Describe how they performed the following phases.",
        "subQuestions": [
            {
                "id": "q46a",
                "questionText": "Approach",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable descriptions:\n\n1. **Approach:** Running along the runway to build maximum controllable speed before reaching the take-off board.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for a correct description.",
                "subNumber": "(a)"
            },
            {
                "id": "q46b",
                "questionText": "Take off",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable descriptions:\n\n1. **Take off:** Planting the take-off foot firmly on the board and driving the body forward and upward to initiate the 'hop' phase, without stepping over the foul line.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for a correct description.",
                "subNumber": "(b)"
            }
        ]
    },
    {
        "id": "q47",
        "questionNumber": 47,
        "parentQuestionText": "During an inter-grade netball competition, Grade 8 learners were seen marking their opponents to prevent them from receiving the ball.",
        "subQuestions": [
            {
                "id": "q47a",
                "questionText": "Describe marking as used in netball.",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable descriptions:\n\n1. **Marking:** A defensive technique where a player stays close to an opponent to prevent them from receiving a pass, making a pass, or shooting, while maintaining the required distance (usually 3 feet).",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for a correct description.",
                "subNumber": "(a)"
            },
            {
                "id": "q47b",
                "questionText": "Outline three strategies they applied for successful marking.",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable strategies:\n\n1. **Positioning:** Staying on the toes and keeping between the opponent and the ball.\n2. **Anticipation:** Watching the passer's eyes to intercept the ball.\n3. **Arm positioning:** Raising arms to block the vision or path of the ball (while maintaining 3ft distance).\n4. **Communication:** Talking with teammates to switch marking assignments.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid strategy outlined (Max 3 marks).",
                "subNumber": "(b)"
            }
        ]
    },
    {
        "id": "q48",
        "questionNumber": 48,
        "parentQuestionText": "During a swimming gala, Grade 8 learners were asked to perform the butterfly stroke.",
        "subQuestions": [
            {
                "id": "q48a",
                "questionText": "Describe the butterfly stroke performed by the learners.",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable descriptions:\n\n1. **Description:** A swimming stroke where the swimmer is on their breast, with both arms moving simultaneously over the water in a forward circular motion, accompanied by a dolphin kick (legs moving up and down together).",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for mentioning simultaneous arm movement and 1 mark for mentioning the dolphin kick (Max 2 marks).",
                "subNumber": "(a)"
            },
            {
                "id": "q48b",
                "questionText": "Outline three challenges the learners may have experienced when performing the butterfly style of swimming.",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable challenges:\n\n1. **Fatigue:** It is highly exhausting and requires a lot of upper body strength and stamina.\n2. **Coordination:** Struggling to synchronize the arm pulls with the dolphin kick and breathing.\n3. **Breathing timing:** Finding it hard to lift the head to breathe at the right moment without breaking rhythm.\n4. **Water resistance:** Failing to maintain a streamlined body position, creating drag.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid challenge outlined (Max 3 marks).",
                "subNumber": "(b)"
            }
        ]
    },
    {
        "id": "q49",
        "questionNumber": 49,
        "parentQuestionText": "Grade 9 learners were introduced to indigenous board games during a sports lesson.",
        "subQuestions": [
            {
                "id": "q49a",
                "questionText": "Identify one indigenous board game played in Kenya.",
                "questionType": "structured",
                "maxScore": 1,
                "modelAnswer": "Here is a list of acceptable games:\n\n1. Ajua / Bao (Mancala)\n2. Shisima\n3. Kati (though not a board game, sometimes accepted if conflated, but strictly Ajua/Bao is the answer).",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for a correct game (Max 1 mark).",
                "subNumber": "(a)"
            },
            {
                "id": "q49b",
                "questionText": "Describe how the game identified in 49(a) is played.",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable descriptions (using Ajua as example):\n\n1. **Description:** Players sow seeds (or stones) into pits/holes on a wooden board. The goal is to capture more seeds than the opponent by dropping the last seed into an occupied or specific hole, following turn-based rules.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for a logical and correct description.",
                "subNumber": "(b)"
            },
            {
                "id": "q49c",
                "questionText": "Highlight two benefits of playing indigenous board game.",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable benefits:\n\n1. **Cognitive skills:** Improves critical thinking, counting, and strategy.\n2. **Socialization:** Promotes interaction, turn-taking, and bonding among peers.\n3. **Cultural preservation:** Helps pass down traditions and heritage to younger generations.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid benefit (Max 2 marks).",
                "subNumber": "(c)"
            }
        ]
    },
    {
        "id": "q50",
        "questionNumber": 50,
        "parentQuestionText": "PART III: VISUAL ARTS\nAnswer all questions in this part in the spaces provided.\n\nViron reused old fabric to create a mat using coil technique. Outline the four steps he followed in making the mat.",
        "subQuestions": [
            {
                "id": "q50a",
                "questionText": "",
                "questionType": "structured",
                "maxScore": 4,
                "modelAnswer": "Here is a list of acceptable steps:\n\n1. **Step 1:** Cut the old fabric into long, even strips.\n2. **Step 2:** Twist or braid the fabric strips into a continuous rope/cord.\n3. **Step 3:** Coil the fabric rope tightly starting from the center outward.\n4. **Step 4:** Stitch or bind the adjacent coils together firmly to secure the mat's shape.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correctly sequenced step (Max 4 marks)."
            }
        ]
    },
    {
        "id": "q51",
        "questionNumber": 51,
        "parentQuestionText": "A learner intends to print a fabric in one colour using a paper stencil. Describe four major steps they will follow when preparing the paper stencil for the task.",
        "subQuestions": [
            {
                "id": "q51a",
                "questionText": "",
                "questionType": "structured",
                "maxScore": 4,
                "modelAnswer": "Here is a list of acceptable steps:\n\n1. **Step 1:** Sketch the desired motif/design on a piece of paper or card.\n2. **Step 2:** Mark out the positive and negative spaces (areas to be cut out vs areas to be left solid).\n3. **Step 3:** Place the paper on a cutting mat/board.\n4. **Step 4:** Use a sharp craft knife or cutter to carefully cut out the positive spaces, ensuring 'ties' are left to hold the stencil together.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each logical and sequential step in preparing the stencil (Max 4 marks)."
            }
        ]
    },
    {
        "id": "q52",
        "questionNumber": 52,
        "parentQuestionText": "The following reproduction of a painting was displayed for a critique session at the end of a painting activity.\n\nAnalyse the painting fully and include points about:",
        "imagePath": "/assets/kjsea_cas_2025_q52.png",
        "subQuestions": [
            {
                "id": "q52a",
                "questionText": "a possible title for the artwork;",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable titles:\n\n1. \"Sunset Swing\"\n2. \"Evening Play\"\n3. \"Silhouette at Dusk\"\n(Accept any creative title relevant to a child swinging during sunset).",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for a relevant and creative title.",
                "subNumber": "(a)"
            },
            {
                "id": "q52b",
                "questionText": "forms present in the painting;",
                "questionType": "structured",
                "maxScore": 2,
                "modelAnswer": "Here is a list of acceptable forms:\n\n1. A tree branch.\n2. A swing with ropes.\n3. A human figure (child/girl) sitting on the swing.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each relevant form identified (Max 2 marks).",
                "subNumber": "(b)"
            },
            {
                "id": "q52c",
                "questionText": "use of colour;",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable observations:\n\n1. **Warm Colours:** Prominent use of warm colors (orange, yellow, red) to depict the sunset/sunrise.\n2. **Cool Colours:** A band of violet/blue at the top to represent the darkening sky.\n3. **Black/Silhouette:** Solid black is used for the foreground forms (tree, swing, child) to create a striking silhouette contrast against the bright sky.\n4. **Blending/Gradation:** Smooth blending of colors in the background from dark blue to yellow.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid point on color usage (Max 3 marks).",
                "subNumber": "(c)"
            },
            {
                "id": "q52d",
                "questionText": "use of space in the painting.",
                "questionType": "structured",
                "maxScore": 3,
                "modelAnswer": "Here is a list of acceptable observations:\n\n1. **Negative Space:** The vast, colorful sky forms the negative space, giving a sense of openness and tranquility.\n2. **Positive Space:** The black silhouette of the tree and swing occupies the positive space on the left side.\n3. **Balance:** The artwork uses asymmetrical balance; the heavy visual weight of the tree and swing on the left is balanced by the expansive negative space on the right.",
                "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid point on the use of space (Max 3 marks).",
                "subNumber": "(d)"
            }
        ]
    }
]

# Find Q43 and append subquestions
for q in data['sectionB']:
    if q['id'] == 'q43':
        q['subQuestions'].extend(new_q43_sub)
        break

data['sectionB'].extend(new_sectionB_rest)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

dest_json = 'electron/app/data/kjsea-creative-arts-sports-2025.json'
shutil.copy(filepath, dest_json)

print(f"Added remaining questions to Section B.")
