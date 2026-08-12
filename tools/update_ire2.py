import json
import re

file_path = 'src/data/kpsea-sst-ire-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

explanations = {
    41: """The correct answer is **C**.

**Analysis of the Correct Answer:**
The verse "Kalla saufa ta'lamun" translates to "No! You are going to know." This is the third (and fourth) verse of **Surah At-Takathur** (Chapter 102), which warns humanity against the dangerous distraction of competing for worldly wealth and status.

**Why Other Options Are Incorrect:**
* **A:** Surah Al-Qariah focuses on the striking calamity (the Day of Judgment).
* **B:** Surah Al-Humazah condemns the slanderer and the hoarder of wealth.
* **D:** Surah Al-Kawthar speaks about the abundant goodness given to the Prophet and instructs him to pray and sacrifice.

📌 **Key Learning Note:**
Surah At-Takathur reminds believers that worldly competition distracts them until they visit the graves, where they will finally "know" the truth.""",

    42: """The correct answer is **D**.

**Analysis of the Correct Answer:**
**Surah Al-Maun** strongly condemns people who perform religious duties (like prayer) only to be seen by others (showing off or *Riya*) and who refuse small kindnesses or assistance to others. Mariam's behavior of showing off her new watch falls under this discouraged characteristic.

**Why Other Options Are Incorrect:**
* **A:** Surah An-Naas is a prayer seeking protection from the whispers of Satan.
* **B:** Surah An-Nasr talks about the victory of Islam and the forgiveness of Allah.
* **C:** Surah Al-Falaq seeks refuge from external evils (like magic, envy, and darkness).

📌 **Key Learning Note:**
In Islam, *Riya* (showing off) ruins the sincerity of good deeds. Surah Al-Maun warns that prayers done just to impress others are empty.""",

    43: """The correct answer is **A**.

**Analysis of the Correct Answer:**
The famous Hadith narrated by Abu Huraira (in Sahih Muslim) states: "Verily, Allah does not look at your appearance or wealth, but rather He looks at your **hearts and actions**." This emphasizes that true value in Islam is determined by inner sincerity and righteous deeds, not superficial wealth or beauty.

**Why Other Options Are Incorrect:**
* **B:** While intentions (Niyyah) are crucial, the exact wording of this specific Hadith pairs "hearts" with "actions" (A'maal).
* **C & D:** Physical strength is entirely irrelevant to this Hadith's context about divine judgment.

📌 **Key Learning Note:**
Allah judges a person based on their Taqwa (piety in the heart) and the good deeds (actions) they perform, disregarding physical status.""",

    44: """The correct answer is **C**.

**Analysis of the Correct Answer:**
The name **Al-Haafidh** translates to "The Protector" or "The Preserver." When a Muslim seeks safety, security, and protection from harm (especially during a journey), invoking this specific attribute of Allah is the most appropriate action.

**Why Other Options Are Incorrect:**
* **A:** Al-Ghaffar means "The All-Forgiving," used when seeking forgiveness for sins.
* **B:** Al-Waahid means "The One," used to declare Allah's absolute unity and indivisibility.
* **D:** Al-Hakam means "The Judge," used when seeking justice or fairness.

📌 **Key Learning Note:**
Allah has 99 names (Asma-ul-Husna), and Muslims are encouraged to call upon the specific name that best matches their need or prayer.""",

    45: """The correct answer is **B**.

**Analysis of the Correct Answer:**
Wudhu (ablution) is the ritual purification required before prayer. It is immediately nullified (broken) by any discharge from the front or back passages, which includes **passing wind**. 

**Why Other Options Are Incorrect:**
* **A & C:** Swallowing saliva or eating food does not break wudhu (though rinsing the mouth after eating is recommended).
* **D:** Laughing loudly invalidates the *prayer* if it happens during Swalat, but it does not break the *wudhu* itself.

📌 **Key Learning Note:**
Acts that nullify Wudhu include passing wind, urination, defecation, deep sleep, and loss of consciousness.""",

    46: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Zakat is an obligatory alms tax calculated on accumulated wealth that has reached a specific threshold (Nisab). It is payable on productive or hoarded assets, such as agricultural produce, livestock, cash, and **precious metals/goods for trade** (like gold).

**Why Other Options Are Incorrect:**
* **A, B & D:** Zakat is *not* payable on personal belongings used for everyday living. This includes a residential house, personal books, clothing, and household furniture. These items are meant for personal use, not for generating wealth.

📌 **Key Learning Note:**
Zakat purifies wealth. It is only levied on surplus wealth and assets that have the potential to grow, never on the basic necessities of life.""",

    47: """The correct answer is **B**.

**Analysis of the Correct Answer:**
Betting (gambling or *Maysir*) is strictly forbidden in Islam. When a Muslim sees another doing something wrong, the first and best course of action is to politely and wisely **advise them on the harmful effects**, encouraging them to stop through reasoning and brotherhood (enjoining good and forbidding evil).

**Why Other Options Are Incorrect:**
* **A:** Immediately threatening to report them creates hostility and breaks trust, making them less likely to listen and change.
* **C:** Praying for them is good, but Islam requires *action* (advising) alongside prayer when witnessing a wrong.
* **D:** Ignoring them is a failure of a Muslim's duty to guide their brothers away from sin.

📌 **Key Learning Note:**
The Islamic concept of "Amr bil Ma'ruf wa Nahy 'anil Munkar" means actively enjoining what is right and forbidding what is wrong through gentle advice.""",

    48: """The correct answer is **A**.

**Analysis of the Correct Answer:**
**Israf** means wastefulness, extravagance, or exceeding limits in the use of resources. By **switching off the lights** in an empty classroom, a learner is actively preventing the wastage of electricity, which perfectly demonstrates guarding against Israf.

**Why Other Options Are Incorrect:**
* **B:** Using excessive water for Wudhu is a direct example *of* Israf; the Prophet advised using minimal water.
* **C:** Serving too much food often leads to leftovers being thrown away, which is Israf.
* **D:** Abandoning partially used books for new ones wastes paper and money, which is also Israf.

📌 **Key Learning Note:**
Islam teaches moderation in all things. Wasting resources—whether water, electricity, food, or money—is strongly condemned.""",

    49: """The correct answer is **A**.

**Analysis of the Correct Answer:**
In Islam, everyday good deeds performed with the right intention are considered **Ibadah** (acts of worship). Respecting parents, elders, and family members is highly commanded by Allah in the Quran. Therefore, fulfilling this command is a direct act of worshipping and obeying Allah.

**Why Other Options Are Incorrect:**
* **B:** Sadaqah refers specifically to voluntary charity (giving wealth, a smile, or helping hands), whereas respect is a mandatory duty (Fard) towards parents.
* **C & D:** While respect does prepare one for adulthood and shows responsibility, the fundamental *religious* reason (in an IRE context) is that it is a divine command and a form of worship.

📌 **Key Learning Note:**
Ibadah is not limited to prayer and fasting; any righteous action (like respecting family) done to please Allah is counted as worship.""",

    50: """The correct answer is **D**.

**Analysis of the Correct Answer:**
When Prophet Muhammad (PBUH) traveled to the city of Taif to preach Islam, he was rejected, mocked, and violently pelted with stones until he bled. When the Angel of Mountains offered to crush the city between two mountains in retaliation, the Prophet refused and instead prayed for their guidance. This demonstrated unparalleled **forgiveness** and mercy.

**Why Other Options Are Incorrect:**
* **A:** Generosity involves giving wealth, which was not the theme of the Taif incident.
* **B:** Honesty (truthfulness) was his constant trait, but Taif is specifically famous for his reaction to extreme abuse.
* **C:** Justice involves fair punishment, but the Prophet chose mercy and forgiveness over justice in this instance.

📌 **Key Learning Note:**
The incident at Taif is the greatest historical example of the Prophet's mercy and his willingness to forgive even his harshest enemies."""
}

for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

new_content = "export const kpseaSstIre2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 3 completed successfully.")
