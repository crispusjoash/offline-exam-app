import json

filepath = 'src/data/kpsea-sst-hre-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaSstHre2023 = '
clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

hre_explanations = {
    36: """The correct answer is **Peacock.**.

**Detailed Analysis of the Correct Answer:**
In Hindu tradition, various deities are closely associated with specific sacred animals and birds. **Lord Krishna** is famously depicted wearing a **peacock feather (*Mayur Pankh*)** in His crown, symbolizing purity, beauty, divine grace, and joy.

**Why Other Options Are Incorrect:**
* **Dove.:** Symbolizes peace in Western/Christian traditions, but is not specifically associated with Lord Krishna.
* **Swan.:** The Swan (*Hamsa*) is associated with Goddess Saraswati and Lord Brahma as a symbol of wisdom and spiritual discernment.
* **Eagle.:** The Eagle (*Garuda*) is the divine carrier (*Vahana*) of Lord Vishnu, whereas Lord Krishna is specifically adorned with the peacock feather.

📌 **Key Learning Note:**
Lord Krishna is instantly recognized by the vibrant **peacock feather (*Mayur Pankh*)** in His crown.""",

    37: """The correct answer is **Brahma.**.

**Detailed Analysis of the Correct Answer:**
In Hindu Sanatan Dharma, the Supreme Cosmic Functions are performed by the **Trimurti** (the Divine Trinity):
1. **Lord Brahma:** The Creator of the universe.
2. **Lord Vishnu:** The Preserver and Protector of creation.
3. **Lord Shiva (Mahesh):** The Transformer and Dissolver of the universe.

Therefore, **Lord Brahma** is the deity associated with creation.

**Why Other Options Are Incorrect:**
* **Vishnu.:** Responsible for preserving, protecting, and maintaining order in the cosmos.
* **Shiv.:** Responsible for transformation, dissolution, and destruction of evil/ignorance.
* **Ganesh.:** The deity of wisdom, intellect, and remover of obstacles (*Vighnaharta*).

📌 **Key Learning Note:**
The Trimurti: **Lord Brahma (Creator), Lord Vishnu (Preserver), Lord Shiva (Transformer)**.""",

    38: """The correct answer is **Abhinandannath**.

**Detailed Analysis of the Correct Answer:**
In Jainism, Ayodhya is a deeply venerated holy city because it is the birthplace of five Tirthankaras. **Abhinandannath Swami** is the 4th Jain Tirthankar whose birth (*Janma Kalyanak*) took place in the sacred city of Ayodhya.

**Why Other Options Are Incorrect:**
* **Mahavir:** The 24th Tirthankar, born in Kshatriyakund/Vaishali (Bihar).
* **Mallinath:** The 19th Tirthankar, born in Mithila.
* **Neminath.:** The 22nd Tirthankar, born in Sauripura/Dwarka.

📌 **Key Learning Note:**
Ayodhya is celebrated in Jainism as the sacred birthplace of five Tirthankaras, including **Abhinandannath Swami**.""",

    39: """The correct answer is **Hanuman.**.

**Detailed Analysis of the Correct Answer:**
**Sri Hanuman** is an enlightened divine being, the epitome of selfless devotion (*Bhakti*), immense spiritual strength, profound wisdom, and complete humility. He is revered as a Chiranjivi (immortal, enlightened soul) renowned for His divine protection of the righteous.

**Why Other Options Are Incorrect:**
* **Bishma.:** The grand patriarch of the Kuru dynasty in the Mahabharata, bound by his solemn vow to the throne.
* **Dashrath.:** King of Ayodhya and father of Lord Rama, a noble mortal monarch.
* **Dronacharya.:** The royal guru of the Pandavas and Kauravas in the Mahabharata.

📌 **Key Learning Note:**
**Sri Hanuman** represents supreme devotion, courage, wisdom, and spiritual enlightenment.""",

    40: """The correct answer is **Shikshapatri**.

**Detailed Analysis of the Correct Answer:**
The **Shikshapatri** is a sacred code of conduct written by Lord Swaminarayan. It lays down moral, practical, and spiritual guidelines for daily living, including strict instructions on **Ahimsa (non-violence)** and the sacred duty to preserve and protect all animals from harm or slaughter.

**Why Other Options Are Incorrect:**
* **Ramayan:** The epic narrative detailing the life, duties, and righteous path of Lord Rama.
* **Dhammapada:** A collection of core moral teachings of the Buddha.
* **Bhagwad Gita.:** The sacred discourse delivered by Lord Krishna to Arjuna on duty (*Dharma*) and righteousness.

📌 **Key Learning Note:**
The **Shikshapatri** emphasizes strict non-violence (*Ahimsa*) and the sacred duty to protect animals.""",

    41: """The correct answer is **in translating into vernacular, the inner meaning is lost**.

**Detailed Analysis of the Correct Answer:**
Sanskrit is known as *Devavani* (the divine language). In Hindu scriptures, original Sanskrit mantras contain precise phonetic vibrations (*Dhvani*) and deep spiritual meanings that literal translations into modern vernacular languages often lose.

**Why Other Options Are Incorrect:**
* **the rhythm of recitation gives pleasure to listeners:** While melodic, the primary spiritual reason is preserving original divine meaning and mantra power.
* **will motivates people to learn Sanskrit:** A secondary educational byproduct, not the primary reason for chanting in Sanskrit.
* **Sanskrit is easier than the vernacular.:** Sanskrit grammar is highly sophisticated and intricate, not easier than local spoken languages.

📌 **Key Learning Note:**
Chanting in original **Sanskrit** preserves the deep spiritual essence and precise vibrational meaning of sacred mantras.""",

    42: """The correct answer is **Buddhists.**.

**Detailed Analysis of the Correct Answer:**
In **Buddhism**, sacred chants such as *Buddham Saranam Gacchami, Dhammam Saranam Gacchami, Sangham Saranam Gacchami* represent taking **Refuge in the Three Jewels** (the Buddha, the Dhamma/Teachings, and the Sangha/Community).

**Why Other Options Are Incorrect:**
* **Sanatan:** Sanatan Dharma prayers include Vedic mantras like the Gayatri Mantra or Om Namah Shivaya.
* **Jains:** Jain prayers prominently feature the Navkar Mantra (*Namo Arihantanam*).
* **Sikhs:** Sikh prayers center on the Mool Mantar (*Ik Onkar*) and Gurbani.

📌 **Key Learning Note:**
Seeking refuge in the **Buddha, Dhamma, and Sangha** is the core daily prayer of Buddhists.""",

    43: """The correct answer is **helps devotees identify the faith**.

**Detailed Analysis of the Correct Answer:**
The **Dhwaj** (sacred flag or banner) is hoisted atop temples and places of worship. It acts as a beacon visible from afar, helping devotees **identify the place of worship and the faith** it represents while signaling divine presence and righteousness (*Dharma*).

**Why Other Options Are Incorrect:**
* **beautify the place of worship:** Beautification is secondary; its main purpose is identification and sacred symbolism.
* **gives importance to the faith's symbol:** Symbols are important, but the flag specifically identifies the shrine for visiting devotees.
* **It gives direction to the devotees.:** While visible from afar, its primary function is marking the presence and identity of the holy temple.

📌 **Key Learning Note:**
A **Dhwaj (temple flag)** identifies the place of worship and signals divine presence and Dharma.""",

    44: """The correct answer is **Purushartha**.

**Detailed Analysis of the Correct Answer:**
In Hindu philosophy, **Purushartha** refers to righteous self-effort, hard work, and goal-directed action. Overcoming failure or poor performance in studies or physical assessments requires persistent practice, diligence, and self-effort (*Purushartha*).

**Why Other Options Are Incorrect:**
* **Punarjanam:** Refers to the cycle of rebirth/reincarnation.
* **Pranidaya:** Refers to showing mercy and compassion to living beings.
* **Prarthana.:** Refers to prayer, which complements work but does not replace practical effort (*Purushartha*).

📌 **Key Learning Note:**
**Purushartha** means dedicated self-effort and hard work needed to achieve success in life goals.""",

    45: """The correct answer is **Naam Japna**.

**Detailed Analysis of the Correct Answer:**
In Sikhism, the three core pillars established by Guru Nanak Dev Ji are:
1. **Naam Japna:** Remembrance and chanting of God's Name (*Waheguru*).
2. **Kirat Karna:** Earning an honest living through truthful hard work.
3. **Vand Chhako (Wand shakna):** Sharing wealth and food with the community.

Therefore, morning chanting in a Sikh place of worship is guided by **Naam Japna**.

**Why Other Options Are Incorrect:**
* **Kirat Karna:** Means earning an honest living through truthful means.
* **Wand shakna:** Means sharing food and wealth with those in need.
* **Sewa karna.:** Means performing selfless service for the community without expecting reward.

📌 **Key Learning Note:**
**Naam Japna** is the Sikh pillar of meditating upon and chanting God's Name.""",

    46: """The correct answer is **a symbol of protection of the temple.**.

**Detailed Analysis of the Correct Answer:**
In Jain Derasa (temple) architecture, sculptures of sacred elephants (*Gaja*) placed at doorways serve as symbolic guardians, signifying majesty, nobility, and divine **protection of the sacred temple space**.

**Why Other Options Are Incorrect:**
* **loyalty:** Loyalty is more commonly associated with domestic animals like dogs.
* **taming of wildlife:** Temples do not represent taming wild animals, but preserving sacred purity.
* **a symbol for removing negative energy:** While sacred, entrance elephants specifically function as architectural protectors/guardians.

📌 **Key Learning Note:**
Elephant figures at temple entrances symbolize noble strength and **protection of the sacred space**.""",

    47: """The correct answer is **Jai Shri Krishna.**.

**Detailed Analysis of the Correct Answer:**
Different traditions use distinct traditional greetings. In mandirs dedicated to Lord Krishna or avatars of Lord Vishnu, devotees greet each other with **"Jai Shri Krishna"** or *"Radhe Radhe"*.

**Why Other Options Are Incorrect:**
* **Jai Ambe.:** Used among devotees of Goddess Durga/Amba (Shakti).
* **Jai Jinendra.:** The universal sacred greeting used among Jains.
* **Jai Bhole Nath.:** Used among devotees of Lord Shiva.

📌 **Key Learning Note:**
**"Jai Shri Krishna"** is the respectful greeting used in temples dedicated to Lord Krishna.""",

    48: """The correct answer is **responsibility**.

**Detailed Analysis of the Correct Answer:**
Helping an injured peer immediately by stopping play and taking them for first aid demonstrates practical social **responsibility**, empathy, and moral duty of care toward others.

**Why Other Options Are Incorrect:**
* **respect:** Showing honor to elders/peers; caring for an injured friend is an active duty of responsibility.
* **patience:** Bearing delays calmly; responding to an emergency requires prompt responsible action.
* **tolerance.:** Accepting differences; responding to an injury is a matter of practical care and responsibility.

📌 **Key Learning Note:**
Taking swift action to assist an injured classmate shows moral **responsibility** and care.""",

    49: """The correct answer is **Diwali and Holi.**.

**Detailed Analysis of the Correct Answer:**
In Hindu culture, *Utsavs* (festivals) carry deep spiritual meanings. Both **Diwali** (celebrating Lord Rama's victorious return to Ayodhya after defeating Ravana) and **Holi** (celebrating Prahlada's devotion and the destruction of Holika) commemorate the ultimate **victory of good over evil**.

**Why Other Options Are Incorrect:**
* **Paryushan Parv and Vasant Panchami.:** Paryushan is a Jain festival of forgiveness/fasting; Vasant Panchami celebrates Goddess Saraswati and spring.
* **Navratri and Janamashtami.:** Janamashtami celebrates the birth of Lord Krishna.
* **Ramnavmi and Gurupurab.:** Ramnavmi celebrates Lord Rama's birth; Gurupurab celebrates Sikh Gurus' birth anniversaries.

📌 **Key Learning Note:**
**Diwali and Holi** are major Hindu festivals celebrating the victory of good over evil.""",

    50: """The correct answer is **grow spiritually**.

**Detailed Analysis of the Correct Answer:**
While Yoga provides great physical flexibility and health benefits, its true ancient purpose in spiritual traditions (derived from the root *Yuj*, meaning to join/unite) is uniting the mind, body, and spirit to **grow spiritually** and achieve inner peace.

**Why Other Options Are Incorrect:**
* **participate in sports:** Yoga is a spiritual discipline of mind and body, not a competitive sport.
* **enhance social cohesion:** Community cohesion is a social benefit, but spiritual growth is the core objective.
* **be physically fit.:** Physical fitness is a positive health benefit, but physical poses (*Asanas*) serve as a preparation for deep meditation and spiritual growth.

📌 **Key Learning Note:**
The primary and highest goal of **Yoga** is spiritual growth and inner peace."""
}

for q in data['sectionA']:
    qn = q['questionNumber']
    if qn in hre_explanations:
        q['explanation'] = hre_explanations[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print("All 15 HRE questions updated successfully in kpsea-sst-hre-2023.js!")
