import json
import os
import shutil

section_a_data = {
  "id": "kjsea-science-sectiona-2025",
  "title": "KJSEA 2025 Integrated Science (Section A)",
  "subject": "Integrated Science (Section A)",
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "Learners prepared the following list of first aid measures.",
      "questionList": [
        "(i) Wash the affected area with cool running water.",
        "(ii) Apply lotion to the affected area.",
        "(iii) Keep the affected area open."
      ],
      "questionSuffix": "The first aid measures would be applied in case of a",
      "options": [
        { "text": "burn", "isCorrect": True },
        { "text": "cut", "isCorrect": False },
        { "text": "chemical splashed in the eyes", "isCorrect": False },
        { "text": "ingestion of harmful chemicals.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\n**Burns** require immediate cooling to prevent further tissue damage, which is done by washing with cool running water. Mild lotions (like aloe vera) are sometimes applied after cooling to soothe minor burns, and keeping it open (unbandaged) helps minor burns heal without sticking to fabrics.\n\n**Why Other Options Are Incorrect:**\n* **B:** For a cut, one would apply pressure to stop bleeding and usually cover it with a sterile bandage, not keep it open.\n* **C:** For chemicals in the eyes, you wash with water, but you do not apply lotion.\n* **D:** Ingestion of chemicals requires seeking immediate medical help or calling a poison control center, not applying lotion or washing an external area.\n\n📌 **Key Learning Note:**\nImmediate cooling with running water is the most critical first aid step for treating burns and scalds."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "The following diagram represents an instrument used to measure a basic physical quantity.",
      "imagePath": "/assets/kjsea_science_2025_q2.png",
      "questionSuffix": "Which one of the following quantities is measured using the instrument?",
      "options": [
        { "text": "Temperature", "isCorrect": True },
        { "text": "Electric current", "isCorrect": False },
        { "text": "Weight", "isCorrect": False },
        { "text": "Length", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nThe instrument shown is a thermometer, which is explicitly used to measure **temperature** (the degree of hotness or coldness of a body), usually in degrees Celsius (°C) or Fahrenheit (°F).\n\n**Why Other Options Are Incorrect:**\n* **B:** Electric current is measured using an ammeter.\n* **C:** Weight is measured using a weighing balance or spring scale.\n* **D:** Length is measured using a ruler or tape measure.\n\n📌 **Key Learning Note:**\nTemperature is a fundamental physical quantity, and a thermometer utilizes the expansion and contraction of liquids (like mercury or alcohol) to measure it."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "Most cooking utensils are made of aluminium metals. Which of the following properties of aluminium makes it suitable for making cooking utensils?",
      "options": [
        { "text": "Good conductor of heat", "isCorrect": True },
        { "text": "Good conductor of electricity", "isCorrect": False },
        { "text": "Low melting point", "isCorrect": False },
        { "text": "It is easy to clean", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nAluminium is a **good conductor of heat**. This allows thermal energy from the stove to quickly and evenly transfer to the food being cooked, saving energy and time.\n\n**Why Other Options Are Incorrect:**\n* **B:** While aluminium conducts electricity, this property is irrelevant for cooking.\n* **C:** A low melting point would be dangerous, as the utensil could melt over the fire! Aluminium actually has a relatively high melting point.\n* **D:** While ease of cleaning is a benefit, the primary functional requirement for a cooking pot is its ability to transfer heat effectively.\n\n📌 **Key Learning Note:**\nMetals are widely used in cooking applications primarily because of their high thermal conductivity."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "An atom is the smallest particle of an element. Which of the following particles make up the nucleus of the atom?",
      "options": [
        { "text": "Protons and neutrons", "isCorrect": True },
        { "text": "Neutrons only", "isCorrect": False },
        { "text": "Protons only", "isCorrect": False },
        { "text": "Protons and electrons", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nThe dense, central core of an atom is called the nucleus. It consists of positively charged **protons** and neutrally charged **neutrons** (collectively known as nucleons).\n\n**Why Other Options Are Incorrect:**\n* **B, C:** The nucleus contains *both* protons and neutrons (except in regular Hydrogen-1, which lacks neutrons, but universally, the nucleus is defined by both).\n* **D:** Electrons are negatively charged particles that orbit *around* the nucleus in electron shells, not inside it.\n\n📌 **Key Learning Note:**\nAlmost all of an atom's mass is concentrated in its nucleus because protons and neutrons are much heavier than electrons."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "During a field visit to a farm, learners observed that some fruits have sour taste. The sour taste is caused by",
      "options": [
        { "text": "a base", "isCorrect": False },
        { "text": "water", "isCorrect": False },
        { "text": "a salt", "isCorrect": False },
        { "text": "an acid.", "isCorrect": True }
      ],
      "explanation": "The correct answer is **D**.\n\n**Analysis of the Correct Answer:**\nThe sour taste in many fruits (like lemons, oranges, and unripe mangoes) is caused by the presence of natural **acids**, such as citric acid, ascorbic acid, or malic acid.\n\n**Why Other Options Are Incorrect:**\n* **A:** Bases generally have a bitter taste and a soapy feel.\n* **B:** Pure water is neutral and tasteless.\n* **C:** Salts generally have a salty taste.\n\n📌 **Key Learning Note:**\nAcids are chemical substances characterized by a sour taste and their ability to turn blue litmus paper red."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "Susan, a Grade 8 learner, observed that elements combine to form compounds. The following pairs of elements can combine to form a compound except",
      "options": [
        { "text": "hydrogen and oxygen", "isCorrect": False },
        { "text": "copper and aluminium", "isCorrect": True },
        { "text": "nitrogen and hydrogen", "isCorrect": False },
        { "text": "oxygen and nitrogen.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\n**Copper and aluminium** are both metallic elements. When metals are mixed together, they form an *alloy* (a physical mixture), not a chemical compound.\n\n**Why Other Options Are Incorrect:**\n* **A:** Hydrogen and oxygen combine chemically to form water (H2O), a compound.\n* **C:** Nitrogen and hydrogen combine to form ammonia (NH3), a compound.\n* **D:** Oxygen and nitrogen combine to form nitrogen oxides (e.g., NO, NO2), which are compounds.\n\n📌 **Key Learning Note:**\nChemical compounds are typically formed by the chemical bonding of non-metals with non-metals (covalent) or metals with non-metals (ionic). Two metals do not chemically bond to form a compound."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "During a nature walk, learners collected samples of a solid substance and put it in water. They observed that the substance dissolved in water but left out some soil particles undissolved. The learners concluded that the solid sample is likely to be a",
      "questionList": [
        "(i) substance with salt and soil",
        "(ii) heterogeneous mixture",
        "(iii) homogeneous mixture",
        "(iv) soluble salt"
      ],
      "questionSuffix": "Which of the following combinations is true about the solid?",
      "options": [
        { "text": "(i) and (ii)", "isCorrect": True },
        { "text": "(ii) and (iv)", "isCorrect": False },
        { "text": "(i) and (iii)", "isCorrect": False },
        { "text": "(iii) and (iv)", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nSince part of the solid dissolved (like a salt) and part remained undissolved (soil), the original solid must have been a mixture of both **(i) salt and soil**. Because you can distinguish the different parts of this solid mixture (it is not uniform), it is classified as a **(ii) heterogeneous mixture**.\n\n**Why Other Options Are Incorrect:**\n* **(iii):** A homogeneous mixture has a uniform composition (like pure saltwater or air). The presence of visible, undissolving soil particles means it is not homogeneous.\n* **(iv):** Calling it a 'soluble salt' ignores the insoluble soil portion that was clearly part of the sample.\n\n📌 **Key Learning Note:**\nHeterogeneous mixtures contain visibly different substances or phases that can often be separated by physical means like filtration."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "The following are some of the changes that take place in nature:",
      "questionList": [
        "(i) boiling of water",
        "(ii) rusting of iron sheets",
        "(iii) burning of charcoal",
        "(iv) mixing water and salt"
      ],
      "questionSuffix": "Which two are chemical changes?",
      "options": [
        { "text": "(i) and (iv)", "isCorrect": False },
        { "text": "(ii) and (iv)", "isCorrect": False },
        { "text": "(ii) and (iii)", "isCorrect": True },
        { "text": "(i) and (iii)", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nA chemical change results in the formation of new substances and is usually irreversible. **(ii) Rusting of iron sheets** forms iron oxide (a new substance). **(iii) Burning of charcoal** produces carbon dioxide and ash (new substances).\n\n**Why Other Options Are Incorrect:**\n* **(i) Boiling water** is a change of state from liquid to gas (steam), which is a reversible physical change.\n* **(iv) Mixing water and salt** forms a solution which can easily be reversed by evaporation, making it a physical change.\n\n📌 **Key Learning Note:**\nChemical changes involve chemical reactions that alter the internal molecular structure of the original materials, whereas physical changes merely alter the state or appearance."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "The following picture shows a fire triangle.",
      "imagePath": "/assets/kjsea_science_2025_q9.png",
      "questionSuffix": "Which component of the fire triangle is missing in the picture?",
      "options": [
        { "text": "Oxygen", "isCorrect": True },
        { "text": "Extinguisher", "isCorrect": False },
        { "text": "Matches", "isCorrect": False },
        { "text": "Wood", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nThe fire triangle represents the three elements a fire needs to ignite: Heat, Fuel, and an oxidizing agent, usually **Oxygen**.\n\n**Why Other Options Are Incorrect:**\n* **B:** An extinguisher is used to put out a fire by removing one of the triangle's components, not part of the triangle itself.\n* **C, D:** Matches provide the 'Heat' and wood provides the 'Fuel', which are already represented on the triangle.\n\n📌 **Key Learning Note:**\nIf any one of the three components (Heat, Fuel, Oxygen) is removed, the fire will be extinguished. This principle is the basis of all fire-fighting techniques."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "Which of the following methods can only be used to separate homogeneous mixtures?",
      "options": [
        { "text": "Decantation", "isCorrect": False },
        { "text": "Distillation", "isCorrect": True },
        { "text": "Filtration", "isCorrect": False },
        { "text": "Evaporation", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\n**Distillation** (and fractional distillation) is specifically used to separate components of a homogeneous liquid mixture (like miscible liquids) based on their different boiling points, while recovering both the solute and the solvent.\n\n**Why Other Options Are Incorrect:**\n* **A, C:** Decantation and Filtration are exclusively used for separating heterogeneous mixtures (like sand and water).\n* **D:** While evaporation can separate a homogeneous solution (like salt in water), it is simply the vaporization of the liquid and does not allow for the recovery of the solvent, making distillation the more exclusive and complete method for separating such liquid mixtures.\n\n📌 **Key Learning Note:**\nHomogeneous mixtures (solutions) require separation methods that rely on physical properties like boiling points, rather than physical barriers like filter paper."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "The atomic number of chlorine is 17. Given that the number of neutrons in the nucleus of the atom is 18, calculate the mass number of chlorine.",
      "options": [
        { "text": "17", "isCorrect": False },
        { "text": "18", "isCorrect": False },
        { "text": "35", "isCorrect": True },
        { "text": "1", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nThe mass number of an atom is calculated by adding the number of protons (atomic number) to the number of neutrons. \nMass Number = Protons + Neutrons\nMass Number = 17 + 18 = **35**.\n\n**Why Other Options Are Incorrect:**\n* **A:** 17 is the atomic number (number of protons).\n* **B:** 18 is the number of neutrons.\n* **D:** 1 represents the difference, which has no atomic significance here.\n\n📌 **Key Learning Note:**\nThe atomic number identifies the element, while the mass number determines the specific isotope of that element."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "The following table shows the volume of soap solution used to form lather with four samples of equal volume of water.",
      "imagePath": "/assets/kjsea_science_2025_q12.png",
      "questionSuffix": "Which sample of water is the softest?",
      "options": [
        { "text": "(i)", "isCorrect": False },
        { "text": "(ii)", "isCorrect": True },
        { "text": "(iii)", "isCorrect": False },
        { "text": "(iv)", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nSoft water forms lather easily with soap, requiring very little soap solution. Hard water contains dissolved calcium and magnesium ions that react with soap to form scum, meaning a lot of soap is wasted before lather forms. Sample **(ii)** used the least volume of soap (1.5 cm³), meaning it is the softest.\n\n**Why Other Options Are Incorrect:**\n* **A, C, D:** These samples required much more soap (8.2, 5.4, and 11.2 cm³ respectively), indicating higher levels of water hardness. Sample (iv) is the hardest water.\n\n📌 **Key Learning Note:**\nThe amount of soap required to form a permanent lather is a direct indicator of water hardness; the less soap needed, the softer the water."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "During a class discussion, learners were tasked to classify the following substances as either metals or alloys:",
      "questionList": [
        "(i) Iron",
        "(ii) Bronze",
        "(iii) Brass",
        "(iv) Steel"
      ],
      "questionSuffix": "Which of the following combinations consists of alloys only?",
      "options": [
        { "text": "(i), (ii) and (iv)", "isCorrect": False },
        { "text": "(ii), (iii) and (iv)", "isCorrect": True },
        { "text": "(i), (ii) and (iv)", "isCorrect": False },
        { "text": "(i), (ii) and (iii)", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nAn alloy is a metallic substance made by mixing two or more elements. **(ii) Bronze** is an alloy of copper and tin. **(iii) Brass** is an alloy of copper and zinc. **(iv) Steel** is an alloy of iron and carbon.\n\n**Why Other Options Are Incorrect:**\n* **(i) Iron** is a pure elemental metal on the periodic table, not an alloy. Any combination containing (i) is therefore incorrect.\n\n📌 **Key Learning Note:**\nAlloys are created to improve the properties of pure metals, such as making them harder, stronger, or resistant to corrosion."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "The following diagram represents a human reproductive system.",
      "imagePath": "/assets/kjsea_science_2025_q14.png",
      "questionSuffix": "Implantation takes place at the part labelled",
      "options": [
        { "text": "4", "isCorrect": False },
        { "text": "1", "isCorrect": False },
        { "text": "3", "isCorrect": True },
        { "text": "2", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nImplantation is the process where a fertilized egg attaches to the uterine wall to begin developing into a fetus. Part **3** represents the Uterus (womb), which is where implantation occurs.\n\n**Why Other Options Are Incorrect:**\n* **1 (Fallopian tube/Oviduct):** This is where *fertilization* takes place, not implantation.\n* **2 (Ovary):** This is where eggs (ova) are produced and released.\n* **4 (Vagina):** This is the birth canal and the receptacle for sperm during mating.\n\n📌 **Key Learning Note:**\nThe inner lining of the uterus (endometrium) thickens with blood vessels each month specifically to prepare for the implantation of a fertilized embryo."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "Peter and his friends were discussing the functions of the human skin. Which of the following is not one of the functions they are likely to have discussed?",
      "options": [
        { "text": "Protection against germs", "isCorrect": False },
        { "text": "Exchange of gases", "isCorrect": True },
        { "text": "Protecting tissues from injury", "isCorrect": False },
        { "text": "Excretion of waste", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nIn humans, the **exchange of gases** (oxygen and carbon dioxide) occurs exclusively in the lungs (specifically the alveoli). The human skin is too thick and lacks the necessary structures for significant gas exchange, unlike amphibians (like frogs) that can breathe through their skin.\n\n**Why Other Options Are Incorrect:**\n* **A, C:** The skin acts as a physical barrier, protecting internal tissues from mechanical injury, UV radiation, and invading pathogens (germs).\n* **D:** The skin excretes waste products (like excess water, urea, and salts) through sweat.\n\n📌 **Key Learning Note:**\nThe skin is the largest organ of the human body and serves primarily for protection, thermoregulation, and sensation."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Which of the following components is only found in plant cells?",
      "options": [
        { "text": "Nucleus", "isCorrect": False },
        { "text": "Cell membrane", "isCorrect": False },
        { "text": "Cell wall", "isCorrect": True },
        { "text": "Mitochondrion", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nA **cell wall** is a rigid, structural layer found outside the cell membrane in plant cells (as well as fungi and bacteria), providing support and shape. Animal cells completely lack a cell wall.\n\n**Why Other Options Are Incorrect:**\n* **A, B, D:** The nucleus (control center), cell membrane (boundary controlling entry/exit), and mitochondrion (powerhouse) are fundamental organelles found in *both* plant and animal cells.\n\n📌 **Key Learning Note:**\nKey differences distinguishing plant cells from animal cells include the presence of a cell wall, chloroplasts (for photosynthesis), and large permanent vacuoles."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Osmosis involves movement of molecules across a membrane. Which row represents the correct type of molecule and membrane during osmosis?",
      "imagePath": "/assets/kjsea_science_2025_q17.png",
      "options": [
        { "text": "A. Water | Semi-permeable", "isCorrect": True },
        { "text": "B. Oxygen | Semi-permeable", "isCorrect": False },
        { "text": "C. Water | Permeable", "isCorrect": False },
        { "text": "D. Oxygen | Permeable", "isCorrect": False }
      ],
      "explanation": "The correct answer is **A**.\n\n**Analysis of the Correct Answer:**\nOsmosis is specifically defined as the movement of **water** molecules (solvent) from a region of low solute concentration to a region of high solute concentration across a **semi-permeable** (partially permeable) membrane.\n\n**Why Other Options Are Incorrect:**\n* **B, D:** The movement of gases like oxygen across a membrane is governed by simple *diffusion*, not osmosis.\n* **C:** A fully permeable membrane allows everything to pass freely, which would not result in the selective osmotic pressure effect; a semi-permeable membrane is strictly required.\n\n📌 **Key Learning Note:**\nOsmosis is essentially a special case of diffusion that applies exclusively to the movement of solvent molecules (usually water) across biological membranes."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "Various methods are used to control the number of mosquitoes to prevent the spread of malaria. Which one of the following methods can cause least ecological damage when controlling the number of mosquitoes?",
      "options": [
        { "text": "Draining the swamps where mosquitoes live.", "isCorrect": False },
        { "text": "Spraying swamps with chemical pesticides to kill mosquitoes.", "isCorrect": False },
        { "text": "Spraying oil over swamps to suffocate mosquito larvae.", "isCorrect": False },
        { "text": "Increasing the population of fish to feed on mosquito larvae.", "isCorrect": True }
      ],
      "explanation": "The correct answer is **D**.\n\n**Analysis of the Correct Answer:**\n**Increasing the population of fish** (such as Gambusia or 'mosquitofish') is a form of biological control. It relies on natural predator-prey relationships to control pests and introduces zero toxic chemicals into the environment, causing the least ecological damage.\n\n**Why Other Options Are Incorrect:**\n* **A:** Draining swamps destroys entire wetland ecosystems and habitats for countless other species.\n* **B:** Chemical pesticides are highly toxic, pollute the water, and kill non-target beneficial insects.\n* **C:** Spraying oil cuts off the oxygen supply to the water surface, which suffocates not just mosquito larvae, but also frogs, fish, and aquatic insects.\n\n📌 **Key Learning Note:**\nBiological pest control is the most environmentally friendly and sustainable method of managing agricultural and health-related pests."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "Which of the following is a condition required for photosynthesis to take place in plants?",
      "options": [
        { "text": "Glucose", "isCorrect": False },
        { "text": "Light", "isCorrect": True },
        { "text": "Oxygen", "isCorrect": False },
        { "text": "Heat", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\n**Light** energy (usually from the sun) is an absolute requirement for photosynthesis. Chlorophyll in the plant leaves captures this light energy to power the chemical reaction that turns water and carbon dioxide into food.\n\n**Why Other Options Are Incorrect:**\n* **A:** Glucose is the *product* (result) of photosynthesis, not a condition required for it to start.\n* **C:** Oxygen is also a *by-product* released during photosynthesis, not a raw material or condition.\n* **D:** While a suitable temperature is necessary for the enzymes to work, 'Heat' itself is not the specific driving energy condition for the reaction—light is.\n\n📌 **Key Learning Note:**\nThe equation for photosynthesis is: Carbon Dioxide + Water + (Light Energy) -> Glucose + Oxygen."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "The following picture shows a dentition obtained from a certain animal.",
      "imagePath": "/assets/kjsea_science_2025_q20.png",
      "questionSuffix": "The animal feeds on",
      "options": [
        { "text": "decaying matter", "isCorrect": False },
        { "text": "flesh", "isCorrect": False },
        { "text": "vegetation", "isCorrect": True },
        { "text": "vegetation and flesh.", "isCorrect": False }
      ],
      "explanation": "The correct answer is **C**.\n\n**Analysis of the Correct Answer:**\nThe skull clearly shows a large gap between the front teeth and the back teeth (a **diastema**) and broad, flat molars. This dentition is characteristic of herbivores, meaning the animal feeds strictly on **vegetation**.\n\n**Why Other Options Are Incorrect:**\n* **B:** Carnivores (flesh-eaters) have prominent, sharp canine teeth for tearing meat, which are absent here.\n* **D:** Omnivores (vegetation and flesh) have a mix of sharp canines and flatter molars, and lack a pronounced diastema.\n* **A:** Detritivores (decaying matter) generally do not have this type of advanced mammalian dentition.\n\n📌 **Key Learning Note:**\nA diastema allows herbivores to manipulate large quantities of plant material in their mouths without the front and back teeth interfering with each other."
    },
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "During a field study within the school compound, learners observed flowers with the following characteristics:",
      "imagePath": "/assets/kjsea_science_2025_q21.png",
      "questionSuffix": "Which pair of the flowers observed is insect pollinated?",
      "options": [
        { "text": "Q and S", "isCorrect": False },
        { "text": "R and T", "isCorrect": True },
        { "text": "R and S", "isCorrect": False },
        { "text": "Q and T", "isCorrect": False }
      ],
      "explanation": "The correct answer is **B**.\n\n**Analysis of the Correct Answer:**\nInsect-pollinated flowers have specific adaptations to attract pollinators. **Flower R (Sweet scented)** produces fragrance to attract insects like bees and butterflies from a distance. **Flower T (Brightly coloured petals)** acts as a visual beacon to attract insects.\n\n**Why Other Options Are Incorrect:**\n* **Q (Small in size) & S (Long stamen):** These are classic characteristics of *wind-pollinated* flowers. They are small because they don't need to attract insects, and they have long, exposed stamens so the wind can easily blow the pollen away.\n\n📌 **Key Learning Note:**\nInsect-pollinated flowers invest energy in attractions (large bright petals, nectar, scent), whereas wind-pollinated flowers invest energy in producing massive amounts of lightweight pollen."
    }
  ],
  "sectionB": [],
  "sharedContexts": {}
}

section_b_data = {
  "id": "kjsea-science-sectionb-2025",
  "title": "KJSEA 2025 Integrated Science (Section B)",
  "subject": "Integrated Science (Section B)",
  "sectionA": [],
  "sectionB": [],
  "sharedContexts": {}
}

import os
os.makedirs('public/data', exist_ok=True)
os.makedirs('electron/app/data', exist_ok=True)

with open('public/data/kjsea-science-sectiona-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_a_data, f, indent=2, ensure_ascii=False)
with open('public/data/kjsea-science-sectionb-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_b_data, f, indent=2, ensure_ascii=False)

shutil.copy('public/data/kjsea-science-sectiona-2025.json', 'electron/app/data/kjsea-science-sectiona-2025.json')
shutil.copy('public/data/kjsea-science-sectionb-2025.json', 'electron/app/data/kjsea-science-sectionb-2025.json')
print('Successfully generated Science Batch 1 JSON files.')
