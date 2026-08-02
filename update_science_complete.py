import json
import re

# Load raw questions from all_non_math_questions.json
with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

science_qs = all_data['kpsea-science-2023']['sectionA']

explanations_map = {
    1: """The primary site for food production (photosynthesis) in a plant is the **Leaf**. Leaves contain chlorophyll which absorbs sunlight, carbon dioxide, and water to produce carbohydrates.

* **Why other options are incorrect:**
  * **Root:** Absorbs water and dissolved minerals from the soil and anchors the plant firmly in the ground.
  * **Stem:** Transports water, minerals, and manufactured food between roots and leaves, while supporting branches and leaves.
  * **Fruit:** Protects the seeds and aids in their dispersal after fertilization.

💡 **Key Takeaway:** Chlorophyll in green leaves makes them the primary 'food factories' of plants through photosynthesis.""",

    2: """**E: Beans, F: Maize** is the correct match. Diagram E shows a tap root system (a single thick main root growing downward with small branch roots) characteristic of dicotyledonous plants like beans. Diagram F shows a fibrous root system (a cluster of thin, equal-sized roots arising from the base of the stem) typical of monocotyledonous plants like maize.

* **Why other options are incorrect:**
  * **E: Maize, F: Sugarcane:** Both maize and sugarcane are monocotyledonous plants that possess fibrous root systems.
  * **E: Sisal, F: Beans:** Sisal has a fibrous root system while beans have a tap root system, so this pair reverses the root systems shown.
  * **E: Sugarcane, F: Sisal:** Both of these crops are monocots and possess fibrous roots.

💡 **Key Takeaway:** Dicotyledonous crops (beans, peas, groundnuts) feature tap root systems, whereas monocotyledonous crops (maize, wheat, sisal, sugarcane) feature fibrous root systems.""",

    3: """A **Cockroach** belongs to the group of insects (hexapods). Insects are characterized by having three body parts (head, thorax, abdomen), three pairs of jointed legs (6 legs), wings (often present), and a pair of antennae.

* **Why other options are incorrect:**
  * **Tick:** Ticks are arachnids; they have two main body parts (cephalothorax and abdomen), four pairs of legs (8 legs), and no wings or antennae.
  * **Millipede:** Millipedes are myriapods with elongated bodies consisting of numerous segments, two pairs of legs per body segment, and no wings.
  * **Centipede:** Centipedes are myriapods with flattened body segments, one pair of legs per body segment, and no wings.

💡 **Key Takeaway:** Insects are distinctly identified by having 3 body regions (head, thorax, abdomen), 3 pairs of legs, 1 pair of antennae, and usually wings.""",

    4: """The part labelled G represents the left ventricle. The primary function of the left ventricle is **Pumping blood to other parts of the body** (systemic circulation). It has the thickest muscular wall to generate high pressure to force oxygenated blood throughout the body.

* **Why other options are incorrect:**
  * **Pumping blood to the lungs:** This is the specific function of the right ventricle via the pulmonary artery.
  * **Receiving blood from the rest of the body:** This is the function of the right atrium, which receives deoxygenated blood via the vena cava.
  * **Receiving deoxygenated blood:** This is carried out by the right side of the heart (right atrium and right ventricle).

💡 **Key Takeaway:** The left side of the heart handles oxygenated blood, with the thick left ventricle pumping blood across the entire body.""",

    5: """The **Cervix** belongs to the female reproductive system; it is the narrow muscular neck of the uterus that connects the uterus to the vagina.

* **Why other options are incorrect:**
  * **Prostate:** The prostate is a gland in the male reproductive system that secretes fluid to nourish and transport sperm.
  * **Testis:** The testis (testicle) is the male primary reproductive organ that produces sperm cells and testosterone.
  * **Penis:** The penis is the male external reproductive organ used to transfer sperm during copulation.

💡 **Key Takeaway:** Female reproductive parts include ovaries, oviducts, uterus, cervix, and vagina. Male reproductive parts include testes, prostate gland, vas deferens, and penis.""",

    6: """In activity **D**, water is **not conserved** because a running hose pipe is being used continuously to wash a vehicle, allowing large volumes of clean water to be wasted.

* **Why other options are incorrect:**
  * **A:** Harvesting rainwater using roof gutters into storage tanks actively conserves water for domestic use.
  * **B:** Mulching around crops conserves soil moisture by reducing evaporation driven by sunlight.
  * **C:** Using a bucket or container of water to wash or clean instead of a running tap conserves significant amounts of water.

💡 **Key Takeaway:** Using bucket washing or drip irrigation conserves water, whereas using open running hoses leads to high water wastage.""",

    7: """Passing a desktop computer intact to a friend so they can use it is an example of managing solid waste by **reusing only**. The item is used again for its original purpose without undergoing any industrial re-manufacturing process.

* **Why other options are incorrect:**
  * **reusing and recycling:** Recycling involves processing discarded materials mechanically or chemically into raw materials to manufacture new products.
  * **reducing only:** Reducing means minimizing the amount of waste generated initially (e.g., buying less packaging).
  * **reducing and recycling:** Neither reducing initial consumption nor melting/reprocessing materials occurred here.

💡 **Key Takeaway:** Reusing items extends their functional life and directly prevents usable items from entering the solid waste stream.""",

    8: """**Avoiding open defecation** directly prevents human feces containing harmful pathogens, bacteria, and parasite eggs from washing into rivers, streams, and shallow wells, effectively controlling water pollution at its source.

* **Why other options are incorrect:**
  * **Boiling:** Boiling purifies small amounts of water for drinking but does not control or reduce environmental water pollution in water bodies.
  * **Filtration:** Filtration removes suspended solid particles from collected water but does not prevent pollution entering water sources.
  * **Chemical treatment:** Treats contaminated water for safe consumption (point-of-use), but does not stop pollutants from entering water sources.

💡 **Key Takeaway:** Preventing pollutants from entering water sources through proper sanitation (latrines) is the most effective way to control water pollution.""",

    9: """**Wearing shoes** prevents jigger infestations because jiggers (female sand fleas / *Tunga penetrans*) live in dry dusty soil and burrow directly into the skin of bare feet.

* **Why other options are incorrect:**
  * **Not sharing clothes:** Prevents the spread of body lice or skin infections like ringworms, but jiggers live in contaminated soil.
  * **Soaking clothes in hot water:** Kills body lice and parasite eggs in clothing, but jiggers attack bare feet directly from dusty ground.
  * **Ironing clothes:** Destroys lice eggs trapped in garment seams, but does not shield feet from jigger fleas in dirt.

💡 **Key Takeaway:** Wearing protective footwear forms a physical barrier that stops soil-borne parasites like jiggers and hookworms from invading the feet.""",

    10: """The experiment demonstrates that matter **expands and contracts**. When heated, the solid metal ball absorbs thermal energy and expands (increases in volume), preventing it from passing through the metal ring. Upon cooling, it contracts to its original size.

* **Why other options are incorrect:**
  * **exerts pressure and has volume:** While matter occupies space, this specific setup demonstrates dimensional change due to temperature.
  * **changes state and has mass:** The ball remains a solid throughout the activity; it does not change state into a liquid.
  * **occupies space and has weight:** General characteristics of all matter, but thermal expansion/contraction is the specific phenomenon tested.

💡 **Key Takeaway:** Heating matter causes expansion (volume increase), while cooling causes contraction (volume decrease).""",

    11: """**Drying of clothes** is an everyday application of the change of state known as evaporation, where liquid water in wet fabric absorbs heat and changes into water vapor (gas).

* **Why other options are incorrect:**
  * **Working of thermometers:** Relies on thermal expansion and contraction of liquids (mercury/alcohol) inside a narrow tube, not a change of state.
  * **Warming water:** Involves raising the temperature of liquid water without changing its state into gas (unless it reaches boiling point).
  * **Hardening of bricks:** Involves chemical reactions and moisture loss through baking clay, not a simple physical change of state.

💡 **Key Takeaway:** Evaporation (liquid to gas) is driven by heat and airflow, making it essential for drying clothes, crops, and salt production.""",

    12: """**Nitrogen** is the most abundant gas in clean atmospheric air, constituting approximately 78% by volume.

* **Why other options are incorrect:**
  * **Carbon dioxide:** Makes up approximately 0.04% of the Earth's atmosphere by volume.
  * **Oxygen:** Makes up about 21% of atmospheric air by volume.
  * **Inert gases:** Rare gases (such as Argon, Helium, Neon) make up slightly less than 1% combined.

💡 **Key Takeaway:** The Earth's atmosphere consists mainly of Nitrogen (78%) and Oxygen (21%), with trace amounts of carbon dioxide, water vapor, and noble gases.""",

    13: """**Sharpening tools** (such as running a knife edge against a whetstone or file) intentionally increases friction to grind away metal and create a keen cutting edge. It does NOT reduce friction.

* **Why other options are incorrect:**
  * **Lubrication:** Applying oil or grease creates a smooth layer between surfaces, effectively reducing friction.
  * **Smoothening surfaces:** Reduces surface roughness and irregularities, which lowers sliding friction.
  * **Using rollers:** Replaces high sliding friction with significantly lower rolling friction.

💡 **Key Takeaway:** Friction can be reduced by lubrication, smoothing, and using rollers/ball bearings, but is purposefully increased when sharpening tools or applying vehicle brakes.""",

    14: """A ladder acts as an inclined plane (a simple machine) because it allows a person to **move loads through heights** using less effort force over a longer slanted distance.

* **Why other options are incorrect:**
  * **move loads in circles:** This is achieved using wheels, axles, or gears, not a slanted ladder.
  * **move loads horizontally:** Horizontal displacement is made easier using carts, wheelbarrows, or rollers.
  * **overcome loads in the opposite direction of force:** This describes the primary function of a single fixed pulley (changing force direction).

💡 **Key Takeaway:** An inclined plane (ramp or ladder) reduces the effort required to lift objects vertically by spreading the effort over a longer distance.""",

    15: """**cirrus** clouds are high-altitude clouds that appear thin, white, wispy, feather-like, and light, composed mainly of ice crystals.

* **Why other options are incorrect:**
  * **nimbus:** Dark, heavy, dense clouds that bring continuous rain or thunderstorms.
  * **stratus:** Low-level, uniform, grey sheet-like clouds covering the sky like a fog layer.
  * **cumulus:** Fluffy, white, cotton-like clouds with flat bases seen on clear, sunny days.

💡 **Key Takeaway:** Cirrus clouds are wispy and feather-like ice crystal clouds found at very high altitudes.""",

    16: """The photograph shows a **Terrace**. Terracing involves constructing step-like earth structures across a slope to trap water and soil, reducing soil erosion on steep hillsides.

* **Why other options are incorrect:**
  * **Gabion:** Wire mesh boxes filled with rocks constructed in gullies to slow water velocity and trap silt.
  * **Grass strip:** Narrow bands of unplowed grass left along contour lines to slow down surface runoff.
  * **Trash line:** Rows of crop residues, dry grass, or brush laid across the slope along contour lines.

💡 **Key Takeaway:** Terraces are constructed steps along steep slopes that prevent surface runoff from washing away topsoil.""",

    17: """Terraces control soil erosion because the flat horizontal steps **Reduces speed of water** running down the hillside, decreasing its capacity to detach and carry soil particles.

* **Why other options are incorrect:**
  * **Intercepts rain drops:** Canopy foliage and plant mulch intercept raindrops to absorb impact energy before hitting soil.
  * **Stores water:** While terraces increase water infiltration, their main soil conservation mechanism is slowing runoff speed.
  * **Holds the soil back:** Physical retaining walls or gabions specifically hold back shifting gully soil.

💡 **Key Takeaway:** Slowing down the speed of surface runoff reduces its kinetic energy, protecting topsoil from being eroded.""",

    18: """Farm produce labeled 'ORGANIC' indicates that it is **free from artificial chemicals**, meaning it was cultivated without synthetic fertilizers, chemical pesticides, or synthetic growth stimulants.

* **Why other options are incorrect:**
  * **free from pests and diseases:** Organic crops can still experience pest attacks; farmers manage them using natural biological methods rather than synthetic sprays.
  * **fresh:** Freshness depends on harvest timing and storage, not on organic certification standards.
  * **more tasty:** Taste varies by crop variety and soil conditions; it is not the official criterion defining organic produce.

💡 **Key Takeaway:** Organic farming relies on natural ecological processes, compost manure, crop rotation, and biological pest control to grow food free from synthetic chemicals.""",

    19: """The fortified boma/fencing structure shown protects livestock by **preventing entry of the wild animals** (predators like lions, leopards, or hyenas) into the livestock enclosure.

* **Why other options are incorrect:**
  * **producing flashing lights at night:** Refers to automated LED 'lion lights' installed around pens to scare off nocturnal carnivores.
  * **scaring wild animals away:** Scarecrows or auditory deterrents scare animals away, whereas sturdy bomas physically block entry.
  * **trapping the wild animals:** Predator-proof fences exclude predators from entering; they do not trap or capture them.

💡 **Key Takeaway:** Building predator-proof bomas provides a physical barrier that protects farm animals and mitigates human-wildlife conflict.""",

    20: """The goats and sheep in the picture are **herbivorous** because their digestive systems are adapted to consume exclusively plant matter such as grasses, shrubs, and leaves.

* **Why other options are incorrect:**
  * **carnivorous:** Flesh-eating animals (e.g., lions, hyenas, eagles) that prey on other animals.
  * **decomposers:** Microorganisms, fungi, or detritivores that break down dead organic matter into soil nutrients.
  * **omnivorous:** Animals whose diet includes both plant matter and meat (e.g., pigs, domestic dogs, humans).

💡 **Key Takeaway:** Animals are grouped by feeding habits into herbivores (plant eaters), carnivores (meat eaters), and omnivores (plant and meat eaters).""",

    21: """The practice of replacing missing seeds or replanting spots where seeds failed to germinate after sowing is called **Gapping**, ensuring an even crop density across the field.

* **Why other options are incorrect:**
  * **Pruning:** Trimming unwanted, diseased, or overgrown branches and shoots from bushes or trees.
  * **Thinning:** Removing excess, weak, or overcrowded seedlings from a cluster to allow remaining seedlings room to grow.
  * **Training:** Supporting or guiding weak stems of climbing crops (like beans or passion fruit) along stakes or wires.

💡 **Key Takeaway:** Gapping fills empty spaces left by un-germinated seeds, ensuring a full plant population for optimal field yield.""",

    22: """A **Squirrel** is a seed-eating pest known for digging up and consuming sown seeds (like maize or groundnuts) from the soil before or during germination.

* **Why other options are incorrect:**
  * **Mole:** Burrows underground to feed primarily on root tubers, sweet potatoes, and cassava roots in mature crops.
  * **Monkey:** Attacks mature crops, taking ripe maize cobs, fruits, and vegetables prior to harvest.
  * **Weaver bird:** Feeds on developing or ripe grain heads of standing cereal crops (sorghum, millet, rice).

💡 **Key Takeaway:** Different farm pests target crops at different growth stages; rodents like squirrels dig up seeds right at the germination stage.""",

    23: """The farmer is carrying out **Weed control** by removing unwanted plants (weeds) growing alongside maize crops to prevent them from competing for water, light, and nutrients.

* **Why other options are incorrect:**
  * **Harvesting:** Collecting ripe, mature produce at the end of the crop growing season.
  * **Pruning:** Selective cutting of tree branches or dense foliage.
  * **Training:** Securing vine stems to trellises or wooden stakes.

💡 **Key Takeaway:** Controlling weeds early in the crop cycle prevents weeds from robbing young crops of essential nutrients, water, and sunlight.""",

    24: """**Pigweed** (Amaranthus, commonly known as *Terere*) is a traditional indigenous leafy vegetable crop native to local environments. It is highly nutritious, rich in micronutrients, and well-adapted to local climate conditions.

* **Why other options are incorrect:**
  * **Cabbage:** An exotic vegetable introduced from temperate regions requiring high rainfall and cooler conditions.
  * **Kales:** Sukuma wiki is an exotic leafy crop originating from temperate European brassicas.
  * **Spinach:** An exotic green vegetable native to central and western Asia that requires consistent irrigation and cool climate.

💡 **Key Takeaway:** Indigenous crops like pigweed are naturally resilient, drought-tolerant, and require lower chemical inputs compared to exotic vegetables (cabbage, kales, spinach). Promoting indigenous crops alongside standard field crop management (gapping and thinning seen in Q21-Q23) improves farm biodiversity, food security, and family nutrition.""",

    25: """**Cassava and arrowroots** are both traditional indigenous root/tuber crops widely cultivated in African farming systems for their starchy roots and drought resistance.

* **Why other options are incorrect:**
  * **Arrowroots and carrots:** Carrots are exotic root vegetables introduced from Europe and Asia.
  * **Beetroot and cassava:** Beetroot is an exotic root vegetable introduced from temperate regions.
  * **Carrots and yams:** Carrots are exotic root vegetables, making this pair inaccurate.

💡 **Key Takeaway:** Indigenous root crops like cassava, arrowroot, and sweet potatoes are hardy crops that enhance food security during dry spells.""",

    26: """Communicable diseases are defined as infectious illnesses caused by pathogens that **are spread easily from one person to another** (or from animals to humans) through air, water, direct contact, or vector organisms.

* **Why other options are incorrect:**
  * **They are diseases that cannot be spread from one person to another:** This describes non-communicable diseases (e.g., asthma, hypertension, diabetes).
  * **They are diseases that are spread only by communicating to people:** Transmission happens via physical pathogens (viruses, bacteria), not verbal communication.
  * **They are diseases that spread only when people move from one place to another:** Pathogens can spread locally within a household or classroom without geographic movement.

💡 **Key Takeaway:** Communicable diseases are transmissible infectious diseases, whereas non-communicable diseases cannot be transmitted from person to person.""",

    27: """**Fatma** brought items (tie, socks, belt, and scarf) that are clothing accessories worn to complement and enhance personal appearance.

* **Why other options are incorrect:**
  * **Auma:** Brought skin care cosmetics and toiletries (body lotion, petroleum jelly, skin care cream), which are personal hygiene products rather than accessories.
  * **Chris:** Brought needlework tools (thread, thimble, pins) alongside make-up, which are sewing materials rather than clothing accessories.
  * **Festus:** Brought eating utensils (cup, spoon), a sewing needle, and perfume, which do not represent clothing accessories.

💡 **Key Takeaway:** Fashion accessories include items worn alongside clothing (belts, ties, scarves, socks, hats) to complete and enhance personal grooming and appearance.""",

    28: """Savings refers to **the amount of money set aside for future use**, investment, or unforeseen circumstances out of current income.

* **Why other options are incorrect:**
  * **Savings is the amount of money you are left with after buying all items required:** This is unbudgeted pocket change or residual cash, not planned savings.
  * **Savings is the amount of money you are given back after paying for items:** This is called change from a financial transaction.
  * **Savings is the amount of money set aside for unexpected expenses:** Money set aside specifically for sudden emergencies is an emergency fund, whereas general savings covers planned future goals and security.

💡 **Key Takeaway:** Financial discipline involves creating a budget where a dedicated portion of income is allocated to savings for future goals before spending.""",

    29: """When buying packaged food or fat, checking the **Expiry date on the package** is essential to ensure the food product is safe for consumption and has not spoiled or degraded.

* **Why other options are incorrect:**
  * **Colour of the packaging:** Packaging aesthetics or color design do not reflect product freshness, safety, or quality.
  * **The type of packaging used:** Container material (plastic vs tin) does not guarantee that the food inside is unexpired or safe.
  * **Weight of the packaging material:** The weight of the empty box or wrapper is irrelevant to nutritional quality or safety.

💡 **Key Takeaway:** Always inspect product safety labels—especially manufacturing and expiry dates—to protect health when buying packaged goods.""",

    30: """Micronutrients are essential nutrients needed by the human body in small quantities to regulate body processes and build immunity; they consist of **vitamins and minerals**.

* **Why other options are incorrect:**
  * **proteins and lipids:** Proteins and lipids (fats) are macronutrients required in large amounts for body growth, repair, and energy storage.
  * **carbohydrates and lipids:** Both carbohydrates and lipids are energy-giving macronutrients.
  * **carbohydrates and proteins:** Both are macronutrients providing energy and structural building blocks.

💡 **Key Takeaway:** Human diet requires macronutrients (carbohydrates, proteins, fats) in large amounts for energy and growth, and micronutrients (vitamins, minerals) in small amounts for protection against diseases.""",

    31: """Consuming excessive salt (from heavily salted preserved meats) **increases risk of hypertension** (high blood pressure) because excess sodium causes the body to retain extra fluid, putting strain on blood vessels and the heart.

* **Why other options are incorrect:**
  * **Salt increases risk of constipation:** Constipation is primarily caused by a lack of dietary fiber and insufficient water intake, not salt intake.
  * **Salt improves weak bones:** Calcium and Vitamin D strengthen bones; excess salt can actually cause calcium loss through urine.
  * **Salt decreases the risk of asthma:** Salt intake does not reduce asthma risk; asthma is a respiratory tract condition.

💡 **Key Takeaway:** While salting preserves meat by removing moisture to stop bacterial growth, eating excessive sodium increases blood pressure and health risks.""",

    32: """Scurvy is a deficiency disease caused by a **Decreased consumption of fruits and vegetables**, which are the primary sources of Vitamin C (ascorbic acid).

* **Why other options are incorrect:**
  * **Increased consumption of fruits and vegetables:** Eating plenty of fresh citrus fruits and leafy greens supplies abundant Vitamin C, preventing scurvy.
  * **Decreased consumption of foods rich in carbohydrates:** Lack of carbohydrates leads to energy deficiency and weight loss, not scurvy.
  * **Increased consumption of foods rich in fibre and water:** Fiber and water promote digestion and bowel movement, having no link to Vitamin C deficiency.

💡 **Key Takeaway:** Scurvy is caused by Vitamin C deficiency; consuming fresh fruits (oranges, lemons, passion fruit) and green vegetables prevents bleeding gums and poor wound healing.""",

    33: """Putting dirty clothes or handkerchiefs in cold salty water without soap prior to washing is called **soaking** (or steeping). Soaking in salty water loosens mucus, blood, or tough organic stains and softens dirt.

* **Why other options are incorrect:**
  * **washing:** Agitating and scrubbing fabric with water and soap to remove dirt.
  * **sorting:** Grouping garments according to color, fabric type, or degree of dirtiness before laundering.
  * **rinsing:** Rinsing involves dipping washed clothes in clean plain water to remove remaining soap suds.

💡 **Key Takeaway:** Soaking handkerchiefs in cold salty water breaks down proteins and mucus stains, making subsequent washing easier and more hygienic.""",

    34: """**Back stitches** are strong, neat, permanent hand stitches that overlap on the wrong side and resemble machine stitching, making them ideal for repairing open or gaping seams.

* **Why other options are incorrect:**
  * **Loop stitches:** Used primarily for decorative edge finishing or blanket stitching, not for securing structural seams.
  * **Hemming stitches:** Slanted stitches used specifically to hold folded fabric edges (hems) in place at the bottom of skirts or trousers.
  * **Oversewing stitches:** Used to neatly bind raw fabric edges to prevent fraying rather than joining seam folds together.

💡 **Key Takeaway:** Back stitching provides maximum hand-sewing strength and elasticity for repairing garment seams.""",

    35: """Rihana should **use a fabric conditioner when rinsing** her dress. Fabric softeners/conditioners neutralize static electric charges that cause synthetic fabrics to cling uncomfortably to the skin.

* **Why other options are incorrect:**
  * **bleach the dress after washing:** Bleaching removes stains or whitens fabric; it does not eliminate static electricity and can weaken synthetic fibers.
  * **use a disinfectant when rinsing:** Disinfectants destroy germs and bacteria but have no effect on static charge accumulation.
  * **rinse the dress well with clean water:** Plain water removes soap but does not leave behind anti-static conditioning agents.

💡 **Key Takeaway:** Adding fabric conditioner during the final rinse reduces static cling, softens fabric fibers, and leaves clothing smelling fresh.""",

    36: """The correct set of safety and health rules for running events is **i, ii, iii**: (i) Wearing suitable sports shoes, (ii) Keeping strictly to your assigned lane, and (iii) Drinking adequate water before running to stay hydrated.

* **Why other options are incorrect:**
  * **i, ii, iv:** Statement iv ("Avoid performing any exercise before the race") is incorrect because warm-up exercises are mandatory to prevent muscle strains.
  * **i, iii, iv:** Statement iv is unsafe; skipping warm-up exercises increases injury risk.
  * **ii, iii, iv:** Statement iv is incorrect, making this combination invalid.

💡 **Key Takeaway:** Proper athletic safety includes warming up before races, wearing appropriate footwear, staying hydrated, and keeping to assigned track lanes.""",

    37: """Rope skipping is a full-body cardiovascular exercise that **Improves physical fitness**, boosting endurance, leg strength, rhythm, and agility.

* **Why other options are incorrect:**
  * **Makes the leg joints weak:** Regular jumping strengthens leg bones, calves, and ankles when performed on suitable surfaces.
  * **Causes lifestyle disease:** Exercise reduces and prevents lifestyle diseases like obesity, hypertension, and type 2 diabetes.
  * **Can cause injury to ankles:** While improper landing can strain ankles, healthy skipping with good footwear builds ankle stability rather than inherent injury.

💡 **Key Takeaway:** Skipping rope is an efficient exercise that builds cardiovascular fitness, motor coordination, and bone density.""",

    38: """Running to a specified target point in the minimum possible time develops the physical fitness component of **Speed** (the ability to move the body quickly across a distance).

* **Why other options are incorrect:**
  * **Coordination:** The ability to execute smooth, fluid movements combining different body parts and senses (e.g., hand-eye coordination).
  * **Strength:** The maximum force muscular contraction can exert against resistance (e.g., weightlifting).
  * **Balance:** The ability to maintain control of the body's position while static or dynamic.

💡 **Key Takeaway:** Speed is the fitness component that measures how quickly an individual can execute a movement or cover distance.""",

    39: """Sharing food during outdoor camping activities helps to **Promote unity among friends for better group work**, fostering social bonding, empathy, and mutual support.

* **Why other options are incorrect:**
  * **Show friends' background with different kinds of food:** Bragging about social background contradicts community building and teamwork values.
  * **Encourage friends to rely on others for food:** Sharing encourages mutual cooperation, not dependency or laziness.
  * **Saves time for those who do not want to prepare and carry food:** Outdoor planning expects everyone to contribute, not shirk responsibility.

💡 **Key Takeaway:** Collaborative sharing in outdoor activities builds trust, teamwork, and strong interpersonal relationships.""",

    40: """The road/trail sign with an arrow bending to the right indicates **Turn right**, directing individuals to follow the path heading toward the right side.

* **Why other options are incorrect:**
  * **No way through:** Indicated by a red circle or dead-end sign (a T-shaped symbol), not a curved arrow.
  * **Stop:** Represented by an octagonal red sign with the word 'STOP'.
  * **Turn left:** Represented by an arrow curved toward the left side.

💡 **Key Takeaway:** Recognizing directional signs ensures safe navigation during outdoor hiking and road transport.""",

    41: """The technique of supporting body weight on the hands over an apparatus while swinging the legs laterally to clear the barrier is called a **Side vault**.

* **Why other options are incorrect:**
  * **Wall vault:** Involves running up and pushing off a vertical wall structure.
  * **Fence vault:** Vaulting over a fence using specific clearing techniques, but the standard gymnastic apparatus skill shown is the side vault.
  * **Jump vault:** A general term for jumping over hurdles, not the specific hand-supported gymnastic side vault.

💡 **Key Takeaway:** Vaulting skills in gymnastics build upper body strength, agility, spatial coordination, and safe landing techniques.""",

    42: """In a first aid kit, **Cotton wool - applying antiseptics and cleaning cuts** is correctly matched with its proper hygienic purpose.

* **Why other options are incorrect:**
  * **Scissors - cutting papers and muscles that have been injured:** Scissors in first aid are used strictly to cut bandages, adhesive tape, or clothing—never human body tissues or muscles!
  * **Bandages - making straps to support the first aid box:** Bandages are designed to secure dressings, cover wounds, or support sprained joints, not to strap the box itself.
  * **Thermometer - controlling body temperature:** A thermometer measures (diagnoses) body temperature; it does not control or lower fever.

💡 **Key Takeaway:** Sterile cotton wool and antiseptics are used for cleaning cut skin surfaces safely during first aid treatment.""",

    43: """**Wood** (such as smooth wooden dowels or bamboo rods) makes the most durable and suitable improvised relay baton because of its structural rigidity, strength, and safety.

* **Why other options are incorrect:**
  * **Manila paper:** Rolled paper batons crush, tear, or bend easily when gripped tightly during relay handovers.
  * **Clay:** Clay batons are extremely fragile, heavy, and shatter upon falling onto the track.
  * **Grass:** Bound grass lacks structural stiffness and form, making it impossible to pass smoothly during a sprint.

💡 **Key Takeaway:** Effective sports equipment improvisation requires selecting strong, safe, durable local materials like smooth wood or firm plastic tubing.""",

    44: """The photograph shows a gymnast balancing vertically upside down supported entirely on the palms of the hands, which is a **hand stand**.

* **Why other options are incorrect:**
  * **head stand:** Weight is balanced on the crown of the head and forearms forming a triangular base.
  * **inverted stand:** Broad non-specific term; the specific technique executed purely on hands is a handstand.
  * **hand and head stand:** A headstand uses both hands and head simultaneously, whereas a pure handstand relies only on hands.

💡 **Key Takeaway:** Executing a handstand requires shoulder stability, arm strength, core control, and balance.""",

    45: """**Juliet** chose a suitable camping site by picking a gentle slope sheltered by trees, which provides natural protection from strong winds while avoiding drainage and flood hazards.

* **Why other options are incorrect:**
  * **Jane:** Setting up close to a river creates flash flooding risks and high mosquito exposure.
  * **John:** Placing a shelter at the very peak of a hill exposes campers to extreme wind speeds and lightning strikes.
  * **James:** Pitching camp at the bottom of a valley risks water pooling, dampness, and flash flood runoff.

💡 **Key Takeaway:** Safe campsite selection requires choosing elevated, well-drained, gently sloped ground sheltered from heavy wind hazards.""",

    46: """The correct first aid for a nosebleed (epistaxis) is **Sitting while leaning forward and pinching the soft part of the nose** for 10 to 15 minutes while breathing through the mouth.

* **Why other options are incorrect:**
  * **Lying on the back while facing up:** Tilting the head back causes blood to flow down the throat into the stomach or airway, causing choking or vomiting.
  * **Putting cotton wool in the nostrils to block the blood from flowing:** Packing nostrils tightly can cause further tissue trauma or tear clots upon removal.
  * **Sitting down with legs raised to relax and stop bleeding:** Raising legs increases blood pressure toward the head, worsening nasal bleeding.

💡 **Key Takeaway:** Lean slightly forward during a nosebleed so blood drains out safely through the nostrils while applying direct pressure to form a clot.""",

    47: """**Pieces of clothes** (clean, soft fabric cut into a right-angled triangle) are suitable for improvising a triangular bandage used for arm slings and wound dressings.

* **Why other options are incorrect:**
  * **Newspapers:** Paper tears easily when wet, lacks flexibility, and cannot securely support an injured limb.
  * **Banana leaves:** Leaves dry out, tear, and cannot be tied securely around body joints.
  * **A piece of carton:** Stiff cardboard cannot wrap flexibly around curved body limbs to serve as a bandage.

💡 **Key Takeaway:** Clean cloth pieces provide strong, flexible, washable material for improvising triangular bandages and arm slings.""",

    48: """Improvising a soft, safe soccer ball for sports practice involves using **Cotton wool, papers, strings** (or soft rags wrapped tightly in polythene and bound with string).

* **Why other options are incorrect:**
  * **Old newspapers, strings, polythene bags:** Missing soft padding makes paper-only balls hard and misshapen, though polythene bags work well with soft filling.
  * **Leaves, plastic bottles, strings:** Hard plastic bottles inside a ball can cause injuries when kicked.
  * **Cotton wool, wire, old newspapers:** Using metal wire inside a sports ball is hazardous and can cause severe puncture wounds or cuts to players' feet.

💡 **Key Takeaway:** Improvised sports balls should be made of soft, safe, non-hazardous materials bound tightly into a sphere.""",

    49: """A standard official handball team fields **7** players on the court during a match (6 outfield court players and 1 goalkeeper).

* **Why other options are incorrect:**
  * **5:** Standard number of players on court per team in basketball.
  * **6:** Standard number of players on court per team in volleyball.
  * **8:** Incorrect team size; handball uses 7 active players per team on court.

💡 **Key Takeaway:** Official handball matches feature 7 active players per team (6 court players + 1 goalkeeper) on a 40m x 20m court.""",

    50: """In athletics sprint races using block starts, the starter commands are "On your marks" followed by "Set" and the starting gun or "Go!". The command **Run** is NOT an official starter command.

* **Why other options are incorrect:**
  * **Go:** The verbal release signal used when a starter pistol is not available.
  * **Set:** The mandatory second starter command instructing runners to raise hips into the ready position.
  * **On your marks:** The mandatory first starter command instructing runners to take their positions in the blocks.

💡 **Key Takeaway:** Athletics sprint starts follow the official sequence: "On your marks", "Set", followed by the gun report or "Go!" signal."""
}

file_path = 'src/data/kpsea-science-2023.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    prefix = match.group(1)
    q_num = int(match.group(2))
    
    if q_num in explanations_map:
        new_exp = json.dumps(explanations_map[q_num])
        return prefix + new_exp
    return match.group(0)

pattern = re.compile(r'("questionNumber"\s*:\s*(\d+)\s*,[\s\S]*?"explanation"\s*:\s*)(["\'].*?(?<!\\)["\'])', re.DOTALL)
new_content = pattern.sub(replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated all 50 explanations in Science (kpsea-science-2023.js)!")
