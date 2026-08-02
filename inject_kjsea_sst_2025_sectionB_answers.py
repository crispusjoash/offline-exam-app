import json
import re

file_path = 'src/data/kjsea-sst-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const kjseaSst2025 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()
    
data = json.loads(match.group(1))

# Section B answers mapping
answers_data = {
    "kjsea-sst-2025-b-21": {
        "modelAnswer": """1. **Poor or Ineffective Communication:** Inability of family members to listen actively or express feelings openly without hostility.
2. **Bias or Partiality:** Favoritism by parents or arbiters which creates mistrust and resentment among family members.
3. **High Emotional Intensity / Anger / Pride:** Uncontrolled emotions, rigid egos, or unwillingness to compromise and forgive.
4. **Financial Constraints or Poverty:** Economic stress causing ongoing tension and disagreements over resource allocation.
5. **Substance Abuse / Alcoholism:** Impaired judgment and aggressive behavior resulting from drug or alcohol addiction within the home.""",
        "rubric": "Award 1 mark for each relevant barrier to conflict resolution outlined (Max 5 marks)."
    },
    "kjsea-sst-2025-b-22": {
        "modelAnswer": """1. **Showing Mutual Respect and Empathy:** Treating teachers, staff, and fellow learners with dignity regardless of background or differences.
2. **Effective and Open Communication:** Expressing ideas clearly, listening actively to others, and giving constructive feedback.
3. **Promoting Teamwork and Cooperation:** Collaborating peacefully in group work, co-curricular activities, and school projects.""",
        "rubric": "Award 1 mark for each valid way of building healthy relationships highlighted (Max 3 marks)."
    },
    "kjsea-sst-2025-b-23": {
        "modelAnswer": """1. **Personal Interests, Passion, and Career Aspirations:** Evaluating what she truly enjoys and wishes to pursue long-term.
2. **Personal Abilities, Talents, and Academic Performance:** Assessing her natural strengths and academic performance in languages versus performing arts.
3. **Career Opportunities and Market Demand:** Researching future job prospects, higher education requirements, and employability in both fields.""",
        "rubric": "Award 1 mark for each valid decision factor stated (Max 3 marks)."
    },
    "kjsea-sst-2025-b-24": {
        "modelAnswer": """1. **Sensitizing Children on Personal Safety:** Teaching children never to accept gifts, food, or rides from strangers or walk with unfamiliar people.
2. **Enhancing Adult Supervision:** Ensuring young children are accompanied by trusted adults when in public places or commuting to school.
3. **Community Policing and Vigilance (Nyumba Kumi):** Reporting suspicious individuals lurking around schools, playgrounds, or residential areas to authorities.""",
        "rubric": "Award 1 mark for each correct child theft prevention measure outlined (Max 3 marks)."
    },
    "kjsea-sst-2025-b-25-a-i": {
        "modelAnswer": """1. **Members representing single-member constituencies** (Constituency MPs - 290 members).
2. **County Woman Representatives** (47 Woman MPs elected from each county).""",
        "rubric": "Award 1 mark for each correct group of elected MPs named (Max 2 marks)."
    },
    "kjsea-sst-2025-b-25-a-ii": {
        "modelAnswer": """1. **The Speaker of the National Assembly.**
2. **The Deputy Speaker of the National Assembly.**""",
        "rubric": "Award 1 mark for each correct National Assembly office holder identified (Max 2 marks)."
    },
    "kjsea-sst-2025-b-25-b": {
        "modelAnswer": """1. **Legislative Role (Lawmaking):** Deliberating, debating, and passing laws that govern the nation.
2. **Representation Role:** Representing the views, grievances, and development interests of their constituents in Parliament.
3. **Oversight Role:** Monitoring and scrutinizing executive expenditure, public agencies, and state officers to ensure accountability.""",
        "rubric": "Award 2 marks for each well-explained role (1 mark for identification + 1 mark for explanation) (Max 6 marks)."
    },
    "kjsea-sst-2025-b-26-a": {
        "modelAnswer": """1. **Search for Higher Quality Education:** Joining foreign universities and specialized training institutions.
2. **Family Reunification:** Moving to join family members or spouses already residing abroad.
3. **Escaping Civil Unrest or Persecution:** Seeking asylum and refugee status in safer countries due to conflict.
4. **Desire for Improved Healthcare and Living Standards:** Seeking access to advanced medical services and higher quality of life.""",
        "rubric": "Award 1 mark for each valid social reason for migration outlined (Max 4 marks)."
    },
    "kjsea-sst-2025-b-26-b": {
        "modelAnswer": """1. **Financial Remittances:** Sending money back home to families, which supports household livelihoods, education, health, and boosts national foreign exchange reserves.
2. **Direct Foreign Investment / Business Ventures:** Investing in real estate, technology, healthcare, and local enterprises, which creates employment opportunities back home.""",
        "rubric": "Award 2 marks for each well-explained economic contribution (1 mark for identification + 1 mark for explanation) (Max 4 marks)."
    },
    "kjsea-sst-2025-b-27": {
        "modelAnswer": """1. **Eliminated the Problem of Double Coincidence of Wants:** People no longer needed to find someone who had what they wanted and wanted what they had.
2. **Provided a Standard Measure of Value:** Money made it easy to price goods and services accurately and consistently.
3. **Functioned as a Convenient Store of Value:** Money can be saved for future use without deteriorating like agricultural produce or livestock.
4. **Facilitated Long-Distance and International Trade:** Standardized currency made cross-border transactions simpler, faster, and portable.
5. **Allowed Divisibility:** Money could be broken into smaller denominations for purchasing small quantities of goods.""",
        "rubric": "Award 1 mark for each correct way stated (Max 5 marks)."
    },
    "kjsea-sst-2025-b-28": {
        "modelAnswer": """1. **Music and Performing Arts:** Global popularity of Kenyan Kapuka, Afro-pop, and traditional dance troupes internationally.
2. **Traditional Attire and Fashion:** International recognition of Maasai Shuka, beadwork, and Leso in global fashion shows.
3. **Cuisine and Foods:** International appreciation of Kenyan coffee, tea, Ugali, and Nyama Choma in global restaurants.
4. **Language (Kiswahili):** Growth of Kiswahili as an official AU language, taught in international universities, and used in global broadcasting.
5. **Sports and Athletics:** Global dominance of Kenyan long-distance runners promoting Kenya's sporting culture worldwide.""",
        "rubric": "Award 1 mark for each valid cultural element given (Max 5 marks)."
    },
    "kjsea-sst-2025-b-29": {
        "modelAnswer": """1. **Patriotism and National Unity:** Love for one's country and working together as one nation.
2. **Rule of Law:** Adherence to laws and ensuring nobody is above the law.
3. **Democracy and Participation of the People:** Involving citizens in decision-making and governance.
4. **Human Dignity, Equity, and Social Justice:** Treating all persons fairly and upholding fundamental rights.
5. **Integrity, Transparency, and Accountability:** Honesty in public service and taking responsibility for public resources.""",
        "rubric": "Award 1 mark for each correct national value highlighted (Article 10 of Constitution of Kenya) (Max 5 marks)."
    },
    "kjsea-sst-2025-b-30-a": {
        "modelAnswer": """1. **Forest** (located in the North-Eastern part near Kon Hill).
2. **Scrub** (located scattered in the western and central parts of the map).""",
        "rubric": "Award 1 mark for each correct vegetation type identified from the map key (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-b": {
        "modelAnswer": """* **Distance:** **7.5 km** (Accept range between **7.0 km and 8.0 km**).
* **Explanation:** Measuring along the dry-weather road from Kora School eastwards across the bridge to the Church yields approximately 7.5 cm on the map. Based on the scale (1 cm represents 1 km), this equals 7.5 km.""",
        "rubric": "Award 2 marks for correct distance within 7.0 km – 8.0 km (1 mark for measurement/working + 1 mark for correct answer with km units) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-c": {
        "modelAnswer": """1. **Crop Farming / Cash Crop Farming (Coffee Growing):** Evidenced by the "CO" (Coffee) symbols.
2. **Livestock Farming / Cattle Rearing:** Evidenced by the "Cattle Dip" near Kora Village.
3. **Trading / Commerce:** Evidenced by "Market (Mkt)", "Shops", and "Kapas Town".
4. **Quarrying / Mining:** Evidenced by the "Quarry" symbol.""",
        "rubric": "Award 1 mark for each valid economic activity identified with map evidence (Max 4 marks)."
    },
    "kjsea-sst-2025-b-30-d": {
        "modelAnswer": """**Road Transport** (Evidenced by both All-weather road and Dry-weather roads connecting towns, villages, and schools across the map).""",
        "rubric": "Award 1 mark for Road Transport (Max 1 mark)."
    },
    "kjsea-sst-2025-b-30-e": {
        "modelAnswer": """**North East (NE)** (Kon Hill is located to the North East of Kapas School).""",
        "rubric": "Award 1 mark for North East / NE (Max 1 mark)."
    },
    "kjsea-sst-2025-b-31": {
        "modelAnswer": """1. **Frequent and Prolonged Droughts:** Leading to severe water shortages and crop failures.
2. **Unpredictable Weather and Rainfall Patterns:** Disrupting traditional farming schedules and planting seasons.
3. **Flooding and Severe Storms:** Destroying infrastructure, homes, roads, and human settlements.
4. **Loss of Agricultural Productivity / Food Insecurity:** Causing low crop yields and death of livestock.
5. **Outbreak of Climate-Sensitive Diseases:** Increased prevalence of malaria, cholera, and heat stress.
6. **Displacement of Human Settlements (Climate Refugees):** People forced to relocate from flooded or desertified areas.
7. **Loss of Biodiversity and Wildlife Destruction:** Loss of natural flora and fauna impacting ecotourism.
8. **Rising Sea Levels / Coastal Submergence:** Threatening coastal infrastructure, ports, and marine activities.""",
        "rubric": "Award 1 mark for each valid effect of climate change stated (Max 8 marks)."
    },
    "kjsea-sst-2025-b-32": {
        "modelAnswer": """1. **Deforestation and Illegal Logging:** Uncontrolled cutting down of trees without replanting.
2. **Improper Waste Disposal and Pollution:** Dumping plastic waste, domestic garbage, and industrial effluents into land and rivers.
3. **Poor Agricultural Practices:** Overgrazing, farming on steep slopes without terracing, and excessive use of agrochemicals.
4. **Uncontrolled Mining and Quarrying:** Leaving open pits and destroying natural land terrain.
5. **Rapid Urbanization and Population Pressure:** Encroaching on forests, wetlands, and natural habitats for housing.""",
        "rubric": "Award 1 mark for each correct cause of environmental degradation outlined (Max 5 marks)."
    },
    "kjsea-sst-2025-b-33-a": {
        "modelAnswer": """**Mediterranean Climate** (Experienced at the northernmost and southernmost tips of Africa).""",
        "rubric": "Award 1 mark for Mediterranean climate (Max 1 mark)."
    },
    "kjsea-sst-2025-b-33-b": {
        "modelAnswer": """**Presence of River Nile providing fertile silt/soils and permanent water for irrigation in a desert region**, which enables intensive crop farming and supports dense human settlement.""",
        "rubric": "Award 2 marks for clear explanation (1 mark for identifying fertile soils/irrigation water from Nile + 1 mark for linking to human settlement/farming) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-33-c": {
        "modelAnswer": """1. **Generation of Hydro-Electric Power (HEP):** Supplying electricity for domestic and industrial growth.
2. **Provision of Water for Agricultural Irrigation:** Ensuring continuous crop farming regardless of rainfall.""",
        "rubric": "Award 1 mark for each valid economic use stated (Max 2 marks)."
    },
    "kjsea-sst-2025-b-34": {
        "modelAnswer": """1. **Industrial Revolution in Europe (Economic Factor):** High demand for raw materials (rubber, minerals, palm oil) and new markets for finished products.
2. **Strategic Interests (Geopolitical Factor):** Desires to control key trade routes such as the Suez Canal and major rivers like the Nile and Congo.
3. **National Prestige and Imperialism (Political Factor):** European powers competing to acquire vast overseas empires to demonstrate power and dominance.
4. **Humanitarian and Civilizing Mission (Social Factor):** Desire to stop slave trade, spread Christianity, and introduce Western education and medicine.
5. **Discovery of Valuable Minerals:** Discovery of gold and diamonds in South Africa and copper in Katanga.""",
        "rubric": "Award 1 mark for each valid factor for scramble and partition outlined (Max 5 marks)."
    }
}

# Update sectionB items
for item in data["sectionB"]:
    item_id = item["id"]
    if item_id in answers_data:
        item["modelAnswer"] = answers_data[item_id]["modelAnswer"]
        item["rubric"] = answers_data[item_id]["rubric"]
        item["questionType"] = "structured"
    
    if "subQuestions" in item:
        for sub in item["subQuestions"]:
            sub_id = sub["id"]
            if sub_id in answers_data:
                sub["modelAnswer"] = answers_data[sub_id]["modelAnswer"]
                sub["rubric"] = answers_data[sub_id]["rubric"]
                sub["questionType"] = "structured"

js_content = f"export const kjseaSst2025 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully injected all Section B model answers and rubrics!")
