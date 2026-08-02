import json
import re

file_path = 'src/data/kjsea-sst-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the JSON object
match = re.search(r'export const kjseaSst2025 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()
    
data = json.loads(match.group(1))

explanations = {
    1: """The correct answer is **law**.

**Analysis of the Correct Answer:**
Social Studies involves the study of human society, civics, history, governance, and human rights. This subject directly lays the foundation for a career in **law**, where lawyers, advocates, and judges deal with laws and the justice system.

**Why Other Options Are Incorrect:**
* **sports instructor:** This career is associated with Physical Education and Sports Science.
* **surgeon:** This is a medical career associated with STEM (Science, Technology, Engineering, and Mathematics).
* **music producer:** This career is associated with Creative Arts.

📌 **Key Learning Note:**
Social Studies prepares learners for careers like teaching, law, urban planning, administration, and social work.""",

    2: """The correct answer is **Arts and Sports Science**.

**Analysis of the Correct Answer:**
Under the CBC (Competency Based Curriculum) senior school pathways, a learner pursuing a career as a musician would choose the **Arts and Sports Science** pathway. This pathway is designed to nurture creative talents, physical education, performing arts (like music and drama), and visual arts.

**Why Other Options Are Incorrect:**
* **STEM:** Focuses on Science, Technology, Engineering, and Mathematics.
* **Social Sciences:** Focuses on humanities, languages, and social studies.
* **Languages:** Focuses purely on linguistics, literature, and communication.

📌 **Key Learning Note:**
Senior school in CBC offers three main pathways: STEM, Social Sciences, and Arts and Sports Science.""",

    3: """The correct answer is **existence of plateaus**.

**Analysis of the Correct Answer:**
The theory that Africa is the cradle (origin) of humankind is supported by strong archaeological and geographical evidence. However, the **existence of plateaus** (which are simply raised, flat physical features) is a purely geographical aspect and does not act as archaeological proof of early human origins. 

**Why Other Options Are Incorrect:**
* **existence of pre-historic sites:** Sites like Olduvai Gorge provide proof of early human settlements.
* **oldest fossils:** The discovery of the oldest hominid fossils in Africa strongly supports the theory.
* **favourable climate:** A historically warm and favourable climate provided a conducive environment for early human survival and evolution.

📌 **Key Learning Note:**
Archaeological evidence (fossils and tools) found in East Africa makes it the most widely accepted "Cradle of Humankind." """,

    4: """The correct answer is **Topographical map.**.

**Analysis of the Correct Answer:**
A **topographical map** is a highly detailed map that shows both natural physical features (like mountains, rivers, valleys using contours) and human-made features (such as settlements, roads, and farming activities).

**Why Other Options Are Incorrect:**
* **Thematic map:** Focuses on a single specific theme or topic (e.g., only rainfall or only population density).
* **Political map:** Shows governmental boundaries of countries, counties, or states.
* **Climatic map:** Shows weather patterns and climate zones over a period.

📌 **Key Learning Note:**
Topographical maps are essential for land use planning and navigation because they provide a complete picture of the terrain and human activities on it.""",

    5: """The correct answer is **Traditional mode of dressing.**.

**Analysis of the Correct Answer:**
Kenyan culture has significantly contributed to the international community through its unique cultural heritage. The **traditional mode of dressing**, such as the iconic Maasai shuka and intricate beadwork, is recognized globally and represents Kenya's rich cultural identity in international fashion and art.

**Why Other Options Are Incorrect:**
* **Agricultural experts, Global financial system, Exchange programmes:** While Kenya participates in these areas, they are considered economic, educational, or professional contributions rather than purely "cultural" contributions.

📌 **Key Learning Note:**
Culture includes dressing, food, language, music, and traditions. Sharing these with the world promotes international understanding and tourism.""",

    6: """The correct answer is **arbitration**.

**Analysis of the Correct Answer:**
When neighbors have a dispute, the best way to restore a *good relationship* is through peaceful conflict resolution. **Arbitration** (and mediation) involves a neutral third party helping the neighbors reach an amicable and fair solution without destroying their social bond.

**Why Other Options Are Incorrect:**
* **forgiveness:** While noble, forgiveness alone without addressing the destroyed crops may not solve the underlying grievance fairly.
* **compensation:** While compensation is usually part of the final agreement, arbitration is the *process* through which they agree on it peacefully.
* **litigation:** Going to court (litigation) is adversarial, expensive, and often creates permanent enmity between neighbors.

📌 **Key Learning Note:**
Peaceful conflict resolution methods (negotiation, mediation, arbitration) are always preferred over litigation to maintain community harmony.""",

    7: """The correct answer is **availability of water**.

**Analysis of the Correct Answer:**
The **availability of water** from the River Nile was the most critical factor that facilitated the development of agriculture in ancient Egypt. The Nile provided a constant supply of water for irrigation in an otherwise harsh desert environment.

**Why Other Options Are Incorrect:**
* **availability of skilled farmers:** While important, farmers could not grow crops without water.
* **invention of shadoof:** The shadoof was an irrigation tool invented *because* the water was available, it was a secondary factor.
* **existence of trade:** Trade developed as a result of surplus agricultural production, not the cause of it.

📌 **Key Learning Note:**
Ancient Egypt is often called the "Gift of the Nile" because its entire agricultural civilization depended on the river's water and fertile silt.""",

    8: """The correct answer is **Keeping to oneself.**.

**Analysis of the Correct Answer:**
Self-esteem is how much you value, respect, and feel confident about yourself. **Keeping to oneself** (isolation) often denies a person the social interaction, feedback, and positive reinforcement needed to build a healthy self-esteem.

**Why Other Options Are Incorrect:**
* **Accomplishing personal goals, Positive self image, Academic achievements:** These all provide a sense of capability and success, which directly boost and promote high self-esteem.

📌 **Key Learning Note:**
Healthy self-esteem is built through positive social interactions, achieving goals, and self-acceptance. Extreme isolation can lead to low self-esteem.""",

    9: """The correct answer is **understanding the problems facing the community.**.

**Analysis of the Correct Answer:**
Community Service Learning (CSL) is a core component of the CBC curriculum designed to help learners apply classroom knowledge to real-life situations. By participating, learners benefit by gaining a deeper **understanding of the actual problems facing their community**, which fosters empathy, civic responsibility, and problem-solving skills.

**Why Other Options Are Incorrect:**
* **devoting their time:** This is what they *do*, not necessarily the educational *benefit* they gain.
* **making the community know what they can do:** CSL is not about showing off, but about learning and serving.
* **encouraging themselves to work hard:** This is a general benefit, but understanding the community is the specific primary goal of CSL.

📌 **Key Learning Note:**
CSL bridges the gap between theoretical classroom learning and practical community problem-solving.""",

    10: """The correct answer is **population growth rate**.

**Analysis of the Correct Answer:**
Pre-historic sites provide physical archaeological evidence of how early humans lived. However, specific demographic statistics like the **population growth rate** cannot be determined from archaeological digs because there were no written census records or mathematical data from that era.

**Why Other Options Are Incorrect:**
* **shelter they used:** Archaeologists can find remnants of caves or early huts.
* **clothes they wore:** Evidence of animal skins or bone needles can indicate their clothing.
* **tools they used:** Stone tools and weapons are the most common artifacts found at these sites.

📌 **Key Learning Note:**
Archaeology relies on physical artifacts (material culture) to reconstruct history. Abstract statistics require written records, which pre-historic societies did not have.""",

    11: """The correct answer is **rural to urban migration**.

**Analysis of the Correct Answer:**
Migration is the movement of people from one place to another. Shem moved from a dairy co-operative in a **rural area** to settle permanently in Nairobi, which is a major city (**urban area**). This is a classic example of **rural to urban migration**.

**Why Other Options Are Incorrect:**
* **urban to urban migration:** Moving from one city to another (e.g., Mombasa to Nairobi).
* **urban to rural migration:** Moving from a city to a village.
* **rural to rural migration:** Moving from one village to another village (e.g., looking for better farming land).

📌 **Key Learning Note:**
Rural to urban migration is often driven by "pull factors" like the search for better employment, education, and healthcare facilities in cities.""",

    12: """The correct answer is **measure distances**.

**Analysis of the Correct Answer:**
On a map, a scale represents the ratio between the distance on the map and the actual distance on the ground. Therefore, the primary use of a scale is to help map readers **measure actual distances** between two places.

**Why Other Options Are Incorrect:**
* **give directions:** This is done using a compass rose (North, South, East, West).
* **determine physical features:** This is done using the map's key or legend, which explains the symbols used.
* **locate places:** This is done using latitudes and longitudes, or grid references.

📌 **Key Learning Note:**
A map scale can be represented in three ways: as a statement (e.g., 1cm represents 1km), as a representative fraction (e.g., 1:100,000), or as a linear/graphic scale.""",

    13: """The correct answer is **rainforest.**.

**Analysis of the Correct Answer:**
The diagram illustrates mountain vegetation zones, which change as altitude increases. 
* **E (Base):** Savannah grassland
* **D (Lower slopes):** Rainforest (Dense equatorial forest due to heavy relief rainfall)
* **C (Middle slopes):** Bamboo forest
* **B (Upper slopes):** Heath and Moorland
* **A (Peak):** Bare rock, snow, and ice

Therefore, region **D** represents the **rainforest**.

**Why Other Options Are Incorrect:**
* **heath and moorland:** This is found much higher up (Zone B).
* **bamboo:** This is found just above the rainforest (Zone C).
* **savannah:** This is found at the lowest altitude at the base (Zone E).

📌 **Key Learning Note:**
Mountain vegetation is primarily determined by altitude (temperature drops as you go higher) and rainfall.""",

    14: """The correct answer is **Deforestation.**.

**Analysis of the Correct Answer:**
**Deforestation** (the cutting down of trees) directly and negatively influences weather and climate. Trees release moisture into the atmosphere through transpiration; removing them leads to lower rainfall, drier conditions, and contributes to global warming by increasing carbon dioxide levels in the air.

**Why Other Options Are Incorrect:**
* **Cultivation of crops, Road construction, Trade:** While these are human activities, they do not have as massive or direct an impact on altering local weather patterns and global climate as large-scale deforestation does.

📌 **Key Learning Note:**
Afforestation (planting trees) and re-afforestation help stabilize the climate, attract rainfall, and prevent soil erosion.""",

    15: """The correct answer is **disciplining**.

**Analysis of the Correct Answer:**
Appropriate and reasonable **disciplining** by parents or teachers to correct a child's behavior is a normal part of upbringing and is *not* considered an abuse or violation of rights. 

**Why Other Options Are Incorrect:**
* **sexual abuse, child trafficking, child labour:** These are all severe, illegal violations of a child's fundamental human rights that cause deep physical and psychological harm. 

📌 **Key Learning Note:**
While disciplining is allowed, it must not cross the line into physical abuse (like severe caning) or emotional abuse. The Children's Act protects children from harmful practices.""",

    16: """The correct answer is **Prevention of drought.**.

**Analysis of the Correct Answer:**
While the Aswan High Dam stores water that helps mitigate the *effects* of a dry season, humans cannot actually **prevent a meteorological drought** (which is a natural phenomenon caused by a lack of rainfall in the atmosphere). The dam simply manages the water reserves.

**Why Other Options Are Incorrect:**
* **Generation of electricity:** The dam generates massive amounts of Hydroelectric Power (HEP) for Egypt.
* **Controlling of floods:** It controls the annual destructive flooding of the River Nile.
* **Provision of water for irrigation:** It provides a steady year-round supply of water for agriculture.

📌 **Key Learning Note:**
Multi-purpose river projects (like the Aswan High Dam or Seven Forks in Kenya) are built primarily for HEP generation, flood control, and irrigation.""",

    17: """The correct answer is **Invention of fire.**.

**Analysis of the Correct Answer:**
The **invention of fire** (or discovering how to make and control it) is considered the greatest milestone of the Middle Stone Age. Fire fundamentally changed human evolution: it provided warmth, protection against wild animals, a way to cook food (which improved brain development), and light at night.

**Why Other Options Are Incorrect:**
* **Development of agriculture:** This occurred much later, during the New Stone Age (Neolithic period).
* **Development of rock shelters:** Early humans used natural rock shelters long before the Middle Stone Age.
* **Development of composite tools:** While tool-making improved, fire was the most revolutionary "greatest" development.

📌 **Key Learning Note:**
The control of fire allowed early humans to migrate into colder climates out of Africa.""",

    18: """The correct answer is **school enrolment**.

**Analysis of the Correct Answer:**
Primary sources of national demographic population data include the national census, vital registration systems, and statistical abstracts. **School enrolment** only provides specific data on the number of students attending school, not the comprehensive demographics of the entire national population.

**Why Other Options Are Incorrect:**
* **census:** The official, periodic counting of a country's entire population (done every 10 years in Kenya).
* **registration of births and deaths:** Also known as vital registration, it provides continuous population data.
* **statistical abstracts:** Publications by the government containing compiled demographic and economic data.

📌 **Key Learning Note:**
Population data is crucial for the government to plan for resources like schools, hospitals, housing, and infrastructure.""",

    19: """The correct answer is **Nebula Cloud Theory**.

**Analysis of the Correct Answer:**
The **Nebula Cloud Theory** (or Nebular Hypothesis) is a scientific theory explaining the origin of the Solar System. It suggests that the sun and planets formed from a giant, rotating cloud of gas and dust (a nebula) that collapsed under its own gravity.

**Why Other Options Are Incorrect:**
* **Continental Drift Theory:** Explains how the Earth's continents were once one supercontinent (Pangaea) and drifted apart.
* **The Big Bang Theory:** Explains the origin of the *entire universe*, not just our solar system.
* **Plate Tectonic Theory:** Explains the movement of the Earth's solid outer crust (lithosphere).

📌 **Key Learning Note:**
The Nebula Cloud Theory focuses specifically on the formation of the sun and the planets orbiting it.""",

    20: """The correct answer is **participating in a community project**.

**Analysis of the Correct Answer:**
The constitution-making process is a formal, legal, and political process. While **participating in a community project** (like planting trees or cleaning) is a good civic duty and shows active citizenship, it is *not* legally part of the process of making or reviewing a national constitution.

**Why Other Options Are Incorrect:**
* **voting in a referendum:** Citizens vote 'Yes' or 'No' to accept or reject the draft constitution.
* **giving their opinions:** Citizens present memoranda and views to the constitutional review commission.
* **engaging in civic education:** Citizens learn about the contents of the draft constitution before voting.

📌 **Key Learning Note:**
Public participation is a core requirement in Kenya's constitution-making process, ensuring the final document reflects the will of the people."""
}

for q in data["sectionA"]:
    q_num = q["questionNumber"]
    if q_num in explanations:
        q["explanation"] = explanations[q_num]

js_content = f"export const kjseaSst2025 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully injected rich explanations for KJSEA Social Studies 2025 Section A.")
