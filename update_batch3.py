import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

# Update data
for q in d['sectionB']:
    qn = str(q.get('questionNumber'))
    
    if qn == '45':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable answers:\n\n1. **Upcycling / Creative Reusing:** Converting electronic waste materials into a new useful product or decorative artefact of higher value.\n2. **Reusing (Reuse):** Using discarded parts/materials again for a different creative purpose.\n3. **Recycling (Material Recycling):** Repurposing waste materials into new items instead of throwing them away.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating **Upcycling**, **Reusing**, or **Recycling** (Max 1 mark).\n* **Flexibility:** Accept "Upcycling", "Reuse", "Creative repurposing", or "Recycling".'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '46':
        sqa = q['subQuestions'][0]
        sqb = q['subQuestions'][1]
        
        sqa['modelAnswer'] = 'Here is an exhaustive list of acceptable safety precautions when setting up computers:\n\n1. **Ensuring Power is Disconnected Before Setup:** Unplug power cords and switch off mains before connecting internal or external computer cables.\n2. **Handling Components with Dry Clean Hands:** Keeping hands completely dry and clean to prevent electric shock and short circuits.\n3. **Proper Cable Management:** Routing power and data cables neatly through cable trays or against walls to prevent tripping hazards.\n4. **Using Surge Protectors and UPS:** Connecting computers to uninterruptible power supplies (UPS) or surge protectors to guard against power surges.\n5. **Avoiding Overloading Wall Sockets:** Ensuring not too many heavy power appliances share a single wall extension.\n6. **Ensuring Proper Ventilation and Clearance:** Placing system units and monitors in open spaces away from walls to allow cooling airflow and prevent overheating.\n7. **Safe Lifting and Posture (Ergonomics):** Using proper bending/lifting techniques when carrying heavy desktop computers and setting monitors at eye level.\n8. **Avoiding Liquids and Food Near Equipment:** Keeping beverages and snacks away from the computer setup area to prevent spill damage.\n9. **Electrostatic Discharge (ESD) Protection:** Discharging static electricity by touching a grounded metal object before touching sensitive internal computer parts.'
        sqa['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid computer setup safety precaution named (Max 2 marks).\n* **Flexibility:** Accept both electrical safety rules (dry hands, disconnecting power) and physical setup safety rules (cable routing, ventilation, ergonomics).'
        if 'gradingRubric' in sqa: del sqa['gradingRubric']

        sqb['modelAnswer'] = 'Here is the exact accepted characteristic:\n\n1. **Versatility (Versatile):** The ability of a computer to perform completely different types of tasks (such as typing documents, playing music, calculating numbers, editing videos, and scientific simulations) using different software applications.'
        sqb['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating **Versatility** or **Versatile** (Max 1 mark).\n* **Flexibility:** Accept "Multitasking" / "Multi-purpose capability" if adequately explained, but "Versatility" is the primary standard curriculum term.'
        if 'gradingRubric' in sqb: del sqb['gradingRubric']

    elif qn == '47':
        sqa = q['subQuestions'][0]
        sqb = q['subQuestions'][1]
        
        sqa['modelAnswer'] = 'Here is the detailed function of the keys:\n\n* **Key P (Enter / Return Key):**\n  1. Executing a command or confirming an input/selection.\n  2. Moving the cursor to the beginning of a new line or starting a new paragraph in word processing.\n  3. Submitting online forms or accepting dialog box prompts.\n\n* **Key Q (Backspace Key / Spacebar):**\n  1. **Backspace:** Deleting the character immediately to the left of the insertion point/cursor.\n  2. **Spacebar:** Inserting a horizontal blank space between words, letters, or characters.'
        sqa['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating the correct function of Key P, and 1 mark for Key Q (Max 2 marks).\n* **Flexibility:** Accept any accurate description of Enter (executing commands / new line) and Backspace (erasing character to the left) or Spacebar (creating spaces).'
        if 'gradingRubric' in sqa: del sqa['gradingRubric']

        sqb['modelAnswer'] = 'Here is an exhaustive list of acceptable sound output devices:\n\n1. **Speakers (Computer Speakers / Multimedia Speakers):** External or built-in audio output devices that convert electronic signals into audible sound waves for multiple listeners.\n2. **Headphones / Headsets:** Audio output devices worn over or on the ears for personal listening.\n3. **Earphones / Earbuds:** Compact in-ear audio output devices.\n4. **Soundbar:** Compact multi-speaker unit placed near the monitor.'
        sqb['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for naming any valid sound output device (Max 1 mark).\n* **Flexibility:** Accept Speakers, Headphones, Headsets, Earphones, or Earbuds.'
        if 'gradingRubric' in sqb: del sqb['gradingRubric']

    elif qn == '48':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable personal protective equipment (PPE) for handling corrosive substances:\n\n1. **Chemical-Resistant Gloves (Rubber / Nitrile / Neoprene / PVC Gloves):** Protects hands and forearms against chemical burns, acid spills, and caustic reactions.\n2. **Safety Goggles / Chemical Splash Goggles:** Enclosed eye protection preventing dangerous corrosive liquids from splashing into the eyes.\n3. **Full Face Shield:** Provides comprehensive facial and eye protection against intense chemical splashes.\n4. **Laboratory Coat / Chemical Resistant Apron (PVC or Rubber Apron):** Protects the torso, skin, and clothing from corrosive spills and splashes.\n5. **Closed-Toe Chemical Resistant Boots / Safety Shoes (Rubber Gumboots):** Protects feet from spills and dripping caustic liquids.\n6. **Respirator / Chemical Vapor Mask:** Protects the respiratory tract from inhaling corrosive acid fumes or vapors.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid personal protective equipment named (Max 2 marks).\n* **Flexibility:** Accept specific types (e.g., rubber gloves, safety goggles, lab coat, face shield, rubber apron, gumboots, respirator mask).'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '49':
        q['modelAnswer'] = 'Here is an exhaustive list of formatting features applied to the given paragraph:\n\n1. **Italics / Italicizing (*Italic font*):** Applied to the bulleted list items (*being bullied or abused*, *discrimination*, *worries about appearance and body image*).\n2. **Underline (<u>Underlining</u>):** Applied to the sentence "<u>feel positive about themselves and about life.</u>".\n3. **Bullet Points (Bulleted List / Bullets):** Used to list the bulleted points under "For example:".\n4. **Font Styling / Regular Font:** Default regular text style for the introductory body paragraphs.\n5. **Line Spacing / Paragraph Spacing:** Separation between paragraphs and list items.\n6. **Left Alignment (or Justification):** Paragraph text aligned to the left margin.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid formatting feature identified (Max 3 marks).\n* **Flexibility:** Primary expected features are **Italics**, **Underline**, and **Bullets / Bulleted list**. Accept Left alignment, Font style, or Paragraph spacing if clearly described.'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '50':
        sqa = q['subQuestions'][0]
        sqb = q['subQuestions'][1]
        
        sqa['modelAnswer'] = 'Here are the acceptable variables used in the visual programming instructions:\n\n1. **Buying price (or Buying_Price):** Variable holding the cost/purchase price.\n2. **Selling price (or Selling_Price):** Variable holding the sale price.\n3. **Profit / Loss:** Computed outcome variable based on the comparison.'
        sqa['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for identifying either **Buying price** or **Selling price** (Max 1 mark).\n* **Flexibility:** Accept exact variable names as written in the visual blocks (e.g., Buying price, Selling price).'
        if 'gradingRubric' in sqa: del sqa['gradingRubric']

        sqb['modelAnswer'] = 'Here is the accepted selection statement:\n\n1. **IF ... THEN ... ELSE statement (or IF ... THEN statement / Selection / Conditional statement):** A control structure that evaluates a condition (e.g. Selling price > Buying price) and executes specific blocks of code depending on whether the condition is true or false.'
        sqb['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for stating **IF ... THEN ... ELSE statement** (or **IF ... THEN statement**) (Max 1 mark).\n* **Flexibility:** Accept "IF statement", "IF...THEN", "IF...THEN...ELSE", or "Conditional / Decision statement".'
        if 'gradingRubric' in sqb: del sqb['gradingRubric']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Batch 3 (Q45-Q50) complete')
