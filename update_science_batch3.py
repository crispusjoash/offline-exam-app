import json
import os
import shutil

# Section B updates
filepath = 'public/data/kjsea-science-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    section_b = json.load(f)

new_section_b_qs = [
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "Autotrophism is a mode of nutrition where plants make their own food.",
      "subQuestions": [
        {
          "id": "q35a",
          "label": "a",
          "questionText": "Name two raw materials required by plants during autotrophism. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable raw materials:\n\n1. **Water (H2O):** Absorbed from the soil by roots.\n2. **Carbon dioxide (CO2):** Absorbed from the air through stomata.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid raw material (Max 2 marks).\n* **Flexibility:** Do not accept sunlight or chlorophyll as raw materials; they are conditions/agents, not raw materials."
        },
        {
          "id": "q35b",
          "label": "b",
          "questionText": "Identify the cell organelle where photosynthesis occurs. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable organelles:\n\n1. **Chloroplast:** The specific plastid containing chlorophyll where photosynthesis takes place.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'chloroplast' (Max 1 mark)."
        },
        {
          "id": "q35c",
          "label": "c",
          "questionText": "State how the following features of plant leaves affect the photosynthesis process:",
          "questionList": [
            "(i) broad leaf surface; (1 mark)",
            "(ii) network of veins. (1 mark)"
          ],
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable explanations:\n\n1. **Broad leaf surface:** Provides a large surface area for maximum absorption of sunlight and carbon dioxide.\n2. **Network of veins:** Contains xylem (to transport water and minerals to the leaf cells) and phloem (to transport manufactured food away from the leaf), and provides structural support to keep the leaf flat.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for mentioning increased surface area for light/gas absorption, and 1 mark for mentioning transport of water/food or providing structural support."
        }
      ]
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "The following diagram shows a food web in an ecosystem.",
      "imagePath": "/assets/kjsea_science_2025_q36.png",
      "subQuestions": [
        {
          "id": "q36ai",
          "label": "a(i)",
          "questionText": "Use the food web to construct one food chain that ends with a tertiary consumer. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable food chains:\n\n1. **Plants → Rat → Snake → Hawk**\n2. **Plants → Gazelle → Snake → Hawk**",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for a complete, correct food chain starting with plants and ending with the hawk as a tertiary consumer. (Max 1 mark).\n* **Flexibility:** Arrows must point in the direction of energy flow (from prey to predator)."
        },
        {
          "id": "q36aii",
          "label": "a(ii)",
          "questionText": "Identify the producer in the food web. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable producers:\n\n1. **Plants:** They produce their own food through photosynthesis and form the base of the food web.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'Plants' (Max 1 mark)."
        },
        {
          "id": "q36b",
          "label": "b",
          "questionText": "Explain the effect of drought on the ecosystem. (2 marks)",
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable effects:\n\n1. **Death of Producers:** Plants will dry up and die due to lack of water, reducing the food supply at the base of the web.\n2. **Starvation of Consumers:** Primary consumers (gazelle, rat) will starve and die/migrate, which will in turn cause secondary and tertiary consumers (snake, hawk) to also starve or migrate.\n3. **Population Decline:** Overall decrease in the population of all organisms in the ecosystem, leading to possible collapse of the food web.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for mentioning the effect on plants (producers) and 1 mark for mentioning the cascading effect on consumers."
        }
      ]
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "Kidneys are parts of the urinary system that prevent accumulation of waste in the body to dangerous levels.",
      "subQuestions": [
        {
          "id": "q37a",
          "label": "a",
          "questionText": "Name two other parts of the human urinary system. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable parts:\n\n1. **Ureters:** Tubes that carry urine from the kidneys to the bladder.\n2. **Urinary Bladder:** A sac that stores urine temporarily.\n3. **Urethra:** The tube that carries urine from the bladder to the outside of the body.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid part identified (Max 2 marks)."
        },
        {
          "id": "q37b",
          "label": "b",
          "questionText": "State the function of the parts named in (a). (2 marks)",
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable functions:\n\n1. **Ureter:** Transports urine from the kidney to the bladder.\n2. **Urinary Bladder:** Temporarily stores urine until it is expelled.\n3. **Urethra:** Conducts urine out of the body.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct function matching the parts named in (a) (Max 2 marks)."
        },
        {
          "id": "q37c",
          "label": "c",
          "questionText": "Name two waste products excreted through the kidney. (2 marks)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable waste products:\n\n1. **Urea:** A nitrogenous waste product from the breakdown of proteins.\n2. **Excess water:** Regulated to maintain osmotic balance.\n3. **Excess mineral salts:** Such as sodium, potassium, and chloride ions.\n4. **Uric acid / Toxins:** Other metabolic wastes filtered from the blood.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct waste product named (Max 2 marks)."
        }
      ]
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "The following set-up represents a simple electric circuit.",
      "imagePath": "/assets/kjsea_science_2025_q38.png",
      "subQuestions": [
        {
          "id": "q38a",
          "label": "a",
          "questionText": "Identify the source of electricity in the set-up. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable sources:\n\n1. **The Cell (or Dry cell / Battery):** Provides the electromotive force to push electrons around the circuit.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'Cell', 'Dry cell', or 'Battery' (Max 1 mark)."
        },
        {
          "id": "q38b",
          "label": "b",
          "questionText": "State the observation made when the switch is on. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable observations:\n\n1. **Bulb lights up:** The circuit is complete, allowing electric current to flow through the bulb's filament, causing it to emit light and heat.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating that the bulb lights up or glows (Max 1 mark)."
        }
      ]
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "The following picture shows a rope fixed on the wall and held on one side.",
      "imagePath": "/assets/kjsea_science_2025_q39.png",
      "subQuestions": [
        {
          "id": "q39a",
          "label": "a",
          "questionText": "Describe how a wave can be generated in the rope. (2 marks)",
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable descriptions:\n\n1. **Oscillation/Vibration:** By moving the free end of the rope rapidly up and down (or side to side) in a continuous rhythmic motion. This disturbance transfers energy along the rope forming a wave.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for mentioning moving the hand up and down, and 1 mark for mentioning doing it continuously/rhythmically to create a disturbance (Max 2 marks)."
        },
        {
          "id": "q39b",
          "label": "b",
          "questionText": "Name the type of wave generated in (a). (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable wave types:\n\n1. **Transverse wave:** Because the particles of the rope vibrate perpendicularly to the direction of wave propagation.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'Transverse wave' (Max 1 mark)."
        },
        {
          "id": "q39c",
          "label": "c",
          "questionText": "Name one example of the type of the wave in (b). (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable examples:\n\n1. **Water waves:** Ripples on the surface of water.\n2. **Electromagnetic waves:** Light, radio waves, X-rays, microwaves.\n3. **Waves on a string/guitar string.**",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for any valid example of a transverse wave (Max 1 mark)."
        }
      ]
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "The following diagram represents a set-up used to demonstrate a certain factor affecting pressure in liquids.",
      "imagePath": "/assets/kjsea_science_2025_q40.png",
      "subQuestions": [
        {
          "id": "q40a",
          "label": "a",
          "questionText": "State the factor that was being demonstrated. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable factors:\n\n1. **Depth:** Pressure in liquids increases with depth.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'Depth' or 'Height of the liquid column' (Max 1 mark)."
        },
        {
          "id": "q40b",
          "label": "b",
          "questionText": "Indicate on the diagram how water will jet out if another hole is made at point R. (1 mark)",
          "questionType": "long-answer",
          "modelAnswer": "Here is a list of acceptable indications:\n\n1. **Matching curve:** The water jet from the new hole at point R (which is at the same horizontal level as the existing middle hole) would travel the exact same horizontal distance as the jet from the existing middle hole, showing that pressure is equal at the same depth.\n\n*(Note: As this is an interactive app, students would draw a curve matching the middle one).* ",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for a drawn curve that lands at the exact same distance as the existing middle jet (Max 1 mark)."
        },
        {
          "id": "q40c",
          "label": "c",
          "questionText": "Apart from the factor stated in (a) name one other factor that affects pressure in liquids. (1 mark)",
          "questionType": "short-answer",
          "modelAnswer": "Here is a list of acceptable factors:\n\n1. **Density of the liquid:** Denser liquids exert more pressure at the same depth compared to less dense liquids.\n2. **Gravity (Acceleration due to gravity):** Variations in gravitational pull affect liquid pressure.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for 'Density of the liquid' or 'Gravity' (Max 1 mark)."
        }
      ]
    }
]

section_b['sectionB'].extend(new_section_b_qs)
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(section_b, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-science-sectionb-2025.json')
print('Successfully generated Science Batch 3 JSON files.')
