import re

new_explanations = {
    "kpsea-science-2022-q21": """The correct answer is **To prevent spoilage.**

**Analysis of the Correct Answer:**
When harvesting large cucurbits like pumpkins, squashes, and watermelons, farmers are advised to leave a small piece of the stalk (the pedicel, labelled G) attached to the fruit. Cutting too close or removing the stalk completely creates an open wound on the fruit's surface, which allows bacteria and rotting fungi to enter easily, leading to rapid spoilage during storage.

**Why Other Options Are Incorrect:**
* **For hanging during storage.:** Large heavy fruits like pumpkins and watermelons are stored on the floor, shelves, or in crates; hanging them by their weak stalks would cause them to break and fall.
* **For holding during slicing.:** When slicing these large fruits, people hold the firm body of the fruit, not the small stalk.
* **To hold when carrying.:** Carrying heavy fruits by their stalk is risky because the stalk can easily detach, causing the fruit to drop and burst.

📌 **Key Learning Note:**
Always harvest fruits with a short piece of their **stalk** attached to prevent entry of rotting organisms and increase their shelf life.""",
    
    "kpsea-science-2022-q22": """The correct answer is **sunken bed**.

**Analysis of the Correct Answer:**
The picture illustrates crops planted in a depression or trench that is dug lower than the surrounding ground level. This agricultural structure is known as a **sunken bed**. It is specifically designed to trap and conserve water, making it ideal for farming in dry or semi-arid areas.

**Why Other Options Are Incorrect:**
* **container:** Container farming involves growing plants in movable pots, sacks, or buckets above ground, not in a depression dug into the earth.
* **shallow pit:** While it is a pit, in agricultural terms, a wide cultivated depression used for planting multiple crops to conserve water is technically termed a sunken bed.
* **moisture bed.:** Though it conserves moisture, the correct standard agricultural terminology for this specific physical structure is a sunken bed.

📌 **Key Learning Note:**
- **Sunken Bed:** Dug below ground level to collect and conserve water (used in dry areas).
- **Raised Bed:** Built above ground level to improve drainage (used in wet/swampy areas).""",
    
    "kpsea-science-2022-q23": """The correct answer is **Collects surface run-off.**

**Analysis of the Correct Answer:**
Sunken beds are designed as depressions in the soil. Because they are lower than the surrounding land, they act as basins that **trap and collect surface water run-off** during rains. This collected water seeps directly into the root zone of the crops, ensuring they have adequate moisture even in dry conditions.

**Why Other Options Are Incorrect:**
* **Reduces evaporation.:** While the sunken nature might offer slight wind protection, evaporation is primarily reduced by applying **mulch**, not just by the structure of the bed itself.
* **Prevents effects of strong wind.:** Strong winds are prevented by planting **windbreaks** (tall trees/hedges) around the farm, not by digging sunken beds.
* **Protects soil from strong sun.:** Protecting soil from direct strong sun is the function of **mulching** or constructing a **shade**, not digging a sunken bed.

📌 **Key Learning Note:**
The main advantage of a **sunken bed** is its ability to harvest and collect **surface water run-off**, making it excellent for crop survival in arid regions.""",
    
    "kpsea-science-2022-q24": """The correct answer is **to level the nursery bed.**

**Analysis of the Correct Answer:**
The garden tool shown in the diagram is a **rake**. In the preparation of a nursery bed (or any seedbed), after digging and breaking large soil clods with a *jembe* or fork, a rake is used to gather stones/trash and to **level the surface of the soil** to create a fine, smooth tilth suitable for planting tiny seeds.

**Why Other Options Are Incorrect:**
* **to lift seedlings from the nursery bed:** Lifting delicate seedlings without damaging their roots requires a **garden trowel**, not a rake.
* **for weeding the nursery bed:** Removing small weeds from a nursery bed is usually done by hand-pulling or using a small pointed stick, as a large rake would uproot the crop seedlings.
* **to measure the spacing for the crop:** Measuring spacing between crop rows or planting holes is done using a **measuring string/tape** and a tape measure, not a rake.

📌 **Key Learning Note:**
A **rake** is used for gathering trash/stones and **leveling the soil surface** during seedbed preparation.""",
    
    "kpsea-science-2022-q25": """The correct answer is **Cleaning.**

**Analysis of the Correct Answer:**
After using any garden tool (like a *jembe*, fork, or rake) in the farm, the most immediate and basic care practice is **cleaning** it. This involves washing or scraping off wet mud, soil, and plant sap. If dirt is left on metallic tools, it retains moisture which leads to rusting and degradation of the tool.

**Why Other Options Are Incorrect:**
* **Oiling.:** Oiling is an important maintenance practice to prevent rust, but it must be done *after* the tool has been thoroughly cleaned and dried.
* **Painting.:** Painting handles or metal parts prevents rotting and rusting, but it is an occasional long-term maintenance practice, not an immediate post-use step.
* **Sharpening.:** Cutting tools (like *pangas* and axes) require sharpening when blunt, but tools like rakes do not need sharpening; however, all tools need cleaning.

📌 **Key Learning Note:**
The first step in maintaining farm tools after use is always **cleaning** them to remove dirt and moisture, which prevents rusting.""",
    
    "kpsea-science-2022-q26": """The correct answer is **prevent her shoes from losing shape.**

**Analysis of the Correct Answer:**
Leather is a pliable material that can easily crease, fold, or collapse when empty, especially when stored for long periods (like during school holidays). Stuffing leather shoes tightly with old newspapers or shoe trees provides internal structural support, helping the leather maintain its original molded form and **preventing the shoes from losing their shape**.

**Why Other Options Are Incorrect:**
* **prevent her shoes from becoming small:** Leather can shrink if dried improperly (e.g. by a hot fire), but newspapers alone do not physically stretch or stop natural shrinkage if conditions are bad.
* **prevent her shoes from getting dirty:** Newspapers are stuffed *inside* the shoe; they do nothing to protect the outside leather surface from dust or dirt in the storage box.
* **make her shoes dry completely:** While dry newspapers can absorb some interior dampness (like sweat), their primary mechanical function when packed tightly is maintaining the shoe's shape.

📌 **Key Learning Note:**
To properly store leather shoes, stuff them with **newspapers** to help them retain their structural **shape** and prevent permanent creases.""",
    
    "kpsea-science-2022-q27": """The correct answer is **Malaria.**

**Analysis of the Correct Answer:**
**Malaria** is a disease caused by Plasmodium parasites transmitted through the bite of an infected female Anopheles mosquito. The classic, defining symptoms of malaria include high and alternating **fever, severe headaches, joint pains (body aches), shivering/chills, and vomiting**.

**Why Other Options Are Incorrect:**
* **Cough.:** A common cough or flu is primarily characterized by a runny nose, sore throat, and coughing, not typically severe joint pains or shivering fever.
* **Measles.:** Measles is a viral disease characterized by a high fever, runny nose, red eyes, and a distinct red skin rash that spreads over the body.
* **Chicken pox.:** Chickenpox is identified by an itchy skin rash that forms fluid-filled blisters (vesicles) all over the body, along with a mild fever.

📌 **Key Learning Note:**
- **Malaria Symptoms:** High fever, severe headache, joint pains, and vomiting.
- **Measles Symptoms:** Red skin rash, fever, runny nose, and red eyes.""",
    
    "kpsea-science-2022-q28": """The correct answer is **make good use of money**.

**Analysis of the Correct Answer:**
A **family budget** is a written financial plan that outlines the expected family income and how it will be spent on various needs (food, rent, school fees) and savings over a specific period. By prioritizing essential needs over wants, a budget ensures that the family lives within its means, thereby helping them to **make good use of their money** and avoid unnecessary debts.

**Why Other Options Are Incorrect:**
* **make their family happy:** While financial stability brings peace of mind, buying things outside the budget just to make people happy leads to financial ruin.
* **buy expensive items:** A budget often restricts buying expensive luxury items unless money has been specifically saved for them over time.
* **buy all the items in fashion.:** Fashionable items are "wants," not basic "needs." A good budget prioritizes basic needs first.

📌 **Key Learning Note:**
The primary purpose of budgeting is to allocate limited income effectively to satisfy basic needs and **make good use of money** without overspending.""",
    
    "kpsea-science-2022-q29": """The correct answer is **Poster 2**.

**Analysis of the Correct Answer:**
Foods that provide the body with energy are classified as **Carbohydrates**. Poster 2 lists **Cassava, Rice, Bread, and Ugali**, all of which are classic examples of carbohydrate-rich, energy-giving foods.

**Why Other Options Are Incorrect:**
* **Poster 1:** This poster lists Beans, Meat, Eggs, and Fish. These are all **Proteins** (body-building foods) used for growth and repair of tissues, not primarily for energy.
* **Poster 3:** This poster lists Oranges, Spinach, Pineapples, and Cabbages. These are fruits and vegetables rich in **Vitamins and Minerals** (protective foods) which boost immunity.
* **Posters 1 and 3.:** Neither of these posters contains energy-giving foods.

📌 **Key Learning Note:**
- **Energy-giving foods (Carbohydrates/Fats):** Ugali, Rice, Bread, Cassava, Potatoes.
- **Body-building foods (Proteins):** Meat, Beans, Eggs, Milk.
- **Protective foods (Vitamins/Minerals):** Fruits and Vegetables.""",
    
    "kpsea-science-2022-q30": """The correct answer is **Dry completely, pack in airtight bags, store in a dry place.**

**Analysis of the Correct Answer:**
Proper preservation of harvested cereals (like maize or beans) requires a complete sequence of steps to prevent rotting and pest attacks. First, they must be **dried completely** in the hot sun to remove moisture. Second, they must be **packed in airtight bags** (like hermetic bags) to suffocate any weevils or insects. Finally, they must be **stored in a dry, well-ventilated place** (like a granary) elevated off the ground to prevent dampness.

**Why Other Options Are Incorrect:**
* **Wash, dry completely and put in the sun.:** Cereals are never washed with water before storage, as adding moisture encourages rapid fungal/mold growth and rotting.
* **Dry completely, pack in airtight bags:** This sequence is incomplete because it ignores the final critical step of placing the bags in a suitable dry storage area (granary).
* **Dry completely, pack in bags and store.:** Packing in regular porous bags (instead of airtight bags) allows oxygen and pests (weevils) to easily enter and destroy the stored grain.

📌 **Key Learning Note:**
To store grains safely: **Dry completely** (removes moisture) ➔ **Pack in airtight bags** (kills pests) ➔ **Store in a dry place** (prevents rotting)."""
}

with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

for q_id, new_exp in new_explanations.items():
    pattern = r'("id": "' + q_id + r'".*?"explanation": )"(.*?)"'
    def repl(m):
        escaped_exp = new_exp.replace('\n', '\\n').replace('"', '\\"')
        return m.group(1) + '"' + escaped_exp + '"'
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 3 completed!")
