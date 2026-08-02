import json

filepath = 'src/data/kpsea-science-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaScience2023 = '
clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

remaining_explanations = {
    21: """The correct answer is **Gapping.**.

**Detailed Analysis of the Correct Answer:**
**Gapping** is the agricultural practice of planting new seeds or transplanting seedlings into gaps or spaces where seeds failed to germinate or seedlings died after planting. This ensures that the field maintains an optimal plant population and maximum crop yield per unit area.

**Why Other Options Are Incorrect:**
* **Pruning.:** Pruning involves cutting away unwanted, dead, or overgrown branches and leaves from trees and crops to promote healthy growth.
* **Thinning.:** Thinning is the opposite of gapping; it involves removing excess, weak, or overcrowded seedlings to reduce competition for nutrients, sunlight, and water.
* **Training.:** Training involves supporting or guiding the direction of growth of climbing crops (like passion fruit or tomatoes) using stakes or trellises.

📌 **Key Learning Note:**
- **Gapping:** Replacing un-germinated seeds or dead seedlings.
- **Thinning:** Removing excess seedlings to prevent overcrowding.""",

    22: """The correct answer is **Squirrel.**.

**Detailed Analysis of the Correct Answer:**
**Squirrels** are notorious field pests that interfere directly with seed germination. They dig up freshly planted seeds (such as maize, groundnuts, and beans) from the soil and eat them before or during the germination process, preventing crops from growing.

**Why Other Options Are Incorrect:**
* **Mole.:** Moles are underground burrowers that damage crop roots and tubers (like sweet potatoes), but they do not specifically target planted seeds in the topsoil.
* **Monkey.:** Monkeys attack and feed on mature crops, green maize cobs, or ripening fruits, rather than buried germinating seeds.
* **Weaver bird.:** Weaver birds are destructive pests of mature cereal grains (such as millet, sorghum, and rice heads) in the field, not buried germinating seeds.

📌 **Key Learning Note:**
- **Pre-emergence Pests (Target seeds/germination):** Squirrels, rodents, birds (like crows picking seeds).
- **Field/Crop Pests (Target mature plants/tubers):** Monkeys, moles, weaver birds.""",

    23: """The correct answer is **Weed control.**.

**Detailed Analysis of the Correct Answer:**
In the photograph, while the farmer is uprooting excess maize plants (thinning), they are simultaneously removing unwanted wild plants growing alongside the maize. This practice is **weed control** (weeding), which removes unwanted plants that compete with the main crop for water, soil nutrients, sunlight, and space.

**Why Other Options Are Incorrect:**
* **Harvesting.:** Harvesting involves gathering mature, ripe crops at the end of the growing season; young maize seedlings are far too young to harvest.
* **Pruning.:** Pruning is the removal of branches/leaves from trees and bushes, which is not practiced on cereal crops like maize.
* **Training.:** Training is providing structural support for climbing crops (e.g. passion fruit), which is not required for erect cereal crops like maize.

📌 **Key Learning Note:**
**Weed control** is essential early in crop growth to eliminate competition between weeds and young crop seedlings for nutrients, light, and water.""",

    24: """The correct answer is **Pigweed.**.

**Detailed Analysis of the Correct Answer:**
**Pigweed** (commonly known in Kenya as **Terere** or **Amaranthus**) is an **indigenous (traditional) African leafy vegetable**. It has been grown and consumed naturally in local communities for generations and is highly rich in iron, calcium, and vitamins.

**Why Other Options Are Incorrect:**
* **Cabbage.:** Cabbage is an exotic (exogenous) vegetable introduced to Africa from Europe.
* **Kales.:** Kales (commonly known as *Sukuma Wiki*) are exotic vegetables originating from Europe and the Mediterranean region.
* **Spinach.:** Spinach is an exotic leafy vegetable introduced from southwestern Asia.

📌 **Key Learning Note:**
- **Indigenous Vegetables (Local/Traditional):** Pigweed (*Terere*), Black nightshade (*Managu*), Spider plant (*Sagaa/Akaaka*), Amaranth, Slender leaf (*Mitoo*).
- **Exotic Vegetables (Introduced):** Cabbage, Kale (*Sukuma Wiki*), Spinach, Carrots, Lettuce.""",

    25: """The correct answer is **Cassava and arrowroots.**.

**Detailed Analysis of the Correct Answer:**
**Cassava** and **arrowroots** (*Nduma*) are both traditional **indigenous root/tuber crops** heavily cultivated in tropical Africa. They produce swollen underground roots or corms that store starch and serve as vital food security crops.

**Why Other Options Are Incorrect:**
* **Arrowroots and carrots.:** Arrowroots are indigenous, but carrots are exotic root crops introduced from temperate regions.
* **Beetroot and cassava.:** Cassava is indigenous, but beetroot is an exotic root crop.
* **Carrots and yams.:** Yams are indigenous, but carrots are exotic root crops.

📌 **Key Learning Note:**
- **Indigenous Root/Tuber Crops:** Cassava, Arrowroots (*Nduma*), Yams, Sweet potatoes.
- **Exotic Root Crops:** Carrots, Beetroots, Radishes, Turnips.""",

    26: """The correct answer is **They are diseases that are spread easily from one person to another.**.

**Detailed Analysis of the Correct Answer:**
**Communicable (infectious) diseases** are illnesses caused by microscopic pathogens (such as bacteria, viruses, fungi, or protozoa) that can be **transmitted or spread from an infected person, animal, or environment to a healthy person**. Examples include cholera, malaria, tuberculosis, COVID-19, and the common cold.

**Why Other Options Are Incorrect:**
* **They are diseases that cannot be spread from one person to another.:** Diseases that cannot be transmitted between individuals (e.g. diabetes, cancer, asthma, hypertension) are classified as **non-communicable diseases**.
* **They are diseases that are spread only by communicating to people.:** Communicable does not refer to verbal speech or communication; it refers to biological transmission of pathogens.
* **They are diseases that spread only when people move from one place to another.:** Transmission can easily occur within a static household, classroom, or localized environment without physical travel.

📌 **Key Learning Note:**
- **Communicable Diseases:** Can spread from person to person (e.g. Flu, Cholera, TB, Measles).
- **Non-Communicable Diseases:** Cannot spread from person to person (e.g. Cancer, Diabetes, Heart Disease).""",

    27: """The correct answer is **Fatma.**.

**Detailed Analysis of the Correct Answer:**
In Home Science and clothing design, **accessories** are supplementary items worn alongside garments to complete, complement, or enhance personal appearance. **Fatma** brought a **tie, socks, belt, and scarf**, all of which are classic examples of fashion accessories used to complement clothing and improve one's outfit.

**Why Other Options Are Incorrect:**
* **Auma.:** Body lotion, petroleum jelly, and skin care cream are **cosmetics and skin care products**, not clothing accessories.
* **Chris.:** Thread, thimble, pins, and needles are **sewing and mending equipment**, not clothing accessories.
* **Festus.:** Cup and spoon are **kitchen utensils**, which are completely unrelated to personal grooming or fashion accessories.

📌 **Key Learning Note:**
- **Accessories:** Ties, belts, scarves, socks, hats, bags, and jewelry worn to complement clothing.
- **Cosmetics:** Products applied to the body to clean or beautify skin and hair (e.g. lotions, creams).
- **Sewing Equipment:** Tools used for stitching clothes (e.g. thread, needles, thimbles, pins).""",

    28: """The correct answer is **Savings is the amount of money set aside for future use.**.

**Detailed Analysis of the Correct Answer:**
**Savings** is defined in financial planning as the portion of income or money that is deliberately **set aside today for future use or long-term goals** rather than spent immediately. Including savings in a family budget ensures financial security and helps achieve future objectives like education or buying assets.

**Why Other Options Are Incorrect:**
* **Savings is the amount of money you are left with after buying all items required.:** Unspent money remaining after purchases is simply leftover balance or surplus cash; true savings requires intentional planning.
* **Savings is the amount of money you are given back after paying for items.:** The money returned by a seller after paying with a larger denomination is called **change**.
* **Savings is the amount of money set aside for unexpected expenses.:** Money set aside specifically for sudden emergencies is known as an **emergency fund** (a specific sub-category of savings).

📌 **Key Learning Note:**
- **Savings:** Money intentionally set aside for **future use or goals**.
- **Change:** Money returned after paying for goods with excess cash.
- **Emergency Fund:** Money set aside specifically for unexpected events (like sickness or accidents).""",

    29: """The correct answer is **Expiry date on the package.**.

**Detailed Analysis of the Correct Answer:**
The **expiry date (or best before date)** is the most critical factor to check when purchasing processed food items like cooking fat. Consuming food products past their expiry date is hazardous to health because expired fats become rancid, lose nutritional value, and can cause severe **food poisoning** or stomach upset.

**Why Other Options Are Incorrect:**
* **Colour of the packaging.:** The color of the tub or wrapper is purely for brand marketing and does not affect the safety or quality of the food.
* **The type of packaging used.:** Whether packaged in plastic tubs, tins, or foil wrappers is secondary compared to ensuring the product is safe for consumption.
* **Weight of the packaging material.:** The tare weight of the plastic container itself is irrelevant to nutritional quality and food safety.

📌 **Key Learning Note:**
Always check the **expiry date**, **ingredient list**, and **seal integrity** when purchasing food items to safeguard your family's health.""",

    30: """The correct answer is **vitamins and minerals.**.

**Detailed Analysis of the Correct Answer:**
Nutrients are divided into two main categories based on the quantities required by the body:
1. **Micronutrients:** Essential nutrients required by the body in **small amounts** to protect against diseases and regulate body processes. **Vitamins and minerals** are the two classes of micronutrients.

**Why Other Options Are Incorrect:**
* **proteins and lipids:** Both proteins and lipids (fats) are **macronutrients** required by the body in large quantities for growth, repair, and energy.
* **carbohydrates and lipids:** Carbohydrates and lipids are both **macronutrients** that serve as the main energy sources for the body.
* **carbohydrates and proteins:** Both are **macronutrients** needed in daily bulk amounts.

📌 **Key Learning Note:**
- **Micronutrients (Needed in small amounts):** Vitamins and Minerals (e.g. Vitamin A, C, Calcium, Iron).
- **Macronutrients (Needed in large amounts):** Carbohydrates, Proteins, and Fats/Lipids.""",

    31: """The correct answer is **Salt increases risk of hypertension.**.

**Detailed Analysis of the Correct Answer:**
Preserving meat using excessive salt (salting/curing) increases the sodium content of the meat dramatically. High dietary intake of sodium causes the body to retain excess water, increasing blood volume and placing extra strain on blood vessels. This significantly increases the risk of developing **hypertension (high blood pressure)** and cardiovascular diseases.

**Why Other Options Are Incorrect:**
* **Salt increases risk of constipation.:** Constipation is primarily caused by a lack of dietary fiber and insufficient water intake, not high salt consumption.
* **Salt improves weak bones.:** Weak bones (osteoporosis) are improved by calcium and Vitamin D, whereas excessive sodium actually causes calcium loss in urine.
* **Salt decreases the risk of asthma.:** Salt intake has no proven medical benefit in reducing asthma risks.

📌 **Key Learning Note:**
Excessive intake of **salty foods** (like salted preserved meat) leads to **high blood pressure (hypertension)** and heart conditions.""",

    32: """The correct answer is **Decreased consumption of fruits and vegetables.**.

**Detailed Analysis of the Correct Answer:**
**Scurvy** is a nutritional deficiency disease caused by a severe lack of **Vitamin C (ascorbic acid)** in the diet. Fresh fruits (especially citrus fruits like oranges, lemons, and passion fruit) and fresh green vegetables are the primary natural sources of Vitamin C. Therefore, a **decreased consumption of fruits and vegetables** directly leads to Vitamin C deficiency and scurvy (characterized by bleeding gums, skin spots, and poor wound healing).

**Why Other Options Are Incorrect:**
* **Increased consumption of fruits and vegetables.:** Eating plenty of fruits and vegetables provides abundant Vitamin C, which **prevents** scurvy.
* **Decreased consumption of foods rich in carbohydrates.:** Lack of carbohydrates leads to marasmus/underweight, not scurvy.
* **Increased consumption of foods rich in fibre and water.:** Fiber and water improve digestion and prevent constipation, having no relation to Vitamin C deficiency.

📌 **Key Learning Note:**
Deficiency Diseases & Causes:
- **Scurvy:** Lack of **Vitamin C** (found in fresh fruits and vegetables).
- **Rickets:** Lack of **Vitamin D / Calcium**.
- **Kwashiorkor:** Lack of **Proteins**.
- **Marasmus:** Lack of **Total Energy/Carbohydrates**.""",

    33: """The correct answer is **soaking**.

**Detailed Analysis of the Correct Answer:**
**Soaking** is the laundering step of immersing clothes in cold water (often with salt added) for a period of time prior to washing. In the case of handkerchiefs, soaking in **cold salty water** helps to dissolve and loosen organic stains such as mucus and blood without setting the stain into the fabric fibers.

**Why Other Options Are Incorrect:**
* **washing:** Washing is the active process of rubbing, agitating, and cleansing garments using soap and warm/hot water.
* **sorting:** Sorting is the initial step of separating garments based on color, fabric type, and degree of dirtiness before laundering begins.
* **rinsing.:** Rinsing is performed *after* washing to remove remaining soap suds using clean, clear water.

📌 **Key Learning Note:**
- **Salty Cold Water Soaking:** Dissolves mucus and blood stains from handkerchiefs before washing.
- **Rinsing:** Removes detergent suds after washing.""",

    34: """The correct answer is **Back stitches.**.

**Detailed Analysis of the Correct Answer:**
A **back stitch** is one of the strongest hand-sewing permanent stitches. It mimics machine stitching, creating a tight, durable line of overlapping stitches. Because of its strength, back stitching is the ideal stitch to use for **repairing a gaping or torn seam** on a school uniform garment.

**Why Other Options Are Incorrect:**
* **Loop stitches.:** Loop stitches are decorative stitches or used for neatening raw edges (like blanket stitch), lacking the structural strength needed to hold a gaping seam.
* **Hemming stitches.:** Hemming stitches are slanted stitches used specifically to secure folded hems at the bottom of skirts, trousers, or sleeves.
* **Oversewing stitches.:** Oversewing stitches are used over the raw cut edges of fabric to prevent fraying rather than joining two seam edges tightly.

📌 **Key Learning Note:**
- **Back Stitch:** Strong permanent stitch used for **repairing open/gaping seams**.
- **Hemming Stitch:** Used to **secure folded hems**.
- **Oversewing Stitch:** Used to **prevent raw fabric edges from fraying**.""",

    35: """The correct answer is **use a fabric conditioner when rinsing.**.

**Detailed Analysis of the Correct Answer:**
Garments (especially synthetic fabrics like polyester and nylon) cling to the body due to **static electricity** generated by friction between fabric fibers. Adding a **fabric conditioner (fabric softener)** to the final rinse water lubricates the fibers, reduces friction, neutralizes static electrical charges, and prevents static cling while keeping clothes soft and fresh.

**Why Other Options Are Incorrect:**
* **bleach the dress after washing:** Bleach is a chemical agent used to whiten fabrics or remove tough stains; it does not eliminate static electricity.
* **use a disinfectant when rinsing:** Disinfectants kill bacteria and germs on laundry, but have no anti-static properties.
* **rinse the dress well with clean water:** Plain water removes soap suds, but plain water alone does not eliminate static cling in synthetic fabrics once dried.

📌 **Key Learning Note:**
- **Fabric Conditioner:** Reduces static cling, softens fabric, and adds pleasant fragrance during final rinse.
- **Bleach:** Whitens white fabrics and removes stubborn stains.""",

    36: """The correct answer is **i, ii, iii.**.

**Detailed Analysis of the Correct Answer:**
Let's evaluate the safety and performance rules for racing games:
- **Rule (i) Wear suitable shoes while running:** Correct! Wearing proper sports shoes prevents slipping, blisters, and foot injuries.
- **Rule (ii) Keep to your lane when running:** Correct! Staying in one's assigned lane prevents collisions with other runners.
- **Rule (iii) Drink adequate amount of water before the race:** Correct! Proper hydration prevents muscle cramps and heat exhaustion.
- **Rule (iv) Avoid performing any exercise before the race:** **Incorrect!** Athletes must perform warm-up exercises before a race to prepare muscles and prevent muscle strains.

Therefore, the set of correct rules is **i, ii, iii.**

**Why Other Options Are Incorrect:**
* **i, ii, iv.:** Includes rule (iv), which is harmful because skipping warm-up exercises causes muscle injuries.
* **i, iii, iv.:** Includes the incorrect rule (iv).
* **ii, iii, iv.:** Includes the incorrect rule (iv).

📌 **Key Learning Note:**
Always perform **warm-up exercises** before any intense physical activity to stretch muscles and increase blood flow, preventing sports injuries.""",

    37: """The correct answer is **Improves physical fitness.**.

**Detailed Analysis of the Correct Answer:**
**Rope skipping** is an excellent cardiovascular endurance and aerobic exercise. Regular rope skipping elevates heart rate, strengthens the heart and lungs, tones muscles, improves hand-eye coordination, and enhances overall **physical fitness** and stamina.

**Why Other Options Are Incorrect:**
* **Makes the leg joints weak.:** Skipping rope actually increases bone density and strengthens the muscles, tendons, and ligaments around leg joints over time.
* **Causes lifestyle disease.:** Regular physical exercise like rope skipping actively **prevents** lifestyle diseases such as obesity, diabetes, and hypertension.
* **Can cause injury to ankles.:** While poor landing technique can strain ankles, injury is not the intended or normal outcome of proper exercise.

📌 **Key Learning Note:**
Regular physical exercises (like skipping, running, swimming) **improve physical fitness** and protect against lifestyle diseases.""",

    38: """The correct answer is **Speed.**.

**Detailed Analysis of the Correct Answer:**
**Speed** is defined in physical education as the ability of the body or body parts to **move across a given distance within the shortest time possible**. Running to a specified finish line as fast as possible directly tests and develops an individual's speed component of physical fitness.

**Why Other Options Are Incorrect:**
* **Coordination.:** Coordination is the ability to execute smooth, accurate movements combining different body parts and senses together (e.g. dribbling a basketball).
* **Strength.:** Muscle strength is the maximum force a muscle can exert against a heavy load (e.g. lifting weights).
* **Balance.:** Balance is the ability to maintain the body's center of gravity without falling (e.g. standing on one leg).

📌 **Key Learning Note:**
Components of Physical Fitness:
- **Speed:** Moving the body across a distance in the shortest time.
- **Strength:** Exerting force against resistance.
- **Balance:** Maintaining body stability.
- **Flexibility:** Range of motion around joints.""",

    39: """The correct answer is **Promote unity among friends for better group work.**.

**Detailed Analysis of the Correct Answer:**
During outdoor camping and recreational activities, **sharing food** fosters social bonding, mutual care, trust, and inclusivity. Sharing builds a spirit of **unity, cooperation, and camaraderie**, which essential for effective group work, problem-solving, and safety during outdoor expeditions.

**Why Other Options Are Incorrect:**
* **Show friends' background with different kinds of food.:** Camping is not a platform for showing off family wealth or background differences.
* **Encourage friends to rely on others for food.:** The goal is not to foster laziness or dependency, but to promote team spirit.
* **Saves time for those who do not want to prepare and carry food.:** Outdoor education teaches personal responsibility; every camper is expected to participate.

📌 **Key Learning Note:**
Sharing resources during group activities promotes **unity, teamwork, empathy, and social harmony**.""",

    40: """The correct answer is **Turn right.**.

**Detailed Analysis of the Correct Answer:**
In outdoor navigation, trail marking, and road signage, a clear arrow icon pointing towards the right side of a path indicates the instruction to **Turn right**.

**Why Other Options Are Incorrect:**
* **No way through.:** A 'no way through' or 'no entry' sign is typically indicated by an 'X' symbol or a red circle with a horizontal bar.
* **Stop.:** A 'stop' sign is indicated by an octagonal red sign with the word 'STOP'.
* **Turn left.:** A 'turn left' sign features an arrow pointing to the left side.

📌 **Key Learning Note:**
Trail signs and directional arrows guide outdoor navigators safely along designated routes.""",

    41: """The correct answer is **Side vault.**.

**Detailed Analysis of the Correct Answer:**
In gymnastics, a **side vault** is a vaulting skill where the performer approaches an obstacle, places one or both hands on the apparatus/box, and shifts their legs and hips to one side, clearing the obstacle horizontally in a sideways body position before landing safely on both feet.

**Why Other Options Are Incorrect:**
* **Wall vault.:** A wall vault involves running up against a vertical wall to gain height.
* **Fence vault.:** Refers to clearing a fence, but the specific technical gymnastic movement execution described is the side vault.
* **Jump vault.:** A general term that does not describe the specific lateral body orientation of the side vault technique.

📌 **Key Learning Note:**
Gymnastic Vaults:
- **Side Vault:** Body passes sideways over the apparatus with hand support.""",

    42: """The correct answer is **Cotton wool - applying antiseptics and cleaning cuts.**.

**Detailed Analysis of the Correct Answer:**
**Cotton wool** is an essential first aid item used to absorb fluids, **clean minor cuts and wounds** with water or antiseptic solutions, and apply liquid antiseptics safely to injured skin.

**Why Other Options Are Incorrect:**
* **Scissors - cutting papers and muscles that have been injured.:** Scissors in a first aid kit are used to cut bandages, adhesive tape, and clothing around a wound—never to cut human body tissues or muscles!
* **Bandages - making straps to support the first aid box.:** Bandages are used to wrap dressings, hold splints in place, apply pressure to stop bleeding, and support injured joints.
* **Thermometer - controlling body temperature.:** A thermometer measures (reads) body temperature; it does not control or reduce temperature (fever is managed with medication or cooling sponges).

📌 **Key Learning Note:**
- **Cotton Wool:** Cleaning wounds and applying antiseptic.
- **Scissors:** Cutting bandages, tape, or clothing.
- **Bandages:** Securing dressings and supporting injured joints.
- **Thermometer:** Measuring body temperature.""",

    43: """The correct answer is **Wood.**.

**Detailed Analysis of the Correct Answer:**
When improvising relay batons for physical education, **wood** (such as a smooth, rounded wooden stick or dowel) provides the highest structural strength, rigidity, and durability. Wooden batons can withstand repeated drops on hard ground without breaking, bending, or tearing.

**Why Other Options Are Incorrect:**
* **Manila paper.:** Manila paper tears easily when wet or dropped and loses its shape quickly under hand pressure.
* **Clay.:** Molded clay is brittle; it will shatter or crack immediately if dropped on the ground during a relay exchange.
* **Grass.:** Bundled grass lacks structural rigidity and unravels easily during running.

📌 **Key Learning Note:**
When improvising sports equipment, choose materials that are **safe, durable, sturdy, and appropriate** for the activity (e.g. smooth wood for batons).""",

    44: """The correct answer is **hand stand**.

**Detailed Analysis of the Correct Answer:**
A **hand stand** is an inverted body balance skill in gymnastics where the performer balances the entire body upside down in a straight vertical line, supported strictly by the **palms of the hands** placed on the floor, with arms fully extended and legs pointing straight up into the air.

**Why Other Options Are Incorrect:**
* **head stand:** A head stand uses a tripod base formed by the head touching the mat and both hands on the floor.
* **inverted stand:** A general descriptive term, but the specific standard gymnastic movement is termed a hand stand.
* **hand and head stand.:** Known technically as a headstand (tripod stand), whereas the image shows balancing on hands alone.

📌 **Key Learning Note:**
- **Handstand:** Balancing upside down supported strictly on the hands.
- **Headstand:** Balancing upside down supported on the head and hands.""",

    45: """The correct answer is **Juliet.**.

**Detailed Analysis of the Correct Answer:**
**Juliet** chose the ideal site for an outdoor shelter: **at a gentle slope sheltered by trees**. A gentle slope ensures proper natural surface water drainage during rain (preventing puddle accumulation), while nearby trees act as a natural windbreak against strong winds and provide shade from harsh sunlight.

**Why Other Options Are Incorrect:**
* **Jane:** Setting up camp close to a riverbank is dangerous due to sudden flash floods, high humidity, and swarms of mosquitoes.
* **John:** The peak of a hill is exposed to harsh, strong winds and potential lightning strikes during storms.
* **James:** The bottom of a valley collects cold sinking air at night and is prone to flooding during heavy rain.

📌 **Key Learning Note:**
Ideal Camping Site Selection:
- **Gentle Slope:** Prevents water pooling during rain.
- **Sheltered by Trees:** Provides wind protection and shade.
- **Avoid:** Riverbanks (flooding/mosquitoes), hilltops (strong winds), valley bottoms (cold/flooding).""",

    46: """The correct answer is **Sitting while leaning forward and pinching the soft part of the nose.**.

**Detailed Analysis of the Correct Answer:**
The correct first aid procedure for a nosebleed (epistaxis) is:
1. **Sit upright and lean slightly forward:** Leaning forward prevents swallowed blood from entering the stomach (which causes vomiting) or entering the windpipe.
2. **Pinch the soft part of the nose:** Apply firm, continuous pressure on the soft lower nostrils for 10 minutes to compress the bleeding blood vessels and encourage clotting.

**Why Other Options Are Incorrect:**
* **Lying on the back while facing up.:** Lying flat causes blood to flow down the throat into the stomach or airways, leading to choking or nausea.
* **Putting cotton wool in the nostrils to block the blood from flowing.:** Stuffing materials inside the nose can tear delicate nasal linings when removed, restarting the bleeding.
* **Sitting down with legs raised to relax and stop bleeding.:** Elevating legs is used for treating shock, not for stopping a nasal hemorrhage.

📌 **Key Learning Note:**
Nosebleed First Aid: **Sit up, lean FORWARD, and PINCH the soft part of the nose** for 10 minutes. Never lean backward!""",

    47: """The correct answer is **Pieces of clothes.**.

**Detailed Analysis of the Correct Answer:**
A **triangular bandage** is a versatile first aid dressing used to support injured arms (slings) or wrap wounds. **Pieces of clean cloth** (such as a cotton bedsheet, shirt, or scarf) can be easily cut into a right-angled triangular shape. Cloth is soft, washable, flexible, and strong enough to support the weight of an injured limb.

**Why Other Options Are Incorrect:**
* **Newspapers.:** Paper tears easily, lacks strength to support an arm, and printer ink can contaminate open wounds.
* **Banana leaves.:** Leaves dry out, tear easily, and cannot be securely tied in a knot to support a sling.
* **A piece of carton.:** Cardboard is rigid and stiff; it is useful for improvising a rigid *splint*, but not a flexible *triangular bandage*.

📌 **Key Learning Note:**
- **Improvised Triangular Bandage:** Use clean, strong, flexible **pieces of cloth**.
- **Improvised Splint:** Use rigid materials like wooden sticks, rulers, or stiff cardboard.""",

    48: """The correct answer is **Cotton wool, papers, strings.**.

**Detailed Analysis of the Correct Answer:**
In Physical and Health Education (PHE), improvising a safe ball involves using **soft core materials wrapped securely**. A combination of **cotton wool (or soft rags), paper, and strings** creates a soft, rounded, compact, and lightweight ball that is safe for learners to kick without sustaining foot injuries.

**Why Other Options Are Incorrect:**
* **Old newspapers, strings, polythene bags.:** Polythene bags are slippery and less compact compared to cloth/cotton wool cores.
* **Leaves, plastic bottles, strings.:** Hard plastic bottles inside a ball can cause foot injuries when kicked forcefully.
* **Cotton wool, wire, old newspapers.:** Wire is extremely dangerous; sharp wire ends can puncture skin or cause severe injuries during play.

📌 **Key Learning Note:**
Improvised sports equipment must prioritize **learner safety**—never use sharp objects, glass, or hard wires.""",

    49: """The correct answer is **7**.

**Detailed Analysis of the Correct Answer:**
In a standard game of **handball**, each team has **7 players** on the court during play: **6 outfield players and 1 goalkeeper**.

**Why Other Options Are Incorrect:**
* **5:** 5 players per team is the standard number for a **basketball** court team.
* **6:** 6 players per team is the standard number for a **volleyball** court team.
* **8:** 8 players is not a standard team size for major court ball games.

📌 **Key Learning Note:**
Standard Court Team Numbers:
- **Handball:** 7 players per team (6 outfield + 1 goalkeeper).
- **Basketball:** 5 players per team.
- **Volleyball:** 6 players per team.
- **Netball:** 7 players per team.""",

    50: """The correct answer is **Run.**.

**Detailed Analysis of the Correct Answer:**
In athletics track events (sprint races), the official starting commands given by the starter for a crouch start are:
1. **"On your marks"** (runners take positions behind the line).
2. **"Set"** (runners raise their hips and hold still).
3. **"Go"** (or a pistol shot / whistle start).

The word **"Run"** is **never** used as an official athletics starting command.

**Why Other Options Are Incorrect:**
* **Go.:** 'Go' is the official final starting command to begin running.
* **Set.:** 'Set' is the official second command requiring runners to hold position.
* **On your marks.:** 'On your marks' is the official first command instructing runners to approach the starting line.

📌 **Key Learning Note:**
Official Sprint Race Commands: **"On your marks" ➔ "Set" ➔ "Go!" (or Pistol Shot)**."""
}

for q in data['sectionA']:
    qn = q['questionNumber']
    if qn in remaining_explanations:
        q['explanation'] = remaining_explanations[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print("Remaining questions (Q21 - Q50) updated successfully in kpsea-science-2023.js!")
