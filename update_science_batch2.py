import json
import os
import shutil

# Section A updates
with open('public/data/kjsea-science-sectiona-2025.json', 'r', encoding='utf-8') as f:
    section_a = json.load(f)

new_section_a_qs = [
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "During a visit to a national park, a learner took a photograph of birds feeding on ticks on a buffalo as shown.",
      "imagePath": "/assets/kjsea_science_2025_q22.png",
      "questionSuffix": "The relationship between the birds and the buffalo is",
      "options": [
        { "text": "holozoic", "isCorrect": False },
        { "text": "parasitic", "isCorrect": False },
        { "text": "saprophytic", "isCorrect": False },
        { "text": "symbiotic.", "isCorrect": True }
      ],
      "explanation": "The correct answer is **D**.\n\n**Analysis of the Correct Answer:**\nThe relationship between the oxpecker birds and the buffalo is **symbiotic** (specifically mutualism). Both organisms benefit: the birds get food (ticks) and the buffalo gets cleaned of blood-sucking parasites.\n\n**Why Other Options Are Incorrect:**\n* **A (Holozoic):** This refers to taking in complex organic matter (like humans eating food), not an ecological relationship.\n* **B (Parasitic):** In parasitism, one benefits and the other is harmed. The tick and the buffalo have a parasitic relationship, but the bird and the buffalo do not.\n* **C (Saprophytic):** This refers to organisms (like fungi) feeding on dead and decaying organic matter.\n\n📌 **Key Learning Note:**\nSymbiosis encompasses any close and long-term biological interaction between two different biological organisms. When both benefit, it is called mutualism."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "The following diagram represents a human digestive tract.",
      "imagePath": "/assets/kjsea_science_2025_q23.png",
      "questionSuffix": "Identify the physiological processes that take place in the parts marked Q and R.",
      "options": [
        { "text": "Q: Ingestion, R: Egestion", "isCorrect": False },
        { "text": "Q: Passage of food, R: Digestion", "isCorrect": True },
        { "text": "Q: Digestion, R: Ingestion", "isCorrect": False },
        { "text": "Q: Egestion, R: Passage of food", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nPart **Q** points to the gullet/oesophagus, whose main function is the **passage of food** (via peristalsis) from the mouth to the stomach. Part **R** points to the stomach, where mechanical and chemical **digestion** of proteins takes place.\n\n**Why Other Options Are Incorrect:**\n* **Ingestion** occurs in the mouth (taking in food).\n* **Egestion** occurs at the anus (removal of undigested waste).\n\n📌 **Key Learning Note:**\nThe digestive system is a long tube where specific processes happen sequentially: Ingestion (mouth) -> Digestion (stomach/small intestine) -> Absorption (small/large intestine) -> Egestion (anus)."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "The following diagram shows how two cells and two bulbs are arranged in a simple circuit.",
      "imagePath": "/assets/kjsea_science_2025_q24.png",
      "questionSuffix": "Which of the following is true about the arrangement?",
      "options": [
        { "text": "Cells: Parallel, Bulbs: Parallel", "isCorrect": False },
        { "text": "Cells: Parallel, Bulbs: Series", "isCorrect": False },
        { "text": "Cells: Series, Bulbs: Parallel", "isCorrect": True },
        { "text": "Cells: Series, Bulbs: Series", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nIn the diagram, the **cells** are connected end-to-end (positive terminal to negative terminal) in a single line, which is a **series** arrangement. The **bulbs** are connected across each other in separate branches, which is a **parallel** arrangement.\n\n**Why Other Options Are Incorrect:**\n* If the cells were in parallel, their positive terminals would be connected together, and their negative terminals connected together.\n* If the bulbs were in series, they would be connected end-to-end in the same single loop of wire.\n\n📌 **Key Learning Note:**\nConnecting cells in series increases the total voltage. Connecting bulbs in parallel ensures that if one bulb blows, the other remains lit because the current has an alternative path."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "The following diagram shows two toy cars each carrying a magnet. The toys were moved close to each other, then left free.",
      "imagePath": "/assets/kjsea_science_2025_q25.png",
      "questionSuffix": "Which of the following happened to the toys?",
      "options": [
        { "text": "They remained where they were.", "isCorrect": False },
        { "text": "The toys moved closer and stuck to each other.", "isCorrect": False },
        { "text": "One of the toys flipped over the other.", "isCorrect": False },
        { "text": "The toys moved away from each other.", "isCorrect": True }
      ],
      "explanation": "The correct answer is **D**.\n\n**Analysis of the Correct Answer:**\nIn the diagram, the North (N) pole of the magnet on the first car is facing the North (N) pole of the magnet on the second car. According to the law of magnetism, **like poles repel**. This repulsion force will push the toy cars away from each other.\n\n**Why Other Options Are Incorrect:**\n* **B:** They would only move closer and stick to each other if opposite poles (N and S) were facing each other (unlike poles attract).\n* **A:** Magnets exert a non-contact force, so they will not remain stationary if free to move.\n\n📌 **Key Learning Note:**\nThe fundamental law of magnetism states that like poles repel each other and unlike poles attract each other."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "Maria described the properties of a certain material she collected from the field as follows:",
      "questionList": [
        "(i) it is a solid",
        "(ii) it does not dissolve in water",
        "(iii) it is attracted by a magnet"
      ],
      "questionSuffix": "The material is likely to have been",
      "options": [
        { "text": "glass", "isCorrect": False },
        { "text": "wood", "isCorrect": False },
        { "text": "iron", "isCorrect": True },
        { "text": "plastic.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\n**Iron** is a solid, it is insoluble in water, and most importantly, it is a **magnetic material** (it is attracted by a magnet).\n\n**Why Other Options Are Incorrect:**\n* **A (Glass), B (Wood), and D (Plastic):** While these are all solids that do not dissolve in water, they are all non-magnetic materials and will not be attracted by a magnet.\n\n📌 **Key Learning Note:**\nOnly a few materials are magnetic. The most common magnetic elements are iron, nickel, and cobalt. Alloys containing these (like steel) are also magnetic."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "The following diagram shows solar cells mounted on a boat to produce electrical energy to power the boat.",
      "imagePath": "/assets/kjsea_science_2025_q27.png",
      "questionSuffix": "Which energy transformations take place for the boat to move?",
      "options": [
        { "text": "Light - mechanical - electrical", "isCorrect": False },
        { "text": "Light - electrical - mechanical", "isCorrect": True },
        { "text": "Electrical - light - mechanical", "isCorrect": False },
        { "text": "Electrical - mechanical - light", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\n1. The solar cells capture **Light** energy from the sun.\n2. They convert this light energy into **Electrical** energy.\n3. The electrical energy powers the boat's motor, which turns the propellers, converting it into **Mechanical** (kinetic) energy to move the boat.\n\n**Why Other Options Are Incorrect:**\n* The sequence must start with the initial source (Light). Mechanical energy cannot be the intermediate step because the solar cells generate electricity, not movement, directly from sunlight.\n\n📌 **Key Learning Note:**\nEnergy cannot be created or destroyed, only transformed from one form to another (Law of Conservation of Energy). Solar panels are photovoltaic, meaning they turn photons (light) directly into voltage (electricity)."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "A brick was placed on a surface. If the area of the brick in contact with the surface is reduced, what happens to the pressure exerted on the surface by the brick? The pressure",
      "options": [
        { "text": "increases", "isCorrect": True },
        { "text": "decreases", "isCorrect": False },
        { "text": "decreases then increases", "isCorrect": False },
        { "text": "increases then decreases.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nPressure is defined as Force divided by Area (P = F/A). The force (the weight of the brick) remains constant. If the area of contact is **reduced** (e.g., standing the brick on its narrowest edge), the same force is concentrated over a smaller area, causing the pressure to **increase**.\n\n**Why Other Options Are Incorrect:**\n* **B:** Pressure would only decrease if the area of contact was increased (e.g., laying the brick flat on its widest side).\n\n📌 **Key Learning Note:**\nThis principle is why sharp knives cut easily (tiny area = huge pressure) and why tractors have wide tires (large area = low pressure, preventing them from sinking into mud)."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "The following diagram shows reflection of light in a torch.",
      "imagePath": "/assets/kjsea_science_2025_q29.png",
      "questionSuffix": "What is the name of the point where the bulb is placed?",
      "options": [
        { "text": "Principal focus", "isCorrect": True },
        { "text": "Principal axis", "isCorrect": False },
        { "text": "Centre of curvature", "isCorrect": False },
        { "text": "Radius of curvature", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nIn a torch or car headlight, the bulb is placed exactly at the **principal focus** (focal point) of a concave reflector. When light rays from a source at the focal point hit the concave mirror, they are reflected forward as a powerful, parallel beam of light.\n\n**Why Other Options Are Incorrect:**\n* **B (Principal axis):** This is the imaginary straight line passing through the center of curvature and the pole of the mirror. It is a line, not a specific point.\n* **C (Centre of curvature):** If the bulb was placed here, the light rays would reflect straight back to the bulb.\n\n📌 **Key Learning Note:**\nConcave mirrors converge light. They are used in torches, car headlights, and solar concentrators to create strong directional beams."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "The following diagram shows a wave.",
      "imagePath": "/assets/kjsea_science_2025_q30.png",
      "questionSuffix": "The part marked L represents the",
      "options": [
        { "text": "amplitude", "isCorrect": True },
        { "text": "frequency", "isCorrect": False },
        { "text": "period", "isCorrect": False },
        { "text": "wavelength.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nThe arrow labeled **L** measures the maximum displacement of the wave from its rest (equilibrium) position to the crest. This distance is called the **amplitude** of the wave.\n\n**Why Other Options Are Incorrect:**\n* **B (Frequency):** The number of complete waves that pass a point per second.\n* **C (Period):** The time taken for one complete wave cycle.\n* **D (Wavelength):** The horizontal distance between two consecutive crests or troughs.\n\n📌 **Key Learning Note:**\nAmplitude indicates the energy of the wave. In sound waves, a larger amplitude means a louder sound. In light waves, a larger amplitude means brighter light."
    }
]
section_a['sectionA'].extend(new_section_a_qs)
with open('public/data/kjsea-science-sectiona-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_a, f, indent=2, ensure_ascii=False)


# Section B updates
with open('public/data/kjsea-science-sectionb-2025.json', 'r', encoding='utf-8') as f:
    section_b = json.load(f)

new_section_b_qs = [
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "Questions 31 involves basic measurement and quantities.",
      "subQuestions": [
        {
          "id": "q31a",
          "label": "a",
          "questionText": "Identify two basic skills in science acquired when using a metre rule. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable basic science skills acquired when using a metre rule:\n\n1. **Measuring:** Determining the exact length or distance between points.\n2. **Observation:** Carefully reading the markings and scale on the rule.\n3. **Recording data:** Noting down the accurate measurements obtained.\n4. **Accuracy/Precision:** Positioning the eye perpendicularly (avoiding parallax error) to get a true reading.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid skill identified (Max 2 marks).\n* **Flexibility:** Accept related skills like 'estimating'."
        },
        {
          "id": "q31b",
          "label": "b",
          "questionText": "State the SI units of the following physical quantities used in Integrated Science. (2 marks)",
          "questionList": [
            "1. Length",
            "2. Time"
          ],
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable SI units:\n\n1. **Length:** Metre (m)\n2. **Time:** Second (s)",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct SI unit (Max 2 marks).\n* **Flexibility:** Accept the symbol (m, s) or the full word."
        }
      ]
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "During a class discussion on mixtures, learners listed the following substances:",
      "questionList": [
        "(i) air",
        "(ii) sandy water",
        "(iii) rain water",
        "(iv) beans and maize"
      ],
      "subQuestions": [
        {
          "id": "q32a",
          "label": "a",
          "questionText": "Classify the substances as either homogeneous or heterogeneous mixtures. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable classifications:\n\n1. **Homogeneous:** Air, Rain water\n2. **Heterogeneous:** Sandy water, Beans and maize",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1/2 mark for each correctly classified substance (Max 2 marks)."
        },
        {
          "id": "q32b",
          "label": "b",
          "questionText": "Describe how a mixture of salt and water can be separated. (2 marks)",
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable ways to separate salt and water:\n\n1. **Evaporation:** The mixture is heated until all the water evaporates into the air as steam, leaving the solid salt crystals behind in the container.\n2. **Simple Distillation:** The mixture is heated so the water evaporates into steam. The steam is then passed through a condenser where it cools and turns back into liquid water (distillate) in a separate container, leaving the salt behind in the original flask.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for naming a correct method (e.g., evaporation or distillation) and 1 mark for a brief description of the process."
        }
      ]
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "Questions 33 covers chemical symbols and elements.",
      "subQuestions": [
        {
          "id": "q33a",
          "label": "a",
          "questionText": "Elements can be represented using chemical symbols. Give the appropriate chemical symbol to each of the following elements. (3 marks)",
          "questionList": [
            "1. Carbon",
            "2. Oxygen",
            "3. Sodium"
          ],
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable chemical symbols:\n\n1. **Carbon:** C\n2. **Oxygen:** O\n3. **Sodium:** Na",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct symbol (Max 3 marks).\n* **Flexibility:** Strict: The first letter must be capitalized (e.g., Na, not na or NA)."
        },
        {
          "id": "q33b",
          "label": "b",
          "questionText": "State one use of oxygen in day-to-day life. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable uses of oxygen:\n\n1. **Respiration:** Used by humans, animals, and plants for breathing to produce energy.\n2. **Combustion (Burning):** Required to support fires for cooking, heating, and running engines.\n3. **Medical use:** Given to patients in hospitals who have breathing difficulties.\n4. **Welding:** Oxy-acetylene flames are used for cutting and welding metals.\n5. **Diving/Mountaineering:** Carried in tanks where natural oxygen levels are low.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for any valid use of oxygen (Max 1 mark)."
        }
      ]
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "The following diagram shows states of matter. A represents tightly packed particles, B represents loosely packed particles, and C represents widely spaced particles.",
      "imagePath": "/assets/kjsea_science_2025_q34.png",
      "subQuestions": [
        {
          "id": "q34a",
          "label": "a",
          "questionText": "Name the states of matter represented by A and B. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable states of matter:\n\n1. **A:** Solid\n2. **B:** Liquid",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct state of matter (Max 2 marks)."
        },
        {
          "id": "q34b",
          "label": "b",
          "questionText": "Identify the processes labeled X (changing from A to B) and Y (changing from B to A). (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable processes:\n\n1. **X:** Melting (changing from solid to liquid)\n2. **Y:** Freezing / Solidification (changing from liquid to solid)",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct process identified (Max 2 marks)."
        }
      ]
    }
]

section_b['sectionB'].extend(new_section_b_qs)
with open('public/data/kjsea-science-sectionb-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_b, f, indent=2, ensure_ascii=False)

shutil.copy('public/data/kjsea-science-sectiona-2025.json', 'electron/app/data/kjsea-science-sectiona-2025.json')
shutil.copy('public/data/kjsea-science-sectionb-2025.json', 'electron/app/data/kjsea-science-sectionb-2025.json')
print('Successfully generated Science Batch 2 JSON files.')
