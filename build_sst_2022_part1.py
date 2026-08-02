import json
import os

part_a_template = {
  "id": "kpsea-sst-parta-2022",
  "title": "KPSEA 2022 Social Studies & Creative Arts (Part A)",
  "subject": "Social Studies & Creative Arts (Part A)",
  "year": "2022",
  "isSubPaper": True,
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": []
}

q1_to_11 = [
  {
    "id": "q1",
    "questionNumber": 1,
    "questionText": "Pambani is in the process of creating a montage composition based on wildlife conservation to be placed at the art curiosity corner as indicated in the diagram below.\n\n[Diagram: Selecting picture -> Cutting picture -> Arranging and applying adhesive -> X]\n\nWhich **one** of the steps best fits in the space marked **X** on the diagram?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Pasting the pictures in a line.", "isCorrect": False},
      {"text": "Pasting the pictures randomly.", "isCorrect": False},
      {"text": "Pasting the pictures by overlapping.", "isCorrect": True},
      {"text": "Pasting pictures while leaving spaces around them.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Pasting the pictures by overlapping.**\n\n**Analysis of the Correct Answer:**\nA montage is an art technique that involves selecting, cutting, arranging, and pasting pictures together. The key characteristic of a montage is that the images are often pasted by overlapping them to create a single, unified composition. Therefore, after arranging and applying adhesive, the final step is pasting the pictures by overlapping.\n\n**Why Other Options Are Incorrect:**\n- **Pasting the pictures in a line / leaving spaces:** This describes a collage or a simple display, not specifically the overlapping nature characteristic of a montage.\n- **Pasting the pictures randomly:** While a montage can look random, \"overlapping\" is the specific technical step expected in the curriculum sequence."
  },
  {
    "id": "q2",
    "questionNumber": 2,
    "questionText": "Rika took a photograph of a ladybird.\n\nAt what angle was Rika's view if the ladybird looked actual?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Aerial view", "isCorrect": False},
      {"text": "Birds eye view", "isCorrect": False},
      {"text": "Worms eye view", "isCorrect": False},
      {"text": "Normal eye view", "isCorrect": True}
    ],
    "explanation": "The correct answer is **Normal eye view.**\n\n**Analysis of the Correct Answer:**\nWhen a subject in a photograph looks \"actual\" or natural (as we usually see it in real life without distortion), it is taken from a normal eye-level view (eye-level shot). This angle provides a realistic perspective of the subject.\n\n**Why Other Options Are Incorrect:**\n- **Aerial / Birds eye view:** Taken from above, making the subject look smaller or flattened.\n- **Worms eye view:** Taken from below, making the subject look larger and imposing."
  },
  {
    "id": "q3",
    "questionNumber": 3,
    "questionText": "The following are ways to critique each other's artwork in class. Which **one** is **not**?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Giving helpful suggestions", "isCorrect": False},
      {"text": "Keeping your opinion to yourself", "isCorrect": True},
      {"text": "Respecting each other's opinion", "isCorrect": False},
      {"text": "Giving honest and positive comments.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Keeping your opinion to yourself.**\n\n**Analysis of the Correct Answer:**\nCritiquing artwork involves actively sharing feedback to help improve the artist's work. Keeping your opinion to yourself defeats the purpose of a critique, which relies on constructive communication. Therefore, it is **not** a way to critique artwork.\n\n**Why Other Options Are Incorrect:**\n- **Giving helpful suggestions, Respecting each other's opinion, Giving honest and positive comments:** These are all excellent, constructive ways to participate in an art critique."
  },
  {
    "id": "q4",
    "questionNumber": 4,
    "questionText": "A group of learners were investigating how primary and secondary colours change when mixed in equal amounts.\n\nThey selected **two** primary colours and **two** secondary colours for the experiment and recorded the results on a table.\n\nBased on the experiment results, which set of colours best identifies the boxes labelled **X**, **Y**, and **Z**?\n\n| | Primary | | |\n| :--- | :--- | :--- | :--- |\n| | | **X** | **Blue** |\n| **Secondary** | | | |\n| | Yellow – Green | **Z** |\n| **Orange** | **Y** | | |\n| **Purple** | | Blue – Purple |\n\n*(Note: The table layout represents mixing primary and secondary colours. X is a primary colour. Z is the mix of X and Yellow-Green/Secondary. Y is the mix of Orange and X...)*\n\nA. **X** Yellow, **Y** Yellow – green, **Z** Blue – purple\nB. **X** Blue, **Y** Blue – green, **Z** Blue – purple\nC. **X** Yellow, **Y** Yellow – orange, **Z** Blue – green\nD. **X** Blue, **Y** Blue – green, **Z** Yellow – green",
    "questionType": "multiple-choice",
    "options": [
      {"text": "A", "isCorrect": False},
      {"text": "B", "isCorrect": False},
      {"text": "C", "isCorrect": True},
      {"text": "D", "isCorrect": False}
    ],
    "explanation": "The correct answer is **C (X Yellow, Y Yellow – orange, Z Blue – green).**\n\n**Analysis of the Correct Answer:**\nLet's analyze the table (which is a colour mixing matrix). The columns represent Primary colours and the rows represent Secondary colours.\n- The primary colours listed on the top right is **Blue**. The other primary colour is **X**. Since the secondary colours are Orange, Purple, and Green (implied), **X** must be **Yellow** (since Red is not producing the given tertiary colours here).\n- **Y** is the mixture of the secondary colour **Orange** and the primary colour **X** (Yellow). Mixing Yellow and Orange gives the tertiary colour **Yellow-Orange**.\n- **Z** is the mixture of **Blue** and the secondary colour **Green** (implied from Yellow-Green row). Mixing Blue and Green gives **Blue-Green**.\nTherefore, X = Yellow, Y = Yellow-orange, Z = Blue-green. This matches option C.\n\n**Why Other Options Are Incorrect:**\n- **A, B, D:** These options provide incorrect tertiary colour combinations based on standard colour theory mixing principles."
  },
  {
    "id": "q5",
    "questionNumber": 5,
    "questionText": "Wangari and Mayo decided to do a leaf print using a block cut out of an old slipper as shown below.\n\n[Image of a leaf motif block cut out]\n\nWhich **one** of the following correctly shows the printed motif?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "A (Mirror image of the block)", "isCorrect": True},
      {"text": "B (Same image as the block)", "isCorrect": False},
      {"text": "C (Inverted image)", "isCorrect": False},
      {"text": "D (Rotated image)", "isCorrect": False}
    ],
    "explanation": "The correct answer is **A (Mirror image of the block).**\n\n**Analysis of the Correct Answer:**\nIn block printing, the motif cut into the block will appear in reverse (as a mirror image) when it is pressed onto paper or fabric. If the stem curves to the right on the block, it will curve to the left on the print.\n\n**Why Other Options Are Incorrect:**\n- **B:** Shows the exact same orientation as the block, which is impossible in direct printing.\n- **C, D:** Show incorrect orientations (upside down or randomly rotated)."
  },
  {
    "id": "q6",
    "questionNumber": 6,
    "questionText": "Mwadine used coloured sand to decorate block letters but the sand fell off the paper.\n\nWhich of the statements **best** describes why the sand fell off the paper?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "The sand was very heavy.", "isCorrect": False},
      {"text": "The paper was very rough.", "isCorrect": False},
      {"text": "The adhesive was unsuitable.", "isCorrect": True},
      {"text": "The colour in the sand made it not stick.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **The adhesive was unsuitable.**\n\n**Analysis of the Correct Answer:**\nWhen creating sand art, the sand is held to the surface using an adhesive (glue). If the sand falls off after drying, it means the adhesive used was either not strong enough (unsuitable) for the weight/texture of the sand, or it wasn't applied correctly.\n\n**Why Other Options Are Incorrect:**\n- **The sand was very heavy:** While heavy sand needs stronger glue, proper adhesive would still hold normal coloured sand.\n- **The paper was very rough:** Rough paper actually provides *better* grip for adhesives than smooth paper.\n- **The colour in the sand made it not stick:** Food colouring or paint on sand does not prevent good glue from working."
  },
  {
    "id": "q7",
    "questionNumber": 7,
    "questionText": "The statements below describe the steps to be followed when making a table mat from sisal using coil and stitch technique.\n\n(i) pin the rope and sew in place to secure the centre\n(ii) continue coiling around as you sew in place\n(iii) twist the sisal into a rope\n(iv) connect the coils and complete the mat\n\nArrange the statements in the correct order.",
    "questionType": "multiple-choice",
    "options": [
      {"text": "iv, ii, iii, i", "isCorrect": False},
      {"text": "iii, i, ii, iv", "isCorrect": True},
      {"text": "i, ii, iii, iv", "isCorrect": False},
      {"text": "iii, i, iv, ii", "isCorrect": False}
    ],
    "explanation": "The correct answer is **iii, i, ii, iv.**\n\n**Analysis of the Correct Answer:**\nThe logical sequence for making a coiled sisal mat is:\n1. **(iii) twist the sisal into a rope:** You must first prepare the material by making a rope.\n2. **(i) pin the rope and sew in place to secure the centre:** You start by forming the core or centre of the mat.\n3. **(ii) continue coiling around as you sew in place:** You build the mat by coiling outwards from the centre.\n4. **(iv) connect the coils and complete the mat:** You finish the edge to complete the item.\nThis matches the sequence iii, i, ii, iv.\n\n**Why Other Options Are Incorrect:**\n- They present steps out of logical order (e.g., starting with securing the centre before even twisting the rope)."
  },
  {
    "id": "q8",
    "questionNumber": 8,
    "questionText": "Kantai modelled a slab container and decorated it at the leather hard stage using wet pellets which fell off.\n\nWhat would have been the cause?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "The slip was too wet.", "isCorrect": False},
      {"text": "The walls of the container were too thin.", "isCorrect": False},
      {"text": "The surface of the container were too thick to hold slip.", "isCorrect": False},
      {"text": "The surface was not scratched before attaching the pellets with slip.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **The surface was not scratched before attaching the pellets with slip.**\n\n**Analysis of the Correct Answer:**\nIn pottery, when joining two pieces of clay (like attaching pellets to a slab container), especially at the leather-hard stage, you must score (scratch) both surfaces and apply slip (liquid clay) to act as glue. This technique is called \"score and slip.\" If the pellets fell off, it is because Kantai failed to scratch the surface to create a strong mechanical bond.\n\n**Why Other Options Are Incorrect:**\n- **The slip was too wet:** Slip is supposed to be wet; it acts as glue.\n- **The walls were too thin / too thick:** Wall thickness does not cause attached decorations to fall off if joined properly."
  },
  {
    "id": "q9",
    "questionNumber": 9,
    "questionText": "You are collecting information for your Grade 6 national assessment project and have come across good artwork.\n\nWhich would be the correct way of using the artwork?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Copy and trace the artwork.", "isCorrect": False},
      {"text": "Edit the artwork and use it.", "isCorrect": False},
      {"text": "Seek permission from the artist.", "isCorrect": True},
      {"text": "Take a photograph when no one is watching.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Seek permission from the artist.**\n\n**Analysis of the Correct Answer:**\nWhen using someone else's artwork, you must respect their intellectual property rights and copyright. The ethical and correct way to use another person's creative work for a project is to seek their permission and credit them properly.\n\n**Why Other Options Are Incorrect:**\n- **Copy and trace / Edit and use it:** This is plagiarism and copyright infringement if done without permission.\n- **Take a photograph when no one is watching:** This is deceptive and still violates the artist's rights."
  },
  {
    "id": "q10",
    "questionNumber": 10,
    "questionText": "Which of the following is the correct order to follow when making a pot using coiling technique?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Form base, add coils, roll out coils and scratch edges.", "isCorrect": False},
      {"text": "Form base, scratch edges, roll out coils and add coils.", "isCorrect": False},
      {"text": "Add coils, form base, roll out coils and scratch edges.", "isCorrect": False},
      {"text": "Form base, roll out coils, scratch edges and add coils.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **Form base, roll out coils, scratch edges and add coils.**\n\n**Analysis of the Correct Answer:**\nThe logical steps for making a coiled clay pot are:\n1. **Form base:** Create the flat bottom of the pot first.\n2. **Roll out coils:** Create the clay \"ropes\" that will build the walls.\n3. **Scratch edges:** Score the base (and subsequent layers) to ensure the coils stick.\n4. **Add coils:** Attach the coils using slip to build the walls upwards.\n*(Note: Option D from the paper reads \"Form base, add coils, scratch edges and roll out coils\", wait, let me check the image. Option D is \"Form base, add coils, scratch edges and roll out coils\"? No, wait. Let me re-read the options from the image. )*\n*Correction: Option B says \"Form base, scratch edges, roll out coils and add coils.\" Option D says \"Form base, add coils, scratch edges and roll out coils.\" Wait, looking closely at the image for Q10:*\n*A. Form base, add coils, roll out coils and scratch edges.*\n*B. Form base, scratch edges, roll out coils and add coils.*\n*C. Add coils, form base, roll out coils and scratch edges.*\n*D. Form base, add coils, scratch edges and roll out coils.*\n*Wait, none of them perfectly match my logic. Let me re-read carefully: \"roll out coils\" must happen before \"add coils\". So B is the only one where \"roll out coils\" is before \"add coils\". Form base -> scratch edges -> roll out coils -> add coils. Yes, B is the correct logical flow.*",
    "options": [
      {"text": "Form base, add coils, roll out coils and scratch edges.", "isCorrect": False},
      {"text": "Form base, scratch edges, roll out coils and add coils.", "isCorrect": True},
      {"text": "Add coils, form base, roll out coils and scratch edges.", "isCorrect": False},
      {"text": "Form base, add coils, scratch edges and roll out coils.", "isCorrect": False}
    ]
  },
  {
    "id": "q11",
    "questionNumber": 11,
    "questionText": "Which type of song is sung to show love for one's country?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Action song.", "isCorrect": False},
      {"text": "Sacred song.", "isCorrect": False},
      {"text": "Patriotic song.", "isCorrect": True},
      {"text": "Topical song.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Patriotic song.**\n\n**Analysis of the Correct Answer:**\nPatriotic songs are specifically composed and sung to express love, devotion, and pride for one's country. Examples include National Anthems.\n\n**Why Other Options Are Incorrect:**\n- **Action song:** Sung with coordinated physical movements for entertainment or learning.\n- **Sacred song:** Religious songs sung for worship.\n- **Topical song:** Songs sung about current events or specific themes happening in society."
  }
]

part_a_template["sectionA"].extend(q1_to_11)

with open("src/data/kpsea-sst-parta-2022.js", "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstParta2022 = {json.dumps(part_a_template, indent=2)};\n")

print("Created kpsea-sst-parta-2022.js with Q1-Q11 successfully.")
