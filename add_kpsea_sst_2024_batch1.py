import json
import os

paper_structure = {
  "id": "kpsea-sst-parta-2024",
  "title": "KPSEA 2024 Social Studies & Creative Arts (Part A)",
  "subject": "Social Studies & Creative Arts (Part A)",
  "year": "2024",
  "isSubPaper": True,
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "A Grade 6 learner mounted and framed the following picture in readiness for an exhibition.\n\n[Image: A framed picture of a lion's head]\n\nWhy was the picture mounted and framed?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "To make it easy to carry to an exhibition.", "isCorrect": False },
        { "text": "For easy labelling of the artwork for exhibition.", "isCorrect": False },
        { "text": "To help identify the artwork during an exhibition.", "isCorrect": False },
        { "text": "To improve the appearance of the artwork for exhibition.", "isCorrect": True }
      ],
      "explanation": "Mounting and framing are primarily done to enhance the visual presentation and improve the appearance of the artwork, as well as to protect it."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "The following are hygiene and safety measures that should be observed when handling a descant recorder except",
      "questionType": "multiple-choice",
      "options": [
        { "text": "proper playing of the recorder", "isCorrect": True },
        { "text": "avoiding sharing of the recorder", "isCorrect": False },
        { "text": "constant cleaning of the recorder", "isCorrect": False },
        { "text": "proper storage of the recorder.", "isCorrect": False }
      ],
      "explanation": "Proper playing of the recorder is a musical skill, whereas avoiding sharing, cleaning, and proper storage are specific hygiene and safety measures."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "The following image shows a passing skill in netball.\n\n[Image: Two people passing a ball. One player is throwing the ball from the shoulder height.]\n\nWhat type of pass does the image represent?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Overhead pass.", "isCorrect": False },
        { "text": "Overhand pass.", "isCorrect": False },
        { "text": "Chest pass.", "isCorrect": False },
        { "text": "Shoulder pass.", "isCorrect": True }
      ],
      "explanation": "The player is holding the ball at shoulder level with one hand behind it, which is the characteristic posture for a shoulder pass in netball."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "The importance of adding texture to a two dimensional artwork is to make the",
      "questionType": "multiple-choice",
      "options": [
        { "text": "objects smooth", "isCorrect": False },
        { "text": "artwork complete", "isCorrect": False },
        { "text": "artwork appear rough", "isCorrect": False },
        { "text": "artwork interesting and realistic.", "isCorrect": True }
      ],
      "explanation": "Texture is added to 2D artwork to give it a tactile quality visually, making it look more interesting, realistic, and three-dimensional."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "The following are techniques of playing indigenous wind instruments. Which one is not?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Blowing.", "isCorrect": False },
        { "text": "Phrasing.", "isCorrect": False },
        { "text": "Tonguing", "isCorrect": False },
        { "text": "Tuning.", "isCorrect": True }
      ],
      "explanation": "Tuning is a preparatory activity to adjust the pitch of an instrument before playing, whereas blowing, phrasing, and tonguing are actual techniques used during playing."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "Which of the following activities would you engage in to enhance cardio-respiratory fitness?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Sleeping for long hours so as to rest.", "isCorrect": False },
        { "text": "Swimming regularly with friends.", "isCorrect": True },
        { "text": "Eating balanced diet at all times.", "isCorrect": False },
        { "text": "Watching soccer games to learn the skills.", "isCorrect": False }
      ],
      "explanation": "Cardio-respiratory fitness is enhanced through continuous, rhythmic physical activities like swimming, running, and cycling that raise the heart rate."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "The repetition of shapes and lines in a work of art creates",
      "questionType": "multiple-choice",
      "options": [
        { "text": "balance", "isCorrect": False },
        { "text": "dominance", "isCorrect": False },
        { "text": "space", "isCorrect": False },
        { "text": "rhythm.", "isCorrect": True }
      ],
      "explanation": "In art, rhythm is a principle of design that suggests movement or action, which is often created by the repetition of elements like shapes, lines, or colors."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Listening to songs from different communities helps us to do the following, except:",
      "questionType": "multiple-choice",
      "options": [
        { "text": "promote unity", "isCorrect": False },
        { "text": "learn others' culture", "isCorrect": False },
        { "text": "respect other people's culture", "isCorrect": False },
        { "text": "know which culture is better.", "isCorrect": True }
      ],
      "explanation": "Listening to diverse music promotes unity, learning, and respect for other cultures. It is not meant to compare or judge which culture is 'better' as all cultures are valuable."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "During break, learners were asked by the teacher to practice various skills in long jump. Which one of the following skills did the learners practice?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Sailing.", "isCorrect": True },
        { "text": "Scoring.", "isCorrect": False },
        { "text": "Bending.", "isCorrect": False },
        { "text": "Serving.", "isCorrect": False }
      ],
      "explanation": "Sailing is one of the flight techniques used in long jump (along with the hang and hitch-kick techniques). The others are not long jump skills."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "Which basketry technique is presented in the following picture?\n\n[Image: A circular basketry base showing spiral stitches]\n\n",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Twining.", "isCorrect": False },
        { "text": "Coiling.", "isCorrect": True },
        { "text": "Stitching.", "isCorrect": False },
        { "text": "Binding.", "isCorrect": False }
      ],
      "explanation": "The image shows the coiling technique, which involves wrapping a core material with a flexible binder and stitching it in a spiral to form a base."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Which of the following types of songs is not correctly matched with its function?\n\nType of song - Function",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Funeral songs - Comfort the bereaved", "isCorrect": False },
        { "text": "Marriage songs - Condemn the couple", "isCorrect": True },
        { "text": "Patriotic songs - Praise one's country", "isCorrect": False },
        { "text": "Work songs - Discourage laziness", "isCorrect": False }
      ],
      "explanation": "Marriage songs are meant to celebrate the union, advise, and praise the couple, not to condemn them."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "At the start of 100 m race, an athlete was disqualified for an improper start. Which one of the following acts did the athlete do?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Placed the hands behind the start line shoulder width apart.", "isCorrect": False },
        { "text": "Placed the knee of the back leg on the ground at the level of the front foot.", "isCorrect": False },
        { "text": "Placed the toes of the front leg slightly ahead of the starting line.", "isCorrect": True },
        { "text": "Kept the head and the neck slightly higher than the hip at the second command.", "isCorrect": False }
      ],
      "explanation": "In a sprint start, all body parts touching the ground (including toes and hands) must be strictly behind the starting line. Placing toes ahead of the line results in a false start."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "The following are steps of preparing leather thongs to be used for finishing a belt. Which one of the choices is in the correct order?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Cleaning, marking, punching.", "isCorrect": False },
        { "text": "Marking, cutting, cleaning.", "isCorrect": False },
        { "text": "Cleaning, marking, cutting.", "isCorrect": True },
        { "text": "Cutting, punching, marking.", "isCorrect": False }
      ],
      "explanation": "When preparing leather, the hide is first cleaned. Then, the desired shapes or strips (thongs) are marked out, and finally, they are cut."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "During a field visit, Grade 6 learners watched a performance of a Kenyan folk dance. They identified four participants and their respective roles as shown:\n\n(i) Dancers - sing solo sections\n(ii) Instrumentalists - accompany the dances\n(iii) Response group - singing chorus sections\n(iv) Soloist - leading the performance\n\nWhich of the participants is wrongly matched with their role?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Soloist.", "isCorrect": False },
        { "text": "Instrumentalists.", "isCorrect": False },
        { "text": "Dancers.", "isCorrect": True },
        { "text": "Response group.", "isCorrect": False }
      ],
      "explanation": "Dancers primarily perform the dance movements. Singing solo sections is the specific role of the soloist, not the dancers."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "Grade 6 learners were given an assignment to improvise a skipping rope. Which one of the following materials is the most suitable to use?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Paper.", "isCorrect": False },
        { "text": "Nylon.", "isCorrect": False },
        { "text": "Sisal.", "isCorrect": True },
        { "text": "Wires.", "isCorrect": False }
      ],
      "explanation": "Sisal fibers are strong, flexible, and commonly twisted together to make durable ropes suitable for skipping. Wires are dangerous, and paper/nylon bags might lack the necessary weight and durability unless extensively processed."
    }
  ]
}

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2024 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("Batch 1 for SST 2024 generated!")
