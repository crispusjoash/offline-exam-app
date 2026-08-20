import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

exp_updates = {
    '11': '''The correct answer is **Using unstable platform.**

**Analysis of the Correct Answer:**
Working at heights poses severe safety risks. Using an unstable, wobbly, or improperly secured raised platform (like a faulty scaffold or rickety ladder) is a direct hazard that can lead to falls, which are a leading cause of severe workplace injuries.

**Why Other Options Are Incorrect:**
* **Leaving the platform unattended:** While perhaps not best practice, simply leaving a platform unattended does not inherently cause a physical injury risk like an unstable one does.
* **Using a new platform:** A new platform is usually structurally sound and inherently *safer*, not a source of risk.
* **Taking long to complete tasks:** Taking a long time is an issue of efficiency, not a direct safety hazard.''',

    '12': '''The correct answer is **Lines on the front face lie on the horizontal axis and rest at 45° angle.**

**Analysis of the Correct Answer:**
In an oblique projection, the front face of the object is drawn true to its actual shape and size (parallel to the projection plane). The depth (receding lines) is typically drawn at an angle of 45° to the horizontal to provide a three-dimensional effect.

**Why Other Options Are Incorrect:**
* *(Assuming other options mention 30° angles or all axes being angled)*: Isometric drawings have receding lines at 30° to the horizontal on both sides. Orthographic drawings are flat 2D views without angled depth lines. Only oblique drawing combines a true-shape front face with 45° receding depth lines.''',

    '13': '''The correct answer is **ensure the work-piece is held firmly.**

**Analysis of the Correct Answer:**
A vice is a heavy-duty mechanical clamping apparatus attached to a workbench. Its primary function is to securely grip and hold a workpiece firmly in place, allowing the user to safely perform operations like sawing, filing, drilling, or planing without the material moving.

**Why Other Options Are Incorrect:**
* **stop the work-piece from cracking / prevent the work-piece from splitting:** While a vice holds the piece securely, applying too much pressure with the jaws can actually *cause* delicate workpieces to crack or split if not careful.
* **hold the work-piece after working on it:** A vice is used *during* the work process, not merely as a storage stand after the work is done.''',

    '14': '''The correct answer is **Spanner**.

**Analysis of the Correct Answer:**
A spanner (also known as a wrench) is a hand tool specifically designed to provide mechanical advantage and grip in applying torque to turn rotary fasteners, such as nuts and bolts.

**Why Other Options Are Incorrect:**
* **Pliers:** Pliers are meant for gripping small objects, pulling, or cutting wire. They can strip the hexagonal edges of a nut if used for tightening.
* **Pincers:** Pincers are used for gripping, pulling out nails, or cutting wire, not for turning nuts.
* **Screw driver:** A screwdriver is designed to fit into the slotted head of a screw to turn it, and cannot be used on the hexagonal outside of a nut.''',

    '15': '''The correct answer is **Weather and climate.**

**Analysis of the Correct Answer:**
When choosing a strategic location for a mobile phone retail shop, an entrepreneur evaluates factors directly affecting business viability. Weather and climate have the *least* direct influence on where a mobile electronics shop is situated inside a town compared to economic factors.

**Why Other Options Are Incorrect:**
* **Competition in town:** Directly impacts potential market share and pricing.
* **Income among the population:** Directly determines the purchasing power and whether customers can afford smartphones.
* **Transportation system:** Determines foot traffic and accessibility for both customers and stock deliveries.''',

    '16': '''The correct answer is **Hobbies and personal interest.**

**Analysis of the Correct Answer:**
Jackie's completion of a hairdressing course reflects her personal interest, skill, and passion for beauty. Turning a hobby or personal interest into a business is one of the most reliable sources of business ideas because the entrepreneur already possesses the necessary passion and foundational skills.

**Why Other Options Are Incorrect:**
* **Real estate magazines:** These focus on property and housing markets, irrelevant to starting a hair salon.
* **Agricultural magazines:** These focus on farming, livestock, and crop yields, which have no connection to a beauty salon.
* **Population census report:** While it provides demographic numbers, it is a statistical document and not a primary source of a creative *idea* for a specific service like a salon.''',

    '17': '''The correct answer is **Ensure the budget deficits are missed out.**

**Analysis of the Correct Answer:**
A budget is a formal financial plan. A headteacher must ensure that the budget is transparent, realistic, and accounts for all financial realities. Deliberately omitting or "missing out" budget deficits (where expected expenses exceed income) leads to a false financial picture and severe cash-flow crises later on.

**Why Other Options Are Incorrect:**
* **Involve stakeholders:** This is a best practice that ensures transparency, ownership, and varied input.
* **Monitor the budget preparation process:** Essential for ensuring accuracy and adherence to financial guidelines.
* **Consider past expenditure items:** Crucial for estimating future costs realistically based on historical data.''',

    '18': '''The correct answer is **Market size, competition and customer preference.**

**Analysis of the Correct Answer:**
When finding a market for agricultural produce like maize, an entrepreneur must consider direct economic forces: the **market size** (demand / number of buyers), the level of **competition** (other maize sellers), and **customer preference** (e.g., preference for dry maize vs. green maize).

**Why Other Options Are Incorrect:**
* **Hobbies and Interests (in Options B and D):** Fatuma's or the customers' personal hobbies have no influence on the mass market for a staple food crop like maize.
* **Political stability:** While important for macroeconomics, it is a broader environmental factor and less of a direct, immediate differentiator when choosing between local markets than demand, competition, and preference.''',

    '19': '''The correct answer is **Producer**.

**Analysis of the Correct Answer:**
In the chain of distribution, the **producer** is the originator, manufacturer, or farmer who creates the goods. They are at the very beginning of the supply chain. Intermediaries are the "middlemen" who operate *between* the producer and the final consumer.

**Why Other Options Are Incorrect:**
* **Wholesaler:** An intermediary who buys in bulk from the producer and sells in smaller quantities to retailers.
* **Broker:** An intermediary who brings buyers and sellers together for a commission without taking ownership of the goods.
* **Agent:** An intermediary authorized to act on behalf of the producer to facilitate sales.''',

    '20': '''The correct answer is **assigning a coach to train Paul**.

**Analysis of the Correct Answer:**
Nurturing a specific, specialized talent like singing requires direct mentorship, vocal practice, and professional guidance. Assigning a vocal coach or music teacher will help Paul refine his pitch, breath control, and stage presence, thereby directly developing his core talent.

**Why Other Options Are Incorrect:**
* **emphasizing on good grades:** While academics are important, focusing *only* on academic grades does not nurture his singing ability.
* **encouraging Paul to vie for a leadership position:** Leadership skills are valuable but unrelated to improving vocal talent.
* **involving Paul in academic contests:** This promotes intellectual skills (like debate or math), not musical or artistic talent.'''
}

for q in d['sectionA']:
    qn = str(q.get('questionNumber'))
    if qn in exp_updates:
        q['explanation'] = exp_updates[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Batch 2 (Q11-Q20) explanations updated successfully.')
