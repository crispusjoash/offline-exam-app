import json
import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

science_pt3 = """      ,
      {
        questionNumber: 26,
        questionText: "Grade 5 learners at Kabila primary school were asked to give the meaning of common communicable diseases. Which one of the following statements is true about common communicable diseases?",
        options: [
          { text: "They are diseases that are spread easily from one person to another.", isCorrect: true },
          { text: "They are diseases that cannot be spread from one person to another.", isCorrect: false },
          { text: "They are diseases that are spread only by communicating to people.", isCorrect: false },
          { text: "They are diseases that spread only when people move from one place to another.", isCorrect: false }
        ],
        explanation: "Communicable diseases are illnesses caused by infectious agents (like viruses or bacteria) that can be easily transmitted from one infected person (or animal) to another. They are not spread by 'communicating' verbally, nor do they only spread when people move places, as they can spread within a household. Non-communicable diseases are the ones that cannot be spread (like diabetes or cancer)."
      },
      {
        questionNumber: 27,
        questionText: "Four Grade 6 learners were asked by their teacher to bring some items needed for a Home Science lesson. Below is what each learner brought:\\nAuma: Body lotion, petroleum jelly and skin care cream.\\nChris: Thread, thimble, make-up kit and pins.\\nFatma: Tie, socks, belt and scarf.\\nFestus: Cup, spoon, perfume and needle.\\nWho among the learners brought accessories used to enhance personal appearance?",
        options: [
          { text: "Auma.", isCorrect: false },
          { text: "Chris.", isCorrect: false },
          { text: "Fatma.", isCorrect: true },
          { text: "Festus.", isCorrect: false }
        ],
        explanation: "In Home Science, accessories are items worn with garments to complete or enhance an outfit. Ties, socks, belts, and scarves are all clothing accessories. Auma brought cosmetics/lotions, Chris brought sewing equipment (plus makeup), and Festus brought utensils and perfume."
      },
      {
        questionNumber: 28,
        questionText: "Razia advised her parents to always include savings in their family budget. Which one of the following statements is true about savings?",
        options: [
          { text: "Savings is the amount of money you are left with after buying all items required.", isCorrect: false },
          { text: "Savings is the amount of money you are given back after paying for items.", isCorrect: false },
          { text: "Savings is the amount of money set aside for unexpected expenses.", is   isCorrect: false },
          { text: "Savings is the amount of money set aside for future use.", isCorrect: true }
        ],
        explanation: "Savings is a deliberate decision to set aside a portion of income for future use or goals. Money set aside specifically for unexpected expenses is usually called an 'emergency fund'. Money left over after buying things is just a balance, and money given back after paying is 'change'."
      },
      {
        questionNumber: 29,
        questionText: "Masiero accompanied her father to the shop to buy cooking fat. Which one of the following is an important factor they should consider when choosing the cooking fat?",
        options: [
          { text: "Colour of the packaging.", isCorrect: false },
          { text: "Expiry date on the package.", isCorrect: true },
          { text: "The type of packaging used.", isCorrect: false },
          { text: "Weight of the packaging material.", isCorrect: false }
        ],
        explanation: "The expiry date is crucial for health and safety, as it indicates whether the cooking fat is still safe for consumption. Consuming expired products can cause food poisoning. The color, type, or weight of the packaging material are secondary factors that do not affect the safety or quality of the food inside."
      },
      {
        questionNumber: 30,
        questionText: "Grade 5 learners were asked to identify micronutrients found in food. Some of the micronutrients they identified are",
        options: [
          { text: "proteins and lipids", isCorrect: false },
          { text: "carbohydrates and lipids", isCorrect: false },
          { text: "carbohydrates and proteins", isCorrect: false },
          { text: "vitamins and minerals.", isCorrect: true }
        ],
        explanation: "Micronutrients are essential elements required by organisms in varying, but small, quantities throughout life (hence 'micro'). Vitamins and minerals fall into this category. Proteins, carbohydrates, and lipids (fats) are macronutrients because the body requires them in large amounts."
      },
      {
        questionNumber: 31,
        questionText: "Lotum has advised his uncle not to use salting method to preserve meat. Which one of the following is a reason Lotum's uncle should avoid using salt to preserve meat?",
        options: [
          { text: "Salt increases risk of constipation.", isCorrect: false },
          { text: "Salt increases risk of hypertension.", isCorrect: true },
          { text: "Salt improves weak bones.", isCorrect: false },
          { text: "Salt decreases the risk of asthma.", isCorrect: false }
        ],
        explanation: "Excessive consumption of salt (sodium) is a major dietary risk factor for developing hypertension (high blood pressure) and heart disease. It does not increase the risk of constipation, nor does it improve weak bones or decrease asthma risks."
      },
      {
        questionNumber: 32,
        questionText: "Salim is suffering from scurvy. Which one of the following eating habits is likely to have made Salim to develop scurvy?",
        options: [
          { text: "Decreased consumption of fruits and vegetables.", isCorrect: true },
          { text: "Increased consumption of fruits and vegetables.", isCorrect: false },
          { text: "Decreased consumption of foods rich in carbohydrates.", isCorrect: false },
          { text: "Increased consumption of foods rich in fibre and water.", isCorrect: false }
        ],
        explanation: "Scurvy is a nutritional deficiency disease caused by a severe lack of Vitamin C (ascorbic acid) in the diet. Vitamin C is abundantly found in fresh fruits (especially citrus) and vegetables. Therefore, a decreased consumption of these foods leads to scurvy."
      },
      {
        questionNumber: 33,
        questionText: "Ann and Ken were talking about one of the steps in laundering a handkerchief. The handkerchief is put in clean cold salty water without soap for some time. The step they were talking about is",
        options: [
          { text: "washing", isCorrect: false },
          { text: "sorting", isCorrect: false },
          { text: "soaking", isCorrect: true },
          { text: "rinsing.", isCorrect: false }
        ],
        explanation: "Soaking involves placing an item in water (often with salt to dissolve mucus in handkerchiefs or blood stains) for a period of time before the actual washing begins. This loosens dirt. Washing involves soap and agitation, rinsing removes soap, and sorting is separating clothes before laundering."
      },
      {
        questionNumber: 34,
        questionText: "Amanda has noticed that her school uniform has a gaping seam. She wants to repair it. Which one of the following stitches can she use to repair the gaping seam?",
        options: [
          { text: "Loop stitches.", isCorrect: false },
          { text: "Back stitches.", isCorrect: true },
          { text: "Hemming stitches.", isCorrect: false },
          { text: "Oversewing stitches.", isCorrect: false }
        ],
        explanation: "A back stitch is a very strong, permanent stitch used to join two pieces of fabric together, making it perfect for repairing a torn or gaping seam. Hemming is used to finish raw edges (like the bottom of a skirt), oversewing is for neatening raw edges to prevent fraying, and loop stitches are often decorative or used for buttonholes."
      },
      {
        questionNumber: 35,
        questionText: "Every time Rihana wears her favourite dress, it clings to the body which makes her uncomfortable. To prevent the dress from clinging to her body, Rihana should",
        options: [
          { text: "bleach the dress after washing", isCorrect: false },
          { text: "use a disinfectant when rinsing", isCorrect: false },
          { text: "rinse the dress well with clean water", isCorrect: false },
          { text: "use a fabric conditioner when rinsing.", isCorrect: true }
        ],
        explanation: "Clothes clinging to the body is usually caused by static electricity built up in synthetic fabrics. Fabric conditioners (softeners) coat the fibers with a lubricating layer that reduces friction and static cling. Bleach removes stains, disinfectants kill germs, and clean water removes soap, but none of these stop static cling."
      },
      {
        questionNumber: 36,
        questionText: "Grade 6 learners developed the following rules for racing games:\\ni. Wear suitable shoes while running;\\nii. Keep to your lane when running;\\niii. Drink adequate amount of water before the race;\\niv. Avoid performing any exercise before the race.\\nWhich one of the following set of rules is correct?",
        options: [
          { text: "i, ii, iv.", isCorrect: false },
          { text: "i, iii, iv.", isCorrect: false },
          { text: "i, ii, iii.", isCorrect: true },
          { text: "ii, iii, iv.", isCorrect: false }
        ],
        explanation: "Rules i, ii, and iii are all correct safety and performance guidelines for racing. However, rule 'iv' is completely wrong—athletes *must* perform warm-up exercises before a race to prepare their muscles and prevent injuries. Therefore, only the set containing i, ii, and iii is correct."
      },
      {
        questionNumber: 37,
        questionText: "Rope skipping is a common physical activity. Which one of the following statement is true about the effects of rope skipping exercise?",
        options: [
          { text: "Makes the leg joints weak.", isCorrect: false },
          { text: "Causes lifestyle disease.", isCorrect: false },
          { text: "Can cause injury to ankles.", isCorrect: false },
          { text: "Improves physical fitness.", isCorrect: true }
        ],
        explanation: "Rope skipping is a cardiovascular exercise that strengthens the heart, improves lung capacity, tones muscles, and improves overall physical fitness. While poor technique *could* hurt ankles, the general and primary intended effect is improving fitness. It actively prevents lifestyle diseases and strengthens (rather than weakens) leg joints over time."
      },
      {
        questionNumber: 38,
        questionText: "Grade 6 learners were asked to run to a specific point within the shortest time possible. Which component of fitness were the learners developing?",
        options: [
          { text: "Speed.", isCorrect: true },
          { text: "Coordination.", isCorrect: false },
          { text: "Strength.", isCorrect: false },
          { text: "Balance.", isCorrect: false }
        ],
        explanation: "Running to a specific point in the *shortest time possible* is a direct measure and training method for speed (the ability to move the body or a part of it rapidly over a distance). Strength is about exerting force, balance is about maintaining stability, and coordination is about smooth, controlled movements."
      }
"""

match = re.search(r"(\s*)\]\,\n\s*KJSEA:\s*\[\]", content)
if match:
    insert_pos = match.start()
    new_content = content[:insert_pos] + science_pt3 + "\n    ]\n  }" + content[insert_pos:]
    with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Q26-Q38 Added!")
else:
    print("Could not find insertion point!")
