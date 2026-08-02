import json

explanations_map = {
    36: """📘 **Study Note & Concept Overview:**
Surah Al-Quraysh highlights Allah's divine blessings upon the tribe of Quraysh, specifically emphasizing how Allah provided them with food against hunger and granted them security and safety from fear. It teaches reliance on Allah during times of hardship, drought, or famine.

✅ **Correct Answer Breakdown:**
**Al-Quraish** is correct because this Surah specifically reminds believers that Allah feeds people during hunger and protects them from fear, giving hope to those suffering from famine.

❌ **Why Other Options Are Incorrect:**
* **Al-Kauthar:** Focuses on the abundance of blessings granted to the Prophet (p.b.u.h) and the command to pray and sacrifice.
* **Al-Humaza:** Warns against backbiting, slandering, and hoarding wealth.
* **At-Takathur:** Warns against being distracted by worldly competition and accumulation of wealth.

💡 **Key Takeaway for Revision:** Surah Al-Quraysh teaches that Allah is the provider who feeds the hungry and grants peace in times of hardship.""",

    37: """📘 **Study Note & Concept Overview:**
Surah Al-Qari'ah describes the events of the Day of Judgment (The Striking Hour). Understanding the correct sequential order of its verses is essential for reciting and studying the Qur'an accurately.

✅ **Correct Answer Breakdown:**
**i, iii, ii** is the correct order because verse (i) *'Al-Qari'ah'*, followed by verse (iii) *'Mal-Qari'ah'*, and then verse (ii) *'Wa ma adraka mal-Qari'ah'* follow the exact revelation sequence of Surah Al-Qari'ah.

❌ **Why Other Options Are Incorrect:**
* **iii, i, ii:** Incorrect because verse (i) must come first as the title and opening line of the Surah.
* **iii, ii, i:** Reverses the opening structure of the Surah completely.
* **i, ii, iii:** Places the third verse before the second verse, breaking the correct recitational order.

💡 **Key Takeaway for Revision:** Surah Al-Qari'ah opens with: (1) Al-Qari'ah, (2) Mal-Qari'ah, (3) Wa ma adraka mal-Qari'ah.""",

    38: """📘 **Study Note & Concept Overview:**
Surah Al-Masad (also known as Surah Al-Lahab) addresses Abu Lahab and his wife, who opposed the Prophet (p.b.u.h). Verse 2 explicitly states: *"Ma aghna 'anhu maluhu wa ma kasab"* (His wealth and his gains will not benefit him).

✅ **Correct Answer Breakdown:**
**Wealth cannot protect a person from Allah's punishment** is correct because Abu Lahab was very wealthy, yet his riches could not save him from divine punishment due to his disbelief and wickedness.

❌ **Why Other Options Are Incorrect:**
* **Allah will reward those who perform good deeds:** While true in Islam, this is not the central lesson of Surah Al-Masad, which warns against arrogance and disbelief.
* **Muslims should seek protection from Allah:** This is the main theme of Surah Al-Falaq and Surah An-Nas (Al-Mu'awwidhatayn).
* **Muslims should ask for forgiveness from Allah:** This is the main focus of Surah An-Nasr.

💡 **Key Takeaway for Revision:** Surah Al-Masad teaches that worldly wealth and high social status cannot save anyone from Allah's punishment.""",

    39: """📘 **Study Note & Concept Overview:**
Islamic teachings emphasize cleanliness and environmental care (*Taharah* and environmental stewardship). Participating in activities like tree planting, clearing garbage, and maintaining clean surroundings reflects Islamic values of caring for Allah's creation.

✅ **Correct Answer Breakdown:**
**iii.** is correct because activity (iii)—such as tree planting or cleaning compound areas—directly promotes environmental protection and community health as encouraged in Islam.

❌ **Why Other Options Are Incorrect:**
* **i.:** Represents an activity that does not directly contribute to environmental conservation.
* **ii.:** Represents an activity unrelated to environmental stewardship or cleanliness.
* **iv.:** Represents an activity that does not meet the goals of Environmental Day.

💡 **Key Takeaway for Revision:** Caring for nature and keeping compounds clean is an act of Ibadah (worship) in Islam.""",

    40: """📘 **Study Note & Concept Overview:**
Prophetic Hadiths place great emphasis on mutual aid and brotherhood (*Ukhuwwah*). The Prophet (p.b.u.h) said: *"Allah continues to help a servant as long as the servant helps his brother."*

✅ **Correct Answer Breakdown:**
**assisting other learners when they have problems** is correct because helping peers in difficulty directly applies the Prophet's Hadith on brotherhood, cooperation, and social responsibility.

❌ **Why Other Options Are Incorrect:**
* **wearing clean clothes:** While personal hygiene is important (*Taharah*), it relates to personal cleanliness rather than helping others in need.
* **following school rules:** Represents general school discipline, not the specific Hadith teaching on helping others.
* **sharing what they learned in school with their friends in Madrasa:** Relates to sharing knowledge, but assisting peers in difficulty best captures overall responsible social living.

💡 **Key Takeaway for Revision:** Helping others in times of need fulfills the Prophet's command on Islamic brotherhood and mutual support.""",

    41: """📘 **Study Note & Concept Overview:**
The *Ulul-Azm* (Prophets of Strong Will and Determination) are Nuh (Noah), Ibrahim (Abraham), Musa (Moses), Isa (Jesus), and Muhammad (p.b.u.h). They faced immense trials, persecution, and hardship, enduring them with extraordinary patience (*Sabr*).

✅ **Correct Answer Breakdown:**
**Patience** is correct because *Sabr* (perseverance and patience) was the defining quality of the Ulul-Azm prophets when facing severe difficulties.

❌ **Why Other Options Are Incorrect:**
* **Justice:** A key virtue in Islam, but *Sabr* (patience) is the specific virtue highlighted when enduring personal hardship and trials.
* **Honesty:** A fundamental virtue (*Sidq*), but endurance during trials specifically requires patience.
* **Kindness:** A noble trait, but overcoming hardship and suffering requires deep spiritual patience (*Sabr*).

💡 **Key Takeaway for Revision:** The Ulul-Azm prophets are exemplary role models of *Sabr* (patience and perseverance) during trials.""",

    42: """📘 **Study Note & Concept Overview:**
Iman (Faith) has 6 fundamental pillars in Islam: (1) Belief in Allah, (2) Belief in His Angels, (3) Belief in His Books, (4) Belief in His Messengers, (5) Belief in the Last Day, and (6) Belief in Divine Decree (Qadar).

✅ **Correct Answer Breakdown:**
**C** is correct because Box C arranges the 6 Pillars of Iman in their exact, traditional Islamic order.

❌ **Why Other Options Are Incorrect:**
* **A:** Contains incorrect ordering or mixes pillars of Islam with pillars of Iman.
* **B:** Omits one of the 6 essential pillars or scrambles the sequence.
* **D:** Includes non-pillar concepts or incorrect traditional order.

💡 **Key Takeaway for Revision:** The 6 Pillars of Iman begin with belief in Allah, His Angels, His Books, His Messengers, the Last Day, and Qadar.""",

    43: """📘 **Study Note & Concept Overview:**
Witr prayer is an emphasized Sunnah prayer (*Sunnah Mu'akkadah*) performed at night. The word *Witr* means "odd number" because it consists of an odd number of rak'ahs (such as 1, 3, or 5).

✅ **Correct Answer Breakdown:**
**After isha prayer.** is correct because Witr prayer is offered during the night time, specifically after completing the obligatory Isha prayer until before Fajr.

❌ **Why Other Options Are Incorrect:**
* **Before dhuhr prayer.:** Mid-morning time is for Sunnah prayers like Salatul-Duha, not Witr.
* **Before Asr prayer.:** Sunnah prayers before Asr exist, but Witr is strictly a night prayer.
* **After fajr prayer.:** Prayers are prohibited immediately after Fajr until sunrise, and Witr time ends at Fajr dawn.

💡 **Key Takeaway for Revision:** Witr is an odd-numbered night prayer performed after Isha up until the dawn of Fajr.""",

    44: """📘 **Study Note & Concept Overview:**
Fasting during the Holy Month of Ramadan (*Saum*) is obligatory for healthy, adult Muslims. However, Islam is a religion of ease and grants exemptions to specific categories of people, including the sick, the elderly, and travelers.

✅ **Correct Answer Breakdown:**
**Sheikha - sick, old and traveller** is correct because Islamic Shariah explicitly exempts the sick, the elderly who cannot bear fasting, and travelers traveling long distances.

❌ **Why Other Options Are Incorrect:**
* **Samira - sick, old and blind:** Blindness by itself does not exempt a healthy person from fasting.
* **Maimuna - sick, traveller and blind:** Blindness is not a ground for exemption from fasting.
* **Jamila - sick, traveller and women:** Women in general are not exempt; only women during specific conditions (post-natal/menstruation, pregnancy, nursing) have temporary concessions.

💡 **Key Takeaway for Revision:** People exempted from fasting include the sick, the elderly, and travelers (who make up missed days later).""",

    45: """📘 **Study Note & Concept Overview:**
Islam strongly condemns wastefulness in all aspects of life, including water usage during ablution (*Wudhu*). Prophet Muhammad (p.b.u.h) warned against wasting water even when performing Wudhu at a running river.

✅ **Correct Answer Breakdown:**
**Israf** is correct because *Israf* in Arabic means extravagance, wastefulness, or excessive spending/usage beyond necessity.

❌ **Why Other Options Are Incorrect:**
* **Tawakkul:** Means putting full trust and reliance on Allah.
* **Taqwa:** Means God-consciousness, piety, and fear of Allah.
* **Ihsan:** Means worshiping Allah as if you see Him, or doing excellence in good deeds.

💡 **Key Takeaway for Revision:** *Israf* means wastefulness or extravagance, which is forbidden in Islam even when using water for Wudhu.""",

    46: """📘 **Study Note & Concept Overview:**
In Islam, all intoxicants (*Khamr*)—whether liquid drinks, drugs, or substances that impair the mind and intellect—are strictly prohibited (*Haram*). The Prophet (p.b.u.h) declared: *"Whatever intoxicates in large quantities is forbidden even in small quantities."*

✅ **Correct Answer Breakdown:**
**A** is correct because Box A lists items that are exclusively classified as mind-altering intoxicants (such as alcohol, illegal drugs, and harmful narcotics).

❌ **Why Other Options Are Incorrect:**
* **B:** Includes non-intoxicating everyday beverages alongside intoxicants.
* **C:** Contains halal healthy drinks like fruit juices or milk.
* **D:** Contains medicinal non-intoxicating items or clean food items.

💡 **Key Takeaway for Revision:** All substances that impair the mind (*Khamr*) are strictly Haram (forbidden) in Islam.""",

    47: """📘 **Study Note & Concept Overview:**
Integrity (*Amanah* and *Nazaaha*) means being honest, moral, and upholding strong moral principles even when unobserved. Taking bribes (*Rishwa*) is a major sin in Islam that destroys justice and trust.

✅ **Correct Answer Breakdown:**
**Integrity** is correct because asking for bribes to hide wrongdoings demonstrates a complete lack of moral honesty, truthfulness, and integrity.

❌ **Why Other Options Are Incorrect:**
* **Responsibility:** Refers to performing assigned duties, but bribing specifically violates moral integrity and honesty.
* **Love:** Refers to affection; taking bribes is an act of corruption and greed rather than lack of love.
* **Unity:** Refers to togetherness; extortion through bribery destroys ethical standards.

💡 **Key Takeaway for Revision:** Taking or giving bribes (*Rishwa*) is forbidden and violates the Islamic value of integrity (*Amanah*).""",

    48: """📘 **Study Note & Concept Overview:**
Parents have sacred obligations toward their children in Islam. These include providing halal sustenance, Islamic education, shelter, love, moral guidance, and protecting them from physical and moral harm.

✅ **Correct Answer Breakdown:**
**Protecting them against harm** is correct because safeguarding children from physical dangers, abuse, and moral corruption is a mandatory Parental duty in Islam.

❌ **Why Other Options Are Incorrect:**
* **buying them gifts:** Buying gifts is a nice gesture of affection, but not a fundamental legal obligation like safety and protection.
* **playing with them:** Spending joyful time with children is recommended, but protection from harm is a mandatory legal duty.
* **doing homework for them:** Parents should support and encourage learning, but doing homework for children prevents them from learning independently.

💡 **Key Takeaway for Revision:** Protecting children from harm and providing proper guidance are fundamental parental obligations in Islam.""",

    49: """📘 **Study Note & Concept Overview:**
When Prophet Muhammad (p.b.u.h) received the first revelation in the Cave of Hira through Angel Jibril (AS), he was initially shaken and returned home to his wife Khadijah (RA). Her support and his ultimate reliance on Allah show the importance of trust in Allah (*Tawakkul*).

✅ **Correct Answer Breakdown:**
**trust in Allah** is correct because the experience teaches believers to place complete reliance and trust in Allah during overwhelming or unfamiliar life trials.

❌ **Why Other Options Are Incorrect:**
* **pray to Allah:** Ritual prayer (*Salah*) was detailed later in the Isra and Mi'raj; the immediate initial lesson was faith and trust in Allah.
* **observe fast:** Fasting (*Saum*) was prescribed in Medina years later.
* **give zakat:** Obligatory charity (*Zakat*) was institutionalized much later in Medina.

💡 **Key Takeaway for Revision:** The first revelation teaches Muslims to place complete trust in Allah (*Tawakkul*) during unexpected trials.""",

    50: """📘 **Study Note & Concept Overview:**
During the *Hijra* (migration from Makkah to Madina), the Muslims of Madina (*Ansar* - the Helpers) welcomed the migrating Muslims from Makkah (*Muhajirun* - the Emigrants). The Ansar shared their homes, wealth, and land in an extraordinary act of brotherhood and Islamic unity.

✅ **Correct Answer Breakdown:**
**unity** is correct because the bond of brotherhood (*Muwakhah*) established between the Ansar and Muhajirun demonstrated the highest level of Islamic unity, sharing, and solidarity.

❌ **Why Other Options Are Incorrect:**
* **peace:** While peaceful, the core action was actively sharing wealth and standing together as one united Ummah.
* **integrity:** Refers to personal honesty; the defining feature of the Ansar's response was communal solidarity and brotherhood.
* **patriotism:** Means love for one's nation; their unity was based on religious brotherhood rather than national pride.

💡 **Key Takeaway for Revision:** The partnership between Ansar and Muhajirun during Hijra is the supreme example of Islamic unity and brotherhood."""
}

file_path = 'src/data/kpsea-sst-ire-2023.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for q_num, exp_text in explanations_map.items():
    q_str = f'"questionNumber": {q_num},'
    q_pos = content.find(q_str)
    if q_pos != -1:
        exp_pos = content.find('"explanation":', q_pos)
        if exp_pos != -1:
            quote_start = content.find('"', exp_pos + 14)
            curr = quote_start + 1
            while curr < len(content):
                if content[curr] == '"' and content[curr-1] != '\\':
                    rest = content[curr+1:curr+30].lstrip()
                    if rest.startswith('}') or rest.startswith(','):
                        quote_end = curr
                        break
                curr += 1
            
            new_json_exp = json.dumps(exp_text)
            content = content[:exp_pos] + '"explanation": ' + new_json_exp + content[quote_end+1:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated IRE explanations successfully!")
