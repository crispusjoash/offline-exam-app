import json
import re

explanations_map = {
    36: """The **Peacock** (Mayura) is intimately associated with Lord Krishna, who famously wears a peacock feather (*Mayur Pankh*) in his crown as a symbol of divine beauty and grace.

* **Why other options are incorrect:**
  * **Dove:** A bird associated with peace in Western/Christian traditions, not Krishna's iconography.
  * **Swan:** The Swan (*Hamsa*) is associated with Goddess Saraswati and Brahma, symbolizing spiritual discrimination.
  * **Eagle:** The Eagle (*Garuda*) is the divine mount (*Vahana*) of Lord Vishnu, while the peacock feather specifically identifies Lord Krishna.

💡 **Key Takeaway:** Lord Krishna is iconographically identified by the peacock feather in his crown.""",

    37: """In the Hindu Trimurti (Trinity), Lord **Brahma** is the deity specifically associated with creation.

* **Why other options are incorrect:**
  * **Vishnu:** The preserver and protector of the universe within the Trimurti.
  * **Shiv:** The destroyer and transformer who facilitates cyclic renewal in the Trimurti.
  * **Ganesh:** The remover of obstacles and deity of new beginnings, wisdom, and intellect.

💡 **Key Takeaway:** The Hindu Trimurti consists of Brahma (Creator), Vishnu (Preserver), and Shiva (Transformer).""",

    38: """In Jain tradition, **Abhinandannath** (the 4th Tirthankar) was born in Ayodhya, making it a sacred Jain pilgrimage site alongside being the birthplace of Lord Rama.

* **Why other options are incorrect:**
  * **Mahavir:** The 24th Tirthankar was born in Kundagrama (near Vaishali, Bihar).
  * **Mallinath:** The 19th Tirthankar was born in Mithila.
  * **Neminath:** The 22nd Tirthankar was born in Sauripura/Dwaraka.

💡 **Key Takeaway:** Five Jain Tirthankars (including Rishabhdev and Abhinandannath) were born in the holy city of Ayodhya.""",

    39: """The statements describe **Hanuman**, an enlightened being revered for selfless devotion (*Bhakti*), humility, supreme strength, and unwavering service to Lord Rama.

* **Why other options are incorrect:**
  * **Bishma:** The grand sire in the Mahabharata renowned for his vow of celibacy and loyalty to the throne.
  * **Dashrath:** The King of Ayodhya and father of Lord Rama.
  * **Dronacharya:** The royal guru and master of archery who taught the Pandavas and Kauravas.

💡 **Key Takeaway:** Lord Hanuman exemplifies supreme devotion (*Bhakti*), humility, and divine strength.""",

    40: """The **Shikshapatri** (written by Lord Swaminarayan) contains explicit scriptural commands on non-violence (*Ahimsa*), sanctity of life, and preserving animals against harm or slaughter.

* **Why other options are incorrect:**
  * **Ramayan:** The epic narrative depicting the life and righteous rule of Lord Rama.
  * **Dhammapada:** Buddhist scriptural text containing verses of the Buddha's ethical teachings.
  * **Bhagwad Gita:** The sacred dialogue between Krishna and Arjuna on duty (*Dharma*) and yoga.

💡 **Key Takeaway:** The Shikshapatri strictly mandates Ahimsa (non-violence) and protecting all animal life.""",

    41: """Scriptures are recited in original Sanskrit because **in translating into vernacular, the inner meaning is lost** along with subtle spiritual vibrations and precise theological nuances.

* **Why other options are incorrect:**
  * **the rhythm of recitation gives pleasure to listeners:** While melodic, the primary theological reason for Sanskrit preservation is preserving exact sacred meaning.
  * **will motivates people to learn Sanskrit:** Motivational side-effect, not the primary reason priests preserve scriptural accuracy.
  * **Sanskrit is easier than the vernacular:** Sanskrit is an ancient classical language, often harder to master than spoken vernaculars.

💡 **Key Takeaway:** Ancient scriptural Sanskrit is preserved to retain untranslatable spiritual vibrations and exact theological meanings.""",

    42: """The prayer text shown belongs to **Buddhists** (e.g., the Vandana or Three Refuges: *Buddham Saranam Gacchami*).

* **Why other options are incorrect:**
  * **Sanatan:** Hindu prayers typically begin with Om or Vedic mantras like the Gayatri Mantra.
  * **Jains:** Jain prayers focus on the Navkar Mantra (*Namo Arihantanam*).
  * **Sikhs:** Sikh prayers focus on *Ardas* or *Japji Sahib* (*Ik Onkar*).

💡 **Key Takeaway:** The Three Refuges (*Tisarana*) form the foundational prayer of Buddhism.""",

    43: """The sacred flag (**Dhwaj**) is hoisted high atop places of worship because it **helps devotees identify the faith** and locate the temple from a distance.

* **Why other options are incorrect:**
  * **beautify the place of worship:** Aesthetic enhancement is secondary to its primary role as a sacred identifier of the shrine.
  * **gives importance to the faith's symbol:** Symbols are displayed, but hoisting the flag on high towers serves primarily as a visual marker for pilgrims.
  * **It gives direction to the devotees:** Wind direction is incidental; the flag marks the sacred location of the house of worship.

💡 **Key Takeaway:** The temple flag (Dhwaj) serves as an emblem that marks and identifies a sacred house of worship.""",

    44: """To overcome academic or physical challenges, one must practice **Purushartha** (self-effort, hard work, and dedicated action), which yields success when combined with grace.

* **Why other options are incorrect:**
  * **Punarjanam:** The doctrine of rebirth/reincarnation.
  * **Pranidaya:** Compassion and mercy toward living beings.
  * **Prarthana:** Prayer; while important, prayer must be accompanied by active personal effort (*Purushartha*).

💡 **Key Takeaway:** Hindu philosophy emphasizes Purushartha (conscious self-effort) as essential for achieving goals.""",

    45: """The fundamental Sikh principle of morning chanting and meditating on God's Name is **Naam Japna** (remembrance of the Divine Name).

* **Why other options are incorrect:**
  * **Kirat Karna:** Earning an honest living through hard work.
  * **Wand shakna:** Sharing one's earnings with the needy and community.
  * **Sewa karna:** Selfless service to humanity without expectation of reward.

💡 **Key Takeaway:** The three pillars of Sikhism are Naam Japna (meditating on God's Name), Kirat Karo (honest work), and Vand Chako (sharing with others).""",

    46: """In Jain Derasa architecture, stone elephant statues flanking the entrance serve as **a symbol of protection of the temple** and royal grandeur guarding the sacred space.

* **Why other options are incorrect:**
  * **loyalty:** Represented by other symbolic figures or guardians.
  * **taming of wildlife:** Captivity or animal training is contrary to Jain Ahimsa principles.
  * **a symbol for removing negative energy:** While auspicious, entrance elephants specifically symbolize protective guardians of the temple.

💡 **Key Takeaway:** Elephants at temple entrances represent dignity, auspiciousness, and protective guardianship.""",

    47: """In a Mandir dedicated to an Avatar of Lord Vishnu (Lord Krishna), Mohini will hear the traditional devotional greeting **Jai Shri Krishna**.

* **Why other options are incorrect:**
  * **Jai Ambe:** Greeting used by devotees of Goddess Durga/Amba.
  * **Jai Jinendra:** Traditional greeting used among followers of Jainism.
  * **Jai Bhole Nath:** Greeting used by devotees of Lord Shiva.

💡 **Key Takeaway:** 'Jai Shri Krishna' is the customary greeting among devotees of Lord Krishna/Vishnu.""",

    48: """When Hanjit immediately stopped playing to assist his injured classmate and seek first aid, he demonstrated **responsibility** and caring citizenship.

* **Why other options are incorrect:**
  * **respect:** Honor shown to elders or peers, whereas acting quickly to assist an injured friend reflects civic responsibility.
  * **patience:** Calm endurance during waiting or hardship.
  * **tolerance:** Accepting differences in others without conflict.

💡 **Key Takeaway:** Responsibility involves taking immediate, caring action to assist others in times of emergency.""",

    49: """The two Utsavs (festivals) that specifically celebrate the victory of good over evil and light over darkness are **Diwali and Holi** (Diwali celebrates Rama's return after defeating Ravana; Holi celebrates Prahlad's victory over Holika).

* **Why other options are incorrect:**
  * **Paryushan Parv and Vasant Panchami:** Paryushan is a Jain festival of repentance and forgiveness; Vasant Panchami celebrates spring and Goddess Saraswati.
  * **Navratri and Janamashtami:** Janamashtami celebrates the birth of Lord Krishna.
  * **Ramnavmi and Gurupurab:** Ramnavmi celebrates Rama's birth; Gurupurab celebrates the birth of Sikh Gurus.

💡 **Key Takeaway:** Diwali and Holi are major festivals symbolizing the ultimate triumph of righteousness (*Dharma*) over evil.""",

    50: """The primary spiritual purpose of practicing Yoga (mind-body union) in Hindu philosophy is to **grow spiritually**, calm the mind, and attain self-realization.

* **Why other options are incorrect:**
  * **participate in sports:** Yoga is a spiritual discipline of self-realization, not a competitive sport.
  * **enhance social cohesion:** Community benefits occur, but the core objective of yoga is internal spiritual development.
  * **be physically fit:** Physical flexibility (*Asanas*) is a secondary benefit, but spiritual growth is the primary ultimate goal.

💡 **Key Takeaway:** Yoga is an ancient discipline designed to unite mind, body, and spirit for spiritual growth."""
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

print("Successfully updated all 15 explanations in HRE (kpsea-sst-hre-2023.js)!")
