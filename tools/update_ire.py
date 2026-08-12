import json

filepath = 'src/data/kpsea-sst-ire-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaSstIre2023 = '
clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

ire_explanations = {
    36: """The correct answer is **Al-Quraish**.

**Detailed Analysis of the Correct Answer:**
**Surah Al-Quraysh** highlights Allah's divine blessings upon the tribe of Quraysh, specifically emphasizing how Allah provided them with food during times of hunger and granted them security from fear (*"Who has fed them, [saving them] from hunger and made them safe, [saving them] from fear"*). Aisha refers to this Surah to encourage people during drought and famine to have hope in Allah as the Provider.

**Why Other Options Are Incorrect:**
* **Al-Kauthar:** Focuses on the abundance of divine blessings granted to the Prophet (p.b.u.h) and the command to pray and sacrifice.
* **Al-Humaza:** Warns against backbiting, slandering, and hoarding wealth.
* **At-Takathur.:** Warns against being distracted by worldly competition and accumulation of material wealth.

📌 **Key Learning Note:**
Surah Al-Quraysh teaches that Allah is the ultimate Provider who feeds the hungry and grants peace in times of hardship.""",

    37: """The correct answer is **i, iii, ii.**.

**Detailed Analysis of the Correct Answer:**
Understanding the correct sequential order of verses in **Surah Al-Qari'ah** is essential for accurate Qur'anic recitation. The opening verses of Surah Al-Qari'ah are:
1. Verse (i): *'Al-Qari'ah'* (The Striking Hour)
2. Verse (iii): *'Mal-Qari'ah'* (What is the Striking Hour?)
3. Verse (ii): *'Wa ma adraka mal-Qari'ah'* (And what will make you know what the Striking Hour is?)

Therefore, the correct sequence is **i, iii, ii.**

**Why Other Options Are Incorrect:**
* **iii, i, ii:** Incorrect because verse (i) *'Al-Qari'ah'* must come first as the title and opening line.
* **iii, ii, i:** Reverses the opening recitational structure of the Surah.
* **i, ii, iii:** Places verse (ii) before verse (iii), breaking the authentic recitational order.

📌 **Key Learning Note:**
Surah Al-Qari'ah opens with: (1) *Al-Qari'ah*, (2) *Mal-Qari'ah*, (3) *Wa ma adraka mal-Qari'ah*.""",

    38: """The correct answer is **Wealth cannot protect a person from Allah's punishment**.

**Detailed Analysis of the Correct Answer:**
**Surah Al-Masad** (Surah Al-Lahab) addresses Abu Lahab and his wife, who vehemently opposed the Prophet (p.b.u.h). Verse 2 explicitly states: *"Ma aghna 'anhu maluhu wa ma kasab"* (**His wealth and his gains will not benefit him**). This teaches that worldly riches cannot shield anyone from Allah's punishment.

**Why Other Options Are Incorrect:**
* **Allah will reward those who perform good deeds:** While true in general Islamic theology, this is not the specific lesson of Surah Al-Masad, which warns against arrogance and disbelief.
* **Muslims should seek protection from Allah:** This is the primary theme of Surah Al-Falaq and Surah An-Nas (*Al-Mu'awwidhatayn*).
* **Muslims should ask for forgiveness from Allah.:** This is the main theme of Surah An-Nasr.

📌 **Key Learning Note:**
Surah Al-Masad teaches that worldly wealth and high social status cannot save anyone from Allah's judgment.""",

    39: """The correct answer is **iii.**.

**Detailed Analysis of the Correct Answer:**
In Islam, environmental stewardship and caring for Allah's creation are highly rewarded acts of charity (*Sadaqah*). Activity **(iii) planting trees** is explicitly mentioned in a Hadith where the Prophet (p.b.u.h) said: *"There is no Muslim who plants a tree or sows a seed, but that a bird, a person, or an animal eats from it, except that it is counted as charity for him."*

**Why Other Options Are Incorrect:**
* **i.:** While cleaning public places is noble, planting trees (iii) is the specific environmental act highlighted as continuous charity (*Sadaqah Jariyah*).
* **ii.:** General compound cleaning is good hygiene (*Taharah*), but tree planting carries ongoing rewards for feeding creation.
* **iv.:** Soil conservation is a farming technique, but tree planting is directly cited in Hadith as charity.

📌 **Key Learning Note:**
Planting trees is considered **Sadaqah Jariyah** (continuous charity) in Islam because its benefits continue as long as living beings use it.""",

    40: """The correct answer is **assisting other learners when they have problems**.

**Detailed Analysis of the Correct Answer:**
Islamic teachings place great emphasis on Islamic brotherhood (*Ukhuwwah*) and mutual assistance. The Prophet (p.b.u.h) said: *"Allah continues to help a servant as long as the servant helps his brother."* **Assisting other learners when they have problems** is a direct practical application of responsible living and brotherhood.

**Why Other Options Are Incorrect:**
* **wearing clean clothes:** Relates to personal hygiene (*Taharah*), not social responsibility toward helping others.
* **following school rules:** Represents general school discipline, but does not capture the Hadith teaching on mutual assistance.
* **sharing what they learned in school with their friends in Madrasa.:** Refers to sharing knowledge, but assisting peers in difficulty best exemplifies responsible social living.

📌 **Key Learning Note:**
Helping others in times of difficulty fulfills the Prophet's command on **Islamic brotherhood and social responsibility**.""",

    41: """The correct answer is **Patience**.

**Detailed Analysis of the Correct Answer:**
The **Ulul-Azm** (Prophets of Strong Will and Determination) are Prophet Nuh, Ibrahim, Musa, Isa, and Muhammad (p.b.u.h). They faced immense trials, persecution, and hardship, enduring them with extraordinary **Patience (Sabr)** and perseverance in fulfilling their divine mission.

**Why Other Options Are Incorrect:**
* **Justice:** A fundamental virtue, but *Sabr* (patience) is the defining characteristic highlighted when enduring hardship.
* **Honesty:** A core virtue (*Sidq*), but overcoming severe trials specifically requires patience.
* **Kindness.:** A noble trait, but enduring suffering and opposition requires deep spiritual patience (*Sabr*).

📌 **Key Learning Note:**
The **Ulul-Azm prophets** are exemplary role models of **Sabr (patience and determination)** during severe trials.""",

    42: """The correct answer is **C**.

**Detailed Analysis of the Correct Answer:**
Iman (Faith) has **6 fundamental pillars** in Islam, which must be believed in the exact traditional order:
1. Belief in Allah
2. Belief in His Angels
3. Belief in His Books
4. Belief in His Messengers
5. Belief in the Last Day (Day of Judgment)
6. Belief in Divine Decree (Qadar)

**Box C** lists these 6 Pillars of Iman in their correct order.

**Why Other Options Are Incorrect:**
* **A:** Contains incorrect ordering or mixes pillars of Islam with pillars of Iman.
* **B:** Omits one of the 6 essential pillars or scrambles the sequence.
* **D:** Includes non-pillar concepts or incorrect traditional order.

📌 **Key Learning Note:**
The **6 Pillars of Iman**: Belief in Allah, His Angels, His Books, His Messengers, the Last Day, and Qadar.""",

    43: """The correct answer is **After isha prayer.**.

**Detailed Analysis of the Correct Answer:**
**Witr prayer** is an emphasized Sunnah prayer (*Sunnah Mu'akkadah*) performed at night. The word *Witr* means "odd number" because it consists of an odd number of rak'ahs (1, 3, or 5). It is performed **after the obligatory Isha prayer** up until the dawn of Fajr.

**Why Other Options Are Incorrect:**
* **Before dhuhr prayer.:** Mid-morning time is for Sunnah prayers like Salatul-Duha, not Witr.
* **Before Asr prayer.:** Sunnah prayers before Asr exist, but Witr is strictly a night prayer.
* **After fajr prayer.:** Prayers are prohibited immediately after Fajr until sunrise, and Witr time ends at Fajr dawn.

📌 **Key Learning Note:**
**Witr prayer** is an odd-numbered Sunnah night prayer performed after Isha before the dawn of Fajr.""",

    44: """The correct answer is **Sheikha - sick, old and traveller**.

**Detailed Analysis of the Correct Answer:**
Fasting during Ramadan (*Saum*) is obligatory for healthy adult Muslims. However, Islam grants exemptions to specific groups of people:
- **The Sick:** Who cannot fast without worsening their health.
- **The Elderly:** Who are too frail to fast.
- **The Traveler:** Who is on a journey and can make up missed days later.

Therefore, **Sheikha's list** is correct.

**Why Other Options Are Incorrect:**
* **Samira - sick, old and blind:** Blindness by itself does not exempt a healthy person from fasting.
* **Maimuna - sick, traveller and blind:** Blindness is not a ground for exemption from fasting.
* **Jamila - sick, traveller and women.:** Women in general are not exempt; only women during specific conditions (menstruation, post-natal, pregnancy, nursing) have temporary concessions.

📌 **Key Learning Note:**
Categories exempted from fasting include **the sick, the elderly, and long-distance travelers**.""",

    45: """The correct answer is **Israf**.

**Detailed Analysis of the Correct Answer:**
**Israf** is an Arabic term meaning extravagance, wastefulness, or excessive consumption beyond necessity. Islam strongly condemns wastefulness in all matters, including using excessive water during ablution (*Wudhu*).

**Why Other Options Are Incorrect:**
* **Tawakkul:** Means putting complete trust and reliance on Allah.
* **Taqwa:** Means God-consciousness, piety, and fear of Allah.
* **Ihsan.:** Means excellence in worship and good deeds.

📌 **Key Learning Note:**
**Israf (wastefulness)** is forbidden in Islam, even when using water for ablution (*Wudhu*).""",

    46: """The correct answer is **A**.

**Detailed Analysis of the Correct Answer:**
In Islam, all **intoxicants (Khamr)**—whether alcoholic drinks, illegal drugs, or mind-altering narcotics—are strictly prohibited (*Haram*). The Prophet (p.b.u.h) declared: *"Whatever intoxicates in large quantities is forbidden even in small quantities."* **Box A** lists items that are exclusively mind-altering intoxicants.

**Why Other Options Are Incorrect:**
* **B:** Includes non-intoxicating everyday beverages alongside intoxicants.
* **C:** Contains halal healthy drinks like fruit juices or milk.
* **D:** Contains non-intoxicating medicinal items or clean food products.

📌 **Key Learning Note:**
All **intoxicants (Khamr)** that impair the mind and intellect are strictly **Haram (forbidden)** in Islam.""",

    47: """The correct answer is **Integrity**.

**Detailed Analysis of the Correct Answer:**
**Integrity (Amanah and Nazaaha)** means being honest, moral, and upholding strong principles even when unobserved. Demanding or accepting bribes (*Rishwa*) is a major sin in Islam that destroys honesty and justice; therefore, Amira lacks **Integrity**.

**Why Other Options Are Incorrect:**
* **Responsibility:** Refers to carrying out tasks, but bribing specifically violates moral honesty and integrity.
* **Love:** Refers to affection; taking bribes stems from greed and dishonesty.
* **Unity.:** Refers to togetherness; extortion through bribery destroys ethical standards.

📌 **Key Learning Note:**
Taking or offering bribes (**Rishwa**) is forbidden and violates the core Islamic value of **Integrity (Amanah)**.""",

    48: """The correct answer is **Protecting them against harm.**.

**Detailed Analysis of the Correct Answer:**
In Islam, parents have sacred obligations toward their children. These include providing halal sustenance, shelter, education, moral guidance, and **protecting them against physical and moral harm**.

**Why Other Options Are Incorrect:**
* **buying them gifts:** Buying gifts is a gesture of affection, but not a mandatory legal duty like safety and protection.
* **playing with them:** Spending joyful time with children is recommended, but protection from harm is a fundamental obligation.
* **doing homework for them:** Parents should support learning, but doing homework for children prevents them from learning independently.

📌 **Key Learning Note:**
Parents have a fundamental Islamic obligation to **protect their children from harm** and provide moral guidance.""",

    49: """The correct answer is **trust in Allah**.

**Detailed Analysis of the Correct Answer:**
When Prophet Muhammad (p.b.u.h) received the first revelation in the Cave of Hira through Angel Jibril (AS), he was shaken by the divine experience. Returning home to his wife Khadijah (RA), his ultimate reliance and faith demonstrated the fundamental importance of **trust in Allah (Tawakkul)** during trials.

**Why Other Options Are Incorrect:**
* **pray to Allah:** Formal ritual prayer (*Salah*) was detailed later during the Isra and Mi'raj.
* **observe fast:** Fasting (*Saum*) was ordained years later in Medina.
* **give zakat.:** Obligatory charity (*Zakat*) was institutionalized later in Medina.

📌 **Key Learning Note:**
The first revelation teaches believers to place complete **trust in Allah (Tawakkul)** during unfamiliar trials.""",

    50: """The correct answer is **unity**.

**Detailed Analysis of the Correct Answer:**
During the *Hijra* (migration from Makkah to Madina), the Muslims of Madina (**Ansar** - the Helpers) welcomed the migrating Muslims (**Muhajirun** - the Emigrants), sharing their homes, wealth, and food. This extraordinary bond of brotherhood (*Muwakhah*) represents the highest level of **Islamic unity** and solidarity.

**Why Other Options Are Incorrect:**
* **peace:** While peaceful, the core action was actively sharing wealth and uniting as one Ummah.
* **integrity:** Refers to personal honesty; the defining feature was communal solidarity and brotherhood.
* **patriotism.:** Refers to love for one's nation; their unity was based on Islamic brotherhood.

📌 **Key Learning Note:**
The brotherhood between the **Ansar and Muhajirun** during the Hijra is the supreme example of **Islamic unity**."""
}

for q in data['sectionA']:
    qn = q['questionNumber']
    if qn in ire_explanations:
        q['explanation'] = ire_explanations[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print("All 15 IRE questions updated successfully in kpsea-sst-ire-2023.js!")
