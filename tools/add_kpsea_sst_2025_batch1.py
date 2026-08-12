import json

paper_structure = {
  "id": "kpsea-sst-parta-2025",
  "title": "KPSEA 2025 Social Studies & Creative Arts (Part A)",
  "subject": "Social Studies & Creative Arts (Part A)",
  "year": "2025",
  "isSubPaper": True,
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "The following chart shows primary and secondary colours.\n\n[Image: A colour wheel divided into 6 sectors. Going clockwise: Red, Orange, Yellow, Green, X, W]\n\nName the colours in the parts labelled W and X.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "W: Orange, X: Yellow", "isCorrect": False },
        { "text": "W: Purple, X: Blue", "isCorrect": True },
        { "text": "W: Orange, X: Blue", "isCorrect": False },
        { "text": "W: Yellow, X: Purple", "isCorrect": False }
      ],
      "explanation": "On a colour wheel, the primary colours are Red, Yellow, and Blue. Secondary colours (Orange, Green, Purple) are formed by mixing two primary colours. Yellow + Blue = Green. Red + Blue = Purple. Therefore, X is Blue and W is Purple."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "Which of the following statements is not true about the Kenya National Anthem? It promotes",
      "questionType": "multiple-choice",
      "options": [
        { "text": "hard work", "isCorrect": False },
        { "text": "patriotism", "isCorrect": False },
        { "text": "individualism", "isCorrect": True },
        { "text": "teamwork.", "isCorrect": False }
      ],
      "explanation": "The Kenya National Anthem promotes national unity, teamwork, patriotism, and hard work. It does not promote individualism."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "When playing a game, players aim at scoring. Which of the following games is correctly matched with the name of the score?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Netball - Point", "isCorrect": False },
        { "text": "Volleyball - Goal", "isCorrect": False },
        { "text": "Soccer - Goal", "isCorrect": True },
        { "text": "Handball - Point", "isCorrect": False }
      ],
      "explanation": "In soccer, a score is called a goal. In netball and handball, they are also called goals. In volleyball, scores are called points."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "Which of the choices shows the correct steps followed when carrying out crayon etching?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Scratch, apply black ink, colour with crayons.", "isCorrect": False },
        { "text": "Apply black ink, scratch, colour with crayons.", "isCorrect": False },
        { "text": "Apply black ink, colour with crayons, scratch.", "isCorrect": False },
        { "text": "Colour with crayons, apply black ink, scratch.", "isCorrect": True }
      ],
      "explanation": "In crayon etching, the paper is first coloured brightly with crayons, then a layer of black ink is applied over the crayons, and finally, a design is scratched out to reveal the bright colours underneath."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "Which of the following is not a Kenyan indigenous wind instrument?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Asili", "isCorrect": False },
        { "text": "Chivoti", "isCorrect": False },
        { "text": "Ishiriri", "isCorrect": True },
        { "text": "Muturiru", "isCorrect": False }
      ],
      "explanation": "The Ishiriri (or shiriri) is an indigenous string instrument (fiddle) from the Luhya community. Asili, Chivoti, and Muturiru are wind instruments."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "A netball coach trained players on the correct skills to apply when catching the ball. Which of the following skills did the coach emphasise?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Hands should be held tightly together, and arms stretched.", "isCorrect": False },
        { "text": "Feet should always be put together to increase the body stability.", "isCorrect": False },
        { "text": "Fingers for both hands should be spread out to enhance ball grip.", "isCorrect": True },
        { "text": "The palms of both hands should be facing the direction of the ball.", "isCorrect": False }
      ],
      "explanation": "When catching a ball in netball, fingers should be spread out to create a larger surface area and enhance the grip on the ball."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "A learner collected dry grass, banana fibre, glue and a board to make a picture.\nWhich of the following techniques should the learner use to make the picture?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Collage", "isCorrect": True },
        { "text": "Montage", "isCorrect": False },
        { "text": "Mosaic", "isCorrect": False },
        { "text": "Painting", "isCorrect": False }
      ],
      "explanation": "Collage is a technique where different textured materials like dry grass, leaves, and banana fibres are glued onto a surface (board) to create an artwork."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Which of the following is not a role played by instruments in a Kenyan folk dance?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Accompany the performance.", "isCorrect": False },
        { "text": "Decorate performers.", "isCorrect": True },
        { "text": "Play interludes.", "isCorrect": False },
        { "text": "Play melodies.", "isCorrect": False }
      ],
      "explanation": "Instruments are used to provide music (accompany the singing, play melodies, and interludes). They are not used as ornaments to decorate the performers."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "Grade 6 learners were making improvised skipping ropes during a lesson.\nWhich of the following actions should the learners take after the lesson to conserve the environment?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Use the improvised ropes to practise rope jumping skills.", "isCorrect": False },
        { "text": "Display the improvised ropes for others to see.", "isCorrect": False },
        { "text": "Clean up the area and dispose of any leftover materials.", "isCorrect": True },
        { "text": "Hang the ropes properly in the class to avoid any damage.", "isCorrect": False }
      ],
      "explanation": "Environmental conservation after a practical lesson involves cleaning up the workspace and properly disposing of leftover materials."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "The role of colour in an ornament is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "make it look smooth", "isCorrect": False },
        { "text": "make it beautiful", "isCorrect": True },
        { "text": "give it texture", "isCorrect": False },
        { "text": "make it durable.", "isCorrect": False }
      ],
      "explanation": "Colour is used in ornaments primarily for aesthetic purposes, to make them look beautiful and attractive."
    }
  ]
}

file_path = 'src/data/kpsea-sst-parta-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("Batch 1 for KPSEA SST Part A 2025 generated!")
