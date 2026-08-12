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

# Comprehensive answers with exhaustive lists of acceptable options
answers_data = {
    "kjsea-sst-2025-b-21": {
        "modelAnswer": """Acceptable barriers include:
1. **Poor or Ineffective Communication:** Lack of active listening, harsh tone, or refusing to talk openly.
2. **Bias and Favoritism:** Parents or arbiters taking sides, creating mistrust and resentment.
3. **Uncontrolled Anger and Emotional Hostility:** High tempers, verbal abuse, or physical violence during discussions.
4. **Pride, Ego, and Unwillingness to Compromise:** Stubbornness and refusal to forgive or admit fault.
5. **Financial Constraints and Economic Stress:** Poverty or disputes over money creating continuous tension.
6. **Substance Abuse / Alcoholism:** Impaired reasoning and aggressive behavior caused by addiction.
7. **External Interference from Extended Family:** Unsolicited advice or meddling from in-laws and relatives.
8. **Rigid Cultural / Traditional Beliefs:** Harmful traditional practices (e.g. gender bias) that prevent fair resolution.
9. **Lack of Privacy and Confidentiality:** Family secrets being exposed to outsiders, causing humiliation.
10. **Unresolved Past Grievances:** Holding grudges and bringing up historical mistakes during new arguments.""",
        "rubric": "Award 1 mark for each valid barrier outlined (Max 5 marks)."
    },
    "kjsea-sst-2025-b-22": {
        "modelAnswer": """Acceptable ways include:
1. **Showing Mutual Respect and Empathy:** Treating teachers, support staff, and fellow learners with dignity.
2. **Effective and Open Communication:** Expressing thoughts clearly, listening actively, and offering constructive feedback.
3. **Promoting Teamwork and Cooperation:** Working collaboratively in group tasks, sports, and school clubs.
4. **Practicing Forgiveness and Peaceful Conflict Resolution:** Resolving disputes amicably without fighting or bullying.
5. **Demonstrating Honesty and Integrity:** Being truthful and trustworthy in interactions with peers and teachers.
6. **Supporting Peers in Need / Inclusivity:** Helping learners with special needs or academic struggles and avoiding discrimination.
7. **Adhering to School Rules and Regulations:** Following guidelines to maintain order, safety, and mutual trust.
8. **Appreciating and Celebrating Diversity:** Respecting different cultures, religions, and socioeconomic backgrounds.""",
        "rubric": "Award 1 mark for each valid way highlighted (Max 3 marks)."
    },
    "kjsea-sst-2025-b-23": {
        "modelAnswer": """Acceptable decision factors include:
1. **Personal Interests, Passion, and Aspirations:** What she genuinely loves and enjoys doing long-term.
2. **Personal Talent, Abilities, and Academic Strengths:** Her natural performance skills vs language proficiency.
3. **Future Career Opportunities and Employability:** Market demand and job availability in both fields.
4. **Higher Education and Training Requirements:** Availability of accredited colleges/universities offering the courses.
5. **Guidance and Counseling Advice:** Input from career counselors, mentors, and experienced professionals.
6. **Financial Implications and Training Cost:** Tuition fees, equipment, and cost of pursuing the discipline.
7. **Parental and Family Support:** Balancing parental guidance with personal passion through dialogue.
8. **Work-Life Balance and Lifestyle:** Working conditions, travel, and schedule associated with each profession.""",
        "rubric": "Award 1 mark for each valid factor stated (Max 3 marks)."
    },
    "kjsea-sst-2025-b-24": {
        "modelAnswer": """Acceptable preventative measures include:
1. **Child Safety Sensitization (Stranger Danger):** Teaching children not to accept gifts, rides, or walk with strangers.
2. **Enhancing Adult Supervision:** Ensuring young children are accompanied by trusted adults in public spaces.
3. **Community Vigilance / Nyumba Kumi:** Reporting suspicious persons near schools, estates, or playgrounds.
4. **Tightening School Security:** Installing security fences, gates, visitor logs, and CCTV in schools.
5. **Vetting Domestic Workers and Caregivers:** Verifying credentials, IDs, and background checks before hiring.
6. **Prompt Reporting to Police:** Quickly reporting missing children to law enforcement agencies for immediate action.
7. **Use of Identification Tags / Child Tracking Devices:** Equipping children with emergency contact details or GPS trackers.
8. **Public Awareness Campaigns:** Educating communities through media on child trafficking networks and tactics.""",
        "rubric": "Award 1 mark for each valid preventative measure outlined (Max 3 marks)."
    },
    "kjsea-sst-2025-b-25-a-i": {
        "modelAnswer": """Acceptable elected groups include:
1. **Constituency Members of Parliament (MPs):** Representing 290 single-member geographical constituencies.
2. **County Woman Representatives:** 47 female members elected representing each of the 47 counties.""",
        "rubric": "Award 1 mark for each correct group of elected MPs named (Max 2 marks)."
    },
    "kjsea-sst-2025-b-25-a-ii": {
        "modelAnswer": """Acceptable offices elected during first sitting include:
1. **The Speaker of the National Assembly.**
2. **The Deputy Speaker of the National Assembly.**""",
        "rubric": "Award 1 mark for each correct office holder identified (Max 2 marks)."
    },
    "kjsea-sst-2025-b-25-b": {
        "modelAnswer": """Acceptable roles include:
1. **Legislative Role (Lawmaking):** Debating, amending, and enacting national legislation.
2. **Representation Role:** Expressing the views, needs, and grievances of their constituents in Parliament.
3. **Oversight Role:** Monitoring and scrutinizing executive organs, ministries, and public officers for accountability.
4. **Resource Allocation and Budget Approval:** Approving the national budget, revenue division, and CDF funds.
5. **Vetting and Approval of State Appointees:** Approving Cabinet Secretaries, Judges, Ambassadors, and Commissioners.
6. **Determining State of Emergency and War:** Deliberating on declarations of war and state of emergency.""",
        "rubric": "Award 2 marks for each well-explained role (1 mark for identification + 1 mark for explanation) (Max 6 marks)."
    },
    "kjsea-sst-2025-b-26-a": {
        "modelAnswer": """Acceptable social reasons include:
1. **Search for Higher Quality Education:** Accessing prestigious universities and specialized technical training.
2. **Family Reunification:** Joining spouses, parents, or relatives already living abroad.
3. **Escaping Civil Conflicts and Persecution:** Seeking asylum/refugee status due to war, political instability, or discrimination.
4. **Seeking Advanced Healthcare:** Accessing specialized medical treatment not readily available at home.
5. **Desire for Improved Quality of Life:** Enjoying better social amenities, infrastructure, and security.
6. **Cultural and Educational Exchange:** Participating in international cultural, research, or athletic programs.""",
        "rubric": "Award 1 mark for each valid social reason outlined (Max 4 marks)."
    },
    "kjsea-sst-2025-b-26-b": {
        "modelAnswer": """Acceptable economic contributions include:
1. **Financial Remittances:** Sending money to families, supporting education, health, and boosting foreign exchange reserves.
2. **Direct Foreign Investment / Business Ventures:** Investing in real estate, healthcare, agriculture, and tech startups.
3. **Knowledge, Skill, and Technology Transfer:** Bringing home expertise, innovation, and modern business models.
4. **Promoting Tourism and Trade:** Marketing home country products, culture, and tourist destinations abroad.
5. **Philanthropy and Community Projects:** Funding local schools, hospitals, boreholes, and charitable causes.""",
        "rubric": "Award 2 marks for each well-explained economic contribution (1 mark for identification + 1 mark for explanation) (Max 4 marks)."
    },
    "kjsea-sst-2025-b-27": {
        "modelAnswer": """Acceptable ways include:
1. **Eliminated Double Coincidence of Wants:** Removed the difficulty of finding matching trade partners required in barter.
2. **Provided a Standard Unit of Account / Measure of Value:** Allowed accurate pricing of goods and services.
3. **Served as a Convenient Store of Value:** Money can be saved long-term without perishing like crops or livestock.
4. **Enabled Portability and Easy Transport:** Lightweight currency made long-distance trade much easier.
5. **Allowed Divisibility into Smaller Denominations:** Facilitated transactions for small-value everyday items.
6. **Standardized Credit and Deferred Payments:** Allowed merchants to buy goods on credit and settle later.
7. **Encouraged Specialization and Market Expansion:** Allowed traders to focus on specific commercial goods.
8. **Facilitated Cross-Border and International Trade:** Standardized money simplified foreign commercial exchanges.""",
        "rubric": "Award 1 mark for each correct way stated (Max 5 marks)."
    },
    "kjsea-sst-2025-b-28": {
        "modelAnswer": """Acceptable cultural elements include:
1. **Music, Dance, and Performing Arts:** Global popularity of Kenyan Kapuka, Gengetone, Afro-pop, and traditional dances.
2. **Traditional Attire and Fashion:** Worldwide recognition of Maasai Shuka, beadwork, and Leso in global fashion.
3. **Cuisine and Local Foods:** International appreciation of Kenyan coffee, tea, Ugali, and Nyama Choma globally.
4. **Language (Kiswahili):** Adoption of Kiswahili by the African Union, international media (BBC/VOA), and global universities.
5. **Sports and Athletics:** World dominance of Kenyan marathoners promoting Kenya's running culture globally.
6. **Visual Arts and Handicrafts:** Akamba wood carvings, soapstone sculptures, and Kiondo baskets sold globally.
7. **Filmmaking and Literature:** Kenyan stories, wildlife documentaries, and books reaching global audiences.""",
        "rubric": "Award 1 mark for each valid cultural element given (Max 5 marks)."
    },
    "kjsea-sst-2025-b-29": {
        "modelAnswer": """Acceptable national values (Article 10 of Constitution of Kenya) include:
1. **Patriotism:** Devotion and love for one's country.
2. **National Unity:** Uniting all Kenyans regardless of tribe, region, or religion.
3. **Sharing and Devolution of Power:** Distributing power and resources to county levels.
4. **The Rule of Law:** Equality before the law and adherence to legal principles.
5. **Democracy and Participation of the People:** Citizen involvement in governance and decision-making.
6. **Human Dignity:** Protecting every individual's self-worth and fundamental rights.
7. **Equity, Social Justice, and Inclusiveness:** Fair distribution of resources and opportunities for all.
8. **Protection of the Marginalized:** Safeguarding vulnerable groups and minorities.
9. **Integrity, Transparency, and Accountability:** Honesty and openness in public administration.
10. **Sustainable Development:** Utilizing natural resources responsibly for future generations.""",
        "rubric": "Award 1 mark for each correct national value highlighted (Max 5 marks)."
    },
    "kjsea-sst-2025-b-30-a": {
        "modelAnswer": """Acceptable vegetation types identified from map key:
1. **Forest** (located in the North-East near Kon Hill).
2. **Scrub** (located in western and central parts).""",
        "rubric": "Award 1 mark for each correct vegetation type identified (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-b": {
        "modelAnswer": """* **Distance:** **7.5 km** (Accept range **7.0 km – 8.0 km**).
* **Working:** Measured distance along dry-weather road from Kora School to Church is ~7.5 cm. On scale of 1 cm rep 1 km, 7.5 cm = 7.5 km.""",
        "rubric": "Award 2 marks for correct distance within tolerance 7.0 km – 8.0 km (1 mark for working + 1 mark for answer with units) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-c": {
        "modelAnswer": """Acceptable economic activities with map evidence:
1. **Crop Farming / Cash Crop Farming (Coffee Growing):** Evidenced by "CO" (Coffee) symbols.
2. **Livestock Farming / Cattle Rearing:** Evidenced by "Cattle Dip" symbol near Kora Village.
3. **Trading / Commerce:** Evidenced by "Market (Mkt)", "Shops", and "Kapas Town".
4. **Quarrying / Mining:** Evidenced by "Quarry" symbol.
5. **Transport Services:** Evidenced by roads and railway line.
6. **Communication Services:** Evidenced by Post Office ("PO").""",
        "rubric": "Award 1 mark for each valid economic activity identified with map evidence (Max 4 marks)."
    },
    "kjsea-sst-2025-b-30-d": {
        "modelAnswer": """**Road Transport** (Evidenced by network of All-weather and Dry-weather roads).""",
        "rubric": "Award 1 mark for Road Transport (Max 1 mark)."
    },
    "kjsea-sst-2025-b-30-e": {
        "modelAnswer": """**North East (NE)**.""",
        "rubric": "Award 1 mark for North East / NE (Max 1 mark)."
    },
    "kjsea-sst-2025-b-31": {
        "modelAnswer": """Acceptable climate change effects include:
1. **Frequent and Prolonged Droughts:** Causing severe water scarcity and livestock deaths.
2. **Unpredictable Weather and Rainfall Patterns:** Disrupting planting and harvesting schedules.
3. **Flooding and Extreme Weather Events:** Destroying roads, bridges, homes, and schools.
4. **Agricultural Failure and Food Insecurity:** Reducing crop yields and worsening hunger.
5. **Outbreak of Climate-Sensitive Diseases:** Surge in malaria, cholera, and heat-related illnesses.
6. **Displacement of Human Populations (Climate Refugees):** Forcing communities to abandon flooded or arid areas.
7. **Loss of Biodiversity and Wildlife Habitat:** Impacting ecotourism and natural ecosystems.
8. **Rising Sea Levels and Coastal Erosion:** Submerging coastal land, ports, and tourist beaches.
9. **Conflict over Scarce Resources:** Increased clashes between pastoralists and farmers over water and pasture.
10. **Hydro-Electric Power Shortages:** Reduced dam water levels leading to power rationing.""",
        "rubric": "Award 1 mark for each valid effect of climate change stated (Max 8 marks)."
    },
    "kjsea-sst-2025-b-32": {
        "modelAnswer": """Acceptable causes of environmental degradation include:
1. **Deforestation and Illegal Logging:** Cutting down trees without replanting (afforestation).
2. **Improper Waste Disposal and Pollution:** Dumping plastics, garbage, and toxic industrial waste into rivers/land.
3. **Poor Agricultural Practices:** Overgrazing, farming on steep riverbanks/slopes without terracing, overuse of chemicals.
4. **Uncontrolled Mining and Quarrying:** Excavating land leaving open pits and land degradation.
5. **Rapid Urbanization and Population Encroachment:** Encroaching on forests, wetlands, and water catchment areas.
6. **Air Pollution from Vehicles and Factories:** Emitting toxic gases causing acid rain and global warming.
7. **Wetland Reclamation:** Draining swamps and marshes for agriculture or building construction.""",
        "rubric": "Award 1 mark for each valid cause outlined (Max 5 marks)."
    },
    "kjsea-sst-2025-b-33-a": {
        "modelAnswer": """**Desert Climate / Arid Climate** (Region X covers the Sahara Desert in North Africa).""",
        "rubric": "Award 1 mark for Desert / Arid climate (Max 1 mark)."
    },
    "kjsea-sst-2025-b-33-b": {
        "modelAnswer": """Acceptable factors for high population density in region Y (West Africa/Gulf of Guinea) include:
1. **Fertile Volcanic / Alluvial Soils:** Supporting intensive agricultural production.
2. **Reliable High Rainfall and Warm Climate:** Favorable for crop growing and human habitation.
3. **Rich Mineral Deposits (e.g. Petroleum/Oil & Gold):** Attracting industrial development and job seekers.
4. **Growth of Major Commercial Ports and Urban Centers:** Providing trade and employment opportunities.""",
        "rubric": "Award 2 marks for clear explanation (1 mark for identifying fertile soil/rainfall/minerals/urban trade + 1 mark for linking to population settlement) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-33-c": {
        "modelAnswer": """Acceptable economic uses of multi-purpose project Z (Aswan High Dam) include:
1. **Hydro-Electric Power (HEP) Generation:** Supplying electricity for industries and homes.
2. **Irrigation Water Supply:** Providing continuous water for crop farming in Egypt.
3. **Flood Control:** Preventing destructive seasonal flooding of the Nile.
4. **Inland Transport and Ecotourism:** Navigation on Lake Nasser and tourism.""",
        "rubric": "Award 1 mark for each valid economic use stated (Max 2 marks)."
    },
    "kjsea-sst-2025-b-34": {
        "modelAnswer": """Acceptable factors for scramble and partition include:
1. **Industrial Revolution in Europe (Economic Factor):** Urgent need for raw materials (rubber, cotton, minerals) and markets for manufactured goods.
2. **Strategic Interests (Geopolitical Factor):** Controlling vital trade routes like the Suez Canal and major rivers (Nile, Congo).
3. **National Prestige and Imperial Competition (Political Factor):** European nations rivaling to build large empires as a symbol of power.
4. **Humanitarian and Civilizing Mission (Social Factor):** Desire to stop the East African slave trade, spread Christianity, and introduce Western education.
5. **Discovery of Mineral Wealth:** Gold and diamond discoveries in South Africa and copper in Katanga.
6. **Investment of Surplus Capital:** European capitalists seeking high returns on investments in African infrastructure/mines.
7. **Population Pressure in Europe:** Seeking land to settle excess European populations.
8. **The Berlin Conference (1884-1885):** Providing a legal framework for peaceful partition without war between European powers.""",
        "rubric": "Award 1 mark for each valid factor outlined (Max 5 marks)."
    }
}

# Apply updates to sectionB
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

print("Successfully injected expanded, exhaustive Section B model answers and rubrics!")
