import json

file_path = 'public/data/kjsea-pretech-2025.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Ensure sectionB array exists
if 'sectionB' not in data:
    data['sectionB'] = []

section_b_questions = [
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "Fire outbreaks may lead to damage of property or injury. Give two ways of preventing fire outbreaks in a learning environment.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• Ensure proper electrical wiring and maintenance.\\n• Switch off electrical appliances when not in use.\\n• Avoid overloading electrical sockets.\\n• Clear dry leaves and rubbish from the compound.\\n• Store flammable materials safely away from heat sources.",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct preventive measure named (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "Using geometrical instruments, construct a rectangle of length 6 cm and a width of 4 cm.",
      "questionType": "drawing",
      "maxScore": 2,
      "modelAnswer": "/images/kjsea_pretech_2025_q35_ans.png",
      "gradingRubric": [
        { "criteria": "Accurate dimensions (6 cm by 4 cm).", "marks": 1 },
        { "criteria": "All corners accurately constructed at 90 degrees.", "marks": 1 }
      ]
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "Learners visited a building to observe the use of ceramic materials. Name two areas in the building where ceramic materials may have been used.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• Floors (ceramic floor tiles)\\n• Walls (ceramic wall tiles, especially in bathrooms/kitchens)\\n• Roofs (clay roofing tiles)\\n• Bathrooms/toilets (ceramic sinks, toilet bowls, bathtubs)",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct area named (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Grade 7 learners visited a work environment to learn more about safety. List three hazards to personal safety that the learners learnt.",
      "questionType": "structured",
      "maxScore": 3,
      "modelAnswer": "• Slippery floors (causing slips and falls).\\n• Exposed electrical wires (risk of electric shock).\\n• Sharp objects or tools lying around.\\n• Falling objects from heights.\\n• Poor lighting.\\n• Poor ventilation.\\n• Inhaling toxic fumes or dust.",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct hazard listed (max 3 marks).", "marks": 3 }
      ]
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "parentQuestionText": "Draw the following types of lines to a length of 6 cm.",
      "subQuestions": [
        {
          "id": "q38a",
          "subNumber": "(a)",
          "questionText": "Break line",
          "questionType": "drawing",
          "maxScore": 1,
          "modelAnswer": "/images/kjsea_pretech_2025_q38a_ans.png",
          "gradingRubric": [
            { "criteria": "Line drawn to 6 cm with the correct break symbol (zigzag for long break or wavy for short break).", "marks": 1 }
          ]
        },
        {
          "id": "q38b",
          "subNumber": "(b)",
          "questionText": "Centre line",
          "questionType": "drawing",
          "maxScore": 1,
          "modelAnswer": "/images/kjsea_pretech_2025_q38b_ans.png",
          "gradingRubric": [
            { "criteria": "Line drawn to 6 cm using the correct pattern (long dash, short dash, long dash).", "marks": 1 }
          ]
        }
      ]
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "parentQuestionText": "Grade 9 learners walked around the school compound to identify items made of metallic materials.",
      "subQuestions": [
        {
          "id": "q39a",
          "subNumber": "(a)",
          "questionText": "Name four items the learners may have identified.",
          "questionType": "structured",
          "maxScore": 2,
          "modelAnswer": "Window grills, door hinges, padlocks, roofing iron sheets, metallic dustbins, metallic chairs/desks frames, water pipes, flag post.",
          "gradingRubric": [
            { "criteria": "Award 0.5 marks for each correct item named (max 2 marks).", "marks": 2 }
          ]
        },
        {
          "id": "q39b",
          "subNumber": "(b)",
          "questionText": "Name two types of metals that may have been used to make the items in (a).",
          "questionType": "structured",
          "maxScore": 2,
          "modelAnswer": "Iron, Steel, Aluminium, Copper, Zinc, Brass.",
          "gradingRubric": [
            { "criteria": "Award 1 mark for each correct type of metal named (max 2 marks).", "marks": 2 }
          ]
        }
      ]
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "The government of Kenya is emphasising the use of e-citizen platform by businesses. State three benefits of this platform to businesses.",
      "questionType": "structured",
      "maxScore": 3,
      "modelAnswer": "• Faster and easier registration of businesses.\\n• Convenient access to government services from anywhere at any time.\\n• Secure payment of taxes, fees, and licenses.\\n• Reduces corruption and bribery by eliminating physical intermediaries.\\n• Saves time and travel costs.\\n• Efficient record keeping and tracking of applications.",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct benefit stated (max 3 marks).", "marks": 3 }
      ]
    },
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Ahmed wants to travel to another country to market his company's products. State two services that commercial banks may offer him during the trip.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• Foreign exchange (converting local currency to foreign currency).\\n• Issuance of credit or debit cards for international use.\\n• Electronic Funds Transfer (EFT) / wire transfers.\\n• Issuance of traveler's cheques.\\n• Safe custody of valuable documents (like contracts).",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct banking service stated (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Juma intends to set up a business of supplying eggs in his community. Give two reasons why he needs a business plan.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• To secure funding or loans from investors and banks.\\n• To set clear business goals and objectives.\\n• To identify potential risks and challenges in the egg supply business.\\n• To understand the market and competition.\\n• To guide day-to-day operations and resource allocation.",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct reason given (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "As a treasurer of Biashara Club in your school, you are provided with the following balances as at 30th August, 2024.\\nCash in hand 15,000\\nCash at bank 10,000\\nCapital 20,000\\nLoans 5,000\\nStock 2,000\\nCreditors 2,000\\nPrepare the statement of financial position for Biashara Club as at 30th August, 2024.",
      "questionType": "structured",
      "maxScore": 3,
      "modelAnswer": "**Biashara Club**\\n**Statement of Financial Position as at 30th August, 2024**\\n\\n**Assets**\\nCash in hand: 15,000\\nCash at bank: 10,000\\nStock: 2,000\\n**Total Assets = 27,000**\\n\\n**Capital and Liabilities**\\nCapital: 20,000\\nLoans: 5,000\\nCreditors: 2,000\\n**Total Capital & Liabilities = 27,000**",
      "gradingRubric": [
        { "criteria": "Correct title (Statement of financial position).", "marks": 0.5 },
        { "criteria": "Correctly classifying and listing Assets.", "marks": 1 },
        { "criteria": "Correctly classifying and listing Capital and Liabilities.", "marks": 1 },
        { "criteria": "Correctly balancing both sides at Ksh 27,000.", "marks": 0.5 }
      ]
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "A learner was given Ksh 800 as pocket money for use during the term. State two factors the learner should consider in setting financial goals for that term.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• The amount of money available (Ksh 800).\\n• Personal needs versus wants (prioritization of essential items).\\n• The duration the money needs to last (the whole term).\\n• Personal savings target (how much they want to save by the end of the term).\\n• Unforeseen emergencies.",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct factor stated (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "Tom made the following artefact from electronic waste materials.\\nWhich method of waste disposal did Tom use?",
      "imagePath": "/images/kjsea_pretech_2025_q45.png",
      "cssFilter": "brightness(0.92) contrast(1.15)",
      "questionType": "structured",
      "maxScore": 1,
      "modelAnswer": "Reusing (or Upcycling / Recycling).",
      "gradingRubric": [
        { "criteria": "Award 1 mark for Reusing, Upcycling, or Recycling.", "marks": 1 }
      ]
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "parentQuestionText": "Grade 8 learners visited a computer user environment to assist in setting up newly purchased computers.",
      "subQuestions": [
        {
          "id": "q46a",
          "subNumber": "(a)",
          "questionText": "Name two safety precautions the learners should adhere to when performing the task.",
          "questionType": "structured",
          "maxScore": 2,
          "modelAnswer": "• Ensure power is switched off before connecting or disconnecting cables.\\n• Avoid eating or drinking near the computers to prevent spills.\\n• Ensure cables are properly insulated.\\n• Avoid overloading power sockets.\\n• Ensure cables are neatly tied and not trailing on the floor to prevent tripping.",
          "gradingRubric": [
            { "criteria": "Award 1 mark for each correct safety precaution named (max 2 marks).", "marks": 2 }
          ]
        },
        {
          "id": "q46b",
          "subNumber": "(b)",
          "questionText": "Learners performed various tasks using computers. State the characteristic that describes computers' ability to carry out various tasks?",
          "questionType": "structured",
          "maxScore": 1,
          "modelAnswer": "Versatility.",
          "gradingRubric": [
            { "criteria": "Award 1 mark for Versatility.", "marks": 1 }
          ]
        }
      ]
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "parentQuestionText": "The following are keys found on a computer keyboard.",
      "imagePath": "/images/kjsea_pretech_2025_q47.png",
      "cssFilter": "brightness(0.92) contrast(1.15)",
      "subQuestions": [
        {
          "id": "q47a",
          "subNumber": "(a)",
          "questionText": "State the function of the keys.\\n**P**\\n**Q**",
          "questionType": "structured",
          "maxScore": 2,
          "modelAnswer": "**P (Enter key):** Used to execute a command, start a new paragraph, or confirm an entry.\\n**Q (Backspace key):** Used to delete characters to the left of the cursor.",
          "gradingRubric": [
            { "criteria": "Award 1 mark for correct function of key P (Enter).", "marks": 1 },
            { "criteria": "Award 1 mark for correct function of key Q (Backspace).", "marks": 1 }
          ]
        },
        {
          "id": "q47b",
          "subNumber": "(b)",
          "questionText": "Name the device used to output sound from a computer.",
          "questionType": "structured",
          "maxScore": 1,
          "modelAnswer": "Speakers (or Headphones / Earphones).",
          "gradingRubric": [
            { "criteria": "Award 1 mark for Speakers, Headphones, or Earphones.", "marks": 1 }
          ]
        }
      ]
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "A group of Grade 9 learners were given a task which involved the use of corrosive substances. Name two personal protective equipment they may have used when handling the substances.",
      "questionType": "structured",
      "maxScore": 2,
      "modelAnswer": "• Gloves (rubber/latex gloves)\\n• Goggles / Safety glasses (eye protection)\\n• Lab coat / Apron\\n• Closed shoes\\n• Face mask / Respirator",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct PPE named (max 2 marks).", "marks": 2 }
      ]
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "The following paragraph was typed in a word processing application.\\n\\nSelf-esteem refers to how we value and perceive ourselves based on our opinions and belief in ourselves. Your self-esteem can determine whether you value yourself as a person and your strengths. There are several things in life that may contribute to low self-esteem.\\nFor example:\\n  • *being bullied or abused*\\n  • *discrimination*\\n  • *worries about appearance and body image*\\nPeople with high self-esteem generally <u>feel positive about themselves and about life.</u>\\n\\nIdentify three formatting features applied to the paragraph.",
      "questionType": "structured",
      "maxScore": 3,
      "modelAnswer": "• Bullets (Bulleted list)\\n• Italics (Italicized text in the list)\\n• Underlining (Underlined text at the end)\\n• Indentation / Alignment",
      "gradingRubric": [
        { "criteria": "Award 1 mark for each correct formatting feature identified (max 3 marks).", "marks": 3 }
      ]
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "parentQuestionText": "The following instructions were created using a visual/programming application.",
      "imagePath": "/images/kjsea_pretech_2025_q50.png",
      "cssFilter": "brightness(0.92) contrast(1.15)",
      "subQuestions": [
        {
          "id": "q50a",
          "subNumber": "(a)",
          "questionText": "Identify one variable used in the instructions.",
          "questionType": "structured",
          "maxScore": 1,
          "modelAnswer": "Buying price (OR Selling price).",
          "gradingRubric": [
            { "criteria": "Award 1 mark for identifying either 'Buying price' or 'Selling price'.", "marks": 1 }
          ]
        },
        {
          "id": "q50b",
          "subNumber": "(b)",
          "questionText": "State the selection statement used in creating the instructions.",
          "questionType": "structured",
          "maxScore": 1,
          "modelAnswer": "IF ... THEN statement.",
          "gradingRubric": [
            { "criteria": "Award 1 mark for stating IF ... THEN statement.", "marks": 1 }
          ]
        }
      ]
    }
]

data['sectionB'].extend(section_b_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Batch 4 added.")
