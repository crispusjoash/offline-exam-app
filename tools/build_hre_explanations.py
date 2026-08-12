import json

explanations_map = {
    36: """📘 **Study Note & Concept Overview:**
In Hindu tradition, various deities are closely associated with specific sacred animals and birds (*Vahanas* or symbols). Lord Krishna is famously depicted wearing a peacock feather (*Mayur Pankh*) in His crown, symbolizing purity, beauty, and grace.

✅ **Correct Answer Breakdown:**
**Peacock.** is correct because the peacock (Mayura) is intimately associated with Lord Krishna, who lovingly wears its feather in His headpiece.

❌ **Why Other Options Are Incorrect:**
* **Dove:** Symbolizes peace in Western/Christian traditions, but is not specifically associated with Lord Krishna.
* **Swan:** The Swan (Hamsa) is associated with Goddess Saraswati and Lord Brahma as a symbol of wisdom.
* **Eagle:** The Eagle (Garuda) is the divine carrier (*Vahana*) of Lord Vishnu, whereas Lord Krishna is specifically adorned with the peacock feather.

💡 **Key Takeaway for Revision:** Lord Krishna is instantly recognized by the vibrant peacock feather (*Mayur Pankh*) in His crown.""",

    37: """📘 **Study Note & Concept Overview:**
In Hindu Sanatan Dharma, the Supreme Cosmic Functions are performed by the *Trimurti* (the Divine Trinity): Brahma (the Creator), Vishnu (the Preserver), and Shiva/Mahesh (the Destroyer/Transformer).

✅ **Correct Answer Breakdown:**
**Brahma.** is correct because Lord Brahma is the deity specifically responsible for the creation of the universe and all living beings.

❌ **Why Other Options Are Incorrect:**
* **Vishnu.:** Responsible for preserving, protecting, and maintaining order in the cosmos.
* **Shiv.:** Responsible for transformation, dissolution, and destruction of evil/ignorance.
* **Ganesh.:** The deity of wisdom, intellect, and remover of obstacles (*Vighnaharta*).

💡 **Key Takeaway for Revision:** Lord Brahma is the creator, Lord Vishnu is the preserver, and Lord Shiva is the transformer.""",

    38: """📘 **Study Note & Concept Overview:**
In Jainism, Ayodhya is a deeply venerated holy city because it is the birthplace of five Tirthankaras: Rishabhdev (1st), Ajitnath (2nd), Abhinandannath (4th), Sumatinath (5th), and Anantnath (14th).

✅ **Correct Answer Breakdown:**
**Abhinandannath** is correct because Abhinandannath Swami is the 4th Jain Tirthankar whose birth (*Chyavan & Janma Kalyanak*) took place in the sacred city of Ayodhya.

❌ **Why Other Options Are Incorrect:**
* **Mahavir:** The 24th Tirthankar, born in Kshatriyakund/Vaishali (Bihar).
* **Mallinath:** The 19th Tirthankar, born in Mithila.
* **Neminath.:** The 22nd Tirthankar, born in Sauripura/Dwarka.

💡 **Key Takeaway for Revision:** Ayodhya is famous in Jainism as the birthplace of 5 Tirthankaras, including Abhinandannath Swami.""",

    39: """📘 **Study Note & Concept Overview:**
In the Ramayana, Sri Hanuman is an enlightened divine being, the epitome of selfless devotion (*Bhakti*), immense physical strength, profound wisdom, and complete humility.

✅ **Correct Answer Breakdown:**
**Hanuman.** is correct because Hanuman is revered as a Chiranjivi (immortal, enlightened soul) renowned for His flawless devotion to Lord Rama and immense spiritual power.

❌ **Why Other Options Are Incorrect:**
* **Bishma.:** The grand patriarch of the Kuru dynasty in the Mahabharata, bound by his vow to the throne.
* **Dashrath.:** King of Ayodhya and father of Lord Rama, a noble mortal monarch.
* **Dronacharya.:** The royal guru of the Pandavas and Kauravas in the Mahabharata.

💡 **Key Takeaway for Revision:** Sri Hanuman represents supreme devotion, wisdom, humility, and spiritual enlightenment.""",

    40: """📘 **Study Note & Concept Overview:**
The *Shikshapatri* is a sacred code of conduct written by Lord Swaminarayan. It lays down moral, practical, and spiritual guidelines for daily living, including strict instructions on *Ahimsa* (non-violence) and the protection of all animals.

✅ **Correct Answer Breakdown:**
**Shikshapatri** is correct because it explicitly instructs followers never to harm or kill any living creature, upholding non-violence (*Ahimsa*) and animal preservation.

❌ **Why Other Options Are Incorrect:**
* **Ramayan:** The epic narrative detailing the life, duties, and journey of Lord Rama.
* **Dhammapada:** A collection of core moral teachings of the Buddha.
* **Bhagwad Gita:** The sacred discourse delivered by Lord Krishna to Arjuna on duty (*Dharma*) and righteousness.

💡 **Key Takeaway for Revision:** The *Shikshapatri* emphasizes strict non-violence (*Ahimsa*) and the sacred duty to protect animals.""",

    41: """📘 **Study Note & Concept Overview:**
Sanskrit is known as *Devavani* (the divine language). In Hindu scriptures, the original Sanskrit mantras contain precise phonetic vibrations (*Dhvani*) and deep spiritual meanings that literal translations into modern vernacular languages often lose.

✅ **Correct Answer Breakdown:**
**in translating into vernacular, the inner meaning is lost** is correct because Sanskrit mantras carry precise spiritual nuances and vibrational potency that direct translations cannot fully convey.

❌ **Why Other Options Are Incorrect:**
* **the rhythm of recitation gives pleasure to listeners:** While melodic, the main spiritual reason is preserving original divine meaning and mantra power.
* **will motivates people to learn Sanskrit:** A secondary educational byproduct, not the primary reason for chanting in Sanskrit.
* **Sanskrit is easier than the vernacular.:** Sanskrit grammar is actually highly sophisticated and intricate, not easier than local spoken languages.

💡 **Key Takeaway for Revision:** Chanting in original Sanskrit preserves the deep spiritual essence and precise vibrational meaning of sacred mantras.""",

    42: """📘 **Study Note & Concept Overview:**
In Buddhism, sacred chants such as *Buddham Saranam Gacchami, Dhammam Saranam Gacchami, Sangham Saranam Gacchami* represent the Refuge in the Three Jewels (Buddha, Dhamma, and Sangha).

✅ **Correct Answer Breakdown:**
**Buddhists.** is correct because taking refuge in the Three Jewels is the fundamental prayer and practice of Buddhism.

❌ **Why Other Options Are Incorrect:**
* **Sanatan:** Sanatan Dharma prayers include Vedic mantras like the Gayatri Mantra or Om Namah Shivaya.
* **Jains:** Jain prayers prominently feature the Navkar Mantra (*Namo Arihantanam*).
* **Sikhs:** Sikh prayers center on the Mool Mantar (*Ik Onkar*) and Gurbani.

💡 **Key Takeaway for Revision:** Seeking refuge in the Buddha, Dhamma, and Sangha is the core daily prayer of Buddhists.""",

    43: """📘 **Study Note & Concept Overview:**
The *Dhwaj* (sacred flag or banner) is hoisted atop temples and places of worship. It acts as a beacon that can be seen from afar, identifying the religious tradition and signifying victory of righteousness (*Dharma*).

✅ **Correct Answer Breakdown:**
**helps devotees identify the faith** is correct because the distinctive color and symbol on the flag clearly signify the faith and mark the sacred house of worship from a distance.

❌ **Why Other Options Are Incorrect:**
* **beautify the place of worship:** Beautification is secondary; its main purpose is identification and sacred symbolism.
* **gives importance to the faith's symbol:** Symbols are important, but the flag specifically identifies the shrine for visiting devotees.
* **It gives direction to the devotees.:** While visible from afar, its primary function is marking the presence and identity of the holy temple.

💡 **Key Takeaway for Revision:** A *Dhwaj* (temple flag) identifies the place of worship and signals divine presence and Dharma.""",

    44: """📘 **Study Note & Concept Overview:**
In Hindu philosophy, human life operates under four key concepts, including *Purushartha* (righteous self-effort and hard work). Overcoming failure or poor performance requires persistent practice, diligence, and self-effort.

✅ **Correct Answer Breakdown:**
**Purushartha** is correct because *Purushartha* means earnest self-effort and hard work, which is required to improve skills and achieve success in studies or sports.

❌ **Why Other Options Are Incorrect:**
* **Punarjanam:** Refers to the cycle of rebirth/reincarnation.
* **Pranidaya:** Refers to showing mercy and compassion to living beings.
* **Prarthana:** Refers to prayer, which complements work but does not replace practical effort (*Purushartha*).

💡 **Key Takeaway for Revision:** *Purushartha* means dedicated self-effort and hard work needed to succeed in life goals.""",

    45: """📘 **Study Note & Concept Overview:**
In Sikhism, the three core pillars established by Guru Nanak Dev Ji are: (1) *Naam Japna* (remembrance and chanting of God's Name), (2) *Kirat Karna* (honest labor), and (3) *Vand Chhako* (sharing with the needy).

✅ **Correct Answer Breakdown:**
**Naam Japna** is correct because *Naam Japna* is the daily practice of chanting and meditating upon the divine Name of God (*Waheguru*).

❌ **Why Other Options Are Incorrect:**
* **Kirat Karna:** Means earning an honest living through truthful, hardworking means.
* **Wand shakna:** Means sharing one's food and wealth with the community and those in need.
* **Sewa karna:** Means performing selfless service for the community without expecting reward.

💡 **Key Takeaway for Revision:** *Naam Japna* is the Sikh pillar of continuously meditating upon and chanting God's Name.""",

    46: """📘 **Study Note & Concept Overview:**
In Jain Derasa (temple) architecture, sculptures of sacred animals like elephants (*Gaja*) placed at doorways serve as symbolic guardians, signifying strength, majesty, and divine protection of the holy shrine.

✅ **Correct Answer Breakdown:**
**a symbol of protection of the temple.** is correct because elephants placed at the entrance guard the temple and mark it as a sacred, protected space.

❌ **Why Other Options Are Incorrect:**
* **loyalty:** Loyalty is more commonly associated with domestic animals like dogs.
* **taming of wildlife:** Temples do not represent taming wild animals, but preserving sacred purity.
* **a symbol for removing negative energy:** While sacred, the entrance elephants specifically function as architectural protectors/guardians of the Derasa.

💡 **Key Takeaway for Revision:** Elephant figures at temple entrances symbolize noble strength and protection of the sacred space.""",

    47: """📘 **Study Note & Concept Overview:**
Different traditions use distinct traditional greetings. In temples dedicated to Lord Krishna or avatars of Lord Vishnu, devotees greet each other with *"Jai Shri Krishna"* or *"Radhe Radhe"*.

✅ **Correct Answer Breakdown:**
**Jai Shri Krishna.** is correct because in temples associated with Lord Krishna (an Avatar of Vishnu), "Jai Shri Krishna" is the standard joyful greeting.

❌ **Why Other Options Are Incorrect:**
* **Jai Ambe.:** Used among devotees of Goddess Durga/Amba (Shakti).
* **Jai Jinendra.:** The universal sacred greeting used among Jains.
* **Jai Bhole Nath.:** Used among devotees of Lord Shiva.

💡 **Key Takeaway for Revision:** "Jai Shri Krishna" is the respectful greeting used in temples dedicated to Lord Krishna.""",

    48: """📘 **Study Note & Concept Overview:**
Helping an injured peer immediately by stopping play and securing first aid demonstrates practical social responsibility, empathy, and duty of care toward others.

✅ **Correct Answer Breakdown:**
**responsibility** is correct because Hanjit acted responsibly by taking immediate charge to care for his hurt classmate.

❌ **Why Other Options Are Incorrect:**
* **respect:** Showing honor to elders/peers; caring for an injured friend is an active duty of responsibility.
* **patience:** Bearing delays calmly; taking action during an emergency requires prompt responsible action.
* **tolerance:** Accepting differences; responding to an injury is a matter of practical care and responsibility.

💡 **Key Takeaway for Revision:** Taking swift action to assist an injured classmate shows moral responsibility and care.""",

    49: """📘 **Study Note & Concept Overview:**
In Hindu culture, *Utsavs* (festivals) carry deep spiritual meanings. Both Diwali (celebrating Lord Rama's victorious return to Ayodhya after defeating Ravana) and Holi (celebrating Prahlada's devotion and the destruction of the demoness Holika) commemorate the triumph of good over evil.

✅ **Correct Answer Breakdown:**
**Diwali and Holi.** is correct because both festivals fundamentally celebrate the victory of light, truth, and righteousness over darkness and evil.

❌ **Why Other Options Are Incorrect:**
* **Paryushan Parv and Vasant Panchami.:** Paryushan is a Jain festival of forgiveness/fasting; Vasant Panchami celebrates Goddess Saraswati and spring.
* **Navratri and Janamashtami.:** Janamashtami celebrates the birth of Lord Krishna.
* **Ramnavmi and Gurupurab.:** Ramnavmi celebrates Lord Rama's birth; Gurupurab celebrates Sikh Gurus' birth anniversaries.

💡 **Key Takeaway for Revision:** Diwali and Holi are key Hindu festivals celebrating the victory of good over evil.""",

    50: """📘 **Study Note & Concept Overview:**
While Yoga provides great physical flexibility and health benefits, its true ancient purpose in spiritual traditions is uniting the mind, body, and spirit to achieve inner peace and spiritual growth (*Atma-Jnana*).

✅ **Correct Answer Breakdown:**
**grow spiritually** is correct because the ultimate objective of Yoga (from the root *Yuj*, meaning to join/unite) is spiritual elevation and self-realization.

❌ **Why Other Options Are Incorrect:**
* **participate in sports:** Yoga is a spiritual discipline of mind and body, not a competitive sport.
* **enhance social cohesion:** Community cohesion is a social benefit, but spiritual growth is the core reason.
* **be physically fit.:** Physical fitness is a positive health benefit, but spiritually, physical poses (*Asanas*) serve as a preparation for deep meditation and spiritual growth.

💡 **Key Takeaway for Revision:** The primary and highest goal of Yoga is spiritual growth and inner peace."""
}

file_path = 'src/data/kpsea-sst-hre-2023.js'
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

print("Updated HRE explanations successfully!")
