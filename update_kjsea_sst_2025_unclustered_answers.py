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

answers_data = {
    "kjsea-sst-2025-b-21": {
        "modelAnswer": """Here is an exhaustive list of acceptable barriers to conflict resolution in a family:

1. **Poor or Ineffective Communication:** Inability of family members to listen actively, using harsh or abusive language, or shutting down discussions completely, which prevents mutual understanding.

2. **Bias and Favoritism:** Family leaders or elders taking sides with particular individuals, creating deep mistrust, feelings of unfairness, and resentment among family members.

3. **Uncontrolled Anger and Emotional Hostility:** High tempers, aggressive outbursts, or physical threats during discussions, which creates fear and stops constructive dialogue.

4. **Pride, Ego, and Unwillingness to Compromise:** Rigid attitudes, refusal to admit wrongdoings, or unwillingness to forgive, making it impossible to reach an amicable agreement.

5. **Financial Constraints and Economic Stress:** Severe poverty or constant arguments over limited financial resources, which heightens stress and triggers recurring disputes.

6. **Substance Abuse and Alcoholism:** Impaired judgment, erratic behavior, and violence caused by drug or alcohol addiction within the household.

7. **External Interference from Extended Family:** Unsolicited advice, gossip, or meddling by in-laws and relatives, which escalates minor private misunderstandings into major conflicts.

8. **Rigid Cultural or Traditional Beliefs:** Harmful traditional practices or patriarchal biases (e.g. ignoring women's or children's voices) that prevent fair and equitable resolution.

9. **Lack of Privacy and Confidentiality:** Exposing private family matters to neighbors or social media, which causes embarrassment and destroys trust between family members.

10. **Unresolved Past Grievances:** Holding long-term grudges and constantly bringing up historical mistakes during new disagreements, shifting focus away from solving the immediate problem.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid barrier to conflict resolution outlined (Max 5 marks).\n* **Flexibility:** Accept any logically correct phrasing or alternative valid family conflict barrier."
    },
    "kjsea-sst-2025-b-22": {
        "modelAnswer": """Here is an exhaustive list of acceptable ways of building healthy relationships in a school community:

1. **Showing Mutual Respect and Empathy:** Treating teachers, support staff, and fellow learners with dignity, kindness, and understanding regardless of their background or academic abilities.

2. **Effective and Open Communication:** Expressing thoughts and feelings clearly, practicing active listening, and giving constructive, non-judgmental feedback.

3. **Promoting Teamwork and Collaboration:** Working cooperatively in group assignments, school projects, sports teams, and co-curricular clubs to build trust and camaraderie.

4. **Practicing Forgiveness and Amicable Conflict Resolution:** Settling misunderstandings peacefully through dialogue or mediation without resorting to physical fights, insults, or bullying.

5. **Demonstrating Honesty and Integrity:** Being truthful, reliable, and authentic in daily interactions with peers and school authorities to foster strong mutual trust.

6. **Supporting Peers in Need and Promoting Inclusivity:** Assisting classmates who face academic or personal challenges, and ensuring learners with special needs are included in all activities.

7. **Adhering to School Rules and Regulations:** Observing school discipline, punctuality, and guidelines to maintain order, safety, and a conducive learning environment for everyone.

8. **Appreciating and Celebrating Cultural Diversity:** Respecting and celebrating different ethnic, religious, and socioeconomic backgrounds represented within the school community.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid way highlighted (Max 3 marks).\n* **Flexibility:** Accept any valid school relationship-building practice."
    },
    "kjsea-sst-2025-b-23": {
        "modelAnswer": """Here is an exhaustive list of acceptable factors to consider when choosing a career path:

1. **Personal Interests, Passion, and Aspirations:** Evaluating what she genuinely enjoys doing and feels enthusiastic about pursuing as a lifelong career.

2. **Personal Talents, Abilities, and Academic Strengths:** Assessing her natural performance skills, creative flair, and academic performance in languages versus performing arts.

3. **Future Career Opportunities and Market Demand:** Researching job availability, self-employment potential, and long-term career growth in both fields within the evolving job market.

4. **Higher Education and Specialized Training Requirements:** Identifying accredited colleges, universities, or academies offering quality training programs in languages or performing arts.

5. **Guidance and Counseling Recommendations:** Seeking professional advice from school career counselors, mentors, and industry experts to gain objective insights.

6. **Financial Implications and Training Costs:** Considering the tuition fees, specialized equipment, costumes, or instruments required for training in each discipline.

7. **Parental Guidance and Family Dialogue:** Engaging in open, respectful discussions with parents to align expectations while advocating for her personal passion.

8. **Work-Life Balance and Professional Lifestyle:** Understanding the working environments, irregular hours, travel demands, and stability associated with each career path.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid decision factor stated (Max 3 marks).\n* **Flexibility:** Accept any reasonable personal, academic, or market factor."
    },
    "kjsea-sst-2025-b-24": {
        "modelAnswer": """Here is an exhaustive list of acceptable ways of preventing child theft:

1. **Child Safety Sensitization (Stranger Danger):** Educating children never to talk to strangers, accept gifts, sweets, or rides from unfamiliar people, or walk alone in secluded areas.

2. **Enhancing Adult Supervision:** Ensuring young children are constantly accompanied by parent-approved, trusted adults when in public places, parks, or traveling to and from school.

3. **Community Vigilance and Nyumba Kumi Security:** Actively monitoring neighborhoods and reporting suspicious individuals or unregistered vehicles lurking near schools and estates.

4. **Tightening School Security Measures:** Installing perimeter fences, manned security gates, visitor identification logs, and CCTV cameras in school premises.

5. **Strict Vetting of Domestic Staff and Caregivers:** Verifying national IDs, certificates of good conduct, and background references before hiring house-helps or child minders.

6. **Prompt Reporting to Law Enforcement:** Immediately reporting missing children to the police and child protection agencies to initiate immediate search operations.

7. **Use of Child Identification Tags and Tracking Devices:** Equipping children with emergency contact information cards or wearing GPS-enabled smart devices.

8. **Public Awareness Campaigns:** Utilizing broadcast media, social media, and community forums to educate the public on child trafficking networks and tactics.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid preventative measure outlined (Max 3 marks).\n* **Flexibility:** Accept any valid security or child protection measure."
    },
    "kjsea-sst-2025-b-25-a-i": {
        "modelAnswer": """Acceptable groups of elected MPs include:

1. **Constituency Members of Parliament (MPs):** 290 members elected directly by voters to represent single-member geographical constituencies.

2. **County Woman Representatives:** 47 female members elected by voters across each of the 47 counties to promote gender representation.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct group named (Max 2 marks).\n* **Note:** Nominated MPs are nominated, not directly elected."
    },
    "kjsea-sst-2025-b-25-a-ii": {
        "modelAnswer": """Acceptable offices elected during the first sitting include:

1. **The Speaker of the National Assembly:** The presiding officer elected by members during their first sitting to control parliamentary proceedings.

2. **The Deputy Speaker of the National Assembly:** An elected member chosen during the first sitting to preside over sittings in the absence of the Speaker.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct National Assembly office holder identified (Max 2 marks)."
    },
    "kjsea-sst-2025-b-25-b": {
        "modelAnswer": """Here is an exhaustive list of acceptable roles of Members of the National Assembly:

1. **Legislative Role (Lawmaking):** Debating, drafting, amending, and enacting national laws that govern the republic.

2. **Representation Role:** Acting as the voice of their constituents by presenting local grievances, needs, and views on the floor of the House.

3. **Oversight Role:** Scrutinizing executive government expenditure, public agencies, and state officers to ensure transparency, accountability, and good governance.

4. **National Revenue Allocation & CDF Management:** Participating in approving the national budget, division of revenue bills, and managing the Constituency Development Fund (CDF).

5. **Vetting and Approval of State Appointees:** Screening and approving presidential nominees for Cabinet Secretaries, Ambassadors, Judges, and Constitutional Commissioners.

6. **Deliberating on State of Emergency & Declarations of War:** Reviewing and approving executive declarations regarding national security, emergencies, or war.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for each well-explained role (1 mark for identification + 1 mark for explanation) (Max 6 marks)."
    },
    "kjsea-sst-2025-b-26-a": {
        "modelAnswer": """Here is an exhaustive list of acceptable social reasons for migration to the Diaspora:

1. **Search for Higher Quality Education:** Enrolling in prestigious foreign universities, research institutions, and specialized technical colleges abroad.

2. **Family Reunification:** Moving to join spouses, parents, or family members who are already established residents in foreign countries.

3. **Escaping Civil Conflicts, Wars, and Persecution:** Seeking asylum and refugee status in safer nations due to political instability, war, or human rights abuses.

4. **Accessing Advanced Healthcare Services:** Seeking specialized medical treatment, surgeries, or care not readily available in their home countries.

5. **Desire for Improved Quality of Life:** Moving to experience higher living standards, better public infrastructure, and improved social amenities.

6. **Cultural and Sports Exchange Programs:** Traveling abroad to participate in international sports leagues, artistic residencies, or cultural exchange initiatives.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid social reason outlined (Max 4 marks).\n* **Note:** Focus must be on social reasons (not purely economic job search)."
    },
    "kjsea-sst-2025-b-26-b": {
        "modelAnswer": """Here is an exhaustive list of acceptable economic contributions of the Diaspora:

1. **Financial Remittances:** Sending money directly to family members back home, which supports household livelihoods, pays school fees, covers healthcare, and boosts national foreign exchange reserves.

2. **Direct Foreign Investment and Entrepreneurship:** Investing capital in real estate, agribusiness, technology hubs, and local private enterprises, which creates employment opportunities back home.

3. **Knowledge, Skill, and Technology Transfer:** Returning home with advanced technical skills, professional expertise, and modern business management practices to uplift local industries.

4. **Promoting Tourism and Trade:** Marketing their home country's tourist destinations, cultural products, and export goods to international markets.

5. **Philanthropy and Community Development Projects:** Funding the construction of local schools, health clinics, water boreholes, and community infrastructure back home.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for each well-explained economic contribution (1 mark for identification + 1 mark for explanation) (Max 4 marks)."
    },
    "kjsea-sst-2025-b-27": {
        "modelAnswer": """Here is an exhaustive list of acceptable ways the invention of money promoted trade:

1. **Eliminated the Problem of Double Coincidence of Wants:** Removed the major drawback of barter trade where a trader had to find someone who had what they wanted and wanted what they had.

2. **Provided a Standard Measure of Value:** Allowed traders to assign consistent, precise prices to goods and services, making comparison and fair trading simple.

3. **Functioned as a Reliable Store of Value:** Currency could be saved and stored long-term without perishing or losing value, unlike agricultural produce or livestock.

4. **Enabled High Portability and Easy Transport:** Lightweight, compact paper money and coins replaced heavy barter goods, making long-distance trade convenient.

5. **Allowed Divisibility into Smaller Denominations:** Enabled transactions of all sizes, allowing buyers to purchase small everyday items without needing large trade items.

6. **Standardized Credit and Deferred Payments:** Allowed merchants to buy goods on credit and settle debts later using a universally accepted medium.

7. **Encouraged Commercial Specialization:** Enabled individuals and communities to specialize in producing specific goods they were best at, relying on money to buy other necessities.

8. **Facilitated Cross-Border and International Trade:** Standardized currencies enabled seamless commercial exchanges between different African kingdoms and foreign traders.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid way stated (Max 5 marks)."
    },
    "kjsea-sst-2025-b-28": {
        "modelAnswer": """Here is an exhaustive list of acceptable elements of cultural globalization:

1. **Music, Dance, and Performing Arts:** Global popularity and streaming of Kenyan Gengetone, Kapuka, Afro-pop, and traditional folk dance performances internationally.

2. **Traditional Attire and Fashion:** International adoption and showcase of the Maasai Shuka, traditional beadwork, and Leso in global high-fashion runways and design.

3. **Cuisine and Local Foods:** Worldwide appreciation and commercialization of Kenyan specialty coffee, premium tea, Ugali, and Nyama Choma in global dining establishments.

4. **Language (Kiswahili):** Growth of Kiswahili into an official working language of the African Union (AU), taught in major global universities, and broadcast on international networks like BBC and VOA.

5. **Sports and Long-Distance Athletics:** Global dominance of Kenyan marathoners and track athletes, making Kenya's running culture famous worldwide.

6. **Visual Arts and Wood Carvings:** Worldwide export and exhibition of Akamba wood carvings, Kisii soapstone sculptures, and woven Kiondo baskets.

7. **Filmmaking, Wildlife Documentaries, and Literature:** Global dissemination of Kenyan wildlife conservation stories, films, and literary works by renowned authors.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid cultural element given (Max 5 marks)."
    },
    "kjsea-sst-2025-b-29": {
        "modelAnswer": """Here is an exhaustive list of acceptable National Values (Article 10 of Constitution of Kenya):

1. **Patriotism:** Demonstrating genuine love, loyalty, devotion, and defense for one's country.

2. **National Unity:** Uniting all Kenyans into one cohesive nation regardless of ethnic, religious, or regional backgrounds.

3. **Sharing and Devolution of Power:** Distributing governance responsibilities and resources from the national government to the 47 county governments.

4. **The Rule of Law:** Ensuring that all individuals, institutions, and government bodies are equal before the law and bound by legal statutes.

5. **Democracy and Participation of the People:** Involving citizens actively in decision-making, policy formulation, and governance processes.

6. **Human Dignity:** Recognizing, respecting, and protecting the inherent self-worth and basic human rights of every person.

7. **Equity, Social Justice, and Inclusiveness:** Ensuring fair treatment, equal opportunities, and non-discrimination for all members of society.

8. **Protection of the Marginalized:** Safeguarding vulnerable groups, minorities, women, youth, and persons with disabilities.

9. **Integrity, Transparency, and Accountability:** Upholding high ethical standards, honesty, openness, and responsibility in public service administration.

10. **Sustainable Development:** Managing and utilizing national resources prudently to meet present needs without compromising future generations.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct national value highlighted (Max 5 marks)."
    },
    "kjsea-sst-2025-b-30-a": {
        "modelAnswer": """Acceptable vegetation types identified from the Kapas Area map key:

1. **Forest Vegetation:** Located in the North-Eastern quadrant around Kon Hill, characterized by tall trees.

2. **Scrub Vegetation:** Located across the western and central areas, characterized by stunted bushes and thorny vegetation.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct vegetation type identified from map key (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-b": {
        "modelAnswer": """* **Distance:** **7.5 km** (Acceptable range between **7.0 km and 8.0 km**).

* **Calculation:** Measuring along the dry-weather road from Kora School eastwards across the river bridge to the Church yields approximately 7.5 cm on the map. Using the scale (1 cm represents 1 km), 7.5 cm × 1 km/cm = 7.5 km.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for correct distance within tolerance 7.0 km – 8.0 km (1 mark for measurement/working + 1 mark for correct value with km unit) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-30-c": {
        "modelAnswer": """Here is an exhaustive list of acceptable economic activities evidenced by the map:

1. **Crop Farming / Cash Crop Farming (Coffee Growing):** Evidenced by the "CO" (Coffee) symbols on the eastern side.

2. **Livestock Rearing / Pastoralism:** Evidenced by the "Cattle Dip" facility near Kora Village.

3. **Trading and Commerce:** Evidenced by the presence of "Market (Mkt)", "Shops", and "Kapas Town".

4. **Quarrying / Mining:** Evidenced by the "Quarry" symbol on the western side.

5. **Transport Services:** Evidenced by the network of All-weather roads, Dry-weather roads, and Railway line.

6. **Communication Services:** Evidenced by the "Post Office (PO)" in Kapas Town.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid economic activity identified with map evidence (Max 4 marks)."
    },
    "kjsea-sst-2025-b-30-d": {
        "modelAnswer": """**Road Transport:** Evidenced by the extensive network of All-weather and Dry-weather roads connecting settlements across the area.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for Road Transport (Max 1 mark)."
    },
    "kjsea-sst-2025-b-30-e": {
        "modelAnswer": """**North East (NE):** Kon Hill is situated in the North-Eastern direction when measured from Kapas School.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for North East / NE (Max 1 mark)."
    },
    "kjsea-sst-2025-b-31": {
        "modelAnswer": """Here is an exhaustive list of acceptable effects of climate change:

1. **Frequent and Prolonged Droughts:** Causing acute water scarcity, drying of rivers, and loss of livestock in pastoralist communities.

2. **Unpredictable Weather and Rainfall Patterns:** Disrupting traditional farming calendars, planting schedules, and harvesting seasons.

3. **Severe Flooding and Extreme Weather Events:** Destroying transport infrastructure, bridges, schools, residential homes, and washing away crops.

4. **Agricultural Failure and Widespread Food Insecurity:** Causing significant decline in crop yields and leading to famine and malnutrition.

5. **Outbreak of Climate-Sensitive Diseases:** Surge in vector-borne diseases like malaria and water-borne illnesses like cholera due to flooding and rising temperatures.

6. **Displacement of Human Populations (Climate Refugees):** Forcing communities living in low-lying coastal areas or desertified lands to abandon their homes.

7. **Loss of Biodiversity and Wildlife Destruction:** Habitat destruction reducing wildlife populations, which severely hampers ecotourism.

8. **Rising Sea Levels and Coastal Inundation:** Submerging coastal agricultural land, port infrastructure, beaches, and coastal settlements.

9. **Increased Resource Conflicts:** Triggering inter-community clashes between farmers and pastoralists competing over shrinking water sources and pasture.

10. **Hydro-Electric Power (HEP) Rationing:** Dropping water levels in major dams leading to electricity shortages, factory downtime, and economic decline.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid effect of climate change stated (Max 8 marks)."
    },
    "kjsea-sst-2025-b-32": {
        "modelAnswer": """Here is an exhaustive list of acceptable causes of environmental degradation:

1. **Deforestation and Illegal Logging:** Uncontrolled felling of trees for timber, charcoal, and firewood without carrying out afforestation.

2. **Improper Waste Disposal and Industrial Pollution:** Indiscriminate dumping of non-biodegradable plastic waste, untreated sewage, and industrial chemicals into land and rivers.

3. **Poor Agricultural Practices:** Overgrazing by livestock, cultivating on steep hillsides without terracing, and excessive use of synthetic fertilizers and pesticides.

4. **Uncontrolled Mining and Quarrying:** Excavating topsoil and rocks without backfilling, leaving dangerous open pits and degraded landscapes.

5. **Rapid Urbanization and Population Encroachment:** Clearing natural forests, wetlands, and water catchment towers to build housing estates and roads.

6. **Air Pollution from Vehicles and Factories:** Emitting greenhouse gases and toxic fumes that cause atmospheric degradation and acid rain.

7. **Wetland Reclamation:** Draining swamps, marshes, and riparian zones for crop farming or commercial construction.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid cause outlined (Max 5 marks)."
    },
    "kjsea-sst-2025-b-33-a": {
        "modelAnswer": """**Desert Climate / Arid Climate:** Region X covers the vast Sahara Desert region in North Africa, characterized by extreme heat and low rainfall.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for Desert / Arid climate (Max 1 mark)."
    },
    "kjsea-sst-2025-b-33-b": {
        "modelAnswer": """Here is an exhaustive list of acceptable factors for high population density in region Y (West Africa/Gulf of Guinea):

1. **Fertile Volcanic and Alluvial Soils:** Supporting intensive crop production and food supply along the West African coastal belt.

2. **Reliable High Annual Rainfall and Warm Climate:** Creating favorable natural conditions for human habitation and farming.

3. **Rich Mineral Wealth (e.g. Petroleum/Oil & Gold):** Attracting major industrial investments, mining operations, and job opportunities.

4. **Growth of Major Commercial Ports and Urban Centers:** Facilitating historic trade, commerce, and high urban settlement.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 2 marks for clear explanation (1 mark for identifying fertile soil/rainfall/minerals/urban trade + 1 mark for linking to population settlement) (Max 2 marks)."
    },
    "kjsea-sst-2025-b-33-c": {
        "modelAnswer": """Here is an exhaustive list of acceptable economic uses of multi-purpose project Z (Aswan High Dam):

1. **Generation of Hydro-Electric Power (HEP):** Supplying abundant electricity for domestic lighting and industrial manufacturing.

2. **Provision of Water for Agricultural Irrigation:** Enabling year-round crop farming along the Nile valley regardless of rainfall.

3. **Control of Seasonal Flooding:** Regulating the annual flooding of the River Nile to protect agricultural land and human settlements.

4. **Promotion of Inland Water Transport and Ecotourism:** Facilitating navigation and fishing activities on Lake Nasser.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid economic use stated (Max 2 marks)."
    },
    "kjsea-sst-2025-b-34": {
        "modelAnswer": """Here is an exhaustive list of acceptable factors for the scramble and partition of Africa:

1. **Industrial Revolution in Europe (Economic Factor):** Urgent demand for cheap raw materials (rubber, cotton, minerals, palm oil) and markets for European manufactured goods.

2. **Strategic Interests (Geopolitical Factor):** Desires to secure vital maritime trade routes such as the Suez Canal and major navigable rivers (Nile, Congo, Niger).

3. **National Prestige and Imperial Rivalry (Political Factor):** European powers (Britain, France, Germany) competing to acquire vast overseas territories to demonstrate global power.

4. **Humanitarian and Civilizing Mission (Social Factor):** Intentions to eradicate the East African slave trade, introduce Western education, medicine, and spread Christianity.

5. **Discovery of Mineral Wealth:** Discovery of gold and diamonds in South Africa and rich copper deposits in Katanga.

6. **Investment of Surplus Capital:** European financiers seeking high returns by investing excess profits in African infrastructure, railways, and mines.

7. **Population Pressure in Europe:** Seeking overseas territories to settle surplus European populations resulting from rapid demographic growth.

8. **The Berlin Conference (1884-1885):** Providing a legal framework for peaceful territorial division among European powers without going to war.""",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid factor outlined (Max 5 marks)."
    }
}

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

print("Successfully injected unclustered, beautifully formatted, exhaustive model answers and rubrics!")
