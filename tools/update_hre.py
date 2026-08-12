import json
import re

file_path = 'src/data/kpsea-sst-hre-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

explanations = {
    41: """The correct answer is **B**.

**Analysis of the Correct Answer:**
In Hinduism, Parmatma (the Supreme Soul) created the sun (Surya) as a vital source of life. The most direct and fundamental importance of the sun to human beings is that **plants need the heat and light from the sun** to grow (photosynthesis). Without plants, there would be no food for humans or animals, leading to the end of life on Earth.

**Why Other Options Are Incorrect:**
* **A:** While the earth's climate depends on the sun, the physical rock of the earth would still exist without it; it's the *life* on earth that depends on it.
* **C:** Evaporation is a process, but the sustenance of the food chain via plant growth is the primary life-giving function.
* **D:** Energy availability is a broad term, but the specific biological necessity is food production via plants.

📌 **Key Learning Note:**
In Hindu teachings, nature is deeply respected because every element (like the sun) plays a crucial, interconnected role in sustaining all life forms.""",

    42: """The correct answer is **B**.

**Analysis of the Correct Answer:**
In this sacred verse from the Sri Guru Granth Sahib Ji, "Mata Dharat Mahat" translates to "the Great Mother Earth." By referring to the Earth as the "Great Mother," the verse elevates **earth** (Dharat) to the highest, most nurturing status among the elements (Panch Mahabhoot).

**Why Other Options Are Incorrect:**
* **A:** "Pavan" (Air) is referred to as Guru (teacher), which is highly respected but "Mahat" (Great Mother) denotes the highest nurturing status.
* **C:** Fire (Agni) is not explicitly mentioned in this specific line.
* **D:** "Pani" (Water) is referred to as Pita (father).

📌 **Key Learning Note:**
Sikhism and Hinduism teach profound environmental stewardship by personifying natural elements as familial and spiritual figures (Guru, Father, Mother).""",

    43: """The correct answer is **B**.

**Analysis of the Correct Answer:**
The Bhagavad Gita, one of the most revered scriptures in Hinduism, is a 700-verse text embedded within the ancient Indian epic, the Mahabharata. It takes the form of a profound philosophical dialogue between the warrior prince **Arjun and his charioteer, Lord Krishna**, on the battlefield of Kurukshetra.

**Why Other Options Are Incorrect:**
* **A:** Sudama was a childhood friend of Lord Krishna; their story is famous for teaching about true friendship and devotion, but is not part of the Gita.
* **C:** "Krisha" is misspelled, and standard phrasing puts the divine figure first or properly spelled.
* **D:** Hanuman is a central figure in the Ramayana, not the primary conversationalist in the Bhagavad Gita.

📌 **Key Learning Note:**
The Bhagavad Gita addresses moral dilemmas, duty (Dharma), and the paths to spiritual liberation (Moksha) through the conversation between Lord Krishna and Arjun.""",

    44: """The correct answer is **A**.

**Analysis of the Correct Answer:**
In the fable, the fox noticed that all the footprints led *into* the lion's cave, but none led *out*. By observing this, the fox deduced the danger without having to enter the cave itself. The moral is that a wise person should observe and **learn from other people's mistakes** (the animals that went in and died) to avoid suffering the same fate.

**Why Other Options Are Incorrect:**
* **B:** The lion pretended to be sick to lure the animals, so "helping the sick" was actually the trap, making this the opposite of the intended moral.
* **C:** While avoiding the lion (troublemaker) was the result, the *method* of survival was observation and learning.
* **D:** The fox survived by its own wisdom, not by associating with others (who were all eaten).

📌 **Key Learning Note:**
Wisdom (Viveka) involves critical thinking, observation, and applying past lessons to present situations to make safe and righteous choices.""",

    45: """The correct answer is **B**.

**Analysis of the Correct Answer:**
Prince Siddhartha (who later became Gautama Buddha) demonstrated **Daya**, which translates to compassion, mercy, or sympathy. By rescuing, nursing, and protecting the swan that his cousin Devadatta had shot, Siddhartha showed deep, active kindness to a suffering living being.

**Why Other Options Are Incorrect:**
* **A:** Santosh means contentment or satisfaction with what one has.
* **C:** Dhiraj (Dharraj) means patience or tolerance.
* **D:** Satya means truthfulness.

📌 **Key Learning Note:**
The story of Siddhartha and the swan teaches that life belongs to the one who saves it (compassion/Daya), not the one who tries to destroy it.""",

    46: """The correct answer is **A**.

**Analysis of the Correct Answer:**
By intervening and correcting the student's bad behavior, the teacher is fulfilling their duty (Dharma) to guide the student towards a righteous and responsible path. This aligns with **Purusharth** (specifically the aspect of Dharma within the four goals of human life), which emphasizes moral duty, righteousness, and proper conduct.

**Why Other Options Are Incorrect:**
* **B:** Prathana means prayer.
* **C:** Pranidaya means compassion for all living beings.
* **D:** Punarjanam refers to the concept of reincarnation or rebirth.

📌 **Key Learning Note:**
Purusharth outlines the four main goals of human life in Hinduism: Dharma (righteousness/duty), Artha (wealth/means of life), Kama (desire/enjoyment), and Moksha (liberation).""",

    47: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Patriotism is the feeling of love, devotion, and a sense of attachment to one's country. **Singing the national anthem** is an active, vocal expression of national pride and unity. It requires personal participation and demonstrates deep respect for the nation's identity.

**Why Other Options Are Incorrect:**
* **A:** Entertaining people is a performance activity, which is enjoyable but not explicitly a demonstration of national devotion.
* **B & D:** Watching a parade or listening to speeches are passive activities; one can observe these without necessarily feeling or demonstrating personal patriotism.

📌 **Key Learning Note:**
Active participation in national symbols and ceremonies (like the anthem or the flag) is a primary way citizens demonstrate loyalty (Desh Bhakti) to their country.""",

    48: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Environmental conservation is a civic duty that benefits the entire community and the nation. When yoga extends beyond personal physical health to encourage communal responsibility (like keeping the environment clean), it actively promotes good **citizenship**.

**Why Other Options Are Incorrect:**
* **A & B:** Fellowship and friendship refer to social bonds and relationships between individuals, but citizenship specifically relates to one's duties and responsibilities to the wider community and country.
* **D:** Mentorship is the act of guiding someone less experienced, which is unrelated to environmental conservation.

📌 **Key Learning Note:**
Yoga promotes holistic well-being, which includes living in harmony with nature and fulfilling one's civic duties (good citizenship) to maintain a healthy society.""",

    49: """The correct answer is **B**.

**Analysis of the Correct Answer:**
**Navratri** (meaning "nine nights") is a major Hindu festival dedicated entirely to the worship of the Goddess Durga and her nine forms (Navadurga). It celebrates the divine feminine power (Shakti) and the victory of good over evil, specifically Goddess Durga's triumph over the buffalo demon Mahishasura.

**Why Other Options Are Incorrect:**
* **A:** Diwali is the festival of lights, primarily celebrating Lord Rama's return to Ayodhya and the worship of Goddess Lakshmi.
* **C:** Holi is the festival of colors, celebrating the arrival of spring and the victory of Prahlada over Holika.
* **D:** Dussehra is celebrated at the end of Navratri to mark Lord Rama's victory over Ravana.

📌 **Key Learning Note:**
Navratri involves fasting, prayer, and vibrant folk dances (like Garba and Dandiya) to honor the protective and victorious nature of Goddess Durga.""",

    50: """The correct answer is **C**.

**Analysis of the Correct Answer:**
**Surya Namaskar** (Sun Salutation) is a comprehensive yoga practice that consists of a specific sequence of **twelve physical postures (asanas)**. Traditionally, it is performed gracefully in a continuous flow, often accompanied by the recitation of specific mantras for each posture to express gratitude to the sun.

**Why Other Options Are Incorrect:**
* **A:** Vajrasana (Diamond pose) is a single kneeling posture used for meditation and digestion.
* **B:** Tadasana (Mountain pose) is a single standing posture, forming the basis for other standing poses.
* **D:** Padmasana (Lotus pose) is a single cross-legged sitting posture used primarily for deep meditation.

📌 **Key Learning Note:**
Surya Namaskar is a complete body workout in yoga, combining physical postures, controlled breathing (Pranayama), and spiritual focus (mantras)."""
}

for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

new_content = "export const kpseaSstHre2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 2 completed successfully.")
