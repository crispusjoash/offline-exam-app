import json
import re

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

explanations = {
    31: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Region F on the provided map of Eastern Africa corresponds to the northernmost part of the region, specifically northern Sudan. This area lies within the **desert** climatic region, being part of the vast Sahara Desert, characterized by extreme heat and virtually no rainfall.

**Why Other Options Are Incorrect:**
* **A:** Modified equatorial climates are found near the equator but modified by high altitudes (like the Lake Victoria basin).
* **B:** Modified tropical climates are found in highland areas within the tropics (like the Kenyan Highlands).
* **D:** Mountain climates are restricted to specific high-altitude peaks (like Mt. Kenya or Mt. Kilimanjaro).

📌 **Key Learning Note:**
The climate of Eastern Africa varies drastically from arid deserts in the north (Sudan/Eritrea) and Horn of Africa to modified equatorial climates in the central highlands and lake basins.""",

    32: """The correct answer is **A**.

**Analysis of the Correct Answer:**
Route G typically depicts a migration path originating from the Nile Valley / Bahr el Ghazal region in modern-day South Sudan, moving southwards into Uganda and western Kenya. This is the historical migration route of the **Nilotes** (specifically the River-Lake and Plain Nilotes).

**Why Other Options Are Incorrect:**
* **B:** Bantus migrated from the Congo Basin in Central and West Africa, entering East Africa from the west and south.
* **C:** Semites migrated primarily into the Horn of Africa (Ethiopia) from the Arabian Peninsula across the Red Sea.
* **D:** Cushites migrated from the Horn of Africa southward into Kenya and Tanzania.

📌 **Key Learning Note:**
The three major indigenous language groups in East Africa have distinct origins: Bantus (Congo Basin), Nilotes (Nile Valley), and Cushites (Horn of Africa).""",

    33: """The correct answer is **A**.

**Analysis of the Correct Answer:**
Harvesting crops that require storage, such as beans, maize, and wheat, is best done during the **dry** season. Dry weather allows the crops to dry completely in the field before harvesting, which is essential to prevent rotting, fungal infections (like aflatoxin), or premature germination during storage.

**Why Other Options Are Incorrect:**
* **B:** Cold weather slows down the drying process.
* **C:** Extremely windy weather can cause crops to shatter and scatter seeds, leading to yield loss.
* **D:** Rainy weather makes the fields muddy, makes harvesting difficult, and causes harvested crops to rot.

📌 **Key Learning Note:**
Different agricultural activities correspond to different seasons: planting is done just before or during the rainy season, weeding during the rains, and harvesting during the dry season.""",

    34: """The correct answer is **B**.

**Analysis of the Correct Answer:**
A "cultural item" refers to traditional artifacts historically used by indigenous communities. A **calabash** (for storing liquids), **arrows** (for hunting/defense), and **carvings** (for decoration or ritual) are all purely traditional cultural items.

**Why Other Options Are Incorrect:**
* **A:** Sufurias (metal cooking pots) are modern, industrially manufactured utensils.
* **C:** Plates (unless specifically defined as traditional wooden/clay plates, standard plates usually imply modern ceramics/plastics) are modern.
* **D:** A stove (especially a modern jiko or gas stove) is a modern appliance, not a traditional cultural artifact.

📌 **Key Learning Note:**
Cultural heritage items are those that were made and used by ancestors using locally available, natural materials before the introduction of modern industrial goods.""",

    35: """The correct answer is **D**.

**Analysis of the Correct Answer:**
Soil conservation aims to prevent erosion and maintain fertility. **Planting cover crops** (like sweet potatoes or pumpkins) is an excellent method because their broad leaves shield the soil from the impact of raindrops, and their roots bind the soil particles together, preventing wind and water erosion.

**Why Other Options Are Incorrect:**
* **A:** Ploughing repeatedly breaks down the soil structure, making it loose and highly susceptible to erosion.
* **B:** Starting a nature corner is an educational activity but does not directly conserve the soil on a large scale.
* **C:** Excessive use of chemicals (like synthetic fertilizers and pesticides) degrades soil health over time and causes pollution.

📌 **Key Learning Note:**
Effective soil conservation methods include planting cover crops, terracing, contour ploughing, crop rotation, and mulching.""",

    36: """The correct answer is **B**.

**Analysis of the Correct Answer:**
When cheap or heavily subsidized beef products are imported into the country, they compete directly with locally produced beef. Consumers may opt for the cheaper imports, which leads to a **reduced market (demand) for local beef products**, causing financial losses for local beef farmers.

**Why Other Options Are Incorrect:**
* **A:** Increased supply from imports usually *lowers* market prices, not increases them.
* **C:** Importing goods *spends* foreign exchange; exporting goods *earns* foreign exchange.
* **D:** Importing beef increases import trade; it does not reduce it.

📌 **Key Learning Note:**
Excessive importation of agricultural products that can be grown locally undermines local industries, reducing incomes and discouraging local farming.""",

    37: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Mining, especially open-cast mining, involves stripping away the topsoil and vegetation to reach the minerals underneath. This process leaves behind massive open pits, heaps of barren waste rock, and destroyed habitats, which **leads to an ugly, degraded landscape** (environmental degradation).

**Why Other Options Are Incorrect:**
* **A:** While abandoned quarries can sometimes fill with water, they do not create natural, beautiful sceneries; they are artificial scars on the land.
* **B:** Mining destroys agricultural land; it does not create it.
* **D:** Mining clears vegetation entirely; it does not promote the growth of dense forests.

📌 **Key Learning Note:**
The negative environmental impacts of mining include land degradation (ugly landscapes), water pollution, air pollution (dust), and loss of biodiversity.""",

    38: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Every child has a fundamental, constitutional right to basic **education**. By forcing his children to stay at home and work on the farm during official school days, Jamol is actively preventing them from attending school, thus directly violating this specific right.

**Why Other Options Are Incorrect:**
* **A:** The right to movement (freedom of movement) is not the primary right being violated here.
* **B:** While working might reduce playtime, the direct conflict during school hours is with education.
* **D:** While child labor can be an issue of protection, the specific act of missing school days points directly to the denial of education.

📌 **Key Learning Note:**
The Children's Act guarantees every child the right to free and compulsory basic education. Child labor that interferes with schooling is illegal.""",

    39: """The correct answer is **C**.

**Analysis of the Correct Answer:**
**Adjudication** is a formal method of conflict resolution where a dispute is taken to a court of law. A judge or magistrate hears the evidence from both sides and makes a legally binding decision (a judgment) to resolve the conflict. This is the exact process used for election petitions.

**Why Other Options Are Incorrect:**
* **A:** Negotiation involves the two disputing parties talking directly to each other to reach an agreement without outside help.
* **B:** Reconciliation is the process of restoring harmony and friendly relations after a dispute.
* **D:** Arbitration involves a neutral third party (an arbitrator) who listens to both sides and makes a binding decision *outside* of the formal court system.

📌 **Key Learning Note:**
Adjudication is the only conflict resolution method that takes place within the formal judicial (court) system.""",

    40: """The correct answer is **D**.

**Analysis of the Correct Answer:**
The description provided perfectly matches the **Coat of Arms** of Kenya. It is the official logo of the country, featuring two lions (symbolizing protection) holding spears and a shield. It also features Mount Kenya, agricultural crops (representing agricultural wealth), and a cockerel holding an axe (symbolizing a new and prosperous life).

**Why Other Options Are Incorrect:**
* **A:** The National Flag consists of black, red, green, and white stripes with a shield and spears in the center; it does not feature lions or crops.
* **B:** The Public Seal is used to stamp official government documents and features a lion, but not the full arrangement described.
* **C:** The Kenyan shield is just one component *within* the Coat of Arms and the flag, not the entire symbol itself.

📌 **Key Learning Note:**
The Coat of Arms is the official government logo used on all state documents, currency, and government buildings, rich in symbolism about Kenya's heritage and aspirations."""
}

for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

new_content = "export const kpseaSstParta2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 4 completed successfully.")
