import json
import re

file_path = 'src/data/kpsea-science-2025.js'

explanations = {
    "q31": """The correct answer is **uprooting the weeds.**

**Analysis of the Correct Answer:**
A container garden is very small, consisting of plants grown in pots, buckets, or sacks. Because of the limited space, you cannot use large farming tools. The safest and most practical way to control weeds is by pulling them out by hand (uprooting).

**Why Other Options Are Incorrect:**
* **spraying with chemicals:** Unnecessary and potentially toxic for a small home container garden.
* **cultivating using a jembe:** A jembe (hoe) is too large and would damage the container and the crops.
* **mulching with dry grass:** Mulching suppresses weeds but does not remove existing ones.

📌 **Key Learning Note:**
Weed control methods depend on the scale of farming. In small, confined spaces like container or vertical gardens, manual uprooting is the most effective method.""",

    "q32": """The correct answer is **Vertical garden.**

**Analysis of the Correct Answer:**
A vertical garden is an innovative gardening method where plants are grown upwards rather than spreading horizontally across the ground. Using stacked tyres, sacks, or wall-mounted containers are common ways to create a vertical garden.

**Why Other Options Are Incorrect:**
* **Container garden:** While tyres are containers, stacking them specifically upwards creates a vertical structure.
* **Horizontal garden:** This would spread out flat on the ground.
* **Sunken bed:** This is dug downwards into the ground to conserve water.

📌 **Key Learning Note:**
Innovative gardens (like vertical, multi-storey, and hanging gardens) are designed to grow food efficiently in spaces where traditional farming isn't possible.""",

    "q33": """The correct answer is **utilize limited space**

**Analysis of the Correct Answer:**
The main advantage of innovative gardening methods (like vertical or multi-storey gardening) is that they allow people to grow a lot of food in very small areas, such as balconies, small urban backyards, or paved surfaces where traditional farming is impossible.

**Why Other Options Are Incorrect:**
* **prevent the spread of pests:** Pests can still attack plants in innovative gardens.
* **control crop diseases:** Diseases can still occur; space utilization is the primary goal.
* **prevent germination of weeds:** Weeds can still grow in the soil used in these gardens.

📌 **Key Learning Note:**
Innovative gardening is the solution for urban agriculture because it maximizes crop yield while minimizing the land area required.""",

    "q34": """The correct answer is **Early in the morning.**

**Analysis of the Correct Answer:**
Watering crops should ideally be done early in the morning or late in the evening. During these times, the sun is not hot, meaning less water will be lost to evaporation, allowing the water to soak deep into the roots.

**Why Other Options Are Incorrect:**
* **At midday / When the sun is too hot:** Watering when it's hot causes rapid evaporation, wasting water. Water droplets on leaves can also act like magnifying glasses and cause the leaves to burn.
* **When plants start to dry:** This is waiting too long. Watering should be regular to prevent the plants from drying and wilting.

📌 **Key Learning Note:**
To conserve water in agriculture, irrigation and watering should be scheduled during the coolest parts of the day.""",

    "q35": """The correct answer is **Rabbit.**

**Analysis of the Correct Answer:**
Rabbits are versatile domestic animals that can be reared for multiple purposes simultaneously: their meat is eaten, their fur/skins are used for clothing or crafts, and their droppings provide excellent manure for farming. 

**Why Other Options Are Incorrect:**
* **Cat:** Mainly kept as a pet or to scare away/catch rats.
* **Dog:** Mainly kept as a pet or for security (alerting on presence of strangers).
* **Chicken:** Kept for meat and eggs, but not typically for fur/skins.

📌 **Key Learning Note:**
Different livestock serve different agricultural purposes. Rabbits are highly productive small stock kept for meat, pelt (skin/fur), and manure.""",

    "q36": """The correct answer is **Seeds.**

**Analysis of the Correct Answer:**
Kales (commonly known as sukuma wiki) and cabbages are vegetables that are propagated using seeds. The seeds are first planted in a nursery bed. Once they grow into strong seedlings, they are transplanted into the main seedbed.

**Why Other Options Are Incorrect:**
* **Vines:** Used for crops like sweet potatoes.
* **Splits:** Used for crops like pyrethrum or napier grass.
* **Stem cuttings:** Used for crops like cassava or sugarcane.

📌 **Key Learning Note:**
Small, delicate seeds (like kale, cabbage, and tomato) require the special care of a nursery bed before transplanting.""",

    "q37": """The correct answer is **Pruning roots of seedlings.**

**Analysis of the Correct Answer:**
A panga is a versatile cutting tool. In a tree nursery, when seedlings have grown too large or their roots have grown into the ground beneath the nursery container, a sharp panga is used to carefully prune (cut) the roots before transplanting.

**Why Other Options Are Incorrect:**
* **Applying fertilizer:** This is done by hand or using small scopes.
* **Lifting seedlings:** A garden trowel or spade is used to lift seedlings.
* **Carrying manure:** A wheelbarrow or bucket is used for carrying.

📌 **Key Learning Note:**
Root pruning in a tree nursery encourages a compact root system, ensuring the seedling survives better when moved to the main field.""",

    "q38": """The correct answer is **sharpened**

**Analysis of the Correct Answer:**
A panga is a cutting tool. For any cutting tool (panga, slasher, axe, knife) to function well and make clean cuts without excessive effort, its cutting edge must be kept sharp using a file or sharpening stone.

**Why Other Options Are Incorrect:**
* **cleaned:** Cleaning prevents rust and hygiene issues, but sharpening directly dictates how well it cuts.
* **oiled:** Oiling prevents rust during storage, not its immediate cutting function.
* **painted:** Painting the handle preserves the wood, but doesn't help the tool cut.

📌 **Key Learning Note:**
Farm tool maintenance involves sharpening cutting edges, oiling metallic parts to prevent rust, and repairing broken handles for safety.""",

    "q39": """The correct answer is **Proteins.**

**Analysis of the Correct Answer:**
Proteins are known as body-building foods. They are essential for the growth, repair, and building of body tissues, particularly muscles. If Jay wants strong muscles for sports, he needs a diet rich in proteins (e.g., beans, meat, eggs, milk).

**Why Other Options Are Incorrect:**
* **Carbohydrates:** These are energy-giving foods. They provide the fuel for playing, but they don't build muscle tissue.
* **Vitamins:** These are protective foods that boost immunity and keep the body healthy.
* **Fats:** These provide stored energy and insulation.

📌 **Key Learning Note:**
Food groups are categorized by function: **Proteins** (Body-building), **Carbohydrates & Fats** (Energy-giving), and **Vitamins & Minerals** (Protective).""",

    "q40": """The correct answer is **Sufuria.**

**Analysis of the Correct Answer:**
When baking without a modern oven, a sufuria (a locally used metal cooking pot) can be used as an improvised baking tin. It is made of metal (usually aluminium), which is a good conductor of heat and can withstand the high temperatures required for baking.

**Why Other Options Are Incorrect:**
* **Melamine bowl:** Melamine is a type of hard plastic that will scorch, crack, or melt when exposed to baking heat.
* **Hot sand:** Sand is used *around* the tin to distribute heat in a charcoal oven, but it cannot be the tin itself.
* **Plastic bowl:** Plastic will quickly melt and catch fire under baking temperatures.

📌 **Key Learning Note:**
Improvising equipment in Home Science requires understanding material properties. Metals withstand heat well, while plastics and most ceramics do not.""",

    "q41": """The correct answer is **in water under low heat**

**Analysis of the Correct Answer:**
Stewing is a slow method of cooking. It involves cooking food in a small amount of liquid (usually water or broth) in a covered pan over low, simmering heat for an extended period. This method makes tough cuts of meat tender and creates a rich sauce.

**Why Other Options Are Incorrect:**
* **using steam:** This is called steaming.
* **using dry heat:** This describes baking or roasting.
* **in water under high heat:** Cooking rapidly in plenty of boiling water is called boiling.

📌 **Key Learning Note:**
**Stewing** is cooking slowly in a little liquid on low heat. **Boiling** is cooking rapidly in lots of liquid on high heat.""",

    "q42": """The correct answer is **(iii), (ii), (i), (iv)**

**Analysis of the Correct Answer:**
To shallow fry an egg correctly, a logical sequence must be followed:
1. **(iii) beat the egg in a bowl** (Preparation)
2. **(ii) heat a little oil in a frying pan** (Pre-heating the cooking medium)
3. **(i) pour the beaten egg into the pan** (Starting the cooking process)
4. **(iv) fry the egg and turn** (Finishing the cooking process)

**Why Other Options Are Incorrect:**
The other sequences are illogical. You cannot pour the egg into the pan before heating the oil, and you cannot beat the egg after pouring it.

📌 **Key Learning Note:**
Shallow frying involves cooking food in a small amount of hot oil. The oil must always be heated before adding the food to prevent the food from absorbing too much oil.""",

    "q43": """The correct answer is **Putting the egg into the hot pan.**

**Analysis of the Correct Answer:**
Putting the egg into the hot pan is simply a step in the cooking procedure, not a safety measure. Safety measures are specific actions taken to prevent injury or accidents.

**Why Other Options Are Incorrect:**
* **Do not splash water into the pan:** A safety measure. Water in hot oil causes violent splattering and severe burns.
* **Keep flammable materials away:** A safety measure. Prevents accidental kitchen fires.
* **Do not add oil to a wet pan:** A safety measure. Same reason as splashing water; it prevents dangerous oil splatters.

📌 **Key Learning Note:**
Kitchen safety revolves around preventing burns, cuts, and fires. Never mix hot oil and water.""",

    "q44": """The correct answer is **The suit should be well fitting.**

**Analysis of the Correct Answer:**
When purchasing clothing, the primary functional requirement is that it fits the wearer properly. A suit that is too large or too small will be uncomfortable and look improper, regardless of its colour or design.

**Why Other Options Are Incorrect:**
* **The colour should match his other suits:** While personal preference, it is not the main practical factor. People often want variety in their wardrobe.
* **The colour should match his friend's suit:** Katana is buying the suit for himself, so his friend's suit is irrelevant.
* **The suit should have bright colours:** Colour choice is subjective and depends on the occasion.

📌 **Key Learning Note:**
Important factors to consider when buying clothes include: **Fit/Size**, **Quality of fabric**, **Occasion**, and **Cost/Budget**.""",

    "q45": """The correct answer is **Bathing every day.**

**Analysis of the Correct Answer:**
Menstrual hygiene requires keeping the body exceptionally clean to prevent bad odours, discomfort, and infections. Bathing daily (and changing sanitary towels regularly) is the most direct and effective hygiene practice during menstruation.

**Why Other Options Are Incorrect:**
* **Eating a balanced diet:** Important for overall health and managing menstrual symptoms, but it is not a direct *hygiene* practice.
* **Applying body sprays:** Masks odours but does not promote actual cleanliness or hygiene.
* **Drinking plenty of water:** Good for health, but not a hygiene practice.

📌 **Key Learning Note:**
Menstrual hygiene management includes: bathing daily, changing sanitary towels every 4-6 hours, and disposing of used towels correctly.""",

    "q46": """The correct answer is **where all information is provided.**

**Analysis of the Correct Answer:**
A wise consumer makes informed decisions. Before buying a packaged household item, it is crucial to read all provided information, including the manufacturer's instructions, ingredients, expiry date, and safety warnings, to ensure the product is safe and suitable for use.

**Why Other Options Are Incorrect:**
* **with attractive advertisements:** Advertisements are designed to persuade, not necessarily to tell the objective truth.
* **that is rare and imported:** Being rare or imported does not guarantee quality or suitability.
* **advertised by popular people:** Celebrity endorsements do not guarantee the product is safe or effective for you.

📌 **Key Learning Note:**
Consumer education teaches us to read labels for **manufacturing dates, expiry dates, weight, and ingredients** before purchasing goods.""",

    "q47": """The correct answer is **Glass surface.**

**Analysis of the Correct Answer:**
The defining step in this procedure is **(v) shining the surface using an old newspaper.** Using crumpled newspaper is a traditional and highly effective method for polishing glass surfaces (like windows or mirrors) because it removes dirt without leaving lint or streaks behind.

**Why Other Options Are Incorrect:**
* **Wooden surface:** Wood is polished using wax or furniture polish, not water and newspaper.
* **Cemented surface:** Cement is scrubbed with hard brushes and water, not shined with newspaper.
* **Earthen surface:** Earthen floors are swept and smeared with mud/cow dung, not washed with soapy water and shined.

📌 **Key Learning Note:**
Different surfaces require different cleaning materials. Glass is shined with newspaper, wood is polished with wax, and tiles are mopped.""",

    "q48": """The correct answer is **Blood stain.**

**Analysis of the Correct Answer:**
Blood is an organic stain that contains proteins. If a protein stain is exposed to hot water, the heat will 'cook' or coagulate the protein, causing it to set permanently into the fabric fibers. Therefore, blood stains must always be soaked and washed in cold water first.

**Why Other Options Are Incorrect:**
* **Chewing gum stain:** Removed by freezing it with ice cubes and scraping it off.
* **Rust stain:** Removed using acidic agents like lemon juice and salt.
* **Grass stain:** Removed using warm soapy water or alcohol.

📌 **Key Learning Note:**
Protein-based stains (like blood, egg, and milk) must be washed in **cold water** to prevent them from setting into the fabric.""",

    "q49": """The correct answer is **Loop stitch.**

**Analysis of the Correct Answer:**
The loop stitch (often called a blanket stitch) is made by passing the thread over the edge of the fabric and catching it in a loop with the needle. It is used to neaten raw edges, prevent fraying, or as a decorative edge finish.

**Why Other Options Are Incorrect:**
* **Back stitch:** Used for strong, permanent seams. It looks like a continuous line of stitches.
* **Hemming stitch:** Used to hold down a folded hem invisibly on the right side.
* **Chain stitch:** A decorative stitch that looks like a series of linked chains on the surface of the fabric.

📌 **Key Learning Note:**
Edge-neatening stitches include the **loop stitch** and **overcasting stitch**. They bind the raw edges of the fabric to stop threads from pulling out.""",

    "q50": """The correct answer is **colour of the thread.**

**Analysis of the Correct Answer:**
When repairing a torn garment or loose stitches, the goal is to make the repair as unnoticeable (neat) as possible. Therefore, the most critical factor to consider is choosing a thread colour that matches the original fabric perfectly.

**Why Other Options Are Incorrect:**
* **size of his shirt / size of the pocket:** These are fixed measurements of the garment and don't dictate how you perform the stitching repair.
* **type of the needle:** While you need an appropriate needle for the fabric thickness, the colour of the thread determines how neat and invisible the repair looks on the outside.

📌 **Key Learning Note:**
For neat garment repairs (like darning, patching, or re-stitching), always match the **colour, strength, and type** of the mending thread to the garment's fabric."""
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(export const kpseaScience2025 = )(\{.*\});?\s*$', content, re.DOTALL)
prefix = match.group(1)
data = json.loads(match.group(2))

section_key = "sectionA" if "sectionA" in data else "questions"
for q in data.get(section_key, []):
    q_id = q.get("id")
    if q_id in explanations:
        q["explanation"] = explanations[q_id]

new_content = prefix + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated 31-50")
