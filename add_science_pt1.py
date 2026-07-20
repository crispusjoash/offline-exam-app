import json
import os
import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

science_paper = """
  {
    id: 'kpsea-science-2023',
    title: 'KPSEA 2023 Integrated Science',
    subject: 'Integrated Science',
    year: 2023,
    timeAllowed: 80, // 1 hr 20 mins typical
    instructions: [
      'You have 1 hour 20 minutes to complete this paper.',
      'Read each question carefully before answering.',
      'Answer ALL the questions.'
    ],
    sharedContexts: {},
    sectionA: [
      {
        questionNumber: 1,
        questionText: "During a lesson, Grade 6 learners discussed functions of different parts of a plant. Which part of a plant is responsible for making plant food?",
        options: [
          { text: "Root.", isCorrect: false },
          { text: "Stem.", isCorrect: false },
          { text: "Fruit.", isCorrect: false },
          { text: "Leaf.", isCorrect: true }
        ],
        explanation: "The leaf is the primary site of photosynthesis, the process by which a plant makes its food. Roots absorb water and minerals, the stem transports these materials and supports the plant, and the fruit protects seeds. None of these other parts are the primary site of food production."
      },
      {
        questionNumber: 2,
        questionText: "The following diagrams were drawn by learners to represent two types of root systems E and F.\\n![Root systems](/assets/q2_roots.png)\\nWhich one of the following pairs of plants is matched to its correct root system.",
        options: [
          { text: "E: Maize, F: Sugarcane", isCorrect: false },
          { text: "E: Beans, F: Maize", isCorrect: true },
          { text: "E: Sisal, F: Beans", isCorrect: false },
          { text: "E: Sugarcane, F: Sisal", isCorrect: false }
        ],
        explanation: "Diagram E shows a tap root system (one main thick root with smaller lateral roots), while Diagram F shows a fibrous root system (many roots of similar size growing from the stem base). Beans are dicotyledons and have tap roots (E). Maize is a monocotyledon and has fibrous roots (F)."
      },
      {
        questionNumber: 3,
        questionText: "During a class activity, learners recorded the following observations about a group of invertebrates:\\n(i) three body parts;\\n(ii) three pairs of legs;\\n(iii) have wings;\\n(iv) have antennae.\\nWhich one of the following is a member of the group observed by the learners?",
        options: [
          { text: "Tick.", isCorrect: false },
          { text: "Millipede.", isCorrect: false },
          { text: "Cockroach.", isCorrect: true },
          { text: "Centipede.", isCorrect: false }
        ],
        explanation: "The characteristics listed (three body parts, three pairs of legs, wings, and antennae) describe insects. A cockroach is an insect. A tick is an arachnid (two body parts, four pairs of legs), while millipedes and centipedes are myriapods with many body segments and numerous legs."
      },
      {
        questionNumber: 4,
        questionText: "The following diagram represents some parts of the human heart drawn by learners during a lesson on functions of parts of the heart.\\n![Heart diagram](/assets/q4_heart.png)\\nWhich one of the following is a function of the part labelled G?",
        options: [
          { text: "Pumping blood to the lungs.", isCorrect: false },
          { text: "Pumping blood to other parts of the body.", isCorrect: true },
          { text: "Receiving blood from the rest of the body.", isCorrect: false },
          { text: "Receiving deoxygenated blood.", isCorrect: false }
        ],
        explanation: "The part labelled G is the left ventricle, which is characterized by its thick muscular wall. Its function is to pump oxygenated blood with high pressure to all other parts of the body. Pumping blood to the lungs is the job of the right ventricle, while receiving blood is the job of the atria (upper chambers)."
      },
      {
        questionNumber: 5,
        questionText: "Grade 6 learners listed the following parts of the human reproductive system. Which part belongs to the female reproductive system?",
        options: [
          { text: "Cervix.", isCorrect: true },
          { text: "Prostate.", isCorrect: false },
          { text: "Testis.", isCorrect: false },
          { text: "Penis.", isCorrect: false }
        ],
        explanation: "The cervix is the lower part of the uterus that opens into the vagina, making it a part of the female reproductive system. The prostate, testis, and penis are all parts of the male reproductive system."
      },
      {
        questionNumber: 6,
        questionText: "During a Science lesson, learners observed activities shown in the following pictures. In which one of the activities is water **not** conserved?\\n![Water activities](/assets/q6_activities.png)",
        options: [
          { text: "A", isCorrect: false },
          { text: "B", isCorrect: false },
          { text: "C", isCorrect: false },
          { text: "D", isCorrect: true }
        ],
        explanation: "Activity D shows a person washing a car using a running hosepipe, which wastes a lot of water. In contrast, harvesting rainwater (A), mulching to retain soil moisture (B), and using a cup while brushing teeth (C) are all excellent methods of conserving water."
      },
      {
        questionNumber: 7,
        questionText: "A person donated a desktop computer to a friend who needed it instead of throwing it away. This is an example of managing solid waste by",
        options: [
          { text: "reusing and recycling", isCorrect: false },
          { text: "reusing only", isCorrect: true },
          { text: "reducing only", isCorrect: false },
          { text: "reducing and recycling.", isCorrect: false }
        ],
        explanation: "Giving an item to someone else to use in its current form is 'reusing'. 'Recycling' would involve breaking down the computer to make a new product, and 'reducing' involves buying less in the first place. Therefore, this action is reusing only."
      },
      {
        questionNumber: 8,
        questionText: "During a class discussion, learners suggested ways of controlling water pollution. Which one of the following ways would control water pollution?",
        options: [
          { text: "Boiling.", isCorrect: false },
          { text: "Filtration.", isCorrect: false },
          { text: "Avoiding open defecation.", isCorrect: true },
          { text: "Chemical treatment.", isCorrect: false }
        ],
        explanation: "Avoiding open defecation prevents harmful human waste from being washed into rivers and lakes, thereby controlling water pollution at its source. Boiling, filtration, and chemical treatment are methods of purifying water *after* it has already been polluted or drawn for use, not ways of controlling the pollution itself."
      },
      {
        questionNumber: 9,
        questionText: "During a class discussion, learners listed ways of preventing infestation by external parasites. Which one of the following ways prevent infestation by jiggers?",
        options: [
          { text: "Not sharing clothes.", isCorrect: false },
          { text: "Wearing shoes.", isCorrect: true },
          { text: "Soaking clothes in hot water.", isCorrect: false },
          { text: "Ironing clothes.", isCorrect: false }
        ],
        explanation: "Jiggers are external parasites found in dust and soil that burrow into bare feet or toes. Wearing shoes protects the feet and prevents jiggers from entering the skin. Not sharing clothes, soaking clothes, and ironing are methods used to prevent lice or bedbugs, not jiggers."
      },
      {
        questionNumber: 10,
        questionText: "Learners used a ball and ring shown in the following set up to demonstrate a certain property of matter. They observed that the ball could pass through the ring before heating but after heating it could not.\\n![Ball and ring](/assets/q10_ball_ring.png)\\nWhich one of the following properties of matter was being demonstrated? Matter",
        options: [
          { text: "exerts pressure and has volume", isCorrect: false },
          { text: "changes state and has mass", isCorrect: false },
          { text: "occupies space and has weight", isCorrect: false },
          { text: "expands and contracts.", isCorrect: true }
        ],
        explanation: "Heating the metal ball caused it to increase in size (expand) so it could no longer fit through the ring. When it cools, it will decrease in size (contract) and fit through again. This classic experiment specifically demonstrates that solid matter expands when heated and contracts when cooled."
      },
      {
        questionNumber: 11,
        questionText: "Which one of the statements describes an application of change of state of matter in everyday life?",
        options: [
          { text: "Working of thermometers.", isCorrect: false },
          { text: "Warming water.", isCorrect: false },
          { text: "Hardening of bricks.", isCorrect: false },
          { text: "Drying of clothes.", isCorrect: true }
        ],
        explanation: "Drying clothes involves evaporation, where liquid water in the wet clothes changes its state into water vapor (gas) and escapes into the air. Working of thermometers involves expansion, warming water is a temperature change without a state change, and hardening of bricks is a chemical/structural change."
      },
      {
        questionNumber: 12,
        questionText: "Which one of the following components of air is 78% by volume?",
        options: [
          { text: "Carbon dioxide.", isCorrect: false },
          { text: "Oxygen.", isCorrect: false },
          { text: "Nitrogen.", isCorrect: true },
          { text: "Inert gases.", isCorrect: false }
        ],
        explanation: "Nitrogen is the most abundant gas in the atmosphere, making up approximately 78% by volume. Oxygen makes up about 21%, while carbon dioxide and inert gases (like argon) make up less than 1% combined."
      },
      {
        questionNumber: 13,
        questionText: "Learners listed the following as ways by which friction can be reduced. Which one was **not** correct?",
        options: [
          { text: "Lubrication.", isCorrect: false },
          { text: "Sharpening tools.", isCorrect: true },
          { text: "Smoothening surfaces.", isCorrect: false },
          { text: "Using rollers.", isCorrect: false }
        ],
        explanation: "Sharpening tools is a way of increasing pressure to cut objects easily, it does not reduce friction between moving parts. In contrast, lubrication (oiling), smoothening rough surfaces, and using rollers (or ball bearings) are all effective methods used specifically to reduce friction."
      }
"""

match = re.search(r"(\s*)\]\,\n\s*KJSEA:\s*\[\]", content)
if match:
    insert_pos = match.start()
    new_content = content[:insert_pos] + ",\n" + science_paper + content[insert_pos:]
    with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Q1-Q13 Added!")
else:
    print("Could not find insertion point!")
