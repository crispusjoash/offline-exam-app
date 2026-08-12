import json
import re

explanations_map = {
    36: """Surah **Al-Quraish** reminds believers of Allah's provisions (feeding them against hunger and giving them security from fear), making it the comforting surah during famine and drought.

* **Why other options are incorrect:**
  * **Al-Kauthar:** Focuses on Allah's abundant favors and prayer/sacrifice, rather than provision during famine and fear.
  * **Al-Humaza:** Warns against slander, backbiting, and hoarding wealth.
  * **At-Takathur:** Warns against rivalry in worldly increase and materialism.

💡 **Key Takeaway:** Surah Al-Quraish emphasizes trusting Allah as the provider of food in hunger and safety in fear.""",

    37: """The correct chronological order of the three verses of Surah Al-Qariah is **i, iii, ii** (Verse i: *Al-Qari'ah*, Verse iii: *Wa ma adraka mal-qari'ah*, Verse ii: *Mal-qari'ah*).

* **Why other options are incorrect:**
  * **iii, i, ii:** Places the explanatory question before the opening title verse.
  * **iii, ii, i:** Reverses the Quranic order of recitation.
  * **i, ii, iii:** Swaps the sequence of the second and third verses.

💡 **Key Takeaway:** Reciting Quranic surahs requires following the exact order of verses as revealed.""",

    38: """Surah Al-Masad teaches that **Wealth cannot protect a person from Allah's punishment**, as illustrated by Abu Lahab whose riches and earnings failed to save him.

* **Why other options are incorrect:**
  * **Allah will reward those who perform good deeds:** Highlighted in surahs like Al-Zalzalah or Al-Asr, not Al-Masad which warns transgressors.
  * **Muslims should seek protection from Allah:** A primary lesson of Surah Al-Falaq and Surah An-Nas (Mu'awwidhatayn).
  * **Muslims should ask for forgiveness from Allah:** A primary lesson of Surah An-Nasr and Surah Al-Istighfar.

💡 **Key Takeaway:** Worldly wealth and status cannot save a person from divine judgment without faith and good deeds.""",

    39: """Activity **iii** demonstrates active environmental conservation (such as planting trees or collecting waste), fulfilling the Islamic duty of stewardship (*Khalifah*).

* **Why other options are incorrect:**
  * **i:** Shows an activity unrelated to environmental conservation.
  * **ii:** Shows a non-conservation task or passive activity.
  * **iv:** Shows an activity that does not contribute directly to environmental protection.

💡 **Key Takeaway:** Muslims are custodians (*Khalifah*) of the Earth and are commanded to care for the environment.""",

    40: """In Islamic teachings, learners practice responsible living by **assisting other learners when they have problems**, demonstrating brotherly care and community support.

* **Why other options are incorrect:**
  * **wearing clean clothes:** Demonstrates personal hygiene (*Taharah*), which is good but limited to self-care rather than interpersonal responsibility.
  * **following school rules:** A basic civic duty, whereas helping others in distress directly fulfills the Hadith on mutual responsibility.
  * **sharing what they learned in school with their friends in Madrasa:** Represents knowledge sharing, but assisting those in hardship reflects compassionate responsibility.

💡 **Key Takeaway:** A Muslim is responsible for supporting, helping, and caring for fellow human beings in need.""",

    41: """The Ulul-Azm prophets (Nuh, Ibrahim, Musa, Isa, and Muhammad p.b.u.h) are renowned for extraordinary **Patience** (*Sabr*) and perseverance in enduring great trials while conveying Allah's message.

* **Why other options are incorrect:**
  * **Justice:** While all prophets were just, 'Sabr' (patience under adversity) is the defining virtue of the Ulul-Azm.
  * **Honesty:** A foundational virtue of all prophets (As-Siddiq), but endurance of hardship specifically tests patience.
  * **Kindness:** A general Islamic virtue, whereas facing severe home/life difficulties specifically requires patience (*Sabr*).

💡 **Key Takeaway:** The Ulul-Azm prophets set the ultimate example of patience (*Sabr*) during severe hardship.""",

    42: """Box **C** lists the pillars of Iman (Faith) in their correct theological order: 1. Belief in Allah, 2. Angels, 3. Books, 4. Prophets, 5. Day of Judgment, 6. Divine Decree (Qadar).

* **Why other options are incorrect:**
  * **A:** Misplaces the order of belief in Prophets or Angels.
  * **B:** Mixes pillars of Islam (like Zakat or Hajj) with pillars of Iman.
  * **D:** Disrupts the sequential order of the 6 pillars of Iman.

💡 **Key Takeaway:** There are 6 pillars of Iman in Islam, beginning with belief in Allah and ending with belief in Qadar.""",

    43: """Witr prayer is an odd-numbered sunnah prayer performed **After isha prayer** before going to sleep or during the night.

* **Why other options are incorrect:**
  * **Before dhuhr prayer:** The sunnah prayer before Dhuhr is Qabliyah, not Witr.
  * **Before Asr prayer:** Non-obligatory sunnah prayers occur prior to Asr, but not Witr.
  * **After fajr prayer:** Voluntary prayers are prohibited immediately after Fajr until sunrise.

💡 **Key Takeaway:** Witr is the final odd-numbered prayer performed after Isha at night.""",

    44: """According to Islamic Shariah, **Sheikha - sick, old and traveller** correctly lists individuals exempted from obligatory fasting during Ramadan (with obligation to makeup days or pay Fidyah).

* **Why other options are incorrect:**
  * **Samira - sick, old and blind:** Blindness is not a ground for exemption from Ramadan fasting.
  * **Maimuna - sick, traveller and blind:** Blindness does not exempt a healthy person from fasting.
  * **Jamila - sick, traveller and women:** Being a woman in general does not exempt one from fasting (only menstruation/postnatal/nursing states do).

💡 **Key Takeaway:** Exemptions from Ramadan fasting apply to the sick, elderly, travelers, and pregnant/nursing mothers.""",

    45: """Using excessive amounts of water during wudhu (ablution) or daily tasks is called **Israf** (extravagance/wastefulness), which is forbidden in Islam.

* **Why other options are incorrect:**
  * **Tawakkul:** Putting complete trust and reliance in Allah.
  * **Taqwa:** God-consciousness and piety.
  * **Ihsan:** Performing worship with perfection as if seeing Allah.

💡 **Key Takeaway:** Islam teaches moderation and forbids 'Israf' (wastefulness), even when performing ablution by a flowing river.""",

    46: """Box **A** contains items that are classified strictly as intoxicants (*Khamr*), which are haram in Islam.

* **Why other options are incorrect:**
  * **B:** Includes non-intoxicating halal beverages alongside forbidden drinks.
  * **C:** Contains natural fruit juices or permissible drinks.
  * **D:** Contains non-alcoholic healthy fluids.

💡 **Key Takeaway:** All intoxicants (*Khamr*) that cloud the mind are forbidden (*Haram*) in Islam.""",

    47: """Demanding bribes to conceal noise makers is corruption; the vital Islamic moral value that Amira lacks is **Integrity** (honesty and moral uprightness).

* **Why other options are incorrect:**
  * **Responsibility:** Amira is performing monitor duties, but doing so corruptly lacks integrity.
  * **Love:** Affection for others; bribery is a violation of justice and moral truthfulness.
  * **Unity:** Harmony in a group, whereas dishonesty destroys trust and moral integrity.

💡 **Key Takeaway:** Integrity means upholding honesty and resisting corruption or bribery in leadership roles.""",

    48: """A primary Islamic parental obligation toward children is **Protecting them against harm**, ensuring their physical, moral, and spiritual safety.

* **Why other options are incorrect:**
  * **buying them gifts:** Gifts are optional acts of affection, not a fundamental parental obligation.
  * **playing with them:** Good for bonding, but safeguarding protection and education are core legal duties.
  * **doing homework for them:** Parents should guide learning, but doing homework for children hinders their intellectual development.

💡 **Key Takeaway:** Parents have a sacred duty in Islam to protect, nurture, educate, and provide for their children.""",

    49: """The Prophet's (p.b.u.h) experience during the first revelation in Cave Hira and the reassurance from Khadija (R.A.) teaches believers to **trust in Allah** during moments of fear or uncertainty.

* **Why other options are incorrect:**
  * **pray to Allah:** While prayer is vital, the immediate lesson from Hira was total trust (*Tawakkul*) in divine wisdom.
  * **observe fast:** Fasting rules were revealed later in Madina, not at the first revelation in Cave Hira.
  * **give zakat:** Almsgiving was legislated as an obligatory pillar later in Islamic history.

💡 **Key Takeaway:** Trusting Allah (*Tawakkul*) provides comfort and courage when facing scary or unfamiliar challenges.""",

    50: """The Ansar (helpers of Madina) welcomed and shared their wealth, homes, and land with the Muhajirun (emigrants from Makkah), demonstrating the value of **unity** and Islamic brotherhood.

* **Why other options are incorrect:**
  * **peace:** Harmony; while peaceful, the extraordinary act was active brotherly sharing and unity (*Ukhuwah*).
  * **integrity:** Personal honesty; the historical event emphasizes communal solidarity and brotherhood.
  * **patriotism:** Love for one's homeland, whereas the Hijrah transcended tribal lands for faith unity.

💡 **Key Takeaway:** The brotherhood between Ansar and Muhajirun illustrates true Islamic unity and selfless sharing."""
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

print("Successfully updated all 15 explanations in IRE (kpsea-sst-ire-2023.js)!")
